import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 CSS 控制中心
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

    /* 4. 動漫角色上下彈跳動畫 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0); }
    }
    
    /* 5. 【核心】直接去撈主人剛上傳在 GitHub 最外層的 IMG_0417.jpeg */
    .hero-sprite {
        display: inline-block;
        width: 66px;   
        height: 66px;  
        background-image: url('https://raw.githubusercontent.com/liaoy445-maker/my-anime-app/main/IMG_0417.jpeg') !important; 
        background-size: 200px 200px !important; 
        image-rendering: pixelated !important;   
        animation: pixelJump 0.6s infinite ease-in-out;
    }

    /* 6. 精確精靈圖座標切片 (對齊 9 宮格原圖) */
    .ochaco   { background-position: -2px -2px !important; }                     
    .deku     { background-position: -67px -2px !important; animation-delay: 0.1s; }  
    .bakugo   { background-position: -132px -2px !important; animation-delay: 0.2s; } 
    .iida     { background-position: -2px -67px !important; animation-delay: 0.15s; } 
    .todoroki { background-position: -67px -67px !important; animation-delay: 0.25s; }
    .kirishima{ background-position: -132px -67px !important; animation-delay: 0.05s; }
    .tokoyami { background-position: -2px -132px !important; animation-delay: 0.3s; } 
    .tsuyu    { background-position: -67px -132px !important; animation-delay: 0.2s; } 
    .denki    { background-position: -132px -132px !important; animation-delay: 0.12s; }

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
    
    button[data-testid="baseButton-primary"] {
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

# 保持網頁穩定運作
else:
    st.write("✨ 請切換至觀看模式體驗完整動態效果唷！")
