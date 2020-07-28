def anagramMappings(A = [12, 28, 46, 32, 50], B = [50, 12, 32, 46, 28]):

    mapping = []

    for num in A:
        if num in B:
            mapping.append(B.index(num))
    print(mapping)

anagramMappings()