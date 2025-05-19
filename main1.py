import streamlit as st

# 🛠 페이지 설정
st.set_page_config(page_title="MBTI 궁합 분석 💞", page_icon="🔮", layout="centered")

# 🎀 페이지 헤더
st.markdown("""
# 💖 MBTI 궁합 분석기 🔮  
### 성격 유형을 기반으로 '찰떡 궁합' 친구와 '어려운 친구'를 알려줄게요!  
**그리고, 어려운 친구랑 더 잘 지내는 법도 함께 알려줄게요!** 🌱🌟
""")

# 🎲 MBTI 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 💘 MBTI 궁합 정보 (간략 예시)
mbti_matches = {
    "INTJ": {
        "best": ["ENFP", "ENTP"],
        "worst": ["ESFP", "ISFP"],
        "tips": "감정 표현을 서툴 수 있어요. 감정 중심적인 친구에게는 솔직하고 따뜻한 언어로 다가가 보세요. 💌"
    },
    "ENFP": {
        "best": ["INFJ", "INTJ"],
        "worst": ["ISTJ", "ESTJ"],
        "tips": "논리보다 규칙을 중요시하는 친구들과는 갈등이 생길 수 있어요. 서로의 방식에 대해 이해하려는 대화가 필요해요! 🤝"
    },
    "ISFJ": {
        "best": ["ESFP", "ISFP"],
        "worst": ["ENTP", "INTP"],
        "tips": "너무 자유로운 친구들과는 계획의 차이로 갈등이 생겨요. 작은 규칙부터 함께 세워보는 게 좋아요. 📅"
    },
    "ENTP": {
        "best": ["INFJ", "INTJ"],
        "worst": ["ISFJ", "ISTJ"],
        "tips": "자유롭게 떠드는 걸 좋아하지만 조용한 친구도 있어요! 그들의 공간을 존중하며 천천히 다가가 보세요. 🕊️"
    },
    # 더 많은 유형은 필요 시 추가 가능
}

# 🧠 사용자 MBTI 선택
selected_mbti = st.selectbox("📌 너의 MBTI를 선택해보자!", mbti_list)

# ✨ 결과 출력
if selected_mbti in mbti_matches:
    best_matches = mbti_matches[selected_mbti]["best"]
    worst_matches = mbti_matches[selected_mbti]["worst"]
    tips = mbti_matches[selected_mbti]["tips"]

    st.markdown(f"## 🌟 {selected_mbti} 유형과의 궁합 정보")

    # 찰떡궁합
    st.markdown("### 💘 찰떡 궁합 유형")
    for b in best_matches:
        st.markdown(f"- {b} ❤️‍🔥")

    # 어려운 유형
    st.markdown("### 💦 친해지기 어려운 유형")
    for w in worst_matches:
        st.markdown(f"- {w} ⚡")

    # 친해지기 팁
    st.markdown("### 🌈 친해지는 팁 💡")
    st.info(tips)

# 📌 사이드바
with st.sidebar:
    st.markdown("## 🎈 이 앱은?")
    st.markdown("MBTI 궁합을 통해 친구를 더 깊이 이해하고, **어떻게 하면 다름을 이해할 수 있을까?**를 배우는 교육용 앱이에요. 💕")
    st.markdown("---")
    st.markdown("👩‍🏫 교실 활동, 진로 상담, 의사소통 수업에 활용 가능!")
    st.markdown("🧡 Made with 사랑 by 팬더님")

# 🎁 하단 명언
st.markdown("""
---
> **“다름은 틀림이 아니라, 새로운 세상을 여는 열쇠다.” 🔑**  
> - MBTI 궁합 분석기
""")
