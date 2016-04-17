from collections import Counter

if __name__ == '__main__':
    src = open('hightemp.txt')
    lst = []
    for line in src:
        lst.append(line.split('\t')[0])
    src.close()

    counter = Counter(lst)
    for word, cnt in counter.most_common():
        print(word, cnt)
