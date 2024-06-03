



class MyList:
    def __init__(self, num4=None):
        self._list = num4 if num4 is not None else []

    def append(self, item):
        self._list.append(item)

    def get_list(self):
        return self._list

from contextlib import contextmanager

@contextmanager
def managed_list(mylist):
    original_list = mylist._list[:]
    try:
        yield mylist
    except Exception as e:
        mylist._list = original_list
        raise e

if __name__ == "__main__":
    num1 = MyList([1, 2, 3])

    try:
        with managed_list(num1) as num2:
            num2.append(4)
            num2.append(5)
            raise ValueError("nimadur hato!")
    except ValueError as e:
        print(f"xatolik: {e}")

    print(num1.get_list())  

    try:
        with managed_list(num1) as num2:
            num2.append(6)
            num2.append(7)
    except ValueError as e:
        print(f"xatolik: {e}")

    print(num1.get_list())  

