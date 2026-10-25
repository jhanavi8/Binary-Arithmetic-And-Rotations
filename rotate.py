def ROL(binary_str, positions):
    print(f"\n--- Rotate Left without Carry (ROL) by {positions} ---")
    print(f"Original: {binary_str}")
    current = binary_str
    
    for i in range(positions):
        msb = current[0]
        current = current[1:] + msb
        print(f"Step {i+1}: Shift left. MSB '{msb}' wraps to LSB -> {current}")
        
    print(f"Final 8-bit Result: {current}")

def RCL(binary_str, positions, initial_carry='0'):
    print(f"\n--- Rotate Left with Carry (RCL) by {positions} ---")
    print(f"Original: 8-bit={binary_str}, Carry={initial_carry}")
    current_bits = binary_str
    carry = initial_carry
    
    for i in range(positions):
        msb = current_bits[0]
        current_bits = current_bits[1:] + carry
        carry = msb
        print(f"Step {i+1}: Shift left. MSB '{msb}' -> Carry. Old Carry -> LSB. Result: 8-bit={current_bits}, Carry={carry}")
        
    print(f"Final 8-bit Result: {current_bits} (Carry Flag: {carry})")

original_binary = "10110110"
ROL(original_binary, 2)
RCL(original_binary, 2, initial_carry='0')