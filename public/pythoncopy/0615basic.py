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
from bs4 import BeautifulSoup

def void(): #main 격의 자리이며 그외 함수는 이 위에 def로 지정
    while True:
        try:
            print("hello")
            time.sleep(1)

            c = input("종료하려면 x를 누르세요 : ")
            if c == 'x':
                break


        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print('예기치 못한 오류가 발생했습니다.')
            print('3초뒤 다시 시작합니다')
            time.sleep(3)

void()


# 거의 모든경우 이렇게 진행
