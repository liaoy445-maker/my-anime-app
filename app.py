import streamlit as st
import json
import os

# 設定網頁標題與分頁圖標
st.set_page_config(page_title="🌸 我的動漫手帳 🌸", layout="centered")

# 💖 終極魔法：強行注入粉嫩粉嫩的櫻花主題樣式 💖
st.markdown(
    """
    <style>
    /* 整個網頁的超級大背景 */
    .stApp {
        background-color: #FFF0F2 !important;
    }
    /* 側邊欄的粉嫩底色 */
    [data-testid="stSidebar"] {
        background-color: #FFE3E7 !important;
    }
    /* 所有大大小小的文字通通變成溫柔的深棕色 */
    h1, h2, h3, p, label, .stMarkdown, span {
        color: #5D4037 !important;
        font-family: "Helvetica Neue", Arial, "Noto Sans TC", sans-serif !important;
    }
    /* 輸入框的可愛邊框與底色 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 2px solid #FFC1CC !important;
        border-radius: 10px !important;
    }
    /* 讓展開卡片也變得白白嫩嫩 */
    .stExpander {
        background-color: #FFFFFF !important;
        border: 2px solid #FFE3E7 !important;
        border-radius: 12px !important;
        box-shadow: 0px 4px 10px rgba(255, 193, 204, 0.2) !important;
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

# --- 💖 網頁畫面內容 💖 ---
st.title("ฅ•ω•ฅ 櫻花飄飄動漫記錄手帳 🌸")
st.caption("歡迎來到主人的追番秘密基地！在這裡記錄下每一份熱血、眼淚與心動吧 💖✨")

# 左側導覽選單
mode = st.sidebar.radio(
    "🎀 祕密基地傳送門",
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
    st.subheader("把今天看番的感動通通鎖進手帳裡吧 📒💞")
    
    col1, col2 = st.columns(2)
    with col1:
        anime_name = st.text_input("🍒 作品名稱", placeholder="例如：約會大作戰")
        anime_author = st.text_input("✍️ 厲害的作者", placeholder="例如：橘公司老師")
    with col2:
        anime_status = st.selectbox("🎯 目前進度", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"])
        anime_type = st.text_input("🏷️ 類型標籤", placeholder="例如：純愛、戰鬥、後宮番")
        
    anime_review = st.text_area("📝 心得悄悄話", placeholder="偷偷寫下你對這部作品的滿滿想法...")
    anime_score = st.slider("⭐ 萌度/推薦指數大評分", 1, 5, 5)
    
    st.subheader("💬 本作神台詞（最多可以寫三句喔！）")
    q1 = st.text_input("🌈 第一句神台詞", placeholder="震撼心靈的名台詞 1")
    q2 = st.text_input("✨ 第二句神台詞", placeholder="名台詞 2")
    q3 = st.text_input("🌸 第三句神台詞", placeholder="名台詞 3")
    
    st.write("")
    if st.button("💝 點我！一鍵傳送入手帳本本", type="primary"):
        if anime_name:
            quotes_box = []
            for q in [q1, q2, q3]:
                if q.strip():
                    quotes_box.append(q.strip())
                    
            anime_list.append([
                anime_name, anime_status, anime_author, anime_type,
                quotes_box, anime_review, anime_score
            ])
            save_data()
            st.success(f" 🌟 嗶嗶！【{anime_name}】已經成功被小精靈收進手帳本本囉！(•̀ᴗ•́)و ̑̑")
        else:
            st.error("❌ 哇哇！主人忘記填寫「作品名稱」了啦，小精靈沒辦法存檔 Q_Q")

# 功能 2：查看與模糊查找
elif mode == "🌸 打開手帳本本 (翻閱/搜尋)":
    st.header("🔍 翻閱我的動漫手帳庫")
    
    search_keyword = st.text_input("🔮 全宇宙模糊大搜尋：", placeholder="搜尋名稱、標籤、神台詞或心得...")
    
    if anime_list:
        found_any = False
        for anime in anime_list:
            all_quotes_text = "".join(anime[4])
            
            if not search_keyword or (
                search_keyword in anime[0] or search_keyword in anime[1] or
                search_keyword in anime[2] or search_keyword in anime[3] or
                search_keyword in all_quotes_text or search_keyword in anime[5] or
                str(anime[6]) in search_keyword
            ):
                found_any = True
                stars = "⭐" * anime[6]
                
                with st.expander(f"🎬 {anime[0]} （{anime[1]} · {stars}）"):
                    st.write(f"**✍️ 創作者：** {anime[2]} | **🏷️ 作品標籤：** {anime[3]}")
                    st.write(f"**💌 心得點滴：** {anime[5] if anime[5] else '（目前空空如也，等待主人填寫中...）'}")
                    if anime[4]:
                        st.write("**💖 命中注定的神台詞：**")
                        for q in anime[4]:
                            st.info(f"✨ 「 {q} 」")
        if not found_any:
            st.warning(f"🥺 咦？雷達找不到符合【{search_keyword}】的動漫紀錄耶...")
    else:
        st.info("🎈 手帳本本目前空空的耶！快點左邊選單的「➕ 填寫新紀錄」來填滿它吧～")

# 功能 3：修改動漫
elif mode == "📝 悄悄修改資料 (補上心情)":
    st.header("📝 悄悄修改資料")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        selected_name = st.selectbox("請選擇哪一部作品想翻修呢：", anime_names)
        
        for anime in anime_list:
            if anime[0] == selected_name:
                st.write(f"正在為【{selected_name}】重新裝飾中：")
                new_status = st.selectbox("新的追番狀態", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"], index=["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"].index(anime[1]) if anime[1] in ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"] else 0)
                new_review = st.text_area("更新心得點滴", value=anime[5])
                
                if st.button("💝 敲定！儲存新心情"):
                    anime[1] = new_status
                    anime[5] = new_review
                    save_data()
                    st.success("✨ 耶！手帳更新成功，小精靈已經重新貼上漂亮的貼紙了！")
                    st.rerun()
    else:
        st.info("🥺 目前沒有資料可以修改唷。")

# 功能 4：刪除動漫
elif mode == "🗑️ 揮揮手道別 (刪除紀錄)":
    st.header("🗑️ 揮揮手道別")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        target_name = st.selectbox("選一個要揮揮手說再見的作品：", anime_names)
        
        st.warning(f"⚠️ 哇！真的要讓【{target_name}】消失在手帳本本裡嗎？消失了就找不回來囉！")
        if st.button("💥 沒關係，確定斷捨離！", type="primary"):
            for anime in anime_list:
                if anime[0] == target_name:
                    anime_list.remove(anime)
                    save_data()
                    st.success(f"🗑️ 橡皮擦擦擦！【{target_name}】已經從手帳中輕輕擦掉囉～")
                    st.rerun()
                    break
    else:
        st.info("🥺 目前沒有資料可以刪除唷。")
