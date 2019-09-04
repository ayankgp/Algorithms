
class MergeSort:
    def merge(self, arr1, arr2):
        if len(arr1) == 0:
            return arr2
        if len(arr2) == 0:
            return arr1
        if arr1[0] <= arr2[0]:
            return [arr1[0]] + self.merge(arr1[1:], arr2)
        else:
            return [arr2[0]] + self.merge(arr1, arr2[1:])

    def sort(self, arr):
        mid = int(len(arr)/2)
        if len(arr) > 1:
            return self.merge(self.sort(arr[:mid]), self.sort(arr[mid:]))
        else:
            return arr


if __name__ == "__main__":
    ms = MergeSort()
    print(ms.sort([2, 5, 3, 6, 4, 1]))