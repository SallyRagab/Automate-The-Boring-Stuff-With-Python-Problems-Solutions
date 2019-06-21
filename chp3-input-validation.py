try:
    while collatz(int(input())) != 1:
        collatz(int(input()))
    
except:
    print('Please enter an integer.') 
    collatz(int(input()))
       
