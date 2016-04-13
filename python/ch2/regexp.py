import re

if __name__ == '__main__':
    src = open('hightemp.txt')
    ans = open('ans11.txt', 'w')
    for line in src:
        ans.write(re.sub(r'\t', ' ', line))
    ans.close()
    src.close()
