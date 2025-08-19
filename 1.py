import streamlit as st
from googleapiclient.discovery import build
import random
import re

st.set_page_config(page_title="실시간 유튜브 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 실시간 유튜브 음악 추천기 🎶")
st.write("아티스트, 기분, 장르 등으로 유튜브에서 바로 노래를 찾아 추천해드립니다!")

# --- 선택 입력 ---
situation = st.selectbox("현재 상황은?", ["", "공부할 때", "운동할 때", "힐링이 필요할 때", "신나고 싶을 때"])
mood = st.selectbox("현재 기분은?", ["", "차분한", "활발한", "감성적인", "모험적인"])
genre = st.text_input("좋아하는 장르를 입력해주세요 (예: K-Pop, Pop, Jazz 등)")
artist = st.text_input("좋아하는 아티스트를 입력해주세요")

# --- 유튜브 embed 변환 함수 ---
def to_embed(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url

# --- 유튜브 검색 함수 ---
def search_youtube(query, max_results=3):
    api_key = "YOUR_YOUTUBE_API_KEY"  # 여기 API 키 입력
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoCategoryId="10",  # 음악 카테고리
        maxResults=max_results
    )
    response = request.execute()
    videos = []
    for item in response.get("items", []):
        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "link": url})
    return videos

# --- 추천 버튼 ---
if st.button("추천받기"):
    query_parts = []
    if artist:
        query_parts.append(artist)
    if genre:
        query_parts.append(genre)
    if mood:
        query_parts.append(mood)
    if situation:
        query_parts.append(situation)
    query = " ".join(query_parts)

    if not query:
        st.warning("아티스트, 장르, 기분, 상황 중 하나 이상 입력해주세요.")
    else:
        results = search_youtube(query)
        if results:
            st.subheader("✨ 추천 노래 ✨")
            for song in results:
                st.markdown(f"**{song['title']}**")
                st.video(to_embed(song["link"]))
        else:
            st.write("조건에 맞는 노래를 찾지 못했어요 😢")


