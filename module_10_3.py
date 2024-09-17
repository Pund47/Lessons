import threading
import random
from threading import Thread,Lock
from time import sleep




class Bank:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0
    def deposit(self):
        for i in range(100):
            pop = 0
            pop = random.randint (50,500)
            self.balance = self.balance + pop
            print(f'Пополнение: {pop}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            pop = 0
            pop = random.randint(50, 500)
            print(f'Запрос на {pop}')
            if pop <= self.balance:
                self.balance = self.balance - pop
                print(f'Снятие: {pop}. Баланс: {self.balance}')
            elif pop > self.balance:
                print(f'Запрос отклонён, недостаточно средств!')
                self.lock.acquire()



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')