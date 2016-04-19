import re

if __name__ == '__main__':
    src = open('British.txt')
    for line in src:
        if re.match(r"^\=+.*?\=+$", line):
            string = re.search(r"^(\=+)(.*?)(\=+$)", line)
            deps = len(string.group(1)) - 1
            print(string.group(0) + 'の階層は' + str(deps))
