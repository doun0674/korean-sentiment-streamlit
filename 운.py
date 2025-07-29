import streamlit as st
import random

# 세션 상태 초기화
if "fortune" not in st.session_state:
    st.session_state.fortune = None

# 운세 리스트
fortunes = [
    "🌞 오늘은 행운이 가득한 날! 원하는 일이 잘 풀릴 거예요.",
    "🌧 잠깐의 어려움이 있을 수 있지만 금방 지나갈 거예요.",
    "🍀 뜻밖의 좋은 소식이 찾아올 수 있어요. 기대해 보세요!",
    "🔥 열정이 넘치는 하루! 새로운 도전을 해보세요.",
    "💤 휴식이 필요한 날이에요. 무리하지 말고 여유를 가지세요.",
    "💰 재물이 들어올 기운이 있어요. 돈 관리에 신경 써보세요.",
    "🧍 사람들과의 관계에서 좋은 일이 생길 거예요.",
    "⚠️ 조심! 작은 실수가 큰 일이 될 수 있어요. 침착하세요.",
    "🎁 누군가에게서 선물을 받게 될 수도 있어요!",
    "📚 배움에 좋은 날이에요. 새로운 것을 공부해보세요."
]

st.title("🔮 오늘의 운세")

st.write("👋 아래 버튼을 눌러 오늘의 운세를 확인해보세요!")

# 운세 보기 버튼
if st.button("운세 보기"):
    st.session_state.fortune = random.choice(fortunes)

# 운세 출력
if st.session_state.fortune:
    st.success(f"✨ 오늘의 운세:\n\n**{st.session_state.fortune}**")

# 초기화 버튼
if st.button("🔄 운세 초기화"):
    st.session_state.fortune = None
    st.experimental_rerun()

