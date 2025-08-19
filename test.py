import streamlit as st
import pandas as pd
import requests
import io
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ------------------------------
# 앱 기본 설정
# ------------------------------
st.set_page_config(page_title="🎵 Spotify 추천 앱", layout="centered")
st.title("🎵 데이터 기반 음악 추천 앱")

# ------------------------------
# 1️⃣ CSV 온라인 불러오기 (GitHub Raw 링크)
# ------------------------------
csv_url = "https://raw.githubusercontent.com/사용자명/리포지토리명/main/SpotifyFeatures.csv"
try:
    response = requests.get(csv_url)
    response.encoding = 'utf-8'
    df = pd.read_csv(io.StringIO(response.text))
except Exception as e:
    st.error("CSV 파일을 불러오는 데 실패했습니다. 링크를 확인하세요.")
    st.stop()

# ------------------------------
# 컬럼 확인 (디버깅용)
# ------------------------------
st.write("CSV 컬럼 확인:", df.columns)

# ------------------------------
# 2️⃣ 사용자 입력
# ------------------------------
st.subheader("곡 분위기 선택 (0: 슬픔/1: 즐거움)")
valence_range = st.slider("분위기 범위를 선택하세요:", 0.0, 1.0, (0.3, 0.7), 0.01)

artist_choice = st.text_input("좋아하는 아티스트를 입력하세요 (없으면 빈칸)")

# ------------------------------
# 3️⃣ 데이터 필터링
# ------------------------------
# 실제 CSV 컬럼명에 맞게 수정
filtered = df[
    (df["track_valence"] >= valence_range[0]) &
    (df["track_valence"] <= valence_range[1])
]

if artist_choice:
    filtered = filtered[df["artist_name"].str.contains(artist_choice, case=False)]

# ------------------------------
# 4️⃣ Spotify API 인증
# ------------------------------
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="여기에 Client ID",
    client_secret="여기에 Client Secret"
))

# ------------------------------
# 5️⃣ 추천 곡 + Spotify 링크 표시
# ------------------------------
if not filtered.empty:
    recommendations = filtered.sample(min(10, len(filtered)))
    st.subheader("추천 곡 🎶")
    for _, row in recommendations.iterrows():
        track_name = row["track_name"]
        artist = row["artist_name"]
        query = f"{track_name} {artist}"
        result = sp.search(q=query, type="track", limit=1)
        if result["tracks"]["items"]:
            track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]
            st.write(f"**{track_name}** - {artist} | [Spotify 링크]({track_url})")
        else:
            st.write(f"**{track_name}** - {artist} | Spotify에서 찾을 수 없음")
else:
    st.warning("조건에 맞는 곡이 없습니다. 선택을 바꿔보세요.")

