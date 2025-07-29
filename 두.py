import streamlit as st
import random
import time

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_pos" not in st.session_state:
    st.session_state.mole_pos = random.randint(1, 9)
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "game_over" not in st.session_state:
    st.session_state.game_over = False

def restart_game():
    st.session_state.score = 0
    st.session_state.mole_pos = random.randint(1, 9)
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.experimental_rerun()

# 타이머
elapsed_time = time.time() - st.session_state.start_time
remaining_time = max(0, int(20 - elapsed_time))
if remaining_time == 0 and not st.session_state.game_over:
    st.session_state.game_over = True

st.title("🕹️ 두더지 게임 (Streamlit)")

st.write(f"⏰ 남은 시간: **{remaining_time}초**")
st.write(f"🎯 현재 점수: **{st.session_state.score}점**")

if not st.session_state.game_over:
    cols = st.columns(3)
    for i in range(1, 10):
        col = cols[(i-1) % 3]
        with col:
            if i == st.session_state.mole_pos:
                if st.button("🐹", key=f"btn{i}"):
                    st.session_state.score += 1
                    st.session_state.mole_pos = random.randint(1, 9)
            else:
                st.button(" ", key=f"btn{i}", disabled=True)
    st.experimental_rerun()
else:
    st.success(f"🏁 게임 종료! 최종 점수는 {st.session_state.score}점입니다.")
    if st.button("🔄 다시 시작"):
        restart_game()
