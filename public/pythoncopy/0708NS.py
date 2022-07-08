# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import time
import traceback
from urllib import parse
import datetime as dt
import pandas as pd
import requests, xmltodict, json

def mkfilename(): # datetime과 지역구로 파일명 생성
    x = dt.datetime.now()
    str(x)
    print(x)
    x2 = x.strftime("%a") + x.strftime("%b") + x.strftime("%d") + x.strftime("%f") + x.strftime("%y")
    print(x2)
    dir = '2022년 7월 8일'
    filename =dir + " " + x2
    print(filename)
    time.sleep(3)
    return filename

def mkdataframe(url): #url로 호출한 api pandas dataframe로 받기
    print (url)
    # print ("1초뒤에 계속됩니다")
    # time.sleep(1)

    res = requests.get(url)

    #파싱 및 변수명 재설정
    #dict_res = xmltodict.parse(res.content)
    dict_res = xmltodict.parse(response)
    print(res)
    print(dict_res)
    print(response)
    response_body = response.read()
    print(response_body)
    print(response_body.decode('utf-8'))
    json_string = json.dumps(dict_res['rss']['channel'], ensure_ascii=False)

    jsonObj = json.loads(json_string)
    df = pd.DataFrame(jsonObj['item'])

    return df

def void():
    while True:
        try:
            global response
            global url
            c = input("종료하려면 x를 누르세요 : ")
            if c == 'x':
                break
            client_id = "gugTIL3H81nbJrGUdxpE"
            client_secret = "gMhJSat0kH"
            encText = urllib.parse.quote("공인중개사")
            for i in range(1, 11):
                # url = "https://openapi.naver.com/v1/search/news?query=" + encText  # json 결과
                ii = str(i)
                url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText + '&display=100&start=' + ii  # xml 결과
                request = urllib.request.Request(url)
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                print(url)
                print(response)
                print(request)
                if (rescode == 200):

                    filename = mkfilename()
                    df = mkdataframe(url)
                    df.columns = ['제목', '원본링크', '뉴스링크', '내용요약', '작성시각']
                    df.to_excel('C:/Users/skflc/Desktop/0708result/' + filename + '.xlsx')  # 폴더경로+ 파일명 + .xlsx
                    # response_body = response.read()
                    # print(response_body.decode('utf-8'))
                    print(i)
                else:
                    print("Error Code:" + rescode)


        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print('예기치 못한 오류가 발생했습니다.')
            print('3초뒤 다시 시작합니다')
            time.sleep(3)
            continue
void()


# 네이버 뉴스검색 api를 대체하지만 이거 판다스로 액셀에 추가해서 하는게 귀찮아서 넘겼음 