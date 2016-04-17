if __name__ == '__main__':
    src = open('hightemp.txt')
    lines = src.readlines()
    src.close()
    lst = []
    for line in lines:
        lst.append(line.split('\t'))

    lst.sort(key=lambda x:x[2], reverse=True)
    print(lst)


