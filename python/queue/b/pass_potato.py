from a.queue import Queue


def pass_potato(lists, num: int):
    """ 传递土豆模拟 """
    queue = Queue()
    for i in lists:
        queue.enqueue(i)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()
