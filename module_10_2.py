from threading import Thread
import requests
from time import sleep

class Knight(Thread):

    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        opponent = 100
        col_days = 0
        print(f'{self.name}, на нас напали!')
        while opponent > 0:
            col_days += 1
            sleep(1)
            opponent -= self.power
            print(f'{self.name} сражается {col_days} день(дня)..., осталось {opponent} воинов.')
            if opponent == 0 :
                print(f'{self.name} одержал победу спустя {col_days} дней(дня)!"')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились!")