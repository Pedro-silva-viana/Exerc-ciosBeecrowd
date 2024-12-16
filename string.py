def get_unique_substrings(s):
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])
    return len(substrings)

entrada = input("")
lista = []

for char in entrada:
    if char != "?":
        lista.append(char)
    else:
        string_lista = ''.join(lista)
        print(get_unique_substrings(string_lista))
