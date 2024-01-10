def find_dtype(atuple, data_type):
    new_tuple = []
    valid_data_types = {'int', 'float', 'complex', 'bool', 'str', 'tuple'}

    if data_type not in valid_data_types:
        raise ValueError("Invalid data_type. Please provide one of: 'int', 'float', 'complex', 'bool', 'str', 'tuple")

    for x in atuple:
        if data_type == 'tuple' and isinstance(x, tuple):
            new_tuple.append(x)
        elif type(x).__name__ == data_type:
            new_tuple.append(x)

    return tuple(new_tuple)