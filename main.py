import streamlit as st
from datetime import datetime

# ===== 페이지 기본 설정 =====
st.set_page_config(
    page_title="MBTI 맞춤 공감 상담",
    page_icon="💬",
    layout="centered"
)

# ===== 스타일 (감성적인 분위기) =====
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        font-family: 'Nanum Pen Script', cursive;
        color: #333333;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        color: #4a2c2a;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
        color: #5a3e36;
    }
    .chat-bubble-user {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 12px;
        border-radius: 20px;
        margin: 8px 0;
        max-width: 70%;
        align-self: flex-end;
    }
    .chat-bubble-bot {
        background-color: rgba(255, 230, 230, 0.9);
        padding: 12px;
        border-radius: 20px;
        margin: 8px 0;
        max-width: 70%;
        align-self: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# ===== 앱 제목 =====
st.markdown('<div class="title">💖 MBTI 맞춤 감성 상담 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 이야기를 들려주세요. 따뜻하게 들어드릴게요.</div>', unsafe_allow_html=True)

# ===== MBTI별 맞춤 반응 =====
mbti_responses = {
    "INFP": "당신의 마음속에 있는 깊은 감정이 느껴져요. 정말 소중한 마음이에요.",
    "ENFP": "정말 흥미롭고 생생한 생각이에요! 당신의 에너지가 저에게도 전해져요.",
    "INFJ": "당신의 고민을 들으며, 그 속에 담긴 깊은 의미를 느껴요. 당신은 결코 혼자가 아니에요.",
    "ENFJ": "당신은 늘 다른 사람을 먼저 생각하는군요. 그 마음이 너무나 아름다워요.",
    "INTP": "이 문제를 정말 분석적으로 바라보셨군요. 그 통찰이 놀라워요.",
    "ENTP": "정말 창의적인 시각이에요! 여러 가능성을 동시에 바라보는 게 멋져요.",
    "INTJ": "당신의 계획적이고 깊은 사고가 인상적이에요. 목표를 향해 가는 모습이 멋져요.",
    "ENTJ": "결단력 있는 생각이 느껴져요. 강인한 리더십이 돋보여요.",
    "ISFP": "당신의 감성적인 면모가 참 따뜻해요. 그 마음을 소중히 간직하세요.",
    "ESFP": "정말 생기 있고 따뜻한 에너지가 전해져요! 지금 이 순간이 빛나요.",
    "ISTP": "차분하게 상황을 바라보는 시선이 멋져요. 현실적인 해결책을 찾을 수 있을 거예요.",
    "ESTP": "당신의 용기와 실행력이 정말 멋져요! 도전 정신이 돋보입니다.",
    "ISFJ": "누군가를 배려하는 당신의 마음이 너무 따뜻해요.",
    "ESFJ": "다른 사람을 살뜰히 챙기는 당신의 모습이 감동적이에요.",
    "ISTJ": "성실하고 책임감 있는 태도가 인상 깊어요.",
    "ESTJ": "조직적이고 확실한 판단이 믿음직스러워요."
}

# ===== 입력 =====
mbti = st.selectbox("당신의 MBTI를 선택해주세요:", list(mbti_responses.keys()))
user_input = st.text_area("당신의 고민을 들려주세요:")

if st.button("따뜻하게 들어주세요 💌"):
    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:
        st.markdown(f"""
        <div class="chat-bubble-user">🙋‍♀️ {user_input}</div>
        <div class="chat-bubble-bot">🤖 {mbti_responses[mbti]}</div>
        <div class="chat-bubble-bot">그리고요... {user_input} 라는 이야기에 제가 함께 마음을 나누고 싶어요.</div>
        """, unsafe_allow_html=True)

