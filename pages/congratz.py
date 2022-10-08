import streamlit as st
from uility import set_page, cheering_sound


set_page()

def congratz_page():
    language = st.session_state['language']
    st.image("https://animatedimagepic.com/image/congratulations/congratulations-4308.gif")
    if st.session_state['scores'] == 10:
        if language == 'english':
            st.header("💯You have full scores!! ")
            st.header("Well Done!!")
        elif language == 'chinese':
            st.header("💯恭喜您拿到满分！！")
    elif st.session_state['scores'] >= 1:
        if language == 'english':
            st.header(f"You have scored {st.session_state['scores']}")
            st.header("Keep up the good work!!😊")
        elif language == 'chinese':
            st.header(f"恭喜!!😊 您的总分是{st.session_state['scores']}分")
    elif st.session_state['scores'] == 0:
        if language == 'english':
            st.header("You have not scored any points")
            st.header("Don't Worry! Keep Trying!!👌")

        elif language == 'chinese':
            st.header("抱歉！您没有得分")
            st.header("没关系!继续努力!👌")

    st.balloons()
    cheering_sound()
    if language == 'english':
        st.subheader("Book an appointment with us to learn more digital skills")
        st.success("Geylang East Public Library - Hotline: 89401782 - 1pm to 6pm")
        st.success("Macpherson Community Centre - Hotline: 89401662 - 10am to 6pm")
        st.success("Kembangan Community Centre - Hotline: 91392414")
    elif language == 'chinese':
        st.subheader("欢迎与我们预约以了解更多数码技能")
        st.success("芽茏图书馆(Geylang East Library) - 热线: 89401782 - 中午1点到下午6点 ")
        st.success("麦波申联络所(Macpherson CC) - 热线: 89401662 - 早上10点到下午6点 ")
        st.success("甘榜景万岸联络所(Kembangan CC) - 热线: 91392414")



congratz_page()

