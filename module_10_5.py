import time
import multiprocessing as mp


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            if file.readline():
                all_data.append(file.readline())
            else:
                break

filenames = [f'file {number}.txt' for number in range(1, 5)]

#start = time.time()
#for file in filenames:
#    read_info(file)
#end = time.time()
#print(end - start)

if __name__ == '__main__':
    start = time.time()
    with mp.Pool(4) as pool:
        pool.map(read_info, filenames)
    end = time.time()
    print(end - start)