import streamlit as st
import json
import os

# 設定網頁標題與分頁圖標
st.set_page_config(page_title="🌸 我的動漫手帳 🌸", layout="centered")

# 💖 安全美化魔法：只調整色彩與基礎框線，保證乾淨、無亂碼
st.markdown(
    """
    <style>
    /* 網頁整體粉嫩點陣背景 */
    .stApp {
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1px, transparent 0px) !important;
        background-size: 20px 20px !important;
    }
    /* 側邊欄變成櫻花粉色 */
    [data-testid="stSidebar"] {
        background-color: #FFE3E7 !important;
    }
    /* 限制所有文字為深棕色，但絕不強制覆蓋系統圖標的字型族群 */
    h1, h2, h3, p, label, .stMarkdown {
        color: #5D4037 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }
    /* 輸入框加上粉紅邊框 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 2px solid #FFC1CC !important;
        border-radius: 8px !important;
    }
    /* 按鈕變成草莓粉色 */
    button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {
        background-color: #FF8A9A !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
    }
    
    /* 自訂動漫卡片樣式：白底、粉紅細邊框、帶有柔和陰影 */
    .anime-card {
        background-color: #FFFFFF !important;
        border: 2px solid #FFC1CC !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 3px 3px 0px #FFD1D9 !important;
    }
    .anime-title {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        margin-bottom: 8px !important;
        border-bottom: 1px dashed #FFC1CC !important;
        padding-bottom: 4px !important;
    }
    .anime-meta {
        font-size: 0.9rem !important;
        color: #8D6E63 !important;
        margin-bottom: 6px !important;
    }
    .anime-quote {
        background-color: #FFF9FA !important;
        border-left: 4px solid #FF8A9A !important;
        padding: 6px 10px !important;
        margin-top: 5px !important;
        font-style: italic !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 檔案儲存路徑
FILE_NAME = "anime_data_web.json"

# 自動讀取現有資料
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

# --- 網頁頂部可愛顏文字裝飾 ---
st.write("🛸 ☁️ 🦄 ☁️ 🎈 ☁️")
st.write("👾 (つ >ω●)つ 🍓【 PIXEL ANIME NOTE 】🍓 ⊂(●ω< つ) 👾")

st.title("ฅ•ω•ฅ 我的動漫手帳 🌸")
st.caption("✨ 歡迎來到主人的二次元秘密基地！功能已經完整復活囉！ ✨")

# --- 側邊欄選單 ---
st.sidebar.write("👩‍🎤【 像素動漫娘軍團 】")
st.sidebar.write(" (🎀•͈ᴗ•͈) 🌟 (•̀ᴗ•́)و ̑̑ 🌟 (🎉'ω')")

mode = st.sidebar.radio(
    "🎀 祕密基地功能選單",
    [
        "🌸 打開手帳本本 (翻閱/搜尋)", 
        "➕ 填寫新紀錄 (捕捉感動)", 
        "📝 悄悄修改資料 (補上心情)", 
        "🗑️ 揮揮手道別 (刪除紀錄)"
    ]
)

# 功能 1：填寫新紀錄
if mode == "➕ 填寫新紀錄 (捕捉感動)":
    st.header("✨ 填寫新紀錄")
    
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
    q1 = st.text_input("🌈 第一句神台詞", placeholder="震撼心靈的名台詞 1")
    
    st.write("")
    if st.button("💝 一鍵傳送入手帳本本", type="primary"):
        if anime_name:
            quotes_box = [q1.strip()] if q1.strip() else []
            anime_list.append([
                anime_name, anime_status, anime_author, anime_type,
                quotes_box, anime_review, anime_score
            ])
            save_data()
            st.success("🌟 成功收進手帳本本囉！")
            st.rerun()
        else:
            st.error("❌ 忘記填寫作品名稱了啦！")

# 功能 2：查看與搜尋（重新設計卡片輸出，徹底防亂碼）
elif mode == "🌸 打開手帳本本 (翻閱/搜尋)":
    st.header("🔍 翻閱我的動漫手帳庫")
    search_keyword = st.text_input("🔮 全宇宙模糊大搜尋：", placeholder="搜尋名稱、標籤...")
    
    if anime_list:
        for anime in anime_list:
            if not search_keyword or search_keyword in anime[0] or search_keyword in anime[3]:
                stars = "⭐" * anime[6]
                
                # 建立純 HTML 的精美卡片，繞過 Streamlit 的圖態引擎，根除文字重疊
                quote_html = f"<div class='anime-quote'>✨ 「 {anime[4][0]} 」</div>" if anime[4] else ""
                
                card_content = f"""
                <div class="anime-card">
                    <div class="anime-title">🎬 {anime[0]} （{anime[1]} · {stars}）</div>
                    <div class="anime-meta"><b>✍️ 創作者：</b> {anime[2]} | <b>🏷️ 標籤：</b> {anime[3]}</div>
                    <div class="anime-meta"><b>💌 心得：</b> {anime[5]}</div>
                    {quote_html}
                </div>
                """
                st.markdown(card_content, unsafe_allow_html=True)
    else:
        st.info("🎈 手帳目前空空的，快去功能選單點「➕ 填寫新紀錄」吧！")

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
