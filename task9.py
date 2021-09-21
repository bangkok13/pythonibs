# -*- coding: utf-8 -*-
import random
import sys
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"{self.name} is running\n")
        for item in reversed(Array):
            time.sleep(1)
            print(f"{self.name} counter is: {item}")
        print(f"{self.name} has stopped\n")


def create_threads():
    for i in range(2):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()