#import library

import requests, xmltodict, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#url 작성란 요청변수는 입력을 받아야 할 수 있음
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=kGN3LmvLVDIB26IbtOB9522yukFv74%2FVrqMvR2k6fqQftVvcqVj%2FyhIlztF%2BndXlgRCasv4LQd0rklNaCAdMWw%3D%3D&LAWD_CD=11110&DEAL_YMD=201512'
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
df.to_csv('api 테스트15.csv', index=False, encoding="utf-8-sig")
df.to_excel('api액셀 테스트15.xlsx')
ef = pd.read_csv('api 테스트15.csv')
print(ef)

# 단순 끝지점 체크용
print("hello world 끝입니다")


# 개선점들
# 1. 요청변수를 여기선 고정했는데 요청변수를 사용자 입력을 받아서 그걸 url로 지정해야함
# 2. csv 저장하는데 퍼미션 디나이드가 있음 번호도 일단 랜덤하게 정하던지 해서 피해야함
# 3. api를 총 7개를 씀 단독 다가구까지 쓰면 10개까지도 가능한 부분 특히 법정동 코드는 그부분만 읽어야 하는데.... 이건 별개
# 4. 가장 마지막 작업일 듯 한데 결국 이걸 하나의 파이썬 exe 파일로 만들어야 할듯 함 아님 액셀 파이썬 연동을 하던가.