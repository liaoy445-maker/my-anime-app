import streamlit as st
import json
import os

# 設定網頁標題與分頁圖標
st.set_page_config(page_title="👾 我的像素動漫手帳 👾", layout="centered")

# 💖 究極像素魔法：強行將全網頁重構成 8-Bit 像素復古可愛風 💖
st.markdown(
    """
    <style>
    /* 引入超可愛的日系像素風英文字體與中文字體風格 */
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    /* 1. 全域背景：改成軟綿綿的像素草莓牛奶色，並加上微微的復古點陣感 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1px, transparent 0px) !important;
        background-size: 16px 16px !important;
    }

    /* 2. 側邊欄：變成復古遊戲機側條 */
    [data-testid="stSidebar"] {
        background-color: #FFE3E7 !important;
        border-right: 4px solid #5D4037 !important;
    }

    /* 3. 消滅所有現代感！把所有大標題、文字全部改成棕色復古字體，並自帶像素陰影 */
    h1, h2, h3, p, label, .stMarkdown, span {
        color: #5D4037 !important;
        font-family: 'VT323', "Courier New", "Noto Sans TC", sans-serif !important;
        text-shadow: 1px 1px 0px #FFFFFF !important;
    }
    
    h1 {
        font-size: 2.5rem !important;
        letter-spacing: 2px !important;
    }

    /* 4. 【核心重置】讓所有卡片（Expander）變成超經典的 NES 遊戲機雙層像素邊框 */
    .stExpander {
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
        border-radius: 0px !important; /* 像素風必須是方方正正的！ */
        margin-bottom: 15px !important;
    }

    /* 5. 輸入框與下拉選單：也全部變成方頭方腦的像素框 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 4px solid #5D4037 !important;
        border-radius: 0px !important;
        box-shadow: 3px 3px 0px #FFE3E7 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }
    
    /* 6. 可愛按鈕：變成一按就會扁下去的 8-bit 遊戲按鈕 */
    button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
        background-color: #FF8A9A !important;
        color: white !important;
        border: 4px solid #5D4037 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #5D4037 !important;
        font-weight: bold !important;
        transition: all 0.1s ease !important;
    }
    button[data-testid="baseButton-primary"]:active, button[data-testid="baseButton-secondary"]:active {
        transform: translate(4px, 4px) !important;
        box-shadow: 0px 0px 0px !important;
    }

    /* 7. 隱藏醜醜的原生開關 */
    button.stSidebarCollapse {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 檔案要存在雲端電腦裡的名字
FILE_NAME = "anime_data_web.json"

# 【自動讀檔小精靈】
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        st.session_state.anime_list = json.load(f)
else:
    if "anime_list" not in st.session_state:
        st.session_state.anime_list = []

anime_list = st.session_state.anime_list

# 💾 儲存檔案的魔法咒語
def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=4)

# --- 💖 網頁畫面頂端：置入可愛的像素動漫裝飾橫條 💖 ---
# 這裡使用了極具復古風的像素 GIF 角色與裝飾
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <img src="https://giffiles.alphacoders.com/214/214695.gif" width="120" style="image-rendering: pixelated; margin: 0 10px;">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbms3cXN4M29wZndpZXF0bWxoM29tZG15YTN3Z3R3Z3d6Znd0YWhubCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/8m4R9K71F_HcA/giphy.gif" width="100" style="image-rendering: pixelated;">
    </div>
    """, 
    unsafe_allow_html=True
)

st.title("📟 🎮 PIXEL ANIME NOTE 👾 🌟")
st.caption("✨ 歡迎光臨主人的 8-Bit 像素二次元秘密終端機！嗶嗶嗶—— ✨")

# --- 側邊欄裝飾：加入像素風動漫娘頭像與裝飾 ---
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXN6OHg4Zm10d3E4MXd0c3Z0ZzNqdzh0ZXN0OHp1Ynd5N3I0ZmsyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v98d89OUpIasPZ8Wv9/giphy.gif" width="130" style="image-rendering: pixelated; border: 3px solid #5D4037;"><br>
        <span style="font-size: 14px; font-weight: bold; color: #5D4037;">SELECT MODE</span>
    </div>
    """,
    unsafe_allow_html=True
)

# 左側導覽選單
mode = st.sidebar.radio(
    "💬 MENU",
    [
        "💾 [LOAD] 打開手帳本本", 
        "➕ [SAVE] 填寫新紀錄", 
        "📝 [EDIT] 悄悄修改資料", 
        "🗑️ [DROP] 揮揮手道別"
    ]
)

st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 30px;">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM290YjRna3g3Mzhic3drY3Z0NjRwbTVmczdwbmM3a2x3cTFtc2d3cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Lw97nLbeUym4e6hSFA/giphy.gif" width="60" style="image-rendering: pixelated;">
    </div>
    """,
    unsafe_allow_html=True
)

# 功能 1：填寫新紀錄
if mode == "➕ [SAVE] 填寫新紀錄":
    st.header("🔮 ➕ INSERT NEW DATA")
    
    col1, col2 = st.columns(2)
    with col1:
        anime_name = st.text_input("📝 TITLE / 作品名稱", placeholder="例如：約會大作戰")
        anime_author = st.text_input("✍️ AUTHOR / 創作者", placeholder="例如：橘公司")
    with col2:
        anime_status = st.selectbox("🎯 STATUS / 目前進度", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
        anime_type = st.text_input("🏷️ TAGS / 類型標籤", placeholder="例如：純愛、戰鬥")
        
    anime_review = st.text_area("💌 COMMENT / 心得悄悄話", placeholder="偷偷寫下你對這部作品的滿滿想法...")
    anime_score = st.slider("⭐ SCORE / 推薦大評分", 1, 5, 5)
    
    st.subheader("💬 QUOTES / 本作神台詞（最多三句）")
    q1 = st.text_input("🌈 LINE 1", placeholder="神台詞 1")
    q2 = st.text_input("✨ LINE 2", placeholder="神台詞 2")
    q3 = st.text_input("🌸 LINE 3", placeholder="神台詞 3")
