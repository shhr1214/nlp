def n_gram_chars(s, n):
    chars = []
    for i in range(len(s)-n+1):
        chars.append(s[i:i+2])
    return chars

if __name__ == '__main__':
    x = set(n_gram_chars("paraparaparadise", 2))
    y = set(n_gram_chars("paragraph", 2))

    union = x.union(y)
    intersection = x.intersection(y)
    difference = x.difference(y)

    print(x)
    print(y)

    print(union)
    print(intersection)
    print(difference)

    print('se' in x)
    print('se' in y)
