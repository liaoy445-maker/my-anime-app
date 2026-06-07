import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 萌力全開 CSS 控制中心：加入 Idle 彈跳動畫、消滅頂部髒字、像素字卡
st.markdown(
    """
    <style>
    /* 1. 網頁粉嫩點陣手帳背景 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1.5px, transparent 0px) !important;
        background-size: 24px 24px !important;
    }
    
    /* 2. 徹底殺死手機頂部因側邊欄按鈕產生的 double_arrow_right 亂碼 */
    header, [data-testid="stSidebarCollapsedControl"] {
        color: transparent !important;
        background: transparent !important;
    }
    [data-testid="stSidebarCollapsedControl"] button {
        color: #FF8A9A !important;
    }
    
    /* 3. 全局可愛字型與顏色 */
    h1, h2, h3, p, label, .stMarkdown {
        color: #5D4037 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }

    /* 4. 【靈魂核心】讓動漫角色活過來！打造上下彈跳動畫 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    
    /* 5. 特製日系動漫像素小人組件 (放大並強化點政顆粒感) */
    .pixel-anime-char {
        display: inline-block;
        font-size: 42px; /* 放大圖案 */
        line-height: 1;
        animation: pixelJump 0.6s infinite ease-in-out;
        text-shadow: 2px 2px 0px #FFC1CC;
    }

    /* 6. 頂部白底黑框看板樣式 */
    .header-box {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 20px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 5px 5px 0px #FFC1CC !important;
    }

    /* 7. 輸入框與按鈕一律改成圓角可愛像素邊框 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 3px solid #FFC1CC !important;
        border-radius: 10px !important;
    }
    
    button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
        background-color: #FF8A9A !important;
        color: white !important;
        border: 3px solid #5D4037 !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0px #5D4037 !important;
        font-weight: bold !important;
    }

    /* 8. 專屬精美動漫字卡 */
    .anime-card {
        background-color: #FFFFFF !important;
        border: 3px solid #5D4037 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
        position: relative;
    }
    .anime-title {
        font-size: 1.25rem !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        border-bottom: 2px dashed #FFC1CC !important;
        padding-bottom: 6px !important;
        margin-bottom: 10px !important;
    }
    .anime-meta {
        font-size: 0.95rem !important;
        color: #6D4C41 !important;
        margin-bottom: 6px !important;
    }
    .anime-quote {
        background-color: #FFF5F6 !important;
        border-left: 4px solid #FF8A9A !important;
        padding: 6px 12px !important;
        margin-top: 8px !important;
        font-style: italic !important;
        color: #795548 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 檔案讀寫設定
FILE_NAME = "anime_data_web.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        st.session_state.anime_list = json.load(f)
else:
    if "anime_list" not in st.session_state:
        st.session_state.anime_list = []

anime_list = st.session_state.anime_list

def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=4)

# --- 💖 網頁最上方：召喚絕對不會壞掉、正在歡樂跳動的動漫角色群 💖 ---
st.markdown(
    """
    <div class="header-box">
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 15px;">
            <div class="pixel-anime-char">🧑‍🎤</div>
            <div class="pixel-anime-char" style="animation-delay: 0.15s; animation-duration: 0.7s;">🧑‍🦰</div>
            <div class="pixel-anime-char" style="animation-delay: 0.3s; animation-duration: 0.5s;">👱‍♂️</div>
            <div class="pixel-anime-char" style="animation-delay: 0.45s;">👾</div>
        </div>
        <div style="font-size: 22px; font-weight: bold; color: #5D4037; letter-spacing: 2px;">
            👾 ANIME PIXEL DIARY 👾
        </div>
        <div style="font-size: 13px; color: #8D6E63; margin-top: 5px;">
            ✨ 主人的專屬像素動漫手帳空間 · 萌力全開中 ✨
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 橫向導覽選單（完美適應手機版，好點選又不噴字）
mode = st.radio(
    "🧭 請選取手帳功能：",
    [
        "🌸 打开手帳庫 (看番紀錄)", 
        "➕ 填寫新紀錄 (捕捉感動)", 
        "📝 悄悄修改資料 (補上心情)", 
        "🗑️ 揮揮手道別 (刪除紀錄)"
    ],
    horizontal=True
)

# 功能 1：查看與搜尋
if mode == "🌸 打开手帳庫 (看番紀錄)":
    st.header("🔍 翻閱我的動漫手帳庫")
    search_keyword = st.text_input("🔮 輸入關鍵字搜搜看：", placeholder="搜尋名稱、標籤...")
    
    if anime_list:
        for anime in anime_list:
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                quote_html = f"<div class='anime-quote'>💬 「 {anime[4][0]} 」</div>" if anime[4] else ""
                
                # 每一張動漫字卡都有獨立的白底粉框，右下角裝飾一隻彈跳的動漫Q版像素
                card_html = f"""
                <div class="anime-card">
                    <div class="anime-title">
                        🎬 {anime[0]} 
                        <span style="font-size: 0.95rem; float: right; color: #FF8A9A;">{anime[1]} · {stars}</span>
                        <div style="clear: both;"></div>
                    </div>
                    <div class="anime-meta"><b>✍️ 創作者：</b> {anime[2]}</div>
                    <div class="anime-meta"><b>🏷️ 分類標籤：</b> {anime[3]}</div>
                    <div class="anime-meta"><b>💌 心得點滴：</b> {anime[5]}</div>
                    {quote_html}
                    <div style="position: absolute; right: 15px; bottom: 5px; font-size: 20px; cubic-bezier(0.28, 0.84, 0.42, 1);">
                        <div class="pixel-anime-char" style="animation-duration: 0.9s;">👧</div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.info("🎈 存檔空間目前空空的，快去點上面的「➕ 填寫新紀錄」吧！")

# 功能 2：填寫新紀錄
elif mode == "➕ 填寫新紀錄 (捕捉感動)":
    st.header("✨ 寫入新紀錄")
    col1, col2 = st.columns(2)
    with col1:
        anime_name = st.text_input("🍒 作品名稱", placeholder="例如：約會大作戰")
        anime_author = st.text_input("✍️ 厲害的作者", placeholder="例如：橘公司老師")
    with col2:
        anime_status = st.selectbox("🎯 目前進度", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
        anime_type = st.text_input("🏷️ 類型標籤", placeholder="例如：純愛、戰鬥、後宮番")
        
    anime_review = st.text_area("📝 心得悄悄話", placeholder="偷偷寫下你對這部作品的滿滿想法...")
    anime_score = st.slider("⭐ 推薦指數大評分", 1, 5, 5)
    
    st.subheader("💬 本作神台詞")
    q1 = st.text_input("🌈 第一句神台詞", placeholder="名台詞 1")
    
    st.write("")
    if st.button("💝 寫入晶片存檔", type="primary"):
        if anime_name:
            quotes_box = [q1.strip()] if q1.strip() else []
            anime_list.append([
                anime_name, anime_status, anime_author, anime_type,
                quotes_box, anime_review, anime_score
            ])
            save_data()
            st.success("🌟 成功寫入存檔！關卡已儲存！")
            st.rerun()
        else:
            st.error("❌ 忘記填寫作品名稱了啦！")

# 功能 3：修改動漫
elif mode == "📝 悄悄修改資料 (補上心情)":
    st.header("📝 悄悄修改資料")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        selected_name = st.selectbox("請選擇哪一部作品想翻修呢：", anime_names)
        
        for anime in anime_list:
            if anime[0] == selected_name:
                new_status = st.selectbox("新的追番狀態", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
                new_review = st.text_area("更新心得點滴", value=anime[5])
                
                if st.button("💝 儲存新心情"):
                    anime[1] = new_status
                    anime[5] = new_review
                    save_data()
                    st.success("✨ 手帳更新成功！")
                    st.rerun()
    else:
        st.info("🥺 目前沒有資料可以修改唷。")

# 功能 4：刪除動漫
elif mode == "🗑️ 揮揮手道別 (刪除紀錄)":
    st.header("🗑️ 揮揮手道別")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        target_name = st.selectbox("選一個要揮揮手說再見的作品：", anime_names)
        
        if st.button("💥 確定斷捨離！", type="primary"):
            for anime in anime_list:
                if anime[0] == target_name:
                    anime_list.remove(anime)
                    save_data()
                    st.success(f"🗑️ 【{target_name}】已擦掉囉～")
                    st.rerun()
                    break
    else:
        st.info("🥺 目前沒有資料可以刪除唷。")
