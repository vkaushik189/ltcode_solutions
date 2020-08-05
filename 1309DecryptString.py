def freqAlphabets(str = '10#11#12'):
    lookup = {}
    j = 0
    for i in range(1,10):
        c = str(i)
        lookup[c] = chr(97 + j)
        j += 1

    for i in range(10, 27):
        d = str(i) + '#'
        lookup[d] = chr(97 + j)
        j += 1
    print(lookup)


freqAlphabets()