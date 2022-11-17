import streamlit as st
from datetime import datetime
from uility import set_page
from database import insert_quiz_result
from streamlit_extras.switch_page_button import switch_page
import time


tm = time.strftime('%a, %d %b %Y %H:%M:%S')
now = datetime.now()
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
date = now.strftime("%d/%m/%Y")


def difference_time(time1, time2):
    time_difference = time2 - time1
    tsecs = round(time_difference.total_seconds())
    remain_sec = round(tsecs % 60)
    tmins = tsecs // 60
    display_time = str(tsecs)
    return display_time


set_page()

placeholder = st.empty()
with placeholder.container():
    language = st.session_state['language']
    if "load_state_10" and "Q10" and "Q10_ans" not in st.session_state:
        st.session_state["load_state_10"] = False
        st.session_state["Q10"] = []
        st.session_state["Q10_ans"] = []
    scoring = st.session_state['scores']
    if st.session_state['correctness']:
        scoring -= 1
    top1, top2, top3 = st.columns([5, 9, 5])
    with top1:
        st.subheader(f"Question: 10")
    question_no = st.session_state['scam_question_list']
    with top3:
        st.text(f"SCAM:{question_no[9]+1}")
    image, text, ask, select, answer, reason = st.session_state['scam_operation'].return_values(question_no[9])
    st.image(image, width=400)
    st.markdown(text)
    placeholder1 = st.empty()
    with placeholder1.container():
        with st.form("Question"):
            st.subheader(ask)
            answer_select = st.radio("", select)
            st.write(" ")
            st.write(" ")
            if language == 'english':
                submit_answer = st.form_submit_button("👉Submit")
            elif language == 'chinese':
                submit_answer = st.form_submit_button("👉提交")
    if submit_answer or st.session_state.load_state_10:
        st.session_state.load_state_10 = True
        placeholder1.empty()
        st.info(answer_select)
        if answer_select == answer:
            scoring += 1
            if language == 'english':
                st.success("Correct!")
                st.success(f"Score: {scoring}")
            elif language == 'chinese':
                st.success("恭喜您答对了!")
                st.success(f"分数: {scoring}")
            st.session_state['correctness'] = True
            correctness = "Right"
        else:
            if language == 'english':
                st.error("That's incorrect")
                st.error(f"Score: {scoring}")
                st.error(f"Please find the Digital Ambassador for assistance on Scam Question: {question_no[9]+1}")
            elif language == 'chinese':
                st.error("抱歉！您答错了")
                st.error(f"分数: {scoring}")
                st.error(f"请向数码大使寻求帮助: 骗局问题 {question_no[9] + 1}")
            st.session_state['correctness'] = False
            correctness = "Wrong"
        question_number = question_no[9]+1
        st.write(reason)
        st.session_state['scores'] = scoring
        if language == 'english':
            submit_qns = st.button("👉Finish")
        elif language == 'chinese':
            submit_qns = st.button("👉完成")
        if submit_qns:
            stop_time = datetime.now()
            display_time = difference_time(st.session_state["start_time"], stop_time)
            st.session_state.Qns.append(question_number)
            st.session_state.Ans.append(correctness)
            placeholder.empty()
            del st.session_state["load_state_10"]
            senior_name = st.session_state.senior_name
            key = str(tm) + senior_name
            insert_quiz_result(key, date, st.session_state.senior_name, st.session_state.scores, display_time,
                               st.session_state.Qns, st.session_state.Ans)

            switch_page("congratz")

