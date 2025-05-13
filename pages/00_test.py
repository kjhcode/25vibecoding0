
import streamlit as st
import random

# 이모지 테마 설정
mbti_emojis = {
    "ENFP": "🌈✨🎨🧠🎉",
    "INFJ": "🌌📚🕊️🔮🧘",
    "ESTJ": "📊💼🛠️📈🔧",
    "ISFP": "🍃🎨🎧🐾🌸",
    "INTJ": "🧠📘📐♟️🌑",
    "ESFP": "🎉🎤🎈🌟💃",
    "ISTJ": "📏🗂️🏛️🧾📚",
    "INFP": "🦄📖🕯️🎼🌻",
    "ENTP": "🚀🎭🧩💡🌪️",
    "ISFJ": "🌷🍪🧺🏡📋",
    "ENTJ": "🦁📊🎯🏆⚖️",
    "INTP": "🧬🔍💻📖🧠",
    "ESFJ": "🎁🎀🧁👩‍🍳🫶",
    "ISTP": "🔧🛠️🏍️💣🧊",
    "ENFJ": "🕊️🎤📢🌟🤝",
    "ESTP": "🏎️🔥🎯💥🎲"
}

# 추천 직업 목록
career_recommendations = {
    "ENFP": ["광고기획자", "작가", "홍보 전문가", "방송인"],
    "INFJ": ["심리상담가", "작가", "교육자", "사회운동가"],
    "ESTJ": ["경영자", "정책분석가", "군인", "프로젝트 매니저"],
    "ISFP": ["디자이너", "사진작가", "수의사", "플로리스트"],
    "INTJ": ["데이터 과학자", "전략기획가", "연구원", "AI 개발자"],
    "ESFP": ["연예인", "이벤트 플래너", "뮤지션", "운동선수"],
    "ISTJ": ["회계사", "공무원", "법률 전문가", "기록관리자"],
    "INFP": ["시인", "예술가", "상담사", "교육 콘텐츠 기획자"],
    "ENTP": ["기업가", "혁신가", "방송작가", "발명가"],
    "ISFJ": ["간호사", "사회복지사", "보육교사", "행정직 공무원"],
    "ENTJ": ["CEO", "변호사", "정치가", "프로젝트 디렉터"],
    "INTP": ["철학자", "개발자", "이론 물리학자", "AI 엔지니어"],
    "ESFJ": ["간호사", "영양사", "교사", "이벤트 코디네이터"],
    "ISTP": ["기계공", "기술자", "응급 구조사", "탐험가"],
    "ENFJ": ["교육자", "연설가", "NGO 활동가", "리더십 코치"],
    "ESTP": ["세일즈맨", "운동선수", "경찰관", "파일럿"]
}

st.set_page_config(page_title="🌟 MBTI 진로 추천기 🌟", page_icon="🧭", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>💖 MBTI 기반 진로 추천 사이트 💖</h1>
    <p style='text-align: center; font-size: 20px;'>당신의 성격 유형에 맞는 찰떡 직업을 추천해드립니다! ✨💼🎯</p>
""", unsafe_allow_html=True)

mbti_types = list(mbti_emojis.keys())
selected_mbti = st.selectbox("💌 MBTI를 선택하세요!", ["-- 선택하세요 --"] + mbti_types)

if selected_mbti and selected_mbti != "-- 선택하세요 --":
    selected_mbti_emojis = mbti_emojis[selected_mbti]
    st.markdown(f"### {selected_mbti_emojis} {selected_mbti} 유형에게 어울리는 직업은...")
    recommended_jobs = career_recommendations[selected_mbti]
    for job in recommended_jobs:
        st.success(f"✨ {job}")

    st.markdown("""
        <div style='text-align: center; margin-top: 30px;'>
            <h2>🌟 당신의 미래를 응원합니다! 🌈</h2>
            <p style='font-size:18px;'>더 많은 진로 정보를 원한다면 선생님께 상담을 신청해보세요! 🧑‍🏫👩‍🏫</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>🎓 이 웹앱은 교육 목적으로 제작되었습니다 🎓</p>
""", unsafe_allow_html=True)
