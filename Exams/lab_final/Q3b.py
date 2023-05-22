def half_adder_output(a, b):
    
    sum = a ^ b
    carry = a & b
    
    print(f"Sum of the two input is {sum}")
    print(f"Carry of the two input is {carry}")
    
 
a = int(input("Enter the 1st input for half-adder: ")) 
b = int(input("Enter the 2nd input for half-adder: ")) 

half_adder_output(a, b)