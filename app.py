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

# 💖 CSS 美化控制中心
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
        font-size: 24px !important;  /* 調整至適合手機的帥氣大字 */
        font-weight: bold !important;
        color: #5D4037 !important;
        letter-spacing: 2px !important;
        margin-bottom: 8px !important;
        white-space: nowrap !important; /* 強制絕不換行 */
    }

    .sub-title {
        font-size: 11px !important;  /* 微調字體，確保手機絕對能塞下一行 */
        color: #8D6E63 !important;
        white-space: nowrap !important; /* 強制絕不換行 */
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

    /* 6. 精美手帳字卡 */
    .anime-card {
        background-color: #FFFFFF !important;
        border: 3px solid #5D4037 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
        box-shadow: 5px 5px 0px #FFC1CC !important;
    }
    .anime-title {
        font-size:
