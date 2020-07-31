def toLowerCase(strg = 'HeLlo'):
    '''
    #add all capital and respective lower chars in below doctionary before submitting
    alp = {'H':'h', 'E':'e', 'L':'l', 'E':'e','O':'o'}

    new_str = []

    for ch in strg:
        if ch in alp.keys():
            new_str.append(alp[ch])
        else:
            new_str.append(ch)
    return ''.join(new_str)
    '''

    # ASCII values A-Z = 65 - 90, a-z = 97 - 122
    # to convert from char to num --> ord(char)
    # to convert from number to char --> chr(97)

    res = ''
    for char in strg:
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            res += chr(ord(char) + 32)
        else:
            res += char
    return res

ans = toLowerCase()
print(ans)

