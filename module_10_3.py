from random import randint
from time import sleep
import threading

class Bank:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            with self.lock:
                if self.balance + a <= 500:
                    self.balance += a
                    print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            a = randint(50, 500)
            print(f"Запрос на {a}")
            with self.lock:
                if a <= self.balance:
                    self.balance -= a
                    print(f"Снятие: {a}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            sleep(0.001)

bank = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bank,))
thread2 = threading.Thread(target=Bank.take, args=(bank,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank.balance}')