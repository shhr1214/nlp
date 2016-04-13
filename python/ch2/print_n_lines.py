if __name__ == '__main__':
    n = int(input())
    f = open('hightemp.txt', 'r')
    for i in range(n):
        print(f.readline().rstrip())
    f.close()
