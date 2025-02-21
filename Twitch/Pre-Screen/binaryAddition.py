def solution(a, b):
    # Pointers for each string, starting from the end
    i = len(a) - 1
    j = len(b) - 1
    
    carry = 0
    result_bits = []
    
    # Loop as long as there is a bit to process or a carry remains
    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        total = bit_a + bit_b + carry
        carry = total // 2  # Determine the new carry
        result_bits.append(str(total % 2))  # Current bit is total mod 2
        
        i -= 1
        j -= 1
    
    # Since we appended the bits from least significant to most,
    # reverse to get the correct order
    result = ''.join(reversed(result_bits))
    
    # Remove any leading zeros (but leave one zero if the sum is actually 0)
    result = result.lstrip('0') or '0'
    return result
