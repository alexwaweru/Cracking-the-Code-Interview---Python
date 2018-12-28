def isUniqieChars1(string):
    ''' Apprach 1 '''
    for i in range(0, len(string)):
        for j in range(len(string), 0, -1):
            if i!=j and string[i]==string[j]:
                return False
    return True


def isUniqueChars2(string):
    '''Approach 2 - This is a slight variation to the approach explained'''
    uniqueChars = []
    for i in range(0, len(string)):
        if string[i] not in uniqueChars:
            uniqueChars.append(string[i])
        else:
            return False
    return True


def isUniqueChars3(string):
    '''Approach 3 - Slight variation:- Instead of using 0 and 1, I used False and True'''
    if len(string) > 256:
        return False
    alphabet = [False]*256
    for i in range(0, len(string)):
        index = ord(string[i]) 
        if (alphabet[index]):
            return False
        else:
            alphabet[index] = True
    return True
