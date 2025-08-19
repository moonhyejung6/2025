pip install -r requirements.txt
import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

st.set_page_config(page_title="🎵 Spotify 추천 앱", layout="centered")
st.title("🎵 데이터 기반 음악 추천 앱")

# 1️⃣ CSV 온라인 불러오기 (예: GitHub raw 링크)
csv_url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/SpotifyFeatures.csv"
df = pd.read_csv(csv_url)

# 2️⃣ 사용자 입력
mood = st.selectbox("분위기를 선택하세요:", df["mood"].unique())
genres = st.multiselect("장르를 선택하세요:", df["genre"].unique())
artist_choice = st.text_input("좋아하는 아티스트를 입력하세요 (없으면 빈칸)")

# 3️⃣ 데이터 필터링
filtered = df[
    (df["mood"] == mood) |
    (df["genre"].isin(genres) if genres else True)
]

if artist_choice:
    filtered = filtered[filtered["artist"].str.contains(artist_choice, case=False)]

# 4️⃣ Spotify API 인증
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="여기에 Client ID",
    client_secret="여기에 Client Secret"
))

# 5️⃣ 추천 곡 + Spotify 링크 표시
if not filtered.empty:
    recommendations = filtered.sample(min(10, len(filtered)))
    st.subheader("추천 곡 🎶")
    for _, row in recommendations.iterrows():
        track_name = row["track_name"]
        artist = row["artist"]
        query = f"{track_name} {artist}"
        result = sp.search(q=query, type="track", limit=1)
        if result["tracks"]["items"]:
            track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]
            st.write(f"**{track_name}** - {artist} | [Spotify 링크]({track_url})")
        else:
            st.write(f"**{track_name}** - {artist} | Spotify에서 찾을 수 없음")
else:
    st.warning("조건에 맞는 곡이 없습니다. 선택을 바꿔보세요.")
