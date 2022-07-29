# streamlit 으로 선택을 연습하는데 중점을 둠
# 안타깢디만 주소검색은 현재 보이지 않음

import streamlit as st
import pandas as pd
import numpy as np
import requests, xmltodict, json
import time
from urllib import parse
import datetime as dt
import traceback

def main():
    try:
        st.title('streamlit 연습')
        ## Header/Subheader
        st.header('This is header')
        st.subheader('This is subheader')

        ## Text
        st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

        ## Markdown syntax
        st.markdown("# This is a Markdown title")
        st.markdown("## This is a Markdown header")
        st.markdown("### This is a Markdown subheader")
        st.markdown("1. item 1\n"
                    "   1. item 1.1\n"
                    "   2. item 1.2\n"
                    "2. item 2\n"
                    "3. item 3")
        st.markdown("# <h1> h1태그 </h1>")

        ## Checkbox
        location = st.text_input("건물 주소를 동 까지 입력해주세요 ex) 경기도 성남시 중원구 여수동")

        if st.checkbox("체크박스위젯"):
            st.write("체크박스가 선택되었습니다.")

        ## Radio button
        status = st.radio("전/월세를 선택하세요.", ("전세", "월세"))
        if status == "전세":
            st.success("전세입니다.")
            deposit= st.text_input("보증금을 만원단위로 입력하세요")
        elif status == "월세":
            st.success("월세입니다")
            rent = st.text_input("월세를 만원 단위로 입력하세요")
            deposit = st.text_input("보증금을 만원단위로 입력하세요")
        else:
            st.write("오류입니다.")

        ## Select Box
        occupation = st.selectbox("건물종류를 선택하세요.",
                                  ["아파트",
                                   "연립,다세대",
                                   "단독,다가구",
                                   "오피스텔"])
        if occupation == "단독,다가구":
            aarea = st.text_input("전용면적을 입력해주세요 (m2)")

        st.write("당신은", occupation,",",status, " 를 선택하셨습니다.")
        st.write("보증금은 ", deposit,"만원인니다.")
        if status == "월세":
            st.write("월세는 ", rent, "만원입니다.")



    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print('예기치 못한 오류가 발생했습니다.')
        print('3초뒤 다시 시작합니다')
        time.sleep(3)

main()

# 아마 안될것 같은데 그래서 예제도 전혀 없지 싶은데
# st.markdown으로 <script> 태그를 이용해서 적는걸 한번은 해봐야된다.