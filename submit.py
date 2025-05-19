import streamlit as st
import pandas as pd
import random

# 설정
st.set_page_config(page_title="진로탐색 도우미", page_icon="🎓", layout="centered")

# -------------------------------
# 1. 화려한 첫 화면
# -------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🌟 고2 진로 선택 맞춤 가이드 🌟</h1>
    <h3 style='text-align: center; color: #306998;'>MBTI 기반 진로 탐색부터 대입 전략까지 한 번에!</h3>
    <div style='text-align: center;'>
        <img src='https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif' width='300'>
    </div>
    <br>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------
# 2. MBTI 선택
# -------------------------------
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 예시 데이터: MBTI → 직업군
mbti_jobs = {
    "INTJ": ["데이터 과학자", "AI 연구원"],
    "ENFP": ["광고기획자", "브랜드 디자이너"],
    "ISFJ": ["간호사", "사회복지사"],
    "ESTP": ["세일즈 매니저", "스타트업 CEO"],
    "INTP": ["빅데이터 분석가", "IT 컨설턴트"],
    "ENTJ": ["경영전략 컨설턴트", "창업가"],
    "INFJ": ["심리상담사", "기획연구원"],
    "INFP": ["시인", "작가"],
    "ENFJ": ["교육컨설턴트", "NGO 활동가"],
    "ENFP": ["마케팅 디렉터", "브랜딩 전문가"],
    "ISTJ": ["공무원", "회계사"],
    "ESTJ": ["프로젝트 매니저", "생산관리자"],
    "ESFJ": ["사회복지사", "병원코디네이터"],
    "ISTP": ["기계공학자", "항공정비사"],
    "ISFP": ["플로리스트", "공간디자이너"],
    "ESFP": ["이벤트 기획자", "엔터테인먼트 매니저"],
  
}
jobs = mbti_jobs.get(mbti, ["직업 데이터 없음"])

selected_job = st.selectbox(f"{mbti} 유형에게 추천하는 직업군:", jobs)

# -------------------------------
# 3. 직업군 → 관련 학과
# -------------------------------
job_to_majors = {
    "데이터 과학자": ["컴퓨터공학과", "통계학과", "AI학과"],
    "AI 연구원": ["인공지능학과", "소프트웨어학과"],
    "광고기획자": ["광고홍보학과", "시각디자인학과"],
    "브랜드 디자이너": ["산업디자인과", "커뮤니케이션디자인과"],
    "간호사": ["간호학과"],
    "사회복지사": ["사회복지학과"],
    "세일즈 매니저": ["경영학과", "마케팅학과"],
    "스타트업 CEO": ["창업학과", "벤처경영학과"]
}
majors = job_to_majors.get(selected_job, ["해당 학과 없음"])
selected_major = st.selectbox(f"'{selected_job}'이 되기 위해 추천하는 학과:", majors)

# -------------------------------
# 4. 학과 → 해당 대학 목록
# -------------------------------
major_to_universities = {
    "컴퓨터공학과": ["서울대학교", "카이스트", "포항공대", "고려대학교", "연세대학교"],
    "통계학과": ["서울대학교", "성균관대학교", "한양대학교"],
    "AI학과": ["KAIST", "UNIST", "서강대학교"],
    "광고홍보학과": ["이화여대", "중앙대학교", "홍익대학교"],
    "간호학과": ["서울대학교", "고려대학교", "한양대학교"],
    "사회복지학과": ["동국대학교", "서울여자대학교"],
}
universities = major_to_universities.get(selected_major, ["대학 정보 없음"])
st.write(f"🎓 `{selected_major}` 가 개설된 대학:")
st.markdown(" - " + "\n - ".join(universities))

# -------------------------------
# 5. 추천 도서
# -------------------------------
recommended_books = {
    "컴퓨터공학과": ["『코드』 - 찰스 페촙", "『인공지능의 미래』 - 닉 보스트롬"],
    "광고홍보학과": ["『브랜드가 되어라』", "『컨셉 잡는 법』"],
    "간호학과": ["『나는 간호사 사람입니다』", "『병원이라는 사찰』"],
}
books = recommended_books.get(selected_major, ["관련 추천 도서 없음"])
st.markdown(f"📚 `{selected_major}` 전공 추천 도서:")
st.markdown(" - " + "\n - ".join(books))

# -------------------------------
# 6. 2025 대입 컨트라인
# -------------------------------
cutlines = {
    "서울대학교 컴퓨터공학과": {"수능 백분위": 98, "학생부 종합": "1.1", "논술전형": "없음"},
    "카이스트 AI학과": {"수능": "미실시", "학생부 종합": "1.4", "특기자 전형": "우수 이과 경시 수상자"},
    "중앙대학교 광고홍보학과": {"수능": 91, "학생부 종합": "2.3"},
}
key = f"{universities[0]} {selected_major}"
info = cutlines.get(key, {"정보 없음": "해당 자료 없음"})
st.markdown(f"📊 `{key}` 2025학년도 대입 컨트라인 예측:")
for k, v in info.items():
    st.write(f"- {k}: {v}")
