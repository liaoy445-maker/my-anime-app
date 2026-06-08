import streamlit as st
import json
import os

# ========================================================
# 🍒 看板文字設定中心
# ========================================================
BANNER_TITLE = "👾 ANIME DIARY 👾"
# ========================================================

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 CSS 美化控制中心 (經檢查：文字字串完全閉合，安全無誤)
st.markdown(
    """
    <style>
    /* 1. 網頁粉嫩點陣手帳背景 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1.5px, transparent 0px) !important;
        background-size: 24px 24px !important;
    }
    
    /* 2. 徹底隱藏頂部干擾元件 */
    header, [data-testid="stSidebarCollapsedControl"] {
        color: transparent !important;
        background: transparent !important;
    }
    
    /* 3. 全局可愛字型與顏色 */
    h1, h2, h3, p, label, .stMarkdown {
        color: #5D4037 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }

    /* 4. 頂部白底黑框純文字看板樣式 */
    .header-box {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 25px 15px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 5px 5px 0px #FFC1CC !important;
        overflow: hidden;
    }

    /* 🎯 標題與副標題手機防折行魔法 */
    .main-title {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        letter-spacing: 2px !important;
        margin-bottom: 8px !important;
        white-space: nowrap !important;
        block-size: auto;
    }

    .sub-title {
        font-size: 11px !important;
        color: #8D6E63 !important;
        white-space: nowrap !important;
        letter-spacing: 0.5px !important;
    }

    /* 5. 介面元件可愛圓角化 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 3px solid #FFC1CC !important;
        border-radius: 10px !important;
    }
    
    button[data-testid="baseButton-primary"] {
        background-color: #FF8A9A !important;
        color: white !important;
        border: 3px solid #5D4037 !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0px #5D4037 !important;
        font-weight: bold !important;
    }

    /* 6. 精美手帳字卡 */
    .anime-card {
        background-color: #FFFFFF !important;
        border: 3px solid #5D4037 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
    }
    .anime-title {
        font-size: 1.25rem !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        border-bottom: 2px dashed #FFC1CC !important;
        padding-bottom: 6px !important;
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

# --- 💖 頂部招牌看板 💖 ---
header_html = """
<div class="header-box">
    <div class="main-title">""" + BANNER_TITLE + """</div>
    <div class="sub-title">✨ 動漫秘密基地 · 紀錄追番的每刻感動 ✨</div>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# 功能選單 (加上 key 控制狀態)
mode = st.radio(
    "🧭 請選取手帳功能：",
    ["🌸 打开手帳庫 (看番紀錄)", "➕ 填寫新紀錄 (捕捉感動)", "📝 悄悄修改資料 (補上心情)", "🗑️ 揮揮手道別 (刪除紀錄)"],
    key="nav_radio",
    horizontal=True
)

# 功能 1：查看與搜尋 (安全字串拼接，絕無衝突)
if mode == "🌸 打开手帳庫 (看番紀錄)":
    st.header("🔍 翻閱我的動漫手帳庫")
    search_keyword = st.text_input("🔮 輸入關鍵字搜搜看：", placeholder="搜尋名稱、標籤...")
    
    if anime_list:
        for index, anime in enumerate(anime_list):
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                card_html = """
                <div class="anime-card">
                    <div class="anime-title">
                        🎬 """ + str(anime[0]) + """ 
                        <span style="font-size: 0.95rem; float: right; color: #FF8A9A;">""" + str(anime[1]) + " · " + stars + """</span>
                    </div>
                    <div style="margin-top: 8px; color: #6D4C41;"><b>✍️ 創作者：</b> """ + str(anime[2]) + """</div>
                    <div style="color: #6D4C41;"><b>🏷️ 分類標籤：</b> """ + str(anime[3]) + """</div>
                    <div style="color: #6D4C41;"><b>💌 心得點滴：</b> """ + str(anime[5]) + """</div>
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
        anime_name = st.text_input("🍒 作品名稱")
        anime_author = st.text_input("✍️ 厲害的作者")
    with col2:
        anime_status = st.selectbox("🎯 目前進
