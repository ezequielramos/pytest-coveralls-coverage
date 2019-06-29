
def concat_string(value: str):
    if not isinstance(value, str):
        raise ValueError(f'value must be a string not a  {type(value).__name__}')

    return f'Hello {value}'