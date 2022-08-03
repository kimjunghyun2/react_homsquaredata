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
        global location  # 지역
        global filename  # 파일네임
        KEY = 'kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D'
        st.title('streamlit 연습')
        ## Header/Subheader
        #st.header('This is header')
        #st.subheader('This is subheader')

        ## Text
        st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

        ## Markdown syntax
        #st.markdown("# This is a Markdown title")
        #st.markdown("## This is a Markdown header")
        #st.markdown("### This is a Markdown subheader")
        #st.markdown("1. item 1\n"
        #            "   1. item 1.1\n"
        #            "   2. item 1.2\n"
        #            "2. item 2\n"
        #            "3. item 3")
        #st.markdown("# <h1> h1태그 </h1> ")

        html = """
            <div style='
                background-color:red;
                color:white;
            '>
                안녕하세요
                </div>
            """

        st.markdown(html ,unsafe_allow_html=True) # 이자리가 원래 주소찾기 자리지만
        #code = '''def hello():
        #            print("test, streamlit")'''

        #st.code(code, language='python')

        ## Checkbox
        location = '서울특별시 종로구'
        location = st.text_input("건물 주소를 구 까지 입력해주세요 서울시는 서울특별시로 입력해 주세요 ex) 서울특별시 송파구, 경기도 성남시 중원구,")
        location_encoded = parse.quote(location)

        url0 = 'https://apis.data.go.kr/1741000/StanReginCd/getStanReginCdList?serviceKey='+ KEY +'&pageNo=1&numOfRows=3&type=xml&locatadd_nm=' + location_encoded
        res0 = requests.get(url0, verify=False)
        dict_res0 = xmltodict.parse(res0.content)
        json_string0 = json.dumps(dict_res0['StanReginCd'], ensure_ascii=False)

        jsonObj0 = json.loads(json_string0)
        df0 = pd.DataFrame(jsonObj0['row'], index=[0])
        df0.columns = ['법정동코드전체', '시도코드', '시군구코드', '읍면동코드', '리코드', '주민지역코드', '지적지역커드', '지역주소명', '서열', '비고',
                       '상위지역코드', '최하위지역명', '생성일']

        st.write(df0)
        search = df0[['법정동코드전체', '시도코드', '시군구코드']].head()
        search2 = df0.loc[0, ['법정동코드전체']]
        sd_code = df0.iloc[0]['시도코드']
        sgg_code = df0.iloc[0]['시군구코드']
        bdleft = sd_code+sgg_code
        st.write(search)
        st.write(search2.head())
        st.write('['+location + '] 의 법정동코드는 [' + bdleft + '] 입니다.' )

        if st.checkbox("체크박스위젯"):
            st.write("체크박스가 선택되었습니다.")

        ## Radio button
        status = st.radio("전/월세를 선택하세요.", ("전세", "월세"))
        if status == "전세":
            st.success("전세입니다.")
            deposit= st.number_input("보증금을 만원단위로 입력하세요")
        elif status == "월세":
            st.success("월세입니다")
            rent = st.number_input("월세를 만원 단위로 입력하세요")
            deposit = st.number_input("보증금을 만원단위로 입력하세요")
        else:
            st.write("오류입니다.")

        ## Select Box
        occupation = st.selectbox("건물종류를 선택하세요.",
                                  ["아파트",
                                   "연립,다세대",
                                   "단독,다가구",
                                   "오피스텔"])
        if occupation == "단독,다가구":
            aarea = st.number_input("전용면적을 입력해주세요 (m2)")

        YMD = st.date_input("연월을 입력해주세요")
        intbd = int(bdleft)
        st.write('['+location + '] 의 법정동 주소 앞 5자리는 ['+ str(intbd) +']입니다.')
        st.write(YMD)
        Qdate = YMD.strftime('%Y%m') #연월만 추출 이역시 문자열
        #Rdate = YMD.isoformat() # 날짜를 문자형으로 변환
        #Sdate = YMD.year # 날짜를 문자형으로 바꿔줌
        #Sdate2 = YMD.month # dt.strftime은 일부만 추출용
        st.write('입력된 연월은 [' + Qdate + '] 입니다.')
        #st.write(Rdate)
        #st.write(Sdate)
        #st.write(Sdate2)
        #st.write(type(YMD)) # type()은 단순 자료형 검사기
        #st.write(type(Sdate2))

        st.write("당신은 [", occupation,"] ,[",status, "] 를 선택하셨습니다.")
        st.write("보증금은 ", deposit,"만원입니다.")
        if status == "월세":
            st.write("월세는 ", rent, "만원입니다.")

    except TypeError as e:
        print(e)
        print(traceback.format_exc())
        st.warning('잘못된 법정동코드/연월 입력입니다.')
        time.sleep(1)
        st.warning(' 법정동코드/연월을 다시 확인해주세요')
        time.sleep(1)
        print('3초뒤 다시 시작합니다')
        time.sleep(3)
    except KeyError as e:
        print(e)
        print(traceback.format_exc())
        print('잘못된 주소입력입니다.')
        st.warning('잘못된 주소입력입니다.')
        time.sleep(1)
        st.warning('주소를 한글로 정확히 입력했는지 확인바랍니다.')
        time.sleep(1)
        st.warning('광역시는 광역시 이름을 붙여야 합니다 예)서울시 >> X 서울특별시 >> O')
        time.sleep(1)
        print('3초뒤 다시 시작합니다')
        st.warning('다시 입력해 주세요')
        time.sleep(3)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print('예기치 못한 오류가 발생했습니다.')
        print('3초뒤 다시 시작합니다')
        st.write('예기치 못한 오류가 발생했습니다.')
        st.write('3초뒤 다시 시작합니다')
        time.sleep(3)

main()

# 아마 안될것 같은데 그래서 예제도 전혀 없지 싶은데
# st.markdown으로 <script> 태그를 이용해서 적는걸 한번은 해봐야된다.