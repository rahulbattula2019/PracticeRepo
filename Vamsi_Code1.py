def solution(S):
    digits = list(map(int, S))
    changed = True
 
    while changed:
        changed = False
        i = 0
        while i < len(digits) - 1:
            s = digits[i] + digits[i + 1]
            if s <= 9:
                digits[i:i + 2] = [s] 
                changed = True
                i = max(i - 1, 0) 
            else:
                i += 1
 
    return ''.join(map(str, digits))

