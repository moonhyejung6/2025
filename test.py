import streamlit as st
import requests
import re
import random

# 페이지 설정
st.set_page_config(page_title="🎶 취향 따라 떠나는 음악 탐험", page_icon="🎧", layout="centered")

# 제목 & 부제
st.title("🎶 취향 따라 떠나는 음악 탐험")
st.write("아티스트, 장르, 기분을 입력하고 나만의 음악을 발견하세요!")

# --- 미리 정의한 곡 데이터 (DB) ---
songs_db = [
    {"artist":"BTS","title":"Dynamite","genre":"Pop","mood":"Happy","link":"https://www.youtube.com/watch?v=gdZLi9oWNZg","thumbnail":"https://img.youtube.com/vi/gdZLi9oWNZg/0.jpg"},
    {"artist":"IU","title":"Blueming","genre":"Pop","mood":"Happy","link":"https://www.youtube.com/watch?v=3eK7YjgTAjQ","thumbnail":"https://img.youtube.com/vi/3eK7YjgTAjQ/0.jpg"},
    {"artist":"Coldplay","title":"Adventure of a Lifetime","genre":"Rock","mood":"Excited","link":"https://www.youtube.com/watch?v=QtXby3twMmI","thumbnail":"https://img.youtube.com/vi/QtXby3twMmI/0.jpg"},
    {"artist":"Adele","title":"Hello","genre":"Pop","mood":"Sad","link":"https://www.youtube.com/watch?v=YQHsXMglC9A","thumbnail":"https://img.youtube.com/vi/YQHsXMglC9A/0.jpg"},
    {"artist":"Ed Sheeran","title":"Shape of You","genre":"Pop","mood":"Happy","link":"https://www.youtube.com/watch?v=JGwWNGJdvx8","thumbnail":"https://img.youtube.com/vi/JGwWNGJdvx8/0.jpg"},
    {"artist":"Imagine Dragons","title":"Believer","genre":"Rock","mood":"Excited","link":"https://www.youtube.com/watch?v=7wtfhZwyrcc","thumbnail":"https://img.youtube.com/vi/7wtfhZwyrcc/0.jpg"},
    {"artist":"Billie Eilish","title":"Bad Guy","genre":"Pop","mood":"Chill","link":"https://www.youtube.com/watch?v=DyDfgMOUjCI","thumbnail":"https://img.youtube.com/vi/DyDfgMOUjCI/0.jpg"},
    {"artist":"Maroon 5","title":"Memories","genre":"Pop","mood":"Sad","link":"https://www.youtube.com/watch?v=SlPhMPnQ58k","thumbnail":"https://img.youtube.com/vi/SlPhMPnQ58k/0.jpg"},
    {"artist":"Bruno Mars","title":"24K Magic","genre":"Pop","mood":"Happy","link":"https://www.youtube.com/watch?v=UqyT8IEBkvY","thumbnail":"https://img.youtube.com/vi/UqyT8IEBkvY/0.jpg"},
    {"artist":"Linkin Park","title":"Numb","genre":"Rock","mood":"Sad","link":"https://www.youtube.com/watch?v=kXYiU_JCYtU","thumbnail":"https://img.youtube.com/vi/kXYiU_JCYtU/0.jpg"},
    {"artist":"Taylor Swift","title":"Love Story","genre":"Pop","mood":"Happy","link":"https://www.youtube.com/watch?v=8xg3vE8Ie_E","thumbnail":"https://img.youtube.com/vi/8xg3vE8Ie_E/0.jpg"},
    {"artist":"Queen","title":"Bohemian Rhapsody","genre":"Rock","mood":"Chill","link":"https://www.youtube.com/watch?v=fJ9rUzIMcZQ","thumbnail":"https://img.youtube.com/vi/fJ9rUzIMcZQ/0.jpg"},
    {"artist":"Ariana Grande","title":"7 rings","genre":"Pop","mood":"Excited","link":"https://www.youtube.com/watch?v=QYh6mYIJG2Y","thumbnail":"https://img.youtube.com/vi/QYh6mYIJG2Y/0.jpg"},
    {"artist":"Linkin Park","title":"In The End","genre":"Rock","mood":"Sad","link":"https://www.youtube.com/watch?v=eVTXPUF4Oz4","thumbnail":"https://img.youtube.com/vi/eVTXPUF4Oz4/0.jpg"},
    {"artist":"Ed Sheeran","title":"Perfect","genre":"Pop","mood":"Relaxing","link":"https://www.youtube.com/watch?v=2Vv-BfVoq4g","thumbnail":"https://img.youtube.com/vi/2Vv-BfVoq4g/0.jpg"},
]

# --- 입력 ---
query_input = st.text_input(
    "검색할 키워드를 입력하세요",
    placeholder="아티스트, 곡명, 장르, 기분 등 다양한 키워드를 입력해주세요!"
)

# --- 유튜브 검색 함수 ---
def search_youtube(query, max_results=3):
    query += " MV Official"
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    try:
        response = requests.get(search_url)
        video_items = re.findall(r'"videoId":"(.*?)".*?"title":\{"runs":\[\{"text":"(.*?)"\}\]', response.text)
        seen = set()
        videos = []
        for vid, title in video_items:
            if vid not in seen:
                seen.add(vid)
                videos.append({
                    "id": vid,
                    "title": title,
                    "link": f"https://www.youtube.com/watch?v={vid}",
                    "thumbnail": f"https://img.youtube.com/vi/{vid}/0.jpg"
                })
            if len(videos) >= max_results:
                break
        return videos
    except:
        return []

# --- 추천 버튼 클릭 시 ---
if st.button("추천 노래 보기"):
    if not query_input.strip():
        st.warning("검색 키워드를 입력해주세요.")
    else:
        keywords = query_input.lower().split()
        recommendations = []

        # DB 기반 추천
        for song in songs_db:
            score = 0
            for kw in keywords:
                if kw in song["artist"].lower() or kw in song["title"].lower() or kw in song["genre"].lower() or kw in song["mood"].lower():
                    score += 1
            if score > 0:
                recommendations.append({
                    "title": f"{song['artist']} - {song['title']}",
                    "link": song["link"],
                    "thumbnail": song["thumbnail"]
                })

        # 유튜브 검색 기반 추천
        yt_results = search_youtube(query_input)
        for video in yt_results:
            recommendations.append({
                "title": video["title"],
                "link": video["link"],
                "thumbnail": video["thumbnail"]
            })

        # 추천 리스트 출력
        st.subheader("🎵 추천 결과 🎵")
        for idx, rec in enumerate(recommendations, 1):
            st.markdown(f"**{idx}. {rec['title']}**")
            st.markdown(f"[![thumbnail]({rec['thumbnail']})]({rec['link']})")
