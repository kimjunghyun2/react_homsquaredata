#import library

import requests, xmltodict, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from urllib import parse
import datetime as dt
import urllib3
import traceback
import os

def mkfilename(): # datetime과 지역구로 파일명 생성
    x = dt.datetime.now()
    str(x)
    print(x)
    x2 = x.strftime("%a") + x.strftime("%b") + x.strftime("%d") + x.strftime("%f") + x.strftime("%y")
    print(x2)
    filename = ee +' '+ x2
    print(filename)
    time.sleep(3)
    return filename

def mkdataframe(url): #url로 호출한 api pandas dataframe로 받기
    print (url)
    print ("3초뒤에 계속됩니다")
    time.sleep(3)

    res = requests.get(url,verify=False)

    #파싱 및 변수명 재설정
    dict_res = xmltodict.parse(res.content)
    json_string = json.dumps(dict_res['response']['fields'], ensure_ascii=False)

    jsonObj = json.loads(json_string)
    df = pd.DataFrame(jsonObj['field'])

    return df

def printarea():
    area = float(input("면적을 숫자로만 입력하세요 (m2) : "))
    areas = area - 3.3
    areab = area + 3.3
    df['전용면적'] = df['전용면적'].astype(float)
    df1 = df.loc[(df['전용면적'] >= (areas)) & (df['전용면적'] <= (areab))]
    print(df1)
    df1.to_excel('C:/Users/skflc/Desktop/0523result/' + filename + ' filtered.xlsx')

while True :
    try:
        #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 경고가 거슬리면 위의 urllib앞 주석(#) 제거

        c = input("그만하려면 x를 누르세요 : ")
        if c == 'x':
            break

        origin = pd.read_excel(' 부동산개발업 목록   FriMay2744301522.xlsx')
        print(origin)
        #task = (origin[])# .loc 조건식
        origin2 = origin[['부동산개발업상호', '대표자', '도로명주소코드', '도로명주소기타주소', '전화번호', '법정동명', '기타주소']]
        print(origin2)
        origin2.to_excel('C:/Users/skflc/Desktop/0527result/teste12.xlsx')
        origin3 = origin2.fillna('NaN')
        print(origin3)
        origin3 = origin3[(origin3['법정동명'] != 'NaN') & (origin3['전화번호'].str.len() > 9)]
        print(origin3)
        origin3.to_excel('C:/Users/skflc/Desktop/0527result/test10-10.xlsx')
        origin3 = origin3[(origin3['기타주소'] != 'NaN')]
        print(origin3)
        origin3.to_excel('C:/Users/skflc/Desktop/0527result/test10-2.xlsx')
        origin4 = origin3[origin3['기타주소'].str.contains('호') == False]
        origin4.to_excel('C:/Users/skflc/Desktop/0527result/test11-2F.xlsx')
        origin5 = origin3[origin3['기타주소'].str.contains('호')]
        print(origin5)
        origin5.to_excel('C:/Users/skflc/Desktop/0527result/test11-2.xlsx')



        b = input("그만하려면 X를 누르세요 : ")
        if b =='X':
            break

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
print ("X를 누르셨습니다. 곧 종료됩니다.")


# 개선점들
# 1. 필터링이 좀 2번 거쳐야 할듯함 등록일자와 등록상태 처리상태로
# 필터링 기능은 부가적인 기능으로 보류 test9로 pyqt진행 여기서는 면적만 받는것으로 함