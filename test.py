import streamlit as st
import pandas as pd

# 샘플 데이터 (실제로는 CSV 불러오기)
data = {
    "곡명": ["Song A", "Song B", "Song C", "Song D", "Song E"],
    "아티스트": ["Artist 1", "Artist 2", "Artist 3", "Artist 1", "Artist 4"],
    "장르": ["팝", "힙합", "발라드", "재즈", "팝"],
    "분위기": ["밝음", "차분함", "슬픔", "에너지", "밝음"],
    "상황": ["운동", "공부", "밤", "드라이브", "공부"]
}
df = pd.DataFrame(data)

st.title("🎵 맞춤형 음악 추천 앱")

# 사용자 입력
mood = st.selectbox("분위기를 선택하세요:", df["분위기"].unique())
genres = st.multiselect("장르를 선택하세요:", df["장르"].unique())
situation = st.radio("상황을 선택하세요:", df["상황"].unique())

# 아티스트 선택: 직접 입력 + 없음 옵션
artist_choice = st.selectbox("좋아하는 아티스트를 선택하세요:", ["없음"] + list(df["아티스트"].unique()))

# 추천 로직
filtered = df[
    (df["분위기"] == mood) &
    (df["상황"] == situation) &
    (df["장르"].isin(genres) if genres else True)
]

# 아티스트 필터 (없음을 고르면 무시)
if artist_choice != "없음":
    filtered = filtered[filtered["아티스트"] == artist_choice]

# 결과 출력
if not filtered.empty:
    st.subheader("추천 노래 🎶")
    for _, row in filtered.iterrows():
        st.write(f"**{row['곡명']}** - {row['아티스트']}")
else:
    st.warning("조건에 맞는 노래가 없어요 😢 다른 선택을 해보세요.")
