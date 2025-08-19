import streamlit as st
import requests
import re

st.set_page_config(page_title="실시간 유튜브 음악 추천기", page_icon="🎧", layout="centered")

st.title("🎶 실시간 유튜브 음악 추천기 🎶")
st.write("아티스트, 기분, 장르 등으로 유튜브에서 바로 노래를 찾아 추천해드립니다!")

# --- 선택 입력 ---
situation = st.selectbox("현재 상황은?", ["", "공부할 때", "운동할 때", "힐링이 필요할 때", "신나고 싶을 때"])
mood = st.selectbox("현재 기분은?", ["", "차분한", "활발한", "감성적인", "모험적인"])
genre = st.multiselect("좋아하는 장르를 선택하세요", ["없음", "K-Pop", "Pop", "Hip-Hop", "Jazz", "Classical", "EDM", "밴드"])
artist = st.text_input("좋아하는 아티스트가 있다면 입력해주세요 (없으면 비워두세요)")

# --- 유튜브 embed 변환 ---
def to_embed(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url

# --- 유튜브 검색 (requests + regex) ---
def search_youtube(query, max_results=10):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    response = requests.get(search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    # 중복 제거
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
    if not any([artist, genre, mood, situation]):
        st.warning("아티스트, 장르, 기분, 상황 중 하나 이상 입력해주세요.")
    else:
        # --- 키워드 조합 ---
        query_parts = []
        if artist:
            query_parts.append(artist)
        if genre and "없음" not in genre:
            query_parts.extend(genre)
        if mood:
            query_parts.append(mood)
        if situation:
            query_parts.append(situation)
        full_query = " ".join(query_parts)

        # --- 1차 검색: 모든 조건 포함 ---
        results = search_youtube(full_query, max_results=10)

        if results:
            # --- 점수 계산: 우선순위 반영 ---
            scored = []
            for song in results:
                score = 0
                title_lower = song["title"].lower()
                if artist and artist.lower() in title_lower:
                    score += 4  # 아티스트 최우선
                if genre:
                    for g in genre:
                        if g != "없음" and g.lower() in title_lower:
                            score += 3
                            break
                if mood and mood.lower() in title_lower:
                    score += 2
                if situation and situation.lower() in title_lower:
                    score += 1
                scored.append((score, song))

            # 점수 내림차순 정렬
            scored.sort(key=lambda x: x[0], reverse=True)
            top_songs = [s for score, s in scored if score > 0][:3]

            if top_songs:
                st.subheader("✨ 추천 노래 ✨")
                for song in top_songs:
                    st.markdown(f"**{song['title']}**")
                    st.video(to_embed(song["link"]))
            else:
                st.write("조건에 맞는 노래를 찾지 못했어요 😢")
        else:
            st.write("조건에 맞는 노래를 찾지 못했어요 😢")

