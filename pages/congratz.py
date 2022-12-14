import streamlit as st
from uility import set_page, cheering_sound


set_page()

def congratz_page():
    language = st.session_state['language']
    st.image("https://animatedimagepic.com/image/congratulations/congratulations-4308.gif")
    if st.session_state['scores'] == 10:
        if language == 'english':
            st.header("ð¯You have full scores!! ")
            st.header("Well Done!!")
        elif language == 'chinese':
            st.header("ð¯æ­åæ¨æ¿å°æ»¡åï¼ï¼")
    elif st.session_state['scores'] >= 1:
        if language == 'english':
            st.header(f"You have scored {st.session_state['scores']} points")
            st.header("Keep up the good work!!ð")
        elif language == 'chinese':
            st.header(f"æ­å!!ð æ¨çæ»åæ¯{st.session_state['scores']}å")
    elif st.session_state['scores'] == 0:
        if language == 'english':
            st.header("You have not scored any points")
            st.header("Don't Worry! Keep Trying!!ð")

        elif language == 'chinese':
            st.header("æ±æ­ï¼æ¨æ²¡æå¾å")
            st.header("æ²¡å³ç³»!ç»§ç»­åªå!ð")

    st.balloons()
    cheering_sound()
    if language == 'english':
        st.subheader("Book an appointment with us to learn more digital skills")
        st.success("Geylang East Public Library - Hotline: 89401782 - 1pm to 6pm")
        st.success("Macpherson Community Centre - Hotline: 89401662 - 10am to 6pm")
        st.success("Kembangan Community Centre - Hotline: 91392414")
    elif language == 'chinese':
        st.subheader("æ¬¢è¿ä¸æä»¬é¢çº¦ä»¥äºè§£æ´å¤æ°ç æè½")
        st.success("è½èå¾ä¹¦é¦(Geylang East Library) - ç­çº¿: 89401782 - ä¸­å1ç¹å°ä¸å6ç¹ ")
        st.success("éº¦æ³¢ç³èç»æ(Macpherson CC) - ç­çº¿: 89401662 - æ©ä¸10ç¹å°ä¸å6ç¹ ")
        st.success("çæ¦æ¯ä¸å²¸èç»æ(Kembangan CC) - ç­çº¿: 91392414")
    st.image("https://www.imda.gov.sg/-/media/Imda/Images/Content/For-Community/Digital-for-Life/DfL-logo.jpg")


congratz_page()

