import random

def pro():
    vac = input("어느 회사 백신을 맞으시나요? 1. 아스트라제네카 2. 얀센 3. 화이자 4. 모더나 :")
    if vac == '1':
        vac = '아스트라제네카'
    elif vac == '2':
        vac = '얀센'
    elif vac == '3':
        vac = '화이자'
    elif vac == '4':
        vac = '모더나'

    time = input("몇 차시인가요? 1. 1차 2. 2차 :")
    if int(time) == 2 and vac == '얀센':
        print("얀센은 1회 접종입니다.")
        return
    answer = input("평소 앓는 질환(고혈압, 저혈압, 당뇨 1,2형, 정신관련 제외)이 있으신가요? 1. 없음 2. 있음 :")
    if int(answer) == 2:
        print("의사와 면담을 요청합니다.")
        return
    answer = input("복용 중인 약(전문의약품 중 혈압, 당뇨, 정신과약 제외)이 있으신가요? 1. 없음 2. 있음 :")
    if int(answer) == 2:
        print("의사와 면담을 요청합니다.")
        return

    while True:
        num = random.randint(1, 30)
        answer = input(str(num) + '번 진료실로 들어가세요 1. 예 2. 아니요 :')
        if int(answer) == 1:
            print("")
            break

    print(vac + '백신' + time + '차 접종하겠습니다.')
    print('의자에 15분간 앉아계세요')
    while True:
        answer = input('상대가 괜찮으십니까? 1. 예 2. 모름 3. 안괜찮음 :')
        if answer == '1':
            print('집에 가셔도 좋습니다. 안녕히 가세요.')
            break
        elif answer == '3':
            print('119를 부릅니다.')
            break
        print('의자에 15분간 더 앉아계세요.')

if __name__ == "__main__":
    pro()
