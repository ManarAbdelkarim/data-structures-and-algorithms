# Shift an Array
this is a program that takes a list and a number and return it a list that contain the number in an order way

## Challenge
take a list and a value and return a list with the value to be added. Without utilizing any of the built-in methods
 

## Approach & Efficiency
it uses O(n) because it is a liner order and we check every two  order list values 

## Solution

>   def array_shift(user_list, num):
>
>    if  type(user_list)!= list or len(user_list)== 0
>
>  or type(num)!= int:
>
>        return None
>    x =[]
>
>    y =[]
>
>    for i in range(len(user_list)):
>
>        if user_list[0] >= num :
>
>            return [num] + user_list
>
>
>        elif user_list[i-1] < num and user_list[i] >=num:
>
>            x = user_list[:i:1]
>
>            y = user_list[i::1]
>            x += [num]
>            break
>        elif user_list[len(user_list)-1] <= num :
>            return  user_list + [num] 
> 
> 
>    return x + y 
    