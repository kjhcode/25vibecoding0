import streamlit as st

# 페이지 설정
st.set_page_config(page_title="진로 유형 탐색기 🧭", page_icon="🎓", layout="centered")

st.title("🎓 너에게 맞는 미래 찾기! – 진로 유형 탐색기")
st.markdown("고등학교 2학년을 위한 진로 설계 도우미 💡")

# 질문 입력
st.header("📌 너의 선호를 알려줘!")

activity = st.selectbox(
    "1. 더 재미있게 느껴지는 활동은?",
    ["사람들과 이야기하기", "혼자 집중하는 작업", "현장체험·몸으로 하는 일", "아이디어를 기획하기"]
)

interest = st.selectbox(
    "2. 가장 관심 있는 분야는?",
    ["예술/디자인", "과학/기술", "인문/사회", "의료/보건", "경영/경제", "교육/상담"]
)

personality = st.selectbox(
    "3. 너를 더 잘 설명하는 말은?",
    ["감성적이고 따뜻함", "논리적이고 분석적임", "활동적이고 외향적임", "조용하고 신중함"]
)

# 추천 로직
recommendation = ""
if activity == "사람들과 이야기하기":
    if interest == "교육/상담":
        recommendation = "🧑‍🏫 **진로 추천:** 교사, 상담사, 청소년지도사 \n📚 관련 학과: 교육학과, 심리학과"
    elif interest == "경영/경제":
        recommendation = "💼 **진로 추천:** 마케팅 전문가, HR매니저, 세일즈 컨설턴트 \n📚 관련 학과: 경영학과, 커뮤니케이션학과"
    else:
        recommendation = "🌐 **진로 추천:** 기자, 사회복지사, 아나운서 \n📚 관련 학과: 사회학과, 신문방송학과"

elif activity == "혼자 집중하는 작업":
    if interest == "과학/기술":
        recommendation = "💻 **진로 추천:** 소프트웨어 개발자, 데이터 분석가 \n📚 관련 학과: 컴퓨터공학과, 정보통계학과"
    elif interest == "예술/디자인":
        recommendation = "🎨 **진로 추천:** 디지털 아티스트, 영상편집자 \n📚 관련 학과: 시각디자인학과, 미디어학과"
    else:
        recommendation = "📖 **진로 추천:** 연구자, 작가, 기획자 \n📚 관련 학과: 문예창작과, 언론정보학과"

elif activity == "현장체험·몸으로 하는 일":
    if interest == "의료/보건":
        recommendation = "🩺 **진로 추천:** 간호사, 응급구조사, 물리치료사 \n📚 관련 학과: 간호학과, 보건학과"
    elif interest == "과학/기술":
        recommendation = "🔧 **진로 추천:** 기계기술자, 로봇제작자 \n📚 관련 학과: 기계공학과, 메카트로닉스학과"
    else:
        recommendation = "🚒 **진로 추천:** 경찰, 소방관, 군인 \n📚 관련 학과: 경찰행정학과, 국방과학과"

elif activity == "아이디어를 기획하기":
    if interest == "예술/디자인":
        recommendation = "🎭 **진로 추천:** 광고기획자, 브랜드 디자이너 \n📚 관련 학과: 시각디자인학과, 미디어커뮤니케이션학과"
    elif interest == "경영/경제":
        recommendation = "📈 **진로 추천:** 창업가, 전략기획자 \n📚 관련 학과: 경영학과, 경제학과"
    else:
        recommendation = "🧠 **진로 추천:** UX디자이너, 교육콘텐츠 기획자 \n📚 관련 학과: 교육공학과, 콘텐츠학과"

# 결과 출력
st.subheader("🔍 너에게 어울리는 진로는?")
st.success(recommendation)

# 사이드바
with st.sidebar:
    st.header("📌 사용 팁")
    st.markdown("""
    - **수업시간 진로탐색 활동**으로 사용해보세요!
    - 친구들과 서로 다른 결과를 비교하며 이야기해도 재밌어요 😄
    - 결과를 바탕으로 관련 학과를 검색해보는 활동도 추천해요!
    """)

# 푸터
st.markdown("""
---
🧡 **진로는 나를 아는 것에서부터 시작돼요.**  
작은 선택이 모여 너만의 멋진 미래를 만들 거예요! 🚀
""")
