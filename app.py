import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 究極可愛像素 CSS 控制中心：加入上下跳動動畫、像素框與背景
st.markdown(
    """
    <style>
    /* 1. 網頁粉嫩點陣手帳背景 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1.5px, transparent 0px) !important;
        background-size: 24px 24px !important;
    }
    
    /* 2. 側邊欄櫻花粉色 */
    [data-testid="stSidebar"] {
        background-color: #FFE3E7 !important;
        border-right: 3px solid #FFC1CC !important;
    }
    
    /* 3. 全局可愛字型與顏色 */
    h1, h2, h3, p, label, .stMarkdown {
        color: #5D4037 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }

    /* 4. 【核心動畫】讓像素角色活過來！打造上下彈跳效果 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0); }
    }
    
    .jumping-pixel {
        display: inline-block;
        animation: pixelJump 0.8s infinite ease-in-out;
        image-rendering: pixelated; /* 確保像素圖案不會變模糊，維持顆粒感 */
    }

    /* 5. 頂部看板樣式 */
    .header-box {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 4px 4px 0px #FFC1CC !important;
    }

    /* 6. 輸入框與按鈕一律改成圓角可愛像素邊框 */
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

    /* 7. 完全防亂碼的特製精美動漫字卡 */
    .anime-card {
        background-color: #FFFFFF !important;
        border: 3px solid #5D4037 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
        position: relative;
        overflow: hidden;
    }
    .anime-title {
        font-size: 1.25rem !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        border-bottom: 2px dashed #FFC1CC !important;
        padding-bottom: 6px !important;
        margin-bottom: 10px !important;
        display: flex;
        align-items: center;
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

# --- 💖 網頁最上方：召喚正在上下跳動的像素動漫小人 💖 ---
st.markdown(
    """
    <div class="header-box">
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 10px;">
            <img class="jumping-pixel" src="https://i.imgur.com/rN3GByo.png" width="45" onerror="this.src='https://openmoji.org/data/color/svg/1F47E.svg'">
            <img class="jumping-pixel" src="https://i.imgur.com/VpZ2p8b.png" width="45" style="animation-delay: 0.2s;" onerror="this.src='https://openmoji.org/data/color/svg/1F440.svg'">
            <img class="jumping-pixel" src="https://i.imgur.com/N7bVzLh.png" width="45" style="animation-delay: 0.4s;" onerror="this.src='https://openmoji.org/data/color/svg/1F525.svg'">
        </div>
        <div style="font-size: 20px; font-weight: bold; color: #5D4037; letter-spacing: 2px;">
            👾 ANIME PIXEL DIARY 👾
        </div>
        <div style="font-size: 12px; color: #8D6E63; margin-top: 5px;">
            ✨ 主人的專屬像素動漫手帳空間 · 萌力全開中 ✨
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 側邊欄選單（加裝像素大頭貼） ---
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 10px; margin-bottom: 15px;">
        <img class="jumping-pixel" src="https://i.imgur.com/v8pA77R.png" width="75" style="border: 3px solid #5D4037; background: #FFF; padding: 3px;" onerror="this.src='https://openmoji.org/data/color/svg/1F469-200D0000.svg'">
        <div style="color: #5D4037; font-weight: bold; font-size: 14px; margin-top: 8px;">【 控制終端機 】</div>
    </div>
    """,
    unsafe_allow_html=True
)

mode = st.sidebar.radio(
    "🧭 系統選單",
    [
        "🌸 打開手帳庫 (看番紀錄)", 
        "➕ 填寫新紀錄 (捕捉感動)", 
        "📝 悄悄修改資料 (補上心情)", 
        "🗑️ 揮揮手道別 (刪除紀錄)"
    ]
)

# 功能 1：查看與搜尋 (無亂碼、內嵌跳動動漫元件)
if mode == "🌸 打開手帳庫 (看番紀錄)":
    st.header("🔍 翻閱我的動漫手帳庫")
    search_keyword = st.text_input("🔮 輸入關鍵字搜搜看：", placeholder="搜尋名稱、標籤...")
    
    if anime_list:
        for anime in anime_list:
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                
                # 建立名台詞 HTML
                quote_html = f"<div class='anime-quote'>💬 「 {anime[4][0]} 」</div>" if anime[4] else ""
                
                # 每一張動漫字卡都自帶一個右下角跳動的像素遊戲手把/小怪物標記，且100%防重疊
                card_html = f"""
                <div class="anime-card">
                    <div class="anime-title">
                        <span style="margin-right: 8px;">🎬</span> {anime[0]} 
                        <span style="font-size: 0.9rem; margin-left: auto; color: #FF8A9A;">{anime[1]} · {stars}</span>
                    </div>
                    <div class="anime-meta"><b>✍️ 創作者：</b> {anime[2]}</div>
                    <div class="anime-meta"><b>🏷️ 分類標籤：</b> {anime[3]}</div>
                    <div class="anime-meta"><b>💌 心得點滴：</b> {anime[5]}</div>
                    {quote_html}
                    <div style="position: absolute; right: 15px; bottom: 10px; opacity: 0.7;">
                        <img class="jumping-pixel" src="https://i.imgur.com/VpZ2p8b.png" width="22" style="animation-duration: 1.2s;">
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.info("🎈 存檔空間目前空空的，快去左邊切換「➕ 填寫新紀錄」吧！")

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
    anime_score = st.slider("⭐ 萌度/推薦指數大評分", 1, 5, 5)
    
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
