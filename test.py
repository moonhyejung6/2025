import streamlit as st
import random

st.set_page_config(page_title="🎶 맞춤 음악 추천기 🎶", page_icon="🎧", layout="centered")

st.title("🎶 앱만의 맞춤 음악 추천기 🎶")
st.write("아티스트, 곡명, 장르, 기분 등 키워드를 입력하면 최대한 맞춰 상위 5곡을 추천합니다!")

# --- 미리 정의한 곡 데이터 ---
# 각 곡은 아티스트, 곡명, 장르, 기분, 유튜브 링크, 썸네일 포함
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
]

# --- 입력 ---
query_input = st.text_input(
    "검색할 키워드를 입력하세요",
    placeholder="아티스트, 곡명, 장르, 기분 등 다양한 키워드를 입력해주세요!"
)

# --- 추천 버튼 클릭 시 ---
if st.button("추천 노래 보기"):
    if not query_input.strip():
        st.warning("검색 키워드를 입력해주세요.")
    else:
        # 입력 키워드 단어 단위로 나누기
        keywords = query_input.lower().split()
        matched = []

        for song in songs_db:
            score = 0
            for kw in keywords:
                if kw in song["artist"].lower() or kw in song["title"].lower() or kw in song["genre"].lower() or kw in song["mood"].lower():
                    score += 1
            if score > 0:
                matched.append((score, song))
        
        # 점수 기준 내림차순 정렬
        matched.sort(reverse=True, key=lambda x: x[0])
        
        if matched:
            st.subheader("✨ 추천 상위 곡 ✨")
            for idx, (score, song) in enumerate(matched[:5], 1):
                st.markdown(f"**{idx}. {song['artist']} - {song['title']}**")
                st.image(song["thumbnail"], width=320)
                st.markdown(f"[▶ 유튜브에서 재생]({song['link']})")
        else:
            st.write("검색 조건과 완전히 일치하는 곡은 없지만, 비슷한 곡을 추천해드릴게요!")
            # 조건과 상관없이 랜덤 5곡 추천
            for idx, song in enumerate(random.sample(songs_db, 5), 1):
                st.markdown(f"**{idx}. {song['artist']} - {song['title']}**")
                st.image(song["thumbnail"], width=320)
                st.markdown(f"[▶ 유튜브에서 재생]({song['link']})")

