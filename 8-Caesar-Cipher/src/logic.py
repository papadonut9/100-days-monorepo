charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # Repeated the list twice to avoid outOfIndex error


# noinspection SpellCheckingInspection
def encrypt(data='', shift=0):
    """
    Encrypts the given text with provided rotation

    :param data: Accepts string data type. The data to be encrypted. Whitespaces and numbers not supported in Alpha versions
    :param shift: Accepts Integer data type. This parameter supplies the rotation factor.
    :return: output(string)
    """
    output = 'Encoded Text: '
    for char in data:
        pos = charList.index(char)
        newPos = pos + shift
        if newPos > 25:
            newPos -= 26
        output += charList[newPos]
    return output

# Test code
# print(f'z\n{encrypt("z", 1)}')
