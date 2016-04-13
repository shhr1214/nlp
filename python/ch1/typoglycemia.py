import random

def shuffle_chars(s):
    if len(s) <= 4:
        return s
    else:
        lst = list(s[1:-1])
        random.shuffle(lst)
        return s[0] + ''.join(lst) + s[-1]

def typoglycemia_str(lst):
    t_str = ''
    for s in lst:
        t_str += shuffle_chars(lst)

if __name__ == '__main__':
    lst = input().split()
    shuffled_chars_lst = map(shuffle_chars, lst)
    print(' '.join(list(shuffled_chars_lst)))
