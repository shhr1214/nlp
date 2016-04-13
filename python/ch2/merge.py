if __name__ == '__main__':
    col1 = open('col1.txt', 'r')
    col2 = open('col2.txt', 'r')
    lst1 = col1.readlines()
    lst2 = col2.readlines()
    col1.close()
    col2.close()

    merge = open('merge.txt', 'w')

    for i in range(len(lst1)):
        merge.write(lst1[i].rstrip() + '\t' + lst2[i])
    merge.close()
