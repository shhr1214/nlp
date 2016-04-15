import pprint

def make_file(n, file_name):
    f = open(file_name)
    lst = f.readlines()
    sub_lst = make_sub_lst(n, lst)
    ans = list((sub_lst))
    output_each_item(ans, file_name)

def make_sub_lst(n, lst):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def output_each_item(lst, file_name):
    for i in range(len(lst)):
        f = open(file_name + '-' + str(i), 'w')
        for line in lst[i]:
            f.write(line)
        f.close()

if __name__ == '__main__':
    n = int(input())
    file_name = 'hightemp.txt'
    make_file(n, file_name)
