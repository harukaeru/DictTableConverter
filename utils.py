from collections import OrderedDict


def conv_dict_to_odict(d, first_sort=sorted, second_sort=sorted):
    sorted_dict = first_sort(d.items())
    ordered = OrderedDict(sorted_dict)
    for k in ordered.keys():
        sorted_value = second_sort(ordered[k].items())
        ordered[k] = OrderedDict(sorted_value)

    return(ordered)


def conv_list_to_2d_dict(list_data, get_column_value, get_header_value):
    dict_2d = dict()
    for l in list_data:
        column_value = get_column_value(l)
        header_value = get_header_value(l)
        if not dict_2d.get(column_value):
            dict_2d[column_value] = dict()
        if not dict_2d[column_value].get(header_value):
            dict_2d[column_value][header_value] = dict()
        dict_2d[column_value][header_value] = l
    return dict_2d
