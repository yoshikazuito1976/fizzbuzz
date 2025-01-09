def fizzbuzzwhile(end):
    x=1
    while x <= end:
        if x % 3 == 0 and x % 5 == 0:
             print("FizzBuzz")
        elif x % 3 ==0:
             print("Fizz")
        elif x % 5 == 0 :
             print("Buzz")
        else :
             print(x) 
        x += 1






def fizzbuzz(end):
    for i in range(1,end+1):
        match (i%3,i%5):
            case (0,0):
                print ('FizzBuzz')
            case (0,_):
                print('Fizz')
            case (_,0):
                print('Buzz')
            case (_,_):
                print(i)

if __name__ == "__main__":
    fizzbuzzwhile(30)