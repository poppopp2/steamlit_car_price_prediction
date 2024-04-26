import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.text('자동차 가격 예측하기')

    #1. 예측하기 위해서 유저한테 입력을 받는다.
    X=['Gender','Age','Annual Salary','Credit Card Debt','Net Wort']
    st.text('성별을 선택하세요')
    Gender=st.radio('성별 선택', ['남자','여자'])
    if Gender== '남자':
        Gender = 1
    elif Gender == '여자':
        Gender = 0

    st.text('나이를 입력하세요.')
    Age=st.number_input('나이 입력',0,100,value=24)

    st.text('연봉을 입력하세요.')
    Salary=st.number_input('연봉 입력.',10000,value=50000,step=1000)

    st.text('카드빚을 입력하세요.')
    debt =st.number_input('카드빚 입력,',0,value=1000,step=1000)

    st.text('자산을 입력하세요.')
    worth= st.number_input('자산 입력.',5000,value=20000,step=1000)

    st.subheader('버튼을 누르면 예측합니다')

    if st.button('예측하기') :
        #2. 예측한다.
        #2-1. 모델이 있어야 한다.
        regressor=joblib.load('data/regressor.pkl')

        #2-2 유저가 입력한 데이터를,  모델에 예측 할 수 있도록 가공해야 한다,
        
        new_data=[Gender,Age,Salary,debt,worth]
        new_data=np.array(new_data).reshape(1,-1)    
        
        

        #2-3 모델의 predict함수로 예측한다.
        y_pred= regressor.predict(new_data)


        #위의 데이터로 예측한 자동차 구매 가능 금액은 6746달러 입니다.
        y_pred=y_pred[0]
        y_pred=round(y_pred)
        y_pred=format(y_pred,',')
        st.text(f'자동차 구매 가능 금액은 ${y_pred}달러 입니다.')





        