# python3
import os;

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2-1,-1,-1):
        j = i
        while True:
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            if rightChild < n and data[rightChild] < data[j]:
                j = rightChild
            if leftChild < n and data[leftChild] < data[j]:
                j = leftChild
            if i != j:
                data[i], data[j] = data[j], data[i]
                swaps.append((i,j))
                i = j
            else:
                break
    return swaps

def main():
    
    word = input()

    if 'I' in word:
        n = int(input())
        data = list(map(int, input().split()))

    elif 'F' in word:
        filename = input().strip()
        filepath = os.path.join(os.getcwd(),'test/' + filename)
        with open(filepath, 'r') as fn:
            n = int(fn.readline())
            data = list(map(int, fn.readline().split()))

    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
