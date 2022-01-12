def sets():

    my_colors1 = {'⚫', '🟣', '🟠', '🔵'}
    my_colors2 = {'🔴', '🔵', '🟡', '🟢', '⚪', '🟤' }

    union_set = my_colors1 | my_colors2
    print("Union", union_set)

    intersection_set = my_colors1 & my_colors2
    print("Intersection", intersection_set)

    difference_set = my_colors1 - my_colors2
    print("Difference", difference_set)

    symmetric_difference_set = my_colors1 ^ my_colors2
    print("Symmetric Difference", symmetric_difference_set)


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates: # is same if we ask .includes in JS
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))



def run():
    # print('Running operations with sets')
    # sets()
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates_with_sets(random_list))


if __name__ == '__main__':
    run()