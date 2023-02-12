import random


# 우리나라의 모든 도를 맞추는 퀴즈를 진행 할 수 있는 Quiz 클래스를 구현하세요.
#   - Quiz 클래스는 다음과 같은 클래스 변수를 들고 있습니다.
#       ㄴ answer = ['경기도', '강원도', '충청도', '전라도', '경상도', '제주특별자치도']
#   - challenge() 메소드는 사용자의 입력을 처리하고 일치하는 정답이 있으면 정답입니다 출력한 뒤, 해당 정답을
#     answer 에서 삭제후, 다시 challenge 호출
#   - challenge() 메소드는 사용자의 입력이 틀린경우, 틀렸습니다. 라는 예외 메세지를 출력할 수 있도록 예외 발생


# class Quiz:
#     answer = ['경기도', '강원도', '충청도', '전라도', '경상도', '제주특별자치도']
#
#     @classmethod
#     def challenge(cls):
#         a = (input("우리나라의 도중 하나를 입력해 주세요. >>> "))
#         if Quiz.answer.count(a) > 0:
#             print('정답입니다.')
#             Quiz.answer.remove(a)
#             cls.challenge()
#         else:
#             raise Exception("틀렸습니다.")

# UpDown 클래스를 구현.
#   - UpDown 클래스를 생성하면 (생성자를 호출하면) 1~100 사이의 난수가 인스턴스 변수 answer 에 저장.
#   - challenge() 메소드는 사용자의 입력을 처리합니다. 유효하지 않은 정숫값을 입력하면 예외를 발생시키고,
#       1~100 사이만 입력하세요 라는 예외 메세지를 출력합니다.
#   - challenge() 메소드가 호출될 때마다 인스턴스 변수 count 가 1 씩 증가 합니다. 최종적으로 count 변숫값으로
#       몇 번의 시도끝에 성공했는지 알 수 있습니다.
#   - 생성된 난수를 맞히기 전에는 프로그램이 종료되지 않습니다.
#   - 정수 대신 다른 자료형의 값은 입력되지 않는다고 가정.

class UpDown:
    def __init__(self):
        self.answer = random.randint(1,100)
        self.count = 0

    def play(self):
        self.challenge()



    def challenge(self):
        self.count += 1
        i = int(input('(1~100) 입력 >>>'))

        try:
            if 1 <= i <= 100:
                if self.answer == i:
                    print(f'{self.count}번 만의 정답입니다.')
                elif self.answer > i:
                    print('Up')
                else:
                    print('Down')
            else:
                raise Exception('1~100사이의 숫자만 입력하세요.')
        except Exception as e:
            print(e)
        self.challenge()

class BankError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BankAccount:
    def __init__(self, account, money):
        self.account = account
        self.money = money

    def deposit(self, money):
        if money <= 0:
            raise BankError(f'{money} 입금 불가')
        else:
            self.money += money

    def withdraw(self, money):
        if money <= 0:
            raise BankError(f'{money} 출금 불가')
        elif self.money < money:
            raise BankError('돈이 없습니다.')
        else:
            self.money -= money

    def transfer(self, bank, money):
        try:
            self.withdraw(money)
            bank.deposit(money)
        except BankError as e:
            print(e)

    def info(self):
        print(f'계좌번호 : {self.account}')
        print(f'잔액 : {self.money}')
