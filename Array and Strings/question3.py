def isPermutation(str1, str2):
    str1 = sort(list(str1))
    str2 = sort(list(str2))
    if str1 ==  str2:
        return True
    return False