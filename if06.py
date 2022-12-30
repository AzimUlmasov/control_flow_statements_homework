def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    pos = 0
    ans =  ''
    if a>0:
        pos +=1
    if b>0:
        pos +=1
    if c>0:
        pos +=1
    
    if pos > 1:
        ans = "there are a lot of positive numbers"
    else:
        ans = "there are a lot of negative numbers"

    return ans

print(main(-5,3,-4))
    
    