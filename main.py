import streamlit as st
import random

# ✅ 반드시 Streamlit 관련 코드 중 가장 위에 위치
st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="🌈", layout="wide")

# 이후에는 어떤 Streamlit 코드든 자유롭게 사용 가능
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌟 MBTI 기반 진로 추천 웹앱 🌟")
