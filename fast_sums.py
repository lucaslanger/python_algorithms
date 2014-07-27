def unique_x_y_sum(d, s):

    for i in d:
        if ((s - i) in d) and (2*i != s):
            return True

    return False

def load_dict():
    d = {}
    with open("a6data.txt","r") as f:
        for line in f:
            d[int(line)] = True

    return d



def count_unique(d):
    unique = 0 
    for i in range(-10000, 10001):
        if i % 10 == 0:
            print i
        b = unique_x_y_sum(d,i)
        if b:
            unique += 1

    return unique

d = load_dict()
print count_unique(d)

