import threading
import time


class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            time.sleep(1)  # Thinking
            print(f"{self.name} is hungry \n")
            self.dine()

    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork

        with fork1:
            with fork2:
                self.eating()

    def eating(self):
        print(f"{self.name} is eating \n")
        time.sleep(1)  # Eating
        print(f"{self.name} finished eating \n")


if __name__ == "__main__":
    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ["Philosopher-1", "Philosopher-2", "Philosopher-3", "Philosopher-4", "Philosopher-5"]

    philosophers = [
        Philosopher(philosopher_names[i], forks[i % 5], forks[(i + 1) % 5])
        for i in range(5)
    ]

    for philosopher in philosophers:
        philosopher.start()
