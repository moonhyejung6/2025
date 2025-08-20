import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🎶 유튜브 음악 링크 추천기 🎶", page_icon="🎧", layout="centered")

st.title("🎶 유튜브 음악 링크 추천기 🎶")
st.write("아티스트, 곡명, 장르 등으로 유튜브 검색 페이지로 바로 연결합니다!")

# --- 입력 ---
query_input = st.text_input("검색할 키워드를 입력하세요 (예: 아티스트, 곡명 등)")

# --- 버튼 클릭 시 동작 ---
if st.button("추천 링크 열기"):
    if not query_input.strip():
        st.warning("검색 키워드를 입력해주세요.")
    else:
        # MV/Official 키워드 자동 추가
        search_query = query_input + " MV Official"
        url_query = search_query.replace(" ", "+")
        youtube_url = f"https://www.youtube.com/results?search_query={url_query}"
        
        st.markdown(f"[🎵 여기를 클릭하면 유튜브 검색 결과로 이동합니다]({youtube_url})")
        st.info("클릭하면 브라우저에서 유튜브 페이지가 열립니다.")



