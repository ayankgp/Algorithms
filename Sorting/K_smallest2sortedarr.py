class KthSmall2SortedArr:
    def find_small_k(self, arr1, arr2, k):
        l1 = len(arr1)
        l2 = len(arr2)

        if k > l1 + l2:
            return "Impossible"
        if len(arr1) == 0:
            return arr2[k]
        if len(arr2) == 0:
            return arr1[k]

        mida1 = l1 // 2
        mida2 = l2 // 2
        if mida1 + mida2 < k:
            if arr1[mida1] > arr2[mida2]:
                return self.find_small_k(arr1, arr2[mida2:], k - mida2 - 1)
            else:
                return self.find_small_k(arr1[mida1+1:], arr2, k - mida1 - 1)
        else:
            if arr1[mida1] > arr2[mida2]:
                return self.find_small_k(arr1[:mida1], arr2, k)
            else:
                return self.find_small_k(arr1, arr2[:mida2], k)


if __name__ == '__main__':
    k_small = KthSmall2SortedArr()
    arr1 = [i for i in range(0, 10, 2)]
    arr2 = [i+1 for i in range(0, 10, 2)]

    k = 3
    print(k_small.find_small_k(sorted(arr1), sorted(arr2), k))

