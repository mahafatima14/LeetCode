def get_product_array(nums):
    
    n = len(nums)
    prefix, postfix = [1] * n, [1] * n 
    product_array = []
    
    #build the prefix array
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1] 
        

    #build the postfix array:
    for i in range(1, n):
        postfix[i] = postfix[i-1] * nums[::-1][i-1]

    
    #append the values in the list
    for i in range(n):
        product_array.append(prefix[i] * postfix[::-1][i])
    # return product_array
    print(prefix)
    print(postfix)


print(get_product_array([1,2,3,4]))
