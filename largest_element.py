def find_largest_element(arr):

    largest = arr[0]
    
 
    for num in arr:
        if num > largest:
            largest = num
            
    return largest

try:
    n = int(input("Enter the number of elements in the array: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        arr = []
    
        print(f"Enter {n} integers:")
        for _ in range(n):
            num = int(input())
            arr.append(num)
        
   
        largest_element = find_largest_element(arr)
        print("The largest element in the array is:", largest_element)

except ValueError:
    print("Please enter valid integers.")
