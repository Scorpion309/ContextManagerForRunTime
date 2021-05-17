from _datetime import datetime


class RunTime:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.now()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start)


if __name__ == '__main__':
    with RunTime():
        # some code here
        for i in range(1000):
            print(i)
