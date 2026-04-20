#palindromo

#algoritmos con strings






def isPalindromo(s):
    return s == s[::-1]

print(isPalindromo("racecar"))
print(isPalindromo("hello"))
print(isPalindromo("abba"))
print(isPalindromo("a"))

