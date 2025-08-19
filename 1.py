import streamlit as st
import requests
import re

st.set_page_config(page_title="실시간 유튜브 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 실시간 유튜브 음악 추천기 🎶")
st.write("아티스트, 기분, 장르 등 원하는 키워드를 입력하면 유튜브에서 상위 3곡을 추천합니다!")

# --- 입력 ---
query_input = st.text_input("검색할 키워드를 입력하세요 (예: 아티스트, 장르, 기분 등)")

# --- 유튜브 embed 변환 ---
def to_embed(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url

# --- 유튜브 검색 (requests + regex) ---
def search_youtube(query, max_results=3):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    response = requests.get(search_url)
    # video ID 추출
    video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    seen = set()
    videos = []
    for vid in video_ids:
        if vid not in seen:
            seen.add(vid)
            videos.append({
                "title": f"유튜브 검색 결과",  # 제목은 단순 표시
                "link": f"https://www.youtube.com/watch?v={vid}"
            })
        if len(videos) >= max_results:
            break
    return videos

# --- 추천 버튼 ---
if st.button("추천받기"):
    if not query_input.strip():
        st.warning("검색 키워드를 입력해주세요.")
    else:
        results = search_youtube(query_input)
        if results:
            st.subheader("✨ 추천 노래 (상위 3곡) ✨")
            for song in results:
                st.markdown(f"**{song['title']}**")
                st.video(to_embed(song["link"]))
        else:
            st.write("검색 결과가 없습니다 😢")
