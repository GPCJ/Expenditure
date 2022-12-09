from datetime import datetime
from dateutil.parser import parse

Start_Date = input("(입력 예시 : 09-11)\n 측정 시작일 정해주세요 : ")
Start_Date = parse(Start_Date)

print(Start_Date)
