import multiprocessing
import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    file = open(name, 'r', encoding="utf-8")
    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)

# Линейный вызов
if __name__ == '__main__':
    start = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    end = datetime.datetime.now()
    print(f'{end - start} (линейный)')


# Многопроцессный
if __name__ == '__main__':
    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.datetime.now()
    print(f'{end2 - start2} (многопроцессный)')


