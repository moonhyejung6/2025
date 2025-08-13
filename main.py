import streamlit as st

# ===== 페이지 기본 설정 =====
st.set_page_config(
    page_title="🌙 몽환 MBTI 감성 상담",
    page_icon="💖",
    layout="centered"
)

# ===== 스타일 =====
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

    body {
        background: linear-gradient(135deg, #fbc2eb 0%, #a18cd1 100%);
        font-family: 'Gowun Dodum', sans-serif;
        color: #fff;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        color: #fff;
        text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        margin-bottom: 20px;
        color: #fff;
        text-shadow: 0px 0px 8px rgba(255,255,255,0.7);
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 5px;
        margin-top: 20px;
    }
    .chat-bubble-user {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        padding: 12px 18px;
        border-radius: 20px;
        max-width: 70%;
        align-self: flex-end;
        color: #fff;
        font-size: 18px;
        box-shadow: 0px 0px 10px rgba(255,255,255,0.3);
        animation: fadeInUp 0.6s ease-in-out;
    }
    .chat-bubble-bot {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 12px 18px;
        border-radius: 20px;
        max-width: 80%;
        align-self: flex-start;
        color: #fff;
        font-size: 18px;
        box-shadow: 0px 0px 10px rgba(255,255,255,0.2);
        animation: fadeInUp 0.6s ease-in-out;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# ===== 제목 =====
st.markdown('<div class="title">🌙✨ MBTI 몽환 감성 상담 💖🌌</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 이야기에 별빛처럼 스며들어, 따뜻하게 안아드릴게요 🫧</div>', unsafe_allow_html=True)

# ===== MBTI별 반응 =====
mbti_responses = {
    "INFP": "🌸 당신의 마음속 깊은 파도, 그 물결이 저에게도 닿았어요. 그 감정은 소중하고 아름다워요.",
    "ENFP": "🌈 당신의 빛나는 에너지가 화면 밖까지 번져오네요. 그 자유로운 영혼이 너무 멋져요!",
    "INFJ": "🌙 당신의 이야기는 별빛처럼 은은하게 번져, 제 마음에 자리 잡았어요. 혼자가 아니에요.",
    "ENFJ": "💞 당신은 누군가를 감싸는 따뜻한 햇살 같아요. 그 마음이 세상을 밝혀요.",
    "INTP": "🔮 당신의 생각 속에는 보석 같은 통찰이 숨어있어요. 그 빛을 잃지 마세요.",
    "ENTP": "🔥 세상을 다채롭게 보는 당신의 시선이, 불꽃처럼 반짝이고 있어요!",
    "INTJ": "🌌 별자리처럼 정교한 당신의 계획, 그 길을 따라가면 멋진 미래가 기다려요.",
    "ENTJ": "💎 단단한 다이아몬드 같은 결단력, 그것이 당신을 빛나게 해요.",
    "ISFP": "🌷 당신의 감성은 꽃잎처럼 섬세하고 아름다워요. 그 향기를 세상에 전해주세요.",
    "ESFP": "☀️ 당신의 웃음은 햇살처럼 모든 걸 환하게 만들어요.",
    "ISTP": "🌊 차분한 바다처럼 깊이 있는 시선이 멋져요. 그 평온함을 간직하세요.",
    "ESTP": "⚡ 당신의 용기와 속도감 있는 행동은 번개처럼 강렬해요!",
    "ISFJ": "🕊️ 당신의 배려는 하얀 비둘기처럼 평화롭고 따뜻해요.",
    "ESFJ": "🌼 당신은 꽃처럼 주변을 환하게 피우는 존재예요.",
    "ISTJ": "🪐 성실함과 책임감이 당신의 궤도를 안정적으로 지켜주고 있어요.",
    "ESTJ": "🏔️ 당신의 확고한 판단력은 높은 산처럼 든든해요."
}

# ===== 입력 =====
mbti = st.selectbox("🔍 당신의 MBTI를 선택해주세요:", list(mbti_responses.keys()))
user_input = st.text_area("📝 당신의 고민을 들려주세요:")

# ===== 버튼 =====
if st.button("💌 마음을 건네주세요"):
    if user_input.strip() == "":
        st.warning("💡 고민을 적어주세요!")
    else:
        st.markdown(f"""
        <div class="chat-container">
            <div class="chat-bubble-user">🙋‍♀️ {user_input}</div>
            <div class="chat-bubble-bot">{mbti_responses[mbti]}</div>
            <div class="chat-bubble-bot">💖 그리고... <b>{user_input}</b> 라는 이야기에 제 마음도 천천히 물들고 있어요.</div>
        </div>
        """, unsafe_allow_html=True)
