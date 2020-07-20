#program to remove vowels
def removeVowels(message):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'u']
    new_message = ''
    for char in message:
        if char not in vowels:
            new_message = new_message + char
    print(new_message)


removeVowels("I like to eat potato")