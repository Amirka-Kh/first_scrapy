def rm_space(value):
    value = value.strip()
    if value[0] == ' ':
        value = value[1:]
    elif value[-1] == ' ':
        value = value[:-2]
    return value


def take_2nd(value):
    value = value.strip().split(' ')
    return value[1]


def take_1st(value):
    value = value.strip().split(' ')
    return value[0]
