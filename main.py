
def add_absolute(value: int):

    if not isinstance(value, int):
        raise ValueError(f'value must be an integer not a  {type(value).__name__}')

    if value < 0:
        value = value * -1

    return value + 1