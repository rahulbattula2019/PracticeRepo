def solution(S, T):
    N = len(S)
    M = len(T)

    if S == T:
        return "EQUAL"

    if M == N + 1:
        diff_idx = -1
        for i in range(N):
            if S[i] != T[i]:
                diff_idx = i
                break
        
        if diff_idx == -1:
            return f"ADD {T[-1]}"
        else:
            if S[diff_idx:] == T[diff_idx+1:]:
                return f"ADD {T[diff_idx]}"

    if M == N - 1:
        diff_idx = -1
        for i in range(M):
            if S[i] != T[i]:
                diff_idx = i
                break

        if diff_idx == -1:
            return f"DELETE {S[-1]}"
        else:
            if T[diff_idx:] == S[diff_idx+1:]:
                return f"DELETE {S[diff_idx]}"

    if M == N:
        diff_indices = [i for i in range(N) if S[i] != T[i]]
        
        if len(diff_indices) == 1:
            idx = diff_indices[0]
            char_s = S[idx]
            char_t = T[idx]
            return f"REPLACE {char_s} with {char_t}"

        if len(diff_indices) > 0:
            
            if sorted(S) == sorted(T):
                
                for i in range(N):
                    moved_char = S[i]
                    
                    S_prime = S[:i] + S[i+1:]
                    
                    for j in range(i + 1, M):
                        if T[j] == moved_char:
                            T_prime = T[:j] + T[j+1:]
                            
                            if S_prime == T_prime:
                                return f"MOVE {moved_char}"
                
    return "IMPOSSIBLE"