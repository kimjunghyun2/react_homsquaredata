import streamlit as st
import pandas as pd
import numpy as np
import requests, xmltodict, json
import time
from urllib import parse
import datetime as dt
import traceback

def mkfilename(): # datetime과 지역구로 파일명 생성
    x = dt.datetime.now()
    str(x)
    print(x)
    x2 = x.strftime("%a") + x.strftime("%b") + x.strftime("%d") + x.strftime("%f") + x.strftime("%y")
    print(x2)
    filename = '에어코리아실습 '+ x2
    print(filename)
    time.sleep(3)
    return filename


def main():
    while True:
        try:
            a = input('종료하려면 x를 누르세요 : ')
            if a =='x':
                break
            location = input("시도를 입력해주세요 : ")
            location_encoded = parse.quote(location)
            print(location)
            print(location_encoded)

            key = 'kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D'
            #url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtpvrnRltmMesureDnsty?serviceKey=' + key + '&returnType=xml&numOfRows=100&pageNo=1&sidoName='+location_encoded+'&ver=1.0'
            url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
            # params ={'serviceKey' : 'kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'searchDate' : '2020-11-14', 'InformCode' : 'PM10' }
            print(url)
            res = requests.get(url, verify=False)
            print(res.content)

            dict_res = xmltodict.parse(res.content)
            json_string = json.dumps(dict_res['response']['body']['items'], ensure_ascii=False)

            jsonObj = json.loads(json_string)
            df = pd.DataFrame(jsonObj['item'])
            df.columns = ['아황산가스지수', '잀산화탄소플래그', '통합대기환경수치', '아황산가스농도', '일산화탄소농도', 'PM2.5 미세먼지 24시간등급', '미세먼지 PM10 플래그', '오존지수', '미세먼지 PM10 농도', '통합대기환경지수', '미세먼지 PM25농도',
                          '시도명', '이산회질소 플래그', '이산회질소 지수', '오존 플래그', '미세먼지 PM25 지수', '아황산가스 플래그', '측정일', '일산화탄소 지수', '이산화질소 농도', '구명', '미세먼지 PM10 지수', '오존 농도']
            #value = 농도,수치 Flag = 플래그 Grade=지수
            print(df)

            filename = mkfilename()
            df.to_excel(filename + ".xlsx")
            df.to_excel('C:/Users/skflc/Desktop/0729result/' + filename + '.xlsx')  # 폴더경로+ 파일명 + .xlsx

            print('여기서부터는 stramlit입니다.')
            df.set_index = df['구명']
            st.title('2022 에어코리아')
            if st.button('data copyright link'):
                st.write('https://www.data.go.kr/data/15073861/openapi.do')

            if st.checkbox('Show raw data'):
                st.subheader('Raw data')
                st.write(df)

            st.subheader('역별 하차 인원')
            option = st.selectbox(
                'select location',
                (df['구명'])
            )

            location_data = df.loc[(df['구명'] == option)]
            location_data = location_data[location_data.columns.difference(['잀산화탄소플래그', 'PM2.5 미세먼지 24시간등급', '미세먼지 PM10 플래그', '시도명', '이산회질소 플래그', '오존 플래그', '아황산가스 플래그', '측정일', '구명'])]
            s_index = location_data.index.tolist()
            st.area_chart(location_data.loc[s_index[0]],use_container_width=True)




            print('완료했습니다 3초뒤 다시 시작합니다.')
            time.sleep(3)

        except KeyError as e:
            print(e)
            print(traceback.format_exc())
            print('잘못된 주소입력입니다.')
            time.sleep(1)
            print('주소를 한글로 정확히 입력했는지 확인바랍니다.')
            time.sleep(1)
            print('광역시는 광역시 이름을 붙여야 합니다 예)서울시 >> X 서울특별시 >> O')
            time.sleep(1)
            print('3초뒤 다시 시작합니다')
            time.sleep(3)
        except TypeError as e:
            print(e)
            print(traceback.format_exc())
            print('잘못된 법정동코드/연월 입력입니다.')
            time.sleep(1)
            print(' 법정동코드/연월을 다시 확인해주세요')
            time.sleep(1)
            print('3초뒤 다시 시작합니다')
            time.sleep(3)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print('예기치 못한 오류가 발생했습니다.')
            print('3초뒤 다시 시작합니다')
            time.sleep(3)

main()
print ("X를 누르셨습니다. 곧 종료됩니다.")



#본파일은 streamlit과 pandas 공공데이터포털 api의 실습 파일
#streamlit 자체에 한계 (카카오 지도 api를 못쓰는듯함)가 있을경우 Fastapi로 대체