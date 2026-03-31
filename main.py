# 파일이름 : main.py
# 작 성 자 : 이인


age = int(input("나이를 입력하세요:"))
discount = input("할인 쿠폰이 있나요? (Y/N):")

print("-------------------------\n결과:")
if( age < 13 and  discount == 'Y'):
    print("🍿 꼬마 VIP 고객님! 팝콘 무료 증정!")
    print("티켓 요금 : 무료입니다.")
elif ( age >= 65 or discount == 'Y'):
    print("티켓 요금 : 무료입니다.")
else :
    print("티켓 요금 : 15,000원입니다")
