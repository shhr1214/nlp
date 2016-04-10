def time_temperature(x, y, z):
    return "{0}時は{1}は{2}です".format(x, y, z)

if __name__ == '__main__':
    x = 12
    y = '気温'
    z = 22.4

    print(time_temperature(x,y,z))
