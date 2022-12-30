def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    neg = 0
    if a<0:
        neg += 1
    if b<0:
        neg += 1
    if c<0:
        neg += 1
    
    return neg 

print(main(-5,-3,5))