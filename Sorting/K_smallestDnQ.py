
class KthSmall:
    def find_k_small(self, arr, k):

        if len(arr) == 0:
            return []
        if (k == 1) and (len(arr) == 1):
            return arr[0]

        lesser = []
        equal = []
        greater = []

        mid = int(len(arr) / 2)

        for i in range(len(arr)):
            if arr[i] < arr[mid]:
                lesser += [arr[i]]
            elif arr[i] > arr[mid]:
                greater += [arr[i]]
            else:
                equal += [arr[i]]

        if len(lesser) >= k:
            return self.find_k_small(lesser, k)
        elif len(lesser + equal) >= k:
            return equal[0]
        else:
            return self.find_k_small(greater, k - len(lesser + equal))


if __name__ == "__main__":
    import numpy as np
    small_k = KthSmall()
    n = 20
    arr = np.random.randint(10, size=n).tolist()
    k = np.random.randint(n-1) + 1
    print(small_k.find_k_small(arr, k))
    print(sorted(arr)[k-1])