

class SparseArray:
    def __init__(self, arr , size):
        self.arr = {}
        self.size = size

        for idx , i in enumerate(arr):
            if i != 0:
                self.arr[idx] = i



    def set(self, idx ,val):
        if idx > self.size or 0 > idx:
            print("Index Error")
        else:
            self.arr[idx] = val


    def get(self, idx):
        if idx > self.size or 0 > idx:
            print("Index Error")
        if self.arr.get(idx) is None:
            return 0
        else:
            return self.arr.get(idx)


arr = SparseArray([0, 0, 0], 5)

## TEST
print(arr.get(0))
print(arr.get(3))

arr.get(-1)
arr.get(5)
arr.set(5, 0)

arr.set(0, 2)
print(arr.get(0))

arr.set(4, 1)
print(arr.get(4))# == 1





