import threading
import time

class Knight(threading.Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.counter = 0

    def run(self):
        print(f"{self.name}, На нас напали!")
        while self.enemy > 0:
            self.enemy -= self.power
            time.sleep(1)
            self.counter += 1
            if self.enemy > 0:
                print(f"{self.name} сражается {self.counter}..., осталось {self.enemy} воинов.")
            else:
                print(f"{self.name} сражается {self.counter}..., осталось 0 воинов.")
        print(f"{self.name} одержал победу спустя {self.counter} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
time.sleep(0.5)
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")