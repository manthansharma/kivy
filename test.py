from re import sub

triquote_pat = r"(?<!\\)'''"


def safe_comment(code, linenum):
    '''Takes any string representing code and returns a list of strings that
    when printed as one string per line will envelope the code as a single or
    multiline string.

    The resulting string also includes formatting indicating the source
    code line (linenum) from which the code originates. For example::

        >>> safe_comment('name = "55"', 7)
        ['\\'\\'\\'Line 7: name = "55" \\'\\'\\'']
        >>> safe_comment('val = 44', 7)
        ["\'''Line 7: val = 44 \'''"]
        >>> safe_comment('val = (1, 2,\\n3, 4)', 7)
        ["\'''Line 7: val = (1, 2,", "3, 4) \'''"]
        >>> safe_comment("val = (1, \'''fruits\\nand veggies\''')", 7)
        ["\'''Line 7: val = (1, \\\\\'''fruits", "and veggies\\\\\''') \'''"]
    '''

    lines = [l for l in code.splitlines()]
    print lines
    if not lines:
        return lines

    lines[0] = "'''Line {}: {}".format(linenum, lines[0])
    print lines
    lines[-1] += " '''"
    return lines

print safe_comment('name = "55"', 7)
# print safe_comment("val = (1, \'''fruits\\nand veggies\''')", 7)
