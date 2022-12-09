import datetime as dt
from dateutil.parser import parse


# 교통비
def transportation(Transportaion, Day):
    Transportaion = Transportaion * 2
    return Transportaion * Day


# 식비
def food(Food_Expenses, Day):
    return Food_Expenses * Day




# 입력
while 1:
    Start_Date = input("(입력 예시 : 09-11)\n 측정 시작일 정해주세요 : ")

    # "오늘"을 입력하면 오늘의 날짜를 시작일 객체에 할당한다.
    if Start_Date == '오늘':
        Start_Date = str(dt.datetime.now())
        Start_Date = parse(Start_Date)
    else:
        Start_Date = parse(Start_Date)

    End_Date = input("(입력 예시 : 03-21)\n 측정 마감일 정해주세요 : ")
    End_Date = parse(End_Date)

    print(Start_Date.strftime("시작일 : %Y년 %m월 %d일 맞나요?"))
    print(End_Date.strftime("마감일 : %Y년 %m월 %d일 맞나요?"))

    Confirm = input('(Y/N)')

    # Yes 이외의 답이 나면 다시 입력 함수를 돌림
    if Confirm == 'Y' or Confirm == 'y' or Confirm == 'yes' or Confirm == 'YES':
        break
    else:
        continue

# 기간 계산
Period = End_Date - Start_Date
# 시작일과 마감일을 구해야 하기에 +2
Period = Period.days+2


# 지출 계산
Day = Period
Transportaion = int(input("교통비 : "))
Food_Expenses = int(input("평균 식비 : "))

# 입력 확인
print("{0}일 동안의 총 소비 예상 교통비 :".format(Day),
      format(transportation(Transportaion, Day), ','), "원")
print("{0}일 동안의 총 소비 예상 식비 :".format(Day),
      format(food(Food_Expenses, Day), ','), "원")

# 지출 합계 출력
sum = transportation(Transportaion, Day) + food(Food_Expenses, Day)
print("지출 :", format(sum, ','), "원")

# 원금
bank = 0
bank = int(input('원금 : '))

print(f'원금 : {bank:,}원')
print(f'지출 : {sum:,}원')
print(f'남는 돈 : {bank - sum:,}원')
