import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 究極 CSS 控制中心：利用精靈圖技術，將主人給的圖片切片並加上 Idle 彈跳動畫
st.markdown(
    """
    <style>
    /* 1. 網頁粉嫩點陣手帳背景 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1.5px, transparent 0px) !important;
        background-size: 24px 24px !important;
    }
    
    /* 2. 徹底隱藏頂部干擾元件與亂碼 */
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

    /* 4. 動漫角色上下彈跳動畫 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0); }
    }
    
    /* 5. 【核心】像素精靈圖基本框架：使用 imgur 託管主人給的九宮格像素圖 */
    .hero-sprite {
        display: inline-block;
        width: 66px;   /* 單個小人的寬度 */
        height: 66px;  /* 單個小人的高度 */
        background-image: url('https://i.imgur.com/vHqorvS.png') !important;
        background-size: 200px 200px !important; /* 縮放整張圖以精確匹配切片 */
        image-rendering: pixelated !important;   /* 完美保留復古點陣顆粒感 */
        animation: pixelJump 0.6s infinite ease-in-out;
    }

    /* 6. 利用座標切片，精確召喚出圖中的每一個專屬角色 */
    .ochaco   { background-position: -2px -2px !important; }                     /* 麗日御茶子 (左上) */
    .deku     { background-position: -67px -2px !important; animation-delay: 0.1s; }  /* 綠谷出久 (中上) */
    .bakugo   { background-position: -132px -2px !important; animation-delay: 0.2s; } /* 爆豪勝己 (右上) */
    .iida     { background-position: -2px -67px !important; animation-delay: 0.15s; } /* 飯田天哉 (左中) */
    .todoroki { background-position: -67px -67px !important; animation-delay: 0.25s; }/* 轟焦凍 (正中) */
    .kirishima{ background-position: -132px -67px !important; animation-delay: 0.05s; }/* 切島銳兒郎 (右中) */
    .tokoyami { background-position: -2px -132px !important; animation-delay: 0.3s; } /* 常闇踏陰 (左下) */
    .tsuyu    { background-position: -67px -132px !important; animation-delay: 0.2s; } /* 蛙吹梅雨 (中下) */
    .denki    { background-position: -132px -132px !important; animation-delay: 0.12s; }/* 上鳴電氣 (右下) */

    /* 7. 頂部白底黑框看板樣式 */
    .header-box {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 20px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 5px 5px 0px #FFC1CC !important;
    }

    /* 8. 介面元件可愛圓角化 */
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

    /* 9. 精美手帳字卡 */
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

# --- 💖 網頁最上方：成功召喚主人專屬的 9 大英雄學院像素小人！ 💖 ---
st.markdown(
    """
    <div class="header-box">
        <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 10px; flex-wrap: wrap;">
            <div class="hero-sprite ochaco"></div>
            <div class="hero-sprite deku"></div>
            <div class="hero-sprite bakugo"></div>
            <div class="hero-sprite iida"></div>
        </div>
        <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 15px; flex-wrap: wrap;">
            <div class="hero-sprite todoroki"></div>
            <div class="hero-sprite kirishima"></div>
            <div class="hero-sprite tokoyami"></div>
            <div class="hero-sprite tsuyu"></div>
            <div class="hero-sprite denki"></div>
        </div>
        <div style="font-size: 22px; font-weight: bold; color: #5D4037; letter-spacing: 2px;">
            👾 ANIME PIXEL DIARY 👾
        </div>
        <div style="font-size: 13px; color: #8D6E63; margin-top: 5px;">
            ✨ 主人的英雄學院像素秘密基地 · 點陣角色熱血跳動中 ✨
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 功能選單
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
        for index, anime in enumerate(anime_list):
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                quote_html = f"<div class='anime-quote'>💬 「 {anime[4][0]} 」</div>" if anime[4] else ""
                
                # 讓手帳字卡右下角隨機分配不同的小人在跳動，超可愛！
                sprites = ["ochaco", "deku", "bakugo", "todoroki", "tsuyu", "denki"]
                chosen_sprite = sprites[index % len(sprites)]
                
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
                    <div style="position: absolute; right: 15px; bottom: 5px;">
                        <div class="hero-sprite {chosen_sprite}" style="width:45px; height:45px; background-size:136px 136px; background-position: inherit; animation-duration: 0.8s;"></div>
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
        anime_name = st.text_input("🍒 作品名稱", placeholder="例如：我的英雄學院")
        anime_author = st.text_input("✍️ 厲害的作者", placeholder="例如：堀越耕平老師")
    with col2:
        anime_status = st.selectbox("🎯 目前進度", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
        anime_type = st.text_input("🏷️ 類型標籤", placeholder="例如：熱血、戰鬥、校園、像素風")
        
    anime_review = st.text_area("📝 心得悄悄話", placeholder="偷偷寫下你對這部作品的滿滿想法...")
    anime_score = st.slider("⭐ 推薦指数大評分", 1, 5, 5)
    
    st.subheader("💬 本作神台詞")
    q1 = st.text_input("🌈 第一句神台詞", placeholder="例如：已經沒事了！因為，我來了！")
    
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
