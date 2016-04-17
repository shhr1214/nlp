import json
from pprint import pprint

if __name__ == '__main__':
    src = open('jawiki-country.json', 'r')
    data = []
    for line in src:
        data.append(json.loads(line))
    src.close()

    for datum in data:
        if datum['title'] == 'イギリス':
            f = open('British.txt', 'w')
            f.write(datum['text'])
