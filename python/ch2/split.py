if __name__ == '__main__':
    src = open('hightemp.txt')
    col1 = open('col1.txt', 'w')
    col2 = open('col2.txt', 'w')
    for line in src:
        lst = line.split('\t')
        col1.write(lst[0] + '\n')
        col2.write(lst[1] + '\n')
    col1.close()
    col2.close()
    src.close()
