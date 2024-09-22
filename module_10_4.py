from threading import Thread
from time import sleep
import random
import queue

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(random.randint(3, 10))

class Cafe:
    def __init__(self,*tables):
        self.queue = queue.Queue()
        self.tables = []
        for table in tables:
            self.tables.append(table)

    def guest_arrival(self, *guests):
#        [table.guest = guest for table in self.tables  for guest in guests if table.guest == None]

        for guest in guests:
                for table in self.tables :
                    if table.guest == None:
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        table.guest = guest
                        break
                    elif guests.index(guest) > len(self.tables):
                        self.queue.put(guest)
                        print(f'{guest.name} в очереди.')
                        break

    def discuss_guests(self):
        while self.queue.empty() != True:
            for table in self.tables:
                    guest = table.guest
                    if guest == None:
                        f=1
                    else:
                        guest.start()
                        guest.join()
                        print(f"{guest.name} за текущим {table.number} покушал(-а) и ушёл(ушла)")
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None

                        if self.queue.empty() == True:
                            pass
                            #print('Все гости наелись и сьебались')
                        else:
                            guest_from_queve = self.queue.get()
                            print(f'{guest_from_queve.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest = guest_from_queve














# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()