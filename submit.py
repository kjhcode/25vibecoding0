import streamlit as st

# 페이지 설정
st.set_page_config(page_title="진로 유형 탐색기 🧭", page_icon="🎓", layout="centered")

# 🎆 첫화면 비주얼 효과
st.markdown(
    """
    <h1 style='text-align: center; color: #8e44ad; font-size: 3em;'>🌈 진로 유형 탐색기 🌈</h1>
    <h3 style='text-align: center; color: #2c3e50;'>너에게 어울리는 미래, 지금 만나보자! 🎓✨</h3>
    <p style='text-align: center; font-size: 20px; color: #16a085;'>
    고등학교 2학년을 위한 맞춤 진로 탐색 도우미 💼<br>
    너의 관심사, 성향, 활동 선호를 바탕으로 <strong>직업군 + 전공학과</strong>를 추천해줘!
    </p>
    <hr style='border: 1px solid #f39c12;'>
    """,
    unsafe_allow_html=True
)

# 질문 섹션
st.subheader("📌 너의 선호를 알려줘!")

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

# 결과 처리 로직
recommendation = ""
if activity == "사람들과 이야기하기":
    if interest == "교육/상담":
        recommendation = "🧑‍🏫 **추천 진로:** 교사, 상담사, 청소년지도사 \n📚 관련 학과: 교육학과, 심리학과"
    elif interest == "경영/경제":
        recommendation = "💼 **추천 진로:** 마케팅 전문가, 인사담당자 \n📚 관련 학과: 경영학과, 커뮤니케이션학과"
    else:
        recommendation = "🌐 **추천 진로:** 사회복지사, 기자, 홍보전문가 \n📚 관련 학과: 사회학과, 언론정보학과"

elif activity == "혼자 집중하는 작업":
    if interest == "과학/기술":
        recommendation = "💻 **추천 진로:** 소프트웨어 개발자, 데이터 분석가 \n📚 관련 학과: 컴퓨터공학과, 정보통계학과"
    elif interest == "예술/디자인":
        recommendation = "🎨 **추천 진로:** 일러스트레이터, 영상편집자 \n📚 관련 학과: 시각디자인학과, 콘텐츠학과"
    else:
        recommendation = "📖 **추천 진로:** 작가, 기획자 \n📚 관련 학과: 문예창작과, 미디어학과"

elif activity == "현장체험·몸으로 하는 일":
    if interest == "의료/보건":
        recommendation = "🩺 **추천 진로:** 간호사, 물리치료사 \n📚 관련 학과: 간호학과, 물리치료학과"
    elif interest == "과학/기술":
        recommendation = "🔧 **추천 진로:** 로봇공학자, 기계설계자 \n📚 관련 학과: 기계공학과, 메카트로닉스학과"
    else:
        recommendation = "🚓 **추천 진로:** 소방관, 군인, 경찰관 \n📚 관련 학과: 경찰행정학과, 국방과학과"

elif activity == "아이디어를 기획하기":
    if interest == "예술/디자인":
        recommendation = "🎭 **추천 진로:** 광고기획자, 브랜드 디자이너 \n📚 관련 학과: 시각디자인학과, 영상학과"
    elif interest == "경영/경제":
        recommendation = "📈 **추천 진로:** 창업가, 전략기획자 \n📚 관련 학과: 경영학과, 경제학과"
    else:
        recommendation = "🧠 **추천 진로:** UX디자이너, 교육콘텐츠 기획자 \n📚 관련 학과: 교육공학과, 콘텐츠학과"

# 결과 출력
st.subheader("🔍 너에게 어울리는 진로는?")
st.success(recommendation)

# 사이드바 안내
with st.sidebar:
    st.markdown("### 🌟 활용 Tip")
    st.markdown("""
    - 수업 시간 1:1 진로 설계 활동에 사용해 보세요.  
    - 친구들과 비교하고 토론하는 ‘진로 토크 활동’으로 확장해도 좋아요!  
    - 프로그래밍 수업에서는 직접 코드 수정해 나만의 진로 앱 만들어보기 💻
    """)

    st.markdown("### 👨‍🏫 확장 활동 예시")
    st.markdown("""
    - `생활기록부 자율활동`: *진로탐색 웹앱 제작 활동*  
    - `진로활동 기록`: *개인성향 기반 진로 설계 체험 및 공유*
    - `교과연계`: 정보(파이썬), 진로, 창체 수업 등과 연계 가능
    """)

# 푸터
st.markdown("""
---
🌈 **너만의 미래는 너만이 설계할 수 있어!**  
이 앱이 너의 진로 여정에 작은 등불이 되길 바래.  
_“가장 빛나는 길은 네가 즐기는 길이다.”_ ✨
""")
