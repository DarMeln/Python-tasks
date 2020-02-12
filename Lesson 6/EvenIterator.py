class EvenIterator():

    def __init__(self, arr):
        self.arr = arr
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.arr):  # Check for end
            self.counter += 1
            if self.counter % 2 == 0:  # Check if index is even
                return self.arr[self.counter]
            else:
                return self.__next__()  # If not then next is even
        else:
            raise StopIteration


  # Example:
x = EvenIterator([1,2,3,4,5,6,7])
for elem in x:
    print(elem)
