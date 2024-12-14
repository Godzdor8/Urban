from random import randint
from time import sleep
import threading

class Bank:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            a = randint(50, 500)
            self.balance += a
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(1, 101):
            a = randint(50, 500)
            print(f"Запрос на {a}")
            if a <= self.balance:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.0013)

bank = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bank,))
thread2 = threading.Thread(target=Bank.take, args=(bank,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank.balance}')