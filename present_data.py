import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import fetch_db


db_content = fetch_db()
# main_df = pd.DataFrame(db_content)
# df_sorted_desc= main_df.sort_values('result',ascending=False)
# df = df_sorted_desc.iloc[:10]
#
# with st.sidebar:
#     st.info(
#     "πThe available dates for viewing will only appear if there is at least **ONE** quiz entry of that date"
#     )

def date_select():
    uniquedates_list = list(db_content['Name'].unique())
    st.selectbox(
        "Select a Date",
        uniquedates_list
    )

def main():
    date_select()
 # st.dataframe(df)
#     page = st.sidebar.selectbox(
#         "Select a Page",
#         [
#             "Count Plot", #New page
#         ]
#     )
#     if page == "Line Plot":
#         print("")
#
#     elif page == "Count Plot":
#         countPlot()
#
# def countPlot():
#     plt.figure(figsize=(9, 5))
#     sns.barplot(data=df, y='results', x='names')
#     plt.title('Top 10 Participants with highest scores/εΎεζι«ηε10ε')
#     plt.xlabel("Names/εε­")
#     plt.xticks(rotation=30, horizontalalignment="center")
#     plt.ylabel('Scores/εζ°');

main()