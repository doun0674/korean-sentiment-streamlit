import streamlit as st
import random
import time

st.set_page_config(page_title="두더지 잡기 게임", page_icon="🦫")

# 세션 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_index" not in st.session_state:
    st.session_state.mole_index = random.randint(0, 8)
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

GAME_TIME = 20  # 제한 시간 (초)
GRID_SIZE = 3   # 3x3 그리드

st.title("🦫 두더지 잡기 게임")
st.markdown("#### 제한 시간 20초 동안 최대한 많은 두더지를 잡아보세요!")

# 게임 시작 버튼
if not st.session_state.game_started:
    if st.button("🚀 게임 시작!"):
        st.session_state.score = 0
        st.session_state.mole_index = random.randint(0, 8)
        st.session_state.start_time = time.time()
        st.session_state.game_started = True
        st.session_state.game_over = False
        st.experimental_rerun()

# 게임 진행
if st.session_state.game_started and not st.session_state.game_over:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, GAME_TIME - int(elapsed))
    st.info(f"⏱️ 남은 시간: {remaining}초")

    cols = st.columns(GRID_SIZE)
    for i in range(GRID_SIZE * GRID_SIZE):
        if i % GRID_SIZE == 0 and i != 0:
            cols = st.columns(GRID_SIZE)
        col = cols[i % GRID_SIZE]

        if i == st.session_state.mole_index:
            if col.button("🦫", key=f"mole_{i}"):
                st.session_state.score += 1
                st.session_state.mole_index = random.randint(0, 8)
                break  # 한 번만 반응
        else:
            col.button("🕳️", key=f"hole_{i}")

    # 시간 초과 시 게임 종료
    if elapsed >= GAME_TIME:
        st.session_state.game_started = False
        st.session_state.game_over = True
        st.experimental_rerun()

# 게임 종료 시 결과
if st.session_state.game_over:
    st.success(f"🎉 게임 종료! 당신의 점수는 {st.session_state.score}점입니다!")
    if st.button("🔄 다시 시작하기"):
        st.session_state.score = 0
        st.session_state.mole_index = random.randint(0, 8)
        st.session_state.start_time = 0
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.experimental_rerun()
