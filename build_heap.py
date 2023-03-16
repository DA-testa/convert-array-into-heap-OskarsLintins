# python3


def build_heap(data):
    swaps = []
    length = len(data)
    j = i
    for i in range(n//2-1,-1,1):
        while True:
            leftChild = 2*i + 1
            rightChild = 2*i + 2
            if rightChild <= n-1:
                j = rightChild
            elif leftChild <= n-1:
                j = leftChild
            if i != j:
                data[i,j] = data [j,i]
                swaps.append(i,j)
                i = j
            else:
                break
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    word = input()
    if 'I' in word:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in word:
        filename = input().strip()
        filepath = os.path.join(os.getcwd(),'test/' + filename)
        if filename.endswith("a"):
            return
        else:
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
