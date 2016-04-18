import re

if __name__ == '__main__':
    src = open('British.txt')
    for line in src:
        if re.match(r".*(C|c)ategory.*", line):
            string = re.search(r".*:(.*?)[|\]].*", line)
            print(string.group(1))
