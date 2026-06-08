import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 CSS 魔法控制中心：直接把內建大圖切成 9 個會跳動的小方塊！
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

    /* 5. 核心：定義像素跳動動畫 */
    @keyframes pixelJump {
        0% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0); }
    }

    /* 6. 像素小人外框：固定 64x64 大小並套用跳動 */
    .hero-frame {
        display: inline-block;
        width: 64px;
        height: 64px;
        overflow: hidden;
        position: relative;
        background: transparent;
        animation: pixelJump 0.6s infinite ease-in-out;
    }

    /* 7. 切片核心：透過 object-fit 控制只顯示原圖的 1/3 區塊 */
    .hero-frame img {
        width: 192px !important;   /* 剛好是 64px * 3 欄 */
        height: 192px !important;  /* 剛好是 64px * 3 列 */
        max-width: none !important;
        object-fit: none !important;
        position: absolute;
    }

    /* 🎯 準確定位九宮格中每個小人的座標 */
    .pos-1 { left: 0px; top: 0px; }
    .pos-2 { left: -64px; top: 0px; }
    .pos-3 { left: -128px; top: 0px; }
    
    .pos-4 { left: 0px; top: -64px; }
    .pos-5 { left: -64px; top: -64px; }
    .pos-6 { left: -128px; top: -64px; }
    
    .pos-7 { left: 0px; top: -128px; }
    .pos-8 { left: -64px; top: -128px; }
    .pos-9 { left: -128px; top: -128px; }

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
        <div style="font-size: 22px; font-weight: bold; color: #5D4037; letter-spacing: 2px; margin-bottom: 15px;">
            👾 ANIME PIXEL DIARY 👾
        </div>
    """,
    unsafe_allow_html=True
)

# 偵測主人 GitHub 裡現有的圖片檔案名稱
img_path = "IMG_0417.jpeg" if os.path.exists("IMG_0417.jpeg") else "heroes.png"

# 如果找得到原圖，就直接在網頁內建進行會跳動的九宮格切片！
if os.path.exists(img_path):
    # 為了在純 HTML 裡讀取 Streamlit 本地圖片，轉為 base64 碼
    import base64
    with open(img_path, "rb") as image_file:
        encoded_img = base64.b64encode(image_file.read()).decode()
    img_src = f"data:image/jpeg;base64,{encoded_img}"

    # 第一排：前 3 位小英雄（錯開跳動時間）
    st.markdown('<div style="margin-bottom: 10px;">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.0s;"><img src="{img_src}" class="pos-1"></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.1s;"><img src="{img_src}" class="pos-2"></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.2s;"><img src="{img_src}" class="pos-3"></div>', unsafe_allow_html=True)

    # 第二排：中間 3 位小英雄
    st.markdown('<div style="margin-bottom: 10px;">', unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    with c4:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.15s;"><img src="{img_src}" class="pos-4"></div>', unsafe_allow_html=True)
    with c5:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.05s;"><img src="{img_src}" class="pos-5"></div>', unsafe_allow_html=True)
    with c6:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.25s;"><img src="{img_src}" class="pos-6"></div>', unsafe_allow_html=True)

    # 第三排：後 3 位小英雄
    st.markdown('<div style="margin-bottom: 10px;">', unsafe_allow_html=True)
    c7, c8, c9 = st.columns(3)
    with c7:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.3s;"><img src="{img_src}" class="pos-7"></div>', unsafe_allow_html=True)
    with c8:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.12s;"><img src="{img_src}" class="pos-8"></div>', unsafe_allow_html=True)
    with c9:
        st.markdown(f'<div class="hero-frame" style="animation-delay: 0.22s;"><img src="{img_src}" class="pos-9"></div>', unsafe_allow_html=True)
else:
    st.write("🌸 正在同步 GitHub 動漫晶片中...")

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
        anime_type = st.text_input("🏷️ 類型標籤")
        
    anime_review = st.text_area("📝 心得悄悄話")
    anime_score = st.slider("⭐ 推薦指數", 1, 5, 5)
    
    if st.button("💝 寫入晶片存檔", type="primary"):
        if anime_name:
            anime_list.append([anime_name, anime_status, anime_author, anime_type, [], anime_review, anime_score])
            save_data()
            st.success("🌟 成功寫入存檔！")
            st.rerun()

# 功能 3：悄悄修改資料
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

# 功能 4：揮揮手道別
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
                    st.success(f"🗑️ 已擦掉囉～")
                    st.rerun()
                    break
