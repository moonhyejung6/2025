import streamlit as st
import random
import re

st.set_page_config(page_title="나만의 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 나만의 음악 추천기 🎶")
st.write("취향, 상황, 기분, 장르, 아티스트에 맞는 노래를 추천해드릴게요!")

# --- 선택 입력 ---
situation = st.selectbox("현재 상황은?", ["없음", "공부할 때", "운동할 때", "힐링이 필요할 때", "신나고 싶을 때"])
mood = st.selectbox("현재 기분은?", ["없음", "차분한", "활발한", "감성적인", "모험적인"])
genre = st.multiselect("좋아하는 장르를 선택하세요", ["없음", "K-Pop", "Pop", "Hip-Hop", "Jazz", "Classical", "EDM"])
artist = st.text_input("좋아하는 아티스트가 있다면 입력해주세요 (없으면 비워두세요)")

# --- 유튜브 embed 변환 함수 ---
def to_embed(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        video_id = match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return url

# --- 곡 데이터베이스 (artist 필드 추가) ---
songs = [
    {"title": "lofi hip hop beats", "artist": "Various", "link": "https://www.youtube.com/watch?v=jfKfPfyJRdk", "situation": "공부할 때", "genre": "Jazz", "mood": "차분한"},
    {"title": "밤편지", "artist": "IU", "link": "https://www.youtube.com/watch?v=BzYnNdJhZQw", "situation": "공부할 때", "genre": "K-Pop", "mood": "감성적인"},
    {"title": "Blue & Grey", "artist": "BTS", "link": "https://www.youtube.com/watch?v=RD6Y6bK8cXQ", "situation": "공부할 때", "genre": "K-Pop", "mood": "차분한"},
    {"title": "Nocturne", "artist": "Chopin", "link": "https://www.youtube.com/watch?v=9E6b3swbnWg", "situation": "공부할 때", "genre": "Classical", "mood": "감성적인"},

    {"title": "Lose Yourself", "artist": "Eminem", "link": "https://www.youtube.com/watch?v=_Yhyp-_hX2s", "situation": "운동할 때", "genre": "Hip-Hop", "mood": "모험적인"},
    {"title": "Maniac", "artist": "Stray Kids", "link": "https://www.youtube.com/watch?v=OvioeS1ZZ7o", "situation": "운동할 때", "genre": "K-Pop", "mood": "활발한"},
    {"title": "Titanium", "artist": "David Guetta", "link": "https://www.youtube.com/watch?v=JRfuAukYTKg", "situation": "운동할 때", "genre": "EDM", "mood": "활발한"},
    {"title": "BOOMBAYAH", "artist": "BLACKPINK", "link": "https://www.youtube.com/watch?v=bwmSjveL3Lc", "situation": "운동할 때", "genre": "K-Pop", "mood": "모험적인"},

    {"title": "모든 날, 모든 순간", "artist": "Paul Kim", "link": "https://www.youtube.com/watch?v=OCQJjEdSs0U", "situation": "힐링이 필요할 때", "genre": "K-Pop", "mood": "감성적인"},
    {"title": "Perfect", "artist": "Ed Sheeran", "link": "https://www.youtube.com/watch?v=2Vv-BfVoq4g", "situation": "힐링이 필요할 때", "genre": "Pop", "mood": "감성적인"},
    {"title": "Paris in the Rain", "artist": "Lauv", "link": "https://www.youtube.com/watch?v=8xg3vE8Ie_E", "situation": "힐링이 필요할 때", "genre": "Pop", "mood": "차분한"},
    {"title": "River Flows in You", "artist": "Yiruma", "link": "https://www.youtube.com/watch?v=7maJOI3QMu0", "situation": "힐링이 필요할 때", "genre": "Classical", "mood": "차분한"},

    {"title": "Gangnam Style", "artist": "PSY", "link": "https://www.youtube.com/watch?v=9bZkp7q19f0", "situation": "신나고 싶을 때", "genre": "K-Pop", "mood": "활발한"},
    {"title": "Don’t Start Now", "artist": "Dua Lipa", "link": "https://www.youtube.com/watch?v=oygrmJFKYZY", "situation": "신나고 싶을 때", "genre": "Pop", "mood": "모험적인"},
    {"title": "DDU-DU DDU-DU", "artist": "BLACKPINK", "link": "https://www.youtube.com/watch?v=IHNzOHi8sJs", "situation": "신나고 싶을 때", "genre": "K-Pop", "mood": "모험적인"},
    {"title": "Summer", "artist": "Calvin Harris", "link": "https://www.youtube.com/watch?v=ebXbLfLACGM", "situation": "신나고 싶을 때", "genre": "EDM", "mood": "활발한"},
]

# --- 추천 로직 ---
if st.button("추천받기"):
    filtered = songs
    if situation != "없음":
        filtered = [s for s in filtered if s["situation"] == situation]
    if "없음" not in genre and genre:
        filtered = [s for s in filtered if s["genre"] in genre]
    if mood != "없음":
        filtered = [s for s in filtered if s["mood"] == mood]
    if artist:
        filtered = [s for s in filtered if artist.lower() in s["artist"].lower()]

    if filtered:
        st.subheader("✨ 조건에 맞는 노래 추천 ✨")
        for song in random.sample(filtered, min(len(filtered), 3)):
            st.markdown(f"**{song['title']}** - {song['artist']}")
            st.video(to_embed(song["link"]))
    else:
        st.subheader("🎵 조건에 완벽히 맞는 노래는 없지만, 최대한 비슷한 곡들을 찾아봤어요 🎵")
        relaxed_filtered = []
        for s in songs:
            score = 0
            if situation != "없음" and s["situation"] == situation:
                score += 1
            if "없음" not in genre and genre and s["genre"] in genre:
                score += 1
            if mood != "없음" and s["mood"] == mood:
                score += 1
            if artist and artist.lower() in s["artist"].lower():
                score += 2
            if score > 0:
                relaxed_filtered.append((score, s))

        if relaxed_filtered:
            relaxed_filtered.sort(key=lambda x: x[0], reverse=True)
            top_songs = [s for _, s in relaxed_filtered[:3]]
            for song in top_songs:
                st.markdown(f"**{song['title']}** - {song['artist']}")
                st.video(to_embed(song["link"]))
        else:
            st.write("조건에 맞는 노래를 전혀 찾지 못했어요 😢")


