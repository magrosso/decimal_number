def shift_decimal_by(orig: str, dist: int) -> str:
    new_str: str = orig
    try:
        pos: int = new_str.index(".")
    except ValueError:
        pos = len(new_str)

    return move_decimal_to_pos(new_str=new_str, new_pos=pos + dist)


def move_decimal_to_pos(new_str: str, new_pos: int) -> str:
    new_str: str = new_str.replace(".", "")
    if new_pos < 0:
        new_str = new_str.zfill(len(new_str) + abs(new_pos))
        return f".{new_str}"
    elif new_pos < len(new_str):
        return f"{new_str[:new_pos]}.{new_str[new_pos:]}"
    else:
        zero_count: int = new_pos - len(new_str)
        if zero_count > 0:
            zeros: str = "0" * zero_count
            return f"{new_str[:new_pos]}{zeros}"
        else:
            return new_str[:new_pos]
