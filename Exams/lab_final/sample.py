def half_adder_output(a, b):
    
    sum = a ^ b
    carry = a & b
    
    print(f"Sum of the two input is {sum}")
    print(f"Carry of the two input is {carry}")
    
 
a = 1 
b = 0 

half_adder_output(a, b)