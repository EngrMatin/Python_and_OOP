def half_adder_output(a, b):
    
    sum = a ^ b
    carry = a & b
    
    list1 = []
    list1.append(sum)
    list1.append(carry)
    return list1
    
 
a = 1 
b = 0 

result = half_adder_output(a, b)

print(f"Sum of the two input is {result[0]}")
print(f"Carry of the two input is {result[1]}")