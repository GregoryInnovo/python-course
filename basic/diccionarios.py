def run():
    # is a structure of keys and values
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }

    print(my_dictionary)
    print(my_dictionary['key1'])
    print(my_dictionary['key2'])
    print(my_dictionary['key3'])

    countries_population = {
        'Argentina': 4491723,
        'Brazil': 274627340,
        'Colombia': 5002631,
    }

    print(countries_population['Argentina'])
    # print(countries_population['Chile'])

    # for country in countries_population.keys():
    #     print(country)

    # for country in countries_population.values():
    #     print(country)


    for country, population in countries_population.items():
        print(f'Hay una población de {population} en el país {country}')


if __name__ == '__main__':
    run()