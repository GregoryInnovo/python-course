def run():
    # my_dic = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dic[i] = i**3


    # my_dic = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    my_dic = {i: i**(1/2) for i in range(1,1001) }
    print(my_dic)


if __name__ == '__main__':
    run()