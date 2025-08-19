import streamlit as st
import pandas as pd
import random

# 샘플 데이터 (실제는 CSV 파일에서 불러오기)
data = {
    "곡명": ["Song A", "Song B", "Song C", "Song D"],
    "아티스트": ["Artist 1", "Artist 2", "Artist 3", "Artist 1"],
    "장르": ["팝", "힙합", "발라드", "재즈"],
    "분위기": ["밝음", "차분함", "슬픔", "에너지"],
    "상황": ["운동", "공부", "밤", "드라이브"]
}
df = pd.DataFrame(data)

st.title("🎵 맞춤형 음악 추천 앱")

# 사용자 입력
mood = st.selectbox("분위기를 선택하세요:", df["분위기"].unique())
genres = st.multiselect("장르를 선택하세요:", df["장르"].unique())
situation = st.radio("상황을 선택하세요:", df["상황"].unique())
artist = st.text_input("좋아하는 아티스트를 입력하세요:")

# 추천 로직
filtered = df[
    (df["분위기"] == mood) &
    (df["상황"] == situation) &
    (df["장르"].isin(genres) if genres else True)
]

if artist:
    filtered = filtered[filtered["아티스트"].str.contains(artist, case=False)]

if not filtered.empty:
    rec = filtered.sample(min(3, len(filtered)))
    st.subheader("추천 노래 🎶")
    for _, row in rec.iterrows():
        st.write(f"**{row['곡명']}** - {row['아티스트']}")
else:
    st.warning("조건에 맞는 노래가 없어요 😢 다른 선택을 해보세요.")
