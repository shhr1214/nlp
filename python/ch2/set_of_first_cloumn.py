if __name__ == '__main__':
    src = open('hightemp.txt')
    lst = []
    for line in src:
        lst.append(line.split('\t')[0])

    print(set(lst))
