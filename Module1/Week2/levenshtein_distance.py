def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        D[i][0] = i

    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            D[i][j] = min(D[i-1][j] + 1,
                          D[i][j-1] + 1,
                          D[i-1][j-1] + substitution_cost)

    return D[m][n]


print(f"Levenshtein distance between 'yu' and 'you' is: {
      levenshtein_distance('yu', 'you')}")
print(f"Levenshtein distance between 'hi' and 'hello' is: {
      levenshtein_distance('hi', 'hello')}")
print(f"Levenshtein distance between 'hola' and 'hello' is: {
      levenshtein_distance('hola', 'hello')}")
print(f"Levenshtein distance between 'kitten' and 'sitting' is: {
      levenshtein_distance('kitten', 'sitting')}")
print(f"Levenshtein distance between 'rosettacode' and 'raisethysword' is: {
      levenshtein_distance('rosettacode', 'raisethysword')}")
print(f"Levenshtein distance between 'flaw' and 'lawn' is: {
      levenshtein_distance('flaw', 'lawn')}")
