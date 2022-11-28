if __name__ == '__main__':
    n = int(input()) 
    arr = map(int, input().split())   
    score = list(arr)

    def nota():
        sec=sorted(score)
        print(sec[2])

    nota()
