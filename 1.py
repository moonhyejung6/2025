import streamlit as st
import random

st.set_page_config(page_title="나만의 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 나만의 음악 추천기 🎶")
st.write("취향, 상황, 성격, 장르에 맞는 노래를 여러 개 추천해드릴게요!")

# --- 선택 입력 ---
situation = st.selectbox("현재 상황은?", ["공부할 때", "운동할 때", "힐링이 필요할 때", "신나고 싶을 때"])
personality = st.selectbox("당신의 성격은?", ["차분한", "활발한", "감성적인", "모험적인"])
genre = st.multiselect("좋아하는 장르를 선택하세요", ["K-Pop", "Pop", "Hip-Hop", "Jazz", "Classical", "EDM"])
artist = st.text_input("좋아하는 아티스트가 있다면 입력해주세요 (선택)")

# --- 곡 데이터베이스 ---
songs = [
    # 공부할 때
    {"title": "lofi hip hop beats", "link": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "situation": "공부할 때", "genre": "Jazz", "personality": "차분한"},
    {"title": "IU - 밤편지", "link": "https://www.youtube.com/watch?v=BzYnNdJhZQw", "situation": "공부할 때", "genre": "K-Pop", "personality": "감성적인"},
    {"title": "BTS - Blue & Grey", "link": "https://www.youtube.com/watch?v=RD6Y6bK8cXQ", "situation": "공부할 때", "genre": "K-Pop", "personality": "차분한"},
    {"title": "Chopin - Nocturne", "link": "https://www.youtube.com/watch?v=9E6b3swbnWg", "situation": "공부할 때", "genre": "Classical", "personality": "감성적인"},
    
    # 운동할 때
    {"title": "Eminem - Lose Yourself", "link": "https://www.youtube.com/watch?v=_Yhyp-_hX2s", "situation": "운동할 때", "genre": "Hip-Hop", "personality": "모험적인"},
    {"title": "Stray Kids - Maniac", "link": "https://www.youtube.com/watch?v=OvioeS1ZZ7o", "situation": "운동할 때", "genre": "K-Pop", "personality": "활발한"},
    {"title": "David Guetta - Titanium", "link": "https://www.youtube.com/watch?v=JRfuAukYTKg", "situation": "운동할 때", "genre": "EDM", "personality": "활발한"},
    {"title": "BLACKPINK - BOOMBAYAH", "link": "https://www.youtube.com/watch?v=bwmSjveL3Lc", "situation": "운동할 때", "genre": "K-Pop", "personality": "모험적인"},
    
    # 힐링이 필요할 때
    {"title": "Paul Kim - 모든 날, 모든 순간", "link": "https://www.youtube.com/watch?v=OCQJjEdSs0U", "situation": "힐링이 필요할 때", "genre": "K-Pop", "personality": "감성적인"},
    {"title": "Ed Sheeran - Perfect", "link": "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "situation": "힐링이 필요할 때", "genre": "Pop", "personality": "감성적인"},
    {"title": "Lauv - Paris in the Rain", "link": "https://www.youtube.com/watch?v=8xg3vE8Ie_E", "situation": "힐링이 필요할 때", "genre": "Pop", "personality": "차분한"},
    {"title": "Yiruma - River Flows in You", "link": "https://www.youtube.com/watch?v=7maJOI3QMu0", "situation": "힐링이 필요할 때", "genre": "Classical", "personality": "차분한"},
    
    # 신나고 싶을 때
    {"title": "PSY - Gangnam Style", "link": "https://www.youtube.com/watch?v=9bZkp7q19f0", "situation": "신나고 싶을 때", "genre": "K-Pop", "personality": "활발한"},
    {"title": "Dua Lipa - Don’t Start Now", "link": "https://www.youtube.com/watch?v=oygrmJFKYZY", "situation": "신나고 싶을 때", "genre": "Pop", "personality": "모험적인"},
    {"title": "BLACKPINK - DDU-DU DDU-DU", "link": "https://www.youtube.com/watch?v=IHNzOHi8sJs", "situation": "신나고 싶을 때", "genre": "K-Pop", "personality": "모험적인"},
    {"title": "Calvin Harris - Summer", "link": "https://www.youtube.com/watch?v=ebXbLfLACGM", "situation": "신나고 싶을 때", "genre": "EDM", "personality": "활발한"},
]

# --- 추천 로직 ---
if st.button("추천받기"):
    filtered = [song for song in songs if song["situation"] == situation]

    if genre:
        filtered = [s for s in filtered if s["genre"] in genre]

    if personality:
        filtered = [s for s in filtered if s["personality"] == personality]

    if artist:
        filtered = [s for s in filtered if artist.lower() in s["title"].lower()] or filtered

    if filtered:
        st.subheader("✨ 추천 곡 리스트 ✨")
        for song in random.sample(filtered, min(len(filtered), 3)):  # 최대 3곡 추천
            st.markdown(f"**{song['title']}**")
            st.video(song["link"])
    else:
        st.write("조건에 맞는 노래를 찾지 못했어요 😢")
