#import library

import requests, xmltodict, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from urllib import parse

while True :

    #법정동코드 api로써 조회
    location = input("건물 주소를 도-시-구-동 까지 입력해주세요 : ")
    location_encoded = parse.quote(location)

    print("입력한 건물주소는 : "+ location +" 입니다. ")
    print("encoding한 주소는 ["+location_encoded+"] 입니다")
    print("3초뒤에 계속됩니다.")
    time.sleep(3)

    url0 = 'https://apis.data.go.kr/1741000/StanReginCd/getStanReginCdList?serviceKey=kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D&pageNo=1&numOfRows=3&type=xml&locatadd_nm='+location_encoded
    res0 = requests.get(url0, verify=False)
    dict_res0 = xmltodict.parse(res0.content)
    json_string0 = json.dumps(dict_res0['StanReginCd'], ensure_ascii=False)

    jsonObj0 = json.loads(json_string0)
    df0 = pd.DataFrame(jsonObj0['row'], index=[0])
    df0.columns = ['법정동코드전체', '시도코드', '시군구코드', '읍면동코드', '리코드', '주민지역코드', '지적지역커드', '지역주소명', '서열', '비고', '상위지역코드', '최하위지역명', '생성일']

    print(df0)
    search = df0[['법정동코드전체', '시도코드', '시군구코드']].head()
    search2 = df0.loc[0, ['법정동코드전체']]
    print(search)
    print(search2.head())


    dd=input("계속하려면 아무키나 누르세요")

    # api 요청변수 입력부분 법정동코드와 연월

    house = input("건물 종류를 숫자로 입력해주세요 1.아파트 2.연립 다세대 3.오피스텔 : ")
    sale = input("거래종류를 숫자로 입력해 주세요 1.매매 2.전/월세 : ")

    print("요청 자료는" + house + "와" + sale + "입니다")
    if house == 1 and sale == 1 :
        print("아파트매매입니다")


    c = input("그만하려면 x를 누르세요 : ")
    if c == 'x':
        break

    #url 작성란 요청변수는 입력을 받아야 할 수 있음
    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D&LAWD_CD=11110&DEAL_YMD=201512'
    print (url)
    print ("10초뒤에 계속됩니다")
    time.sleep(10)
    #url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=YNeaX1XgA%2BRIzGp1lEkTr00tgeUPCaTqxgrpRVXFj8CmfK0w6u6sSLLuHkgk4qR2MjJc6CKYScJVbKgOU6PdbQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200110&endCreateDt=20200810&'
    res = requests.get(url)

    #파싱 및 변수명 재설정
    dict_res = xmltodict.parse(res.content)
    json_string = json.dumps(dict_res['response']['body']['items'], ensure_ascii=False)

    jsonObj = json.loads(json_string)
    df = pd.DataFrame(jsonObj['item'])
    df.columns = ['거래금액','거래유형','건축년도','년','법정동','아파트','월','일','전용면적','중개사소재지','지번','지역코드','층','해제사유발생일','해제사유']

    #csv로 사출
    # 이유는 모르나 utf-8은 깨지고 utf-8-sig는 안깨짐
    #df.to_csv('api 테스트11.csv', index=False)
    #df.to_csv('api 테스트12.csv', index=False, encoding="utf-8")
    #df.to_csv('api 테스트15.csv', index=False, encoding="utf-8-sig")
    #df.to_excel('api액셀 테스트15.xlsx', sheet_name = '아파트 매매')
    ef = pd.read_csv('api 테스트15.csv')
    print(ef)
    #ef.to_excel('api액셀 테스트15.xlsx', sheet_name= '아파트 매매 2')

    writer = pd.ExcelWriter('api액셀 테스트15.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='아파트 매매 1')
    ef.to_excel(writer, sheet_name='아파트 매매 2')

    writer.save()

    # 액셀을 pandas로 열고 쓰고 닫는방식

    # 단순 끝지점 체크용
    a = input("아무 문자나 입려하세요 : ")
    print("hello world" + a + "입니다")
    print("hello world 끝입니다")

    b = input(" 종료하려면 X를 누르세요 : ")
    if b == 'X' :
        break;

print ("while문을 빠져나왔습니다 곧 종료됩니다.")


# 개선점들
# 1. 요청변수를 여기선 고정했는데 요청변수를 사용자 입력을 받아서 그걸 url로 지정해야함
# 2. csv 저장하는데 퍼미션 디나이드가 있음 번호도 일단 랜덤하게 정하던지 해서 피해야함
# 3. api를 총 7개를 씀 단독 다가구까지 쓰면 10개까지도 가능한 부분 특히 법정동 코드는 그부분만 읽어야 하는데.... 이건 별개
# 4. 가장 마지막 작업일 듯 한데 결국 이걸 하나의 파이썬 exe 파일로 만들어야 할듯 함 아님 액셀 파이썬 연동을 하던가.
# 5. 건물 분류와 전세,월세에 따라 다른 api를 적용해야하는 문제.. 현재도 가능은 하나 뭔가 무식하게 하는듯한 기분이