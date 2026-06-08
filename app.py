import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 CSS 魔法控制中心：讓 9 個獨立的小圖片動起來！
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

    /* 4. 頂部白底黑框看板樣式 */
    .header-box {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 20px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 5px 5px 0px #FFC1CC !important;
    }

    /* 5. 核心：定義上下彈跳動畫 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-8px); } /* 向上跳 8 像素 */
        100% { transform: translateY(0); }
    }

    /* 6. 讓包裝圖片的容器套用動畫 */
    .jump-container {
        display: inline-block;
        animation: pixelJump 0.6s infinite ease-in-out;
    }

    /* 7. 介面元件可愛圓角化 */
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

    /* 8. 精美手帳字卡 */
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
st.markdown(
    """
    <div class="header-box">
        <div style="font-size: 22px; font-weight: bold; color: #5D4037; letter-spacing: 2px; margin-bottom: 15px;">
            👾 ANIME PIXEL DIARY 👾
        </div>
    """,
    unsafe_allow_html=True
)

# 🎯 準備 9 張去背小圖的穩定分流網址
heroes = {
    "ochaco": "https://i.imgur.com/vH97Oco.png",     # 御茶子
    "deku": "https://i.imgur.com/f0m76s9.png",       # 出久
    "bakugo": "https://i.imgur.com/kSPhsQY.png",     # 爆豪
    "iida": "https://i.imgur.com/KofW8tT.png",       # 飯田
    "todoroki": "https://i.imgur.com/w90Lg2q.png",   # 轟
    "kirishima": "https://i.imgur.com/3Z6H9kX.png",  # 切島
    "tokoyami": "https://i.imgur.com/C30w5G3.png",   # 常闇
    "tsuyu": "https://i.imgur.com/R8pP6rC.png",      # 梅雨
    "denki": "https://i.imgur.com/V7w7fT6.png"       # 上鳴
}

# 🌟 使用 Streamlit 的欄位功能（Columns）排成美美的九宮格
# 第一排：4 個人
st.markdown('<div style="margin-bottom: 10px;">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.0s;"><img src="{heroes["ochaco"]}" width="65"></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.1s;"><img src="{heroes["deku"]}" width="65"></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.2s;"><img src="{heroes["bakugo"]}" width="65"></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.15s;"><img src="{heroes["iida"]}" width="65"></div>', unsafe_allow_html=True)

# 第二排：5 個人
st.markdown('<div style="margin-top: 15px; margin-bottom: 15px;">', unsafe_allow_html=True)
c5, c6, c7, c8, c9 = st.columns(5)
with c5:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.25s;"><img src="{heroes["todoroki"]}" width="55"></div>', unsafe_allow_html=True)
with c6:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.05s;"><img src="{heroes["kirishima"]}" width="55"></div>', unsafe_allow_html=True)
with c7:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.3s;"><img src="{heroes["tokoyami"]}" width="55"></div>', unsafe_allow_html=True)
with c8:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.2s;"><img src="{heroes["tsuyu"]}" width="55"></div>', unsafe_allow_html=True)
with c9:
    st.markdown(f'<div class="jump-container" style="animation-delay: 0.12s;"><img src="{heroes["denki"]}" width="55"></div>', unsafe_allow_html=True)

st.markdown(
    """
        <div style="font-size: 13px; color: #8D6E63; margin-top: 20px;">
            ✨ 主人的英雄學院像素秘密基地 · 點陣角色熱血跳動中 ✨
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 功能選單
mode = st.radio(
    "🧭 請選取手帳功能：",
    ["🌸 打开手帳庫 (看番紀錄)", "➕ 填寫新紀錄 (捕捉感動)", "📝 悄悄修改資料 (補上心情)", "🗑️ 揮揮手道別 (刪除紀錄)"],
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
                card_html = f"""
                <div class="anime-card">
                    <div class="anime-title">
                        🎬 {anime[0]} 
                        <span style="font-size: 0.95rem; float: right; color: #FF8A9A;">{anime[1]} · {stars}</span>
                    </div>
                    <div style="margin-top: 8px; color: #6D4C41;"><b>✍️ 創作者：</b> {anime[2]}</div>
                    <div style="color: #6D4C41;"><b>🏷️ 分類標籤：</b> {anime[3]}</div>
                    <div style="color: #6D4C41;"><b>💌 心得點滴：</b> {anime[5]}</div>
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
        anime_status = st.selectbox("🎯 目前進度", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
        anime_type = st.text
