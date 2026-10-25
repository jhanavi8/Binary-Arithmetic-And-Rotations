def to_8bit_2s_complement(n):
    if n < -128 or n > 127:
        raise ValueError("Number out of 8-bit signed range")
    return format(n & 0xFF, '08b')

def from_8bit_2s_complement(b_str):
    val = int(b_str, 2)
    if val & (1 << 7): # If sign bit is 1, it's negative
        val -= 256
    return val

def check_overflow(a, b, result):
    a_sign = a >> 7 & 1
    b_sign = b >> 7 & 1
    res_sign = result >> 7 & 1
    if (a_sign == b_sign) and (res_sign != a_sign):
        return True
    return False

def perform_operation(num1, num2_subtract):
    num2 = -num2_subtract
    
    bin1 = to_8bit_2s_complement(num1)
    bin2 = to_8bit_2s_complement(num2)
    
    int1 = int(bin1, 2)
    int2 = int(bin2, 2)
    
    result_int = (int1 + int2)
    result_8bit = result_int & 0xFF
    result_bin = format(result_8bit, '08b')
    final_decimal = from_8bit_2s_complement(result_bin)
    
    overflow = check_overflow(int1, int2, result_8bit)
    
    print(f"Operation: {num1} - ({num2_subtract})  =>  {num1} + ({num2})")
    print(f"Operand 1 (8-bit): {bin1}")
    print(f"Operand 2 (8-bit): {bin2}")
    print(f"Binary Result:     {result_bin}")
    print(f"Decimal Result:    {final_decimal}")
    print(f"Overflow:          {'Yes' if overflow else 'No'}")
    print("-" * 40)

print("Expression a) (45 - (+19))")
perform_operation(45, 19)

print("Expression b) ((-35) - (-12))")
perform_operation(-35, -12)