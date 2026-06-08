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

# --- 💖 初始化與儲存資料功能 💖 --- (保留原本的功能)
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

# --- 🎯 核心修改區塊：功能選單 🎯 ---
# 我們將功能選單移到上方，並在按下按鍵後利用 st.session_state 來重設選單狀態
# 這就像是把使用者的目光引導回「手帳譜」
mode = st.radio(
    "🧭 請選取手帳功能：",
    ["🌸 打开手帳庫 (看番紀錄)", "➕ 填寫新紀錄 (捕捉感動)", "📝 悄悄修改資料 (補上心情)", "🗑️ 揮揮手道別 (刪除紀錄)"],
    key="nav_radio",  # 為選單加上 key
    horizontal=True
)

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
    
    # 🎯 修改 1：「寫入晶片存檔」按鍵 🎯
    submit_btn = st.button("💝 寫入晶片存檔", type="primary")

    if submit_btn:
        if anime_name:
            anime_list.append([anime_name, anime_status, anime_author, anime_type, [], anime_review, anime_score])
            save_data()
            # 🍒 新增視覺反饋：成功訊息與圖示
            st.success(f"🌟 成功寫入存檔！✅ 「{anime_name}」已存入晶片。")
            
            # 🍒 核心邏輯：自動跳轉回手帳譜
            # 透過修改 key="nav_radio" 的值，來強制更改 radio 選單的選取項
            st.session_state.nav_radio = "🌸 打开手帳庫 (看番紀錄)"
            
            # 🍒 強制重整頁面，讓導向生效
            st.rerun()

# 功能 3：悄悄修改資料
elif mode == "📝 悄悄修改資料 (補上心情)":
    st.header("📝 悄悄修改資料")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        selected_name = st.selectbox("請選擇哪一部作品想翻修呢：", anime_names)
        for anime in anime_list:
            if anime[0] == selected_name:
                new_status = st.selectbox("新的追番狀態", ["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"], index=["🌟 想看很久了", "🔥 正在熱血追番", "🎉 已經完美看完", "💤 稍微休息停看"].index(anime[1]))
                new_review = st.text_area("更新心得點滴", value=anime[5])
                
                # 🎯 修改 2：「儲存新心情」按鍵 🎯
                update_btn = st.button("💝 儲存新心情")

                if update_btn:
                    anime[1] = new_status
                    anime[5] = new_review
                    save_data()
                    # 🍒 新增視覺反饋與跳轉
                    st.success(f"✨ 手帳更新成功！✅ 「{selected_name}」的心情已存入。")
                    st.session_state.nav_radio = "🌸 打开手帳庫 (看番紀錄)"
                    st.rerun()

# 功能 4：揮揮手道別
elif mode == "🗑️ 揮揮手道別 (刪除紀錄)":
    st.header("🗑️ 揮揮手道別")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        target_name = st.selectbox("選一個要揮揮手說再見的作品：", anime_names)
        
        # 🎯 修改 3：「確定斷捨離！」按鍵 🎯
        # 我們把按鍵加上一個 unique key，確保其運作
        delete_btn = st.button("💥 確定斷捨離！", type="primary", key="delete_confirm")

        if delete_btn:
            for anime in anime_list:
                if anime[0] == target_name:
                    anime_list.remove(anime)
                    save_data()
                    # 🍒 新增視覺反饋與跳轉
                    st.warning(f"🗑️ 已擦掉囉～ ✅ 「{target_name}」已從存檔移出。揮揮手道別！")
                    st.session_state.nav_radio = "🌸 打开手帳庫 (看番紀錄)"
                    st.rerun()
                    break

# --- 保留 CSS 美化控制中心與頂部招牌看板 (與原本一致) ---
# ... (下方程式碼省略，請保留主人原本寫好的部分)
