def first_repeated(string):
    if string != '':
        repeated_word = ''
        stings = string.replace(',', '').split(' ')
        for i in range(0, len(stings)):
            counter_word = 1
            for j in range(0,len(stings)):
                if stings[i] == stings[j]:
                    counter_word += 1
                if counter_word == 3:
                    repeated_word = stings[i]
                    return  repeated_word
        return 'No repeated words'
    else:
        raise Exception('no String provided')

# print(first_repeated("Once upon a time, there was a brave princess who..."))
