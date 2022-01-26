'''Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.

Sample Input:
23,34,55
Expected Output:
553423 '''

def create_largest_number(number_list):
    num=""
    number_list.sort(reverse=True)
    for no in number_list:
        num=num+str(no)
        largest_number=int(num)
    return largest_number

number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)

