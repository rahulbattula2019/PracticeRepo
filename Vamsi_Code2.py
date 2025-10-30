def solution(S: str) -> str:
    stack = []

    for char in S:
        if stack:
            top_char = stack[-1]

            is_ab_pair = (top_char == 'A' and char == 'B') or (top_char == 'B' and char == 'A')
            is_cd_pair = (top_char == 'C' and char == 'D') or (top_char == 'D' and char == 'C')

            if is_ab_pair or is_cd_pair:
                stack.pop()
                continue

        stack.append(char)

    return "".join(stack)











# print(f'Input: "CBACD" -> Output: "{solution("CBACD")}" (Expected: "C")')
# print(f'Input: "CABABD" -> Output: "{solution("CABABD")}" (Expected: "")')
# print(f'Input: "ACBDACBD" -> Output: "{solution("ACBDACBD")}" (Expected: "ACBDACBD")')
# print(f'Input: "DCAB" -> Output: "{solution("DCAB")}" (Expected: "")')
# print(f'Input: "CDABCABDCD" -> Output: "{solution("CDABCABDCD")}" (Expected: "")')
# print(f'Input: "ADBC" -> Output: "{solution("ADBC")}" (Expected: "ADBC")')
