
from threading import Thread
import requests
from datetime import datetime
from time import sleep

#word_count - количество записываемых слов
#file_name - название файла, куда будут записываться слова
#counter_str = 0
def wite_words(word_count, file_name):
    counter_str = 0
    file = open(file_name, 'w', encoding='utf-8')

    for i in range(word_count):
        counter_str += 1
        file.write(f"Какое-то слово № {counter_str}\n")
        sleep(0.1)
    file.close()


    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_finish = datetime.now()
res_time = time_finish - time_start
print(f'Работа потоков{res_time}')


time_start2 = datetime.now()

thr_fist   = Thread(target=wite_words,args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words,args=(30, 'example6.txt'))
thr_fird   = Thread(target=wite_words,args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words,args=(100, 'example8.txt'))

thr_fist.start()
thr_second.start()
thr_fird.start()
thr_fourth.start()

thr_fist.join()
thr_second.join()
thr_fird.join()
thr_fourth.join()

time_finish2 = datetime.now()
res_time2 = time_finish2 - time_start2
print(f'Работа потоков{res_time2}')
