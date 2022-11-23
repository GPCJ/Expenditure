Transortaion = 0  # 교통비
Day = 0  # 일수
Food_Expenses = 0  # 식비
sum = 0  # 총합


# 교통비
def transportation(Transportaion, Day):
    Transportaion = Transportaion * 2
    return Transportaion * Day


# 식비
def food(Food_Expenses, Day):
    return Food_Expenses * Day


# 입력
Day = int(input("몇일 동안의 지출 금액을 구하고 싶으신가요? \n: "))
Transportaion = int(input("교통비 : "))
Food_Expenses = int(input("평균 식비 : "))

# 출력
print("{0}일 동안의 총 소비 예상 교통비 :".format(Day),
      format(transportation(Transportaion, Day), ','), "원")
print("{0}일 동안의 총 소비 예상 식비 :".format(Day),
      format(food(Food_Expenses, Day), ','), "원")

# 총합 지출 출력
sum = transportation(Transportaion, Day) + food(Food_Expenses, Day)
print("지출 :", format(sum, ','), "원")

# 원금
bank = 0
bank = int(input('원금 : '))

print(f'원금 : {bank:,}원')
print(f'지출 : {sum:,}원')
print(f'남는 돈 : {bank - sum:,}원')
