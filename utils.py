from collections import OrderedDict


def conv_dict_to_odict(d, first_sort=sorted, second_sort=sorted):
    for value in d.values():
        sorted_value = OrderedDict(second_sort(value.items()))
        value = sorted_value

    # print(d)
    sorted_dict = first_sort(d.items())
    ordered = OrderedDict(sorted_dict)
    for k in ordered.keys():
        sorted_value = second_sort(ordered[k].items())
        ordered[k] = OrderedDict(sorted_value)

    return(ordered)
