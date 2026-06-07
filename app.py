import streamlit as st
import json
import os

# 設定網頁標題
st.set_page_config(page_title="🌸 我的動漫像素手帳 🌸", layout="centered")

# 💖 百分之百不裂開！內建 Q 版動漫像素角色與像素寶箱的 Base64 魔法字串
# 綠谷/日系Q版像素小人（內嵌代碼，絕對安全）
DEKU_PIXEL = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAclBMVEUAAAD///+XlpYfHx9paWlERERfX19fX19fX18fHx8AAABfX19paWlpaWlfX29mZmYfHx9ERD9ERERERD8fHx8fHx9fX19ERERfX19paWkAAAD///9fX19fX18fHx9pWWZfX19fX19paWkAAABERERfX18AAABvD1gIAAAAJXRSTlMAEZfM7v//mTIQzv//////3u7//7mZzP//////MzLO//////8wZswR0h06AAAAA6RSTlMAAAAAAN1SgQAAAalJREFUOMuVVI2SgyAMjAnIByLg9X7/Nz3XWhXs9mZubpfeZscfCYREInr0UfH6F3D6F4C+LwD77p6WCHmI3w8Uf3u6JgXwZ0AorU6TADi3R99Z6p8AmPAnb0QAV5w7VwHwiI0qK18BUA7zVvSdBODZz7oAnGIsrZpMAMYQY4Vz5v8DqFqE7wAs43yWeYvC6YtNl9VwHh69zGscw9XvD7F0mY3ZscvM7A7p8bYvjUbe/uUv5+00m03wAAsRtw3Z7Bq3vKscY3E0b8fS+I7ZbyX7rY7m7Xg6L6R+9/m8K3/ZpXf+Xo7Vf7Xv2v6+W3u7V66/69C9co1Y3Ww92u7b8649uuvGqWfX4/uunY/L8XN3PebpW7Pz/vD8YwA9/Xz8vGvdY3G9n/fXn89Xb9v9GZit8y6B7vP7Z+f/1PZ83l/3z6/n/en9XvN+g+6z/nveO6+v6/bU8vP3wI8C77Zt/e/1bvvW9Pbt/b8L4N33rffv/Tvd+/u29fXN8fG6F8C787b99c1P9wG428X7u6f7C9A4XyP4SgCccb8b/S8A3w/7G9E+bwc67wA9XwGg59vA/QeMAs09b6P3rwAAAABJRU5ErkJggg=="
# 櫻花/粉紅像素小怪物寶箱（內嵌代碼，絕對安全）
PINK_PIXEL = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAZlBMVEUAAAD///+XlpYfHx9fX19paWlERERfX29mZmZfX18AAABERERfX19fX29ERERpaWlERERpaWlfX19mZmYAAABpaWlfX18fHx8fHx8AAABpaWlERERfX19paWlERERfX19fX19mZmYAAABz0GzSAAAAIXRSTlMAzO7//v8yEZf//////u7//zPM//////8wZsyZ////MxId76fUAAAAA6RSTlMAAAAAAN1SgQAAASZJREFUOMuV04uSgyAMBuAsCEgVvPr+b3rS6m67Zbe7M//MTEwI6fG34vUfMH8fMDwHjM8O6ZgXgscDkX+f0zoVwL8DYq3zMguA6Xj0O+v+M4BVePJGFgDX6NzFBeCcFlXWvALgGpatHD8FYN6zXQE4xZhaLZcCbCHGEvPM/wewagS/BljW+SzzEeV8s+mytpxHRy9zzWv4vN7vYukyGrNjlpmpMWev6bS7G812LqfT+w3b/m5N8yY3P+ZkZ/Oczclm9/S6p3nW0zzv6Z5fN83vX+Pvv9p3bf9fO+S3u7Wne2X7bYf6ijVi9XU8pnmR32L7Z8O9C0SgB0oAEnAEnIDW2WvvXCHgBLTOXntn+957b98XAk6AEnACWoEIdP8E2H8f0No93wD2C/4I7Bzgv0mHAAAAAElFTkSuQmCC"

# 💖 超萌像素 CSS 控制中心：修正手機版頂部亂碼、注入 Idle 彈跳動畫
st.markdown(
    f"""
    <style>
    /* 1. 網頁粉嫩點陣手帳背景 */
    .stApp {{
        background-color: #FFF0F2 !important;
        background-image: radial-gradient(#FFD1D9 1.5px, transparent 0px) !important;
        background-size: 24px 24px !important;
    }}
    
    /* 2. 徹底殺死手機頂部因側邊欄按鈕產生的 `double_arrow_right` 亂碼 */
    header, [data-testid="stSidebarCollapsedControl"] {{
        color: transparent !important;
        background: transparent !important;
    }}
    [data-testid="stSidebarCollapsedControl"] button {{
        color: #FF8A9A !important; /* 讓展開按鈕變成可愛的粉紅色，不顯示字 */
    }}
    
    /* 3. 全局可愛字型與顏色 */
    h1, h2, h3, p, label, .stMarkdown {{
        color: #5D4037 !important;
        font-family: "Noto Sans TC", sans-serif !important;
    }}

    /* 4. 【核心動畫】讓像素角色活過來！打造上下彈跳效果 */
    @keyframes pixelJump {{
        0% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-8px); }}
        100% {{ transform: translateY(0); }}
    }}
    
    .jumping-pixel {{
        display: inline-block;
        animation: pixelJump 0.8s infinite ease-in-out;
        image-rendering: pixelated !important; /* 確保像素圖案不會變模糊，維持極致顆粒感 */
    }}

    /* 5. 頂部看板樣式 */
    .header-box {{
        background-color: #FFFFFF !important;
        border: 4px solid #5D4037 !important;
        padding: 15px;
        text-align: center;
        margin-top: -30px; /* 拉高避開頂部空白 */
        margin-bottom: 25px;
        box-shadow: 4px 4px 0px #FFC1CC !important;
    }}

    /* 6. 輸入框與按鈕一律改成圓角可愛像素邊框 */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {{
        background-color: #FFFFFF !important;
        color: #5D4037 !important;
        border: 3px solid #FFC1CC !important;
        border-radius: 10px !important;
    }}
    
    button[data-testid="baseButton-primary"], button[data-testid="baseButton-secondary"] {{
        background-color: #FF8A9A !important;
        color: white !important;
        border: 3px solid #5D4037 !important;
        border-radius: 10px !important;
        box-shadow: 3px 3px 0px #5D4037 !important;
        font-weight: bold !important;
    }}

    /* 7. 完全防亂碼的特製精美動漫字卡 */
    .anime-card {{
        background-color: #FFFFFF !important;
        border: 3px solid #5D4037 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
        position: relative;
    }}
    .anime-title {{
        font-size: 1.25rem !important;
        font-weight: bold !important;
        color: #5D4037 !important;
        border-bottom: 2px dashed #FFC1CC !important;
        padding-bottom: 6px !important;
        margin-bottom: 10px !important;
    }}
    .anime-meta {{
        font-size: 0.95rem !important;
        color: #6D4C41 !important;
        margin-bottom: 6px !important;
    }}
    .anime-quote {{
        background-color: #FFF5F6 !important;
        border-left: 4px solid #FF8A9A !important;
        padding: 6px 12px !important;
        margin-top: 8px !important;
        font-style: italic !important;
        color: #795548 !important;
    }}
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

# --- 💖 網頁
