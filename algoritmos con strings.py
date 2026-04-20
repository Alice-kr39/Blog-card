#algoritmos con strings

str1 = "abdgggda"
str2 = "abdggda"




def getRemovaleIndices(str1, str2):
    result = []
    for i in range(len(str1)):
        nueva = str1[:i] + str1[i + 1:]
        if nueva == str2:
            result.append(i)
    return result if result else [-1]


result_variables = getRemovaleIndices(str1,str2)
print(result_variables)
