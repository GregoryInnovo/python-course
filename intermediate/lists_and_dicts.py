def run():
    my_list = [1, "Hello", True, 173.2]
    my_dict = {
        "firstname": "Greg",
        "lastname": "Mur",
    }

    super_list = [
        {"firstname": "Greg", "lastname": "Mur"},
        {"firstname": "Andres", "lastname": "Rodriguez"},
        {"firstname": "María", "lastname": "Lozano"},
        {"firstname": "Carlos", "lastname": "Peréz"},
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -7, 0, 10, 5],
        "floating_nums": [5.6, -9.6, 3.4],
    }

    for key, value in super_dic.items():
        print(key, '-', value)
    

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)




if __name__ == '__main__':
    run()