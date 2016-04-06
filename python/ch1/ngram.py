def n_gram(s, n):
    words = n_gram_words(s, n)
    chars = n_gram_chars(s, n)
    return (words, chars)

def n_gram_words(s, n):
    lists = s.split()
    words = []
    for i in range(len(lists)-n+1):
        n_words = []
        for j in range(n):
            n_words.append(lists[i+j])
        words.append(n_words)
    return words

def n_gram_chars(s, n):
    chars = []
    for i in range(len(s)-n+1):
        n_chars = []
        for j in range(n):
            n_chars.append(s[i+j])
        chars.append(n_chars)
    return chars

if __name__ == '__main__':
    s = 'I am an NLPer'
    n = 2
    words, chars = n_gram(s, n)
    print(words, chars)
