



class MyList:
    def __init__(self, initial=None):
        self._list = initial if initial is not None else []
        self._original = self._list[:]

    def append(self, item):
        self._list.append(item)

    def get_list(self):
        return self._list

    def __enter__(self):
        self._original = self._list[:]
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:  
            self._list = self._original
        return False  
if __name__ == "__main__":
    num1 = MyList([1, 2, 3])

    try:
        with num1 as num2:
            num2.append(4)
            num2.append(5)
            raise ValueError("nimadur hato!")
    except ValueError as e:
        print(f"xatolik: {e}")

    print(num1.get_list()) 

    try:
        with num1 as num2:
            num2.append(6)
            num2.append(7)
    except ValueError as e:
        print(f"xatolik: {e}")

    print(num1.get_list())  
