if __name__ == '__main__':
    a = "11"
    b = "1"
    ret_val = 1
    sum_val = int(a) + int(b)
    bit1 = bin(int(a))
    bit2 = bin(int(b))
    sum_val = bytes()
    print(sum_val)

    for i in str(sum_val):
        if int(i) == 2:
            ret_val = ret_val * 10
        elif int(i == 0):
            ret_val = ret_val * 10
        else:
            ret_val = ret_val * 10 + 1

    print(ret_val)
