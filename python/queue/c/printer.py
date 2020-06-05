class Printer:

    def __init__(self, pages):
        # 打印机每分钟要打印的页数
        self.pages = pages
        self.currentTask = None
        self.remainingTime = 0

    def work(self):
        if self.currentTask is not None:
            self.remainingTime = self.remainingTime - 1
            if self.remainingTime <= 0:
                self.currentTask = None

    def busy(self) -> bool:
        return True if self.currentTask is not None else False

    def startNext(self, task):
        self.currentTask = task
        self.remainingTime = task.getPages() * 60 / self.pages
