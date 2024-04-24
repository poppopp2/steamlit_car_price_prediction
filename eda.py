import streamlit as st
import pandas as pd


def run_eda():
    st.subheader('탐색적 데이터 분석')

    st.text('데이터프레임 보기/ 통계치 보기를 할 수 있습니다.')

    df=pd.read_csv('data/Car_Purchasing_Data.csv')

    radio_menu=['데이터프레임' ,'통계치 보기']

    choice=st.radio('선택하세요.', radio_menu)

    if choice == radio_menu[0]:
        st.dataframe(df)
    elif choice == radio_menu[1]:
        st.dataframe(df.describe())


    #각 컬럼별로 최대/ 최소 값을 보여주는 화면 개발.
    #유저가 컬럼을 선택하면, 해당 커럶의 최대/ 최소 데이터를 보여주도록하자.
    st.text('컬럼을 선택하면, 각 컬럼별 최대/ 최소 데이터를 보여드립니다.')
    column_list=['Age',	'Annual Salary', 'Credit Card Debt',	'Net Worth','Car Purchase Amount']
    st.selectbox('컬럼을 선택 하세요.',column_list)
    
