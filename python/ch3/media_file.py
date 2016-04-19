import re

if __name__ == '__main__':
    src = open('British.txt')
    for line in src:
        if re.match(r"^.*?\[\[(File|ファイル).*?\]\].*$", line):
            string = re.search(r"(^.*?(File|ファイル):)(.*?)(\|.*$)", line)
            print(string.group(3))
