import streamlit as st
import json
import os

# 設定網頁主題與標題
st.set_page_config(page_title="🌸 我的動漫手帳 🌸", layout="centered")

# 檔案要存在雲端電腦裡的名字
FILE_NAME = "anime_data_web.json"

# 1. 【自動讀檔】
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        st.session_state.anime_list = json.load(f)
else:
    if "anime_list" not in st.session_state:
        st.session_state.anime_list = []

anime_list = st.session_state.anime_list

# 💾 儲存檔案的小幫手
def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(anime_list, f, ensure_ascii=False, indent=4)

# --- 網頁畫面美化開始 ---
st.title("ฅ•ω•ฅ 我的動漫記錄手帳")
st.caption("專屬於你的追番小天地，記錄每一份熱血與感動 ✨")

# 左側導覽選單（取代原本的文字選單）
mode = st.sidebar.radio(
    "功能選單",
    ["🌸 看我的手帳 (查找/列表)", "➕ 新增動漫紀錄", "📝 修改動漫資料", "🗑️ 刪除動漫紀錄"]
)

# 功能 1：新增動漫
if mode == "➕ 新增動漫紀錄":
    st.header("✨ 新增動漫紀錄")
    
    # 網頁輸入框，排版超整齊
    col1, col2 = st.columns(2)
    with col1:
        anime_name = st.text_input("🌸 動漫名稱", placeholder="例如：約會大作戰")
        anime_author = st.text_input("✍️ 動漫作者", placeholder="例如：橘公司")
    with col2:
        anime_status = st.selectbox("✨ 觀看狀態", ["想看", "正在看", "已看完", "暫停觀看"])
        anime_type = st.text_input("🏷️ 動漫類型", placeholder="例如：後宮番、熱血")
        
    anime_review = st.text_area("📝 觀後心得", placeholder="寫下你對這部作品的想法...")
    anime_score = st.slider("⭐ 個人評分", 1, 5, 5) # 帥氣的拉桿評分
    
    st.subheader("💬 本作金句（可輸入多句）")
    
    # 在網頁版中，我們直接給主人 3 個輸入框，不用再打 0 迴圈
    q1 = st.text_input("金句 1", placeholder="神台詞 1")
    q2 = st.text_input("金句 2", placeholder="神台詞 2 (選填)")
    q3 = st.text_input("金句 3", placeholder="神台詞 3 (選填)")
    
    if st.button("🎉 點我存入手帳", type="primary"):
        if anime_name:
            # 整理金句箱子
            quotes_box = []
            for q in [q1, q2, q3]:
                if q.strip():
                    quotes_box.append(q.strip())
                    
            # 打包大箱子
            anime_list.append([
                anime_name, anime_status, anime_author, anime_type,
                quotes_box, anime_review, anime_score
            ])
            save_data() # 存檔
            st.success(f"💖 【{anime_name}】已經成功寫入手帳囉！")
        else:
            st.error("❌ 請至少輸入動漫名稱喔！")

# 功能 2：查看與模糊查找
elif mode == "🌸 看我的手帳 (查找/列表)":
    st.header("🔍 我的動漫手帳庫")
    
    search_keyword = st.text_input("🔍 輸入任意關鍵字進行全宇宙大搜尋：", placeholder="搜尋名稱、類型、金句或心得...")
    
    if anime_list:
        found_any = False
        for anime in anime_list:
            all_quotes_text = "".join(anime[4])
            
            # 檢查是否符合關鍵字（若沒輸入關鍵字就秀出全部）
            if not search_keyword or (
                search_keyword in anime[0] or search_keyword in anime[1] or
                search_keyword in anime[2] or search_keyword in anime[3] or
                search_keyword in all_quotes_text or search_keyword in anime[5] or
                str(anime[6]) in search_keyword
            ):
                found_any = True
                # 用網頁漂亮的「卡片 (Expander)」排版呈現
                with st.expander(f"🎬 {anime[0]} （{anime[1]} · ⭐{anime[6]}星）"):
                    st.write(f"**✍️ 作者：** {anime[2]} | **🏷️ 類型：** {anime[3]}")
                    st.write(f"**📝 觀後心得：** {anime[5] if anime[5] else '暫無'}")
                    if anime[4]:
                        st.write("**💬 本作金句：**")
                        for q in anime[4]:
                            st.info(f"👉 {q}")
        if not found_any:
            st.warning(f"找不到符合【{search_keyword}】的動漫紀錄喔。")
    else:
        st.info("手帳空空如也，快去左邊選單點選「➕ 新增動漫紀錄」吧！")

# 功能 3：修改動漫
elif mode == "📝 修改動漫資料":
    st.header("📝 修改動漫資料")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        selected_name = st.selectbox("請選擇你想修改的作品：", anime_names)
        
        # 找出那部動漫
        for anime in anime_list:
            if anime[0] == selected_name:
                st.write(f"正在修改【{selected_name}】的資料：")
                new_status = st.selectbox("新觀看狀態", ["想看", "正在看", "已看完", "暫停觀看"], index=["想看", "正在看", "已看完", "暫停觀看"].index(anime[1]))
                new_review = st.text_area("新觀後心得", value=anime[5])
                
                if st.button("💾 儲存修改"):
                    anime[1] = new_status
                    anime[5] = new_review
                    save_data()
                    st.success("✨ 資料更新成功！")
                    st.rerun()
    else:
        st.info("目前沒有資料可以修改喔。")

# 功能 4：刪除動漫
elif mode == "🗑️ 刪除動漫紀錄":
    st.header("🗑️ 刪除動漫紀錄")
    if anime_list:
        anime_names = [anime[0] for anime in anime_list]
        target_name = st.selectbox("請選擇你想刪除的作品：", anime_names)
        
        st.warning(f"確定要刪除【{target_name}】嗎？刪除後資料就找不回來囉！")
        if st.button("💥 確定刪除", type="primary"):
            for anime in anime_list:
                if anime[0] == target_name:
                    anime_list.remove(anime)
                    save_data()
                    st.success(f"🗑️ 已將【{target_name}】從手帳中徹底移除！")
                    st.rerun()
                    break
    else:
        st.info("目前沒有資料可以刪除喔。")
