import streamlit as st
import random

# 💖 페이지 구성
st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="🌈", layout="wide")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    }
    .stApp {
        background-color: #fff0f5;
    }
    h1 {
        color: #8a2be2;
        font-size: 3em;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .emoji {
        font-size: 1.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 제목
st.markdown("# 🌟 나의 MBTI로 찾는 ✨꿈의 직업✨")
st.markdown("### 💬 아래에서 자신의 MBTI를 선택해 보세요! 흥미로운 직업이 기다리고 있어요! 😎")

# 📊 MBTI 선택
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("🔍 나의 MBTI는?", mbti_list)

# 🎯 추천 직업 데이터
job_recommendations = {
    "ISTJ": ["📊 회계사", "⚖️ 공무원", "🏢 행정 전문가", "💼 금융 분석가", "🧮 세무사"],
    "ISFJ": ["👩‍🏫 교사", "🏥 간호사", "👩‍👧‍👦 사회복지사", "🛡️ 보건행정직", "📚 사서"],
    "INFJ": ["🧠 심리상담사", "📝 작가", "🎨 예술가", "🧘‍♀️ 명상 지도사", "📖 교육 연구자"],
    "INTJ": ["🧪 연구원", "💻 프로그래머", "📊 전략 기획자", "🏦 데이터 사이언티스트", "🛰️ AI 전문가"],
    "ISTP": ["🔧 기술 엔지니어", "🛠️ 정비사", "🚓 경찰", "✈️ 항공정비사", "🕹️ 드론 전문가"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎭 배우", "🍰 제과제빵사", "🎼 음악가"],
    "INFP": ["📚 시인", "🎨 일러스트레이터", "👩‍🏫 문학 교사", "🌿 환경운동가", "✍️ 칼럼니스트"],
    "INTP": ["💻 개발자", "📊 통계분석가", "🧬 생명과학자", "📡 빅데이터 전문가", "🚀 항공우주 엔지니어"],
    "ESTP": ["🎤 방송인", "🕵️ 형사", "📦 물류 관리자", "🚀 스타트업 창업자", "🏋️‍♂️ 운동 트레이너"],
    "ESFP": ["🎤 가수", "🎥 유튜버", "💄 뷰티 크리에이터", "🛍️ 패션 스타일리스트", "🎪 이벤트 플래너"],
    "ENFP": ["🌍 사회운동가", "🎤 강연가", "📝 콘텐츠 크리에이터", "📱 마케팅 전문가", "🌟 브랜드 기획자"],
    "ENTP": ["🚀 스타트업 CEO", "🧠 컨설턴트", "📣 광고기획자", "📊 혁신 전략가", "🎮 게임 개발자"],
    "ESTJ": ["🏛️ 공기업 관리자", "📝 프로젝트 매니저", "📦 물류전문가", "💼 인사담당자", "📊 품질 관리자"],
    "ESFJ": ["👩‍🏫 유아교육 교사", "🏥 간호사", "📞 고객상담원", "🛒 매장 관리자", "🏠 케어매니저"],
    "ENFJ": ["🎓 교육컨설턴트", "🧭 코치", "🧑‍🤝‍🧑 NGO 활동가", "📢 커뮤니케이터", "🌟 사회 리더"],
    "ENTJ": ["🏛️ 기업 CEO", "📈 투자전문가", "🧠 전략 컨설턴트", "🧪 기술 창업자", "🧑‍💼 조직 리더"]
}

if mbti:
    st.markdown(f"## 🎯 {mbti} 유형에게 어울리는 직업 추천 💼")
    jobs = job_recommendations.get(mbti, [])
    for job in jobs:
        st.markdown(f"👉 {job}")

# 🎨 푸터 이모지 뿌리기
st.markdown("---")
st.markdown("#### 🤖 MBTI 기반 진로 추천 웹앱")
st.markdown("##### 만든이: 팬더님 ✨ | 디자인도 교육도 완벽하게 🐼💖")
st.markdown("🌸🌼🌺🌻🌷🌹💐🪻🦋🌈✨💫🎇🎆🪄")
