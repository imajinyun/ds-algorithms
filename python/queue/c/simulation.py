import random

from a.queue import Queue

from printer import Printer
from task import Task


def simulation(seconds, pages):
    """
    打印任务模拟程序

    Args:
        - seconds (int): 允许设置设置的总时间
        - minutes (int): 打印机每分钟打印多少页
    """
    printer = Printer(pages)
    queue = Queue()
    waitingTimes = []

    for i in range(seconds):
        if is_new_task():
            task = Task(i)
            queue.enqueue(task)

        if not printer.busy() and not queue.isEmpty():
            newTask = queue.dequeue()
            waitingTimes.append(newTask.waitingTime(i))
            printer.startNext(newTask)

        printer.work()

    avgWaitingTimes = sum(waitingTimes) / len(waitingTimes)
    print("Average wait %6.2f secs %3d tasks reaming" % (avgWaitingTimes, queue.size()))


def is_new_task():
    """ 模拟平均每 180 秒有一个打印任务 """
    num = random.randrange(1, 181)
    return True if num == 180 else False
