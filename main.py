def move_decimal(orig: str, dist: int) -> str:
    new_str: str = orig
    try:
        pos: int = new_str.index(".")
    except ValueError:
        pos = len(orig)

    new_str: str = new_str.replace(".", "")
    new_pos = pos + dist

    if new_pos < 0:
        new_str = new_str.zfill(len(new_str) + abs(new_pos))
        return f".{new_str}"
    elif new_pos < len(new_str):
        return f"{new_str[:new_pos]}.{new_str[new_pos:]}"
    else:
        return new_str[:new_pos]
