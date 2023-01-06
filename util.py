def nth_power(n, power):
    '''
    calculates power for number up to n
    '''
    if power < = 10:
        return [i**power for i in range(n)]
    else:
        return print("You've exceeded the upper limit")

print(nth_power(10, 4))
