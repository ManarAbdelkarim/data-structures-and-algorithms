
def array_shift(user_list, num):
    if  type(user_list)!= list or len(user_list)== 0 or type(num)!= int:
        return None
    x =[]
    y =[]
    for i in range(len(user_list)):
        if user_list[0] >= num :
            return [num] + user_list
        elif user_list[i-1] < num and user_list[i] >=num:
            x = user_list[:i:1]
            y = user_list[i::1]
            x += [num]
            break
        elif user_list[len(user_list)-1] <= num :
            return  user_list + [num] 


    return x + y
# print(array_shift([2,4,6,8],10))