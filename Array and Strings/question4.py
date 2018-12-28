def stringManipulation(list_of_chars):
    space_count = 0
    original_len = len(list_of_chars)
    for i in range(original_len):
        if string[i] = ' ':
            space_count += 1
    list_of_chars = list_of_chars + []*(2*space_count)
    for j in range(original_len, 0, -1):
        if list_of_chars[j] == ' ':
            list_of_chars[j+2*space_count] = '0'
            list_of_chars[j+2*space_count-1] = '2'
            list_of_chars[j+2*space_count-2] = '%'
        else:
            list_of_chars[j+2*space_count-1] = list_of_chars[j]



