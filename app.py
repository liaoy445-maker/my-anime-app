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

# 💖 CSS 美化控制中心 (移除了所有會跟元件衝突的 card 標籤)
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
st.markdown('<div class="header-box"><div class="main-title">' + BANNER_TITLE + '</div><div class="sub-title">✨ 動漫秘密基地 · 紀錄追番的每刻感動 ✨</div></div>', unsafe_allow_html=True)

# 🎯 初始化頁面索引 (用最安全的方式控制選單跳轉)
if "current_page_idx" not in st.session_state:
    st.session_state.current_page_idx = 0

menu_options = ["🌸 打開手帳庫 (看番紀錄)", "➕ 填寫新紀錄 (捕捉感動)", "📝 悄悄修改資料 (補上心情)", "🗑️ 揮揮手道別 (刪除紀錄)"]

# 功能選單
mode = st.radio(
    "🧭 請選取手帳功能：", 
    menu_options, 
    index=st.session_state.current_page_idx, 
    horizontal=True
)

# 同步選單索引
st.session_state.current_page_idx = menu_options.index(mode)

# 功能 1：查看與搜尋
if mode == "🌸 打開手帳庫 (看番紀錄)":
    st.header("🔍 翻閱我的動漫手帳庫")
    search_keyword = st.text_input("🔮 輸入關鍵字搜搜看：", placeholder="搜尋名稱、標籤...", key="real_search_input")
    
    if anime_list:
        for index, anime in enumerate(anime_list):
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                
                # 改用 Streamlit 原生的分行樣式，完美解決雙輸入框與排版錯亂
                st.write("---")
                st.subheader(f"🎬 {anime[0]}")
                st.write(f"🎯 **進度狀態：** {anime[1]} ｜ {stars}")
                st.write(f"✍️ **創作者：** {anime[2]}")
                st.write(f"🏷️ **分類標籤：** {anime[3]}")
                st.write(f"💌 **心得點滴：** {anime[5]}")
        st.write("---")
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
        anime_type = st.text_input("🏷️ 類型標籤")
        
    anime_review = st.text_area("📝 心得悄悄話")
    anime_score = st.slider("⭐ 推薦指數", 1, 5, 5)
    
    if st.button("💝 寫入晶片存檔", type="primary"):
        if anime_name:
            anime_list.append([anime_name, anime_status, anime_author, anime_type, [], anime_review, anime_score])
            save_data()
            st.success(f"🌟 成功寫入存檔！✅ 「{anime_name}」已存入晶片。")
            st.session_state.current_page_idx = 0  # 安全設定回第一頁
            st.rerun()

# 功能 3：悄悄修改資料
elif mode == "📝 悄悄修改資料 (補上心情)":
    st.header("📝 悄悄修改資料")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        selected_name = st.selectbox("請選擇哪一部作品想翻修呢：", anime_names)
        for anime in anime_list:
            if anime[0] == selected_name:
                status_options = ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"]
                current_index = status_options.index(anime[1]) if anime[1] in status_options else 0
                new_status = st.selectbox("新的追番狀態", status_options, index=current_index)
                new_review = st.text_area("更新心得點滴", value=anime[5])
                
                if st.button("💝 儲存新心情"):
                    anime[1] = new_status
                    anime[5] = new_review
                    save_data()
                    st.success(f"✨ 手帳更新成功！✅ 「{selected_name}」的心情已存入。")
                    st.session_state.current_page_idx = 0  # 安全設定回第一頁
                    st.rerun()

# 功能 4：揮揮手道別
elif mode == "🗑️ 揮揮手道別 (刪除紀錄)":
    st.header("🗑️ 揮揮手道別")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        target_name = st.selectbox("選一個要揮揮手說再見的作品：", anime_names)
        
        if st.button("💥 確定斷捨離！", type="primary", key="delete_confirm"):
            for anime in anime_list:
                if anime[0] == target_name:
                    anime_list.remove(anime)
                    save_data()
                    st.warning(f"🗑️ 已擦掉囉～ ✅ 「{target_name}」已從存檔移出。")
                    st.session_state.current_page_idx = 0  # 安全設定回第一頁
                    st.rerun()
                    break
