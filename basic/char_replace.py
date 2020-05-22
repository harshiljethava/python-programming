def char_replace(val):
    char = val[0]
    val = val.replace(char,'$')
    val = char + val[1:]
    return val

print(char_replace('restart'))
