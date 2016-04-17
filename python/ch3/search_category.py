import re

if __name__ == '__main__':
    src = open('British.txt')
    for line in src:
        if re.match(r".*(C|c)ategory.*", line):
            print(line)
