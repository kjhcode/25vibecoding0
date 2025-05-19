import streamlit as st

# 🎨 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 직업 추천 💼✨",
    page_icon="🧠",
    layout="centered"
)

# 🌈 헤더
st.markdown("""
# 💫 MBTI 기반 진로 추천 시스템 💼  
### 너의 성격을 알려줘! 내가 어울리는 직업을 찾아줄게요! 🧭✨  
""")

# 🎯 MBTI 리스트
mbti_types = [
    "INTJ 🧠", "INTP 💡", "ENTJ 👑", "ENTP 🎤",
    "INFJ 🌌", "INFP 🎨", "ENFJ 🌟", "ENFP 🔥",
    "ISTJ 📘", "ISFJ 🛡️", "ESTJ 🧱", "ESFJ 🎁",
    "ISTP 🔧", "ISFP 🌿", "ESTP 🕶️", "ESFP 🎉"
]

# 💼 추천 직업 사전
mbti_careers = {
    "INTJ": ["전략 컨설턴트 🧠", "데이터 과학자 📊", "UX 디자이너 🎯"],
    "INTP": ["연구원 🔬", "AI 개발자 🤖", "발명가 💡"],
    "ENTJ": ["CEO 🧑‍💼", "프로젝트 매니저 📋", "변호사 ⚖️"],
    "ENTP": ["창업가 🚀", "기획자 📈", "브랜딩 디렉터 🎨"],
    "INFJ": ["상담사 💬", "작가 ✍️", "심리학자 🧠"],
    "INFP": ["예술가 🎨", "작사가 📝", "교육자 📚"],
    "ENFJ": ["교사 🍎", "사회복지사 🤝", "리더십 코치 🎤"],
    "ENFP": ["배우 🎭", "광고 크리에이터 🖌️", "유튜버 📹"],
    "ISTJ": ["공무원 🏛️", "회계사 📊", "엔지니어 🛠️"],
    "ISFJ": ["간호사 💉", "초등교사 🧒", "도서관 사서 📚"],
    "ESTJ": ["경영 관리자 🧾", "군인 🪖", "프로젝트 리더 🧱"],
    "ESFJ": ["이벤트 플래너 🎀", "HR 매니저 🧑‍💼", "상담 교사 🎓"],
    "ISTP": ["기계공 🛠️", "응급 구조대원 🚑", "기술분석가 🧰"],
    "ISFP": ["디자이너 🎨", "플로리스트 💐", "사진작가 📸"],
    "ESTP": ["스포츠 코치 🏋️", "소방관 🔥", "비즈니스 개발자 📈"],
    "ESFP": ["엔터테이너 🎤", "메이크업 아티스트 💄", "무대 연출가 🎬"]
}

# 🧠 MBTI 선택
selected_mbti = st.selectbox("🎯 너의 MBTI를 골라줘!", mbti_types)

# ✨ 추천 결과
if selected_mbti:
    mbti_key = selected_mbti[:4]  # 이모지 제거용
    st.markdown(f"## 🌟 {selected_mbti}에게 어울리는 직업 추천 리스트 💼")

    for job in mbti_careers[mbti_key]:
        st.markdown(f"- {job}")

    st.success("💖 너에게 꼭 맞는 길을 찾길 바랄게요! 미래가 빛나길 🌠")

# 📌 사이드바
with st.sidebar:
    st.markdown("## 🎈 안내")
    st.markdown("이 앱은 성격 유형을 기반으로 적절한 진로를 추천해주는 진로교육용 도구입니다. ✨")
    st.markdown("교실에서, 진로상담 시간에, 또는 자기 탐색 활동 시간에 자유롭게 활용하세요! 💡")
    st.markdown("---")
    st.markdown("Made with ❤️ by 팬더님")

# 🐼 하단 메시지
st.markdown("""
---
🔮 **진로는 선택의 연속이야.  
중요한 건 너 자신을 잘 아는 것!  
MBTI는 너의 첫 걸음이야!** 🌈  
""")
