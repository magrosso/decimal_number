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


def main() -> None:
    orig_str: str = "123456.789"
    for shift in range(-len(orig_str), len(orig_str) + 1):
        new_str: str = shift_decimal_by_split(orig=orig_str, shift=shift)
        print(f"{orig_str} shifted {shift}: {new_str}")


def shift_decimal_by_split(orig: str, shift: int) -> str:
    orig_split: list[str] = orig.split(".")
    if len(orig_split) != 2:
        raise ValueError
    left, right = orig_split[0], orig_split[1]
    if shift < 0:
        dec_pos: int = len(left) + shift
        if dec_pos < 0:
            new_left = ""
            new_right = "0" * abs(dec_pos) + left + right
        else:
            new_left: str = left[: len(left) + shift]
            new_right: str = f"{left[len(left) + shift :]}{right}"
    elif shift > 0:
        new_left: str = f"{left}{right[:shift]}"
        new_right: str = f"{right[shift:]}"
    else:
        return orig

    return f"{new_left}.{new_right}"


if __name__ == "__main__":
    main()
