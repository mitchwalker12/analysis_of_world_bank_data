def nth_power(n, power=2):
    '''
    calculates power for number up to n
    args:
        n: highest number in the list of numbers
        power: power for number to raise, default power is 2
    '''
    if power <= 10:
        return [i**power for i in range(n)]
    else:
        return print("You've exceeded the upper limit")

print(nth_power(10))
