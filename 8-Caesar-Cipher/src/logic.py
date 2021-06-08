charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # Repeated the list twice to avoid outOfIndex error


# noinspection SpellCheckingInspection
def caesar(mode='encrypt', data='', shift=0):
    """
    Encrypts the given text with provided rotation

    :param mode: Accpets string as input, mode is set to encrypt by default
    :param data: Accepts string data type. The data to be encrypted. Whitespaces and numbers not supported as of now.
    :param shift: Accepts Integer data type. This parameter supplies the rotation factor. Default value: 0
    :return: String
    """
    output = ''

    if shift > 26:
        shift = shift % 26

    if mode == 'decrypt':
        shift *= -1
    for char in data:
        if char in charList:
            pos = charList.index(char)
            newPos = pos + shift
            output += charList[newPos]
        else:
            output += char
    return output


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


def decrypt(data='', shift=0):
    """
    Decrypts the given text with provided rotation

    :param data: Accepts string data type. The data to be decrypted. Whitespaces and numbers not supported in Alpha versions
    :param shift: Accepts Integer data type. This parameter supplies the rotation factor.
    :return: output(string)
    """
    output = 'Decoded Text: '
    for char in data:
        pos = charList.index(char)
        newPos = pos - shift
        if newPos < 0:
            newPos += 25
        output += charList[newPos]
    return output
