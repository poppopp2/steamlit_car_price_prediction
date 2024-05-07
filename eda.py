import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from itertools import combinations

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
    choice_column = st.selectbox('컬럼을 선택 하세요.',column_list)

    st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].max()])

    st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].min()])

    st.subheader('상관관계 분석')
    st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')

    corr_column_list=['Age', 'Annual Salary', 'Credit Card Debt',	'Net Worth', 'Car Purchase Amount']
    selected_columns = st.multiselect('컬럼을 선택하세요.', corr_column_list)


    if len(selected_columns) >= 2:

        #.상관계수 보여준다.
        st.dataframe(df[selected_columns].corr())


        
        #1. 페어플롯을 그린다.
        #tobo : 1. pairplot 을 다른 라이브러리 이용해서 하는 방법
        # pairplot 말고, 반복문으로 두 컬럼씩 관계를 차트로 그리는 방법
        pair_plot = sb.pairplot(data=df, vars=selected_columns)
        pair_plot.fig.suptitle("corr",y=1.02)
        st.pyplot(pair_plot)

    


        combinations_list = list(combinations(selected_columns, 2))
        for pair in combinations_list:
            pair_plot = sb.pairplot(data=df, vars=pair)
            st.pyplot(pair_plot)


    else:
        st.text('컬럼은 2개이상 선택해야 합니다.')


    
    
