import streamlit as st
import requests
import re

# 페이지 설정
st.set_page_config(page_title="🎶 유튜브 음악 추천기 🎶", page_icon="🎧", layout="centered")

st.title("🎶 유튜브 음악 추천기 🎶")
st.write("검색 키워드를 입력하면 유튜브 상위 5곡 링크와 썸네일을 보여줍니다!")

# --- 입력 ---
query_input = st.text_input("검색할 키워드를 입력하세요 (예: 아티스트, 곡명 등)")

# --- 유튜브 검색 함수 ---
def search_youtube(query, max_results=5):
    # MV/Official 키워드 자동 추가
    query += " MV Official"
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
                "id": vid,
                "link": f"https://www.youtube.com/watch?v={vid}",
                "thumbnail": f"https://img.youtube.com/vi/{vid}/0.jpg"
            })
        if len(videos) >= max_results:
            break
    return videos

# --- 추천 버튼 클릭 시 동작 ---
if st.button("추천 링크 보기"):
    if not query_input.strip():
        st.warning("검색 키워드를 입력해주세요.")
    else:
        results = search_youtube(query_input)
        if results:
            st.subheader("✨ 추천 노래 상위 5곡 ✨")
            for idx, video in enumerate(results, 1):
                st.markdown(f"**{idx}. [유튜브로 보기]({video['link']})**")
                st.image(video["thumbnail"], width=320)
        else:
            st.write("검색 결과가 없습니다 😢")
