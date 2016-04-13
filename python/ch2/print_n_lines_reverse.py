if __name__ == '__main__':
    n = int(input())
    f = open('hightemp.txt', 'r')
    lst = f.readlines()
    f.close()
    for i in range(n):
        print(lst[-n+i].rstrip())
