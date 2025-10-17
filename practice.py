import sys
sys.setrecursionlimit(200000) 
 
def solution(T):
    N = len(T)
    
    adj = [[] for _ in range(N)]
    
    for I in range(N):
        P = T[I]
        if P != I:
            adj[I].append(P)
            adj[P].append(I)
 
    def dfs(u, parent, has_ticket):
        
        max_extension_length = 0
 
        for v in adj[u]:
            if v != parent:
                v_is_odd = (v % 2 != 0)
                
                if not v_is_odd:
                    new_has_ticket = has_ticket
                    path_len_v = dfs(v, u, new_has_ticket)
                    max_extension_length = max(max_extension_length, path_len_v)
 
                else: 
                    if has_ticket:
                        new_has_ticket = False
                        path_len_v = dfs(v, u, new_has_ticket)
                        max_extension_length = max(max_extension_length, path_len_v)
                        
        return 1 + max_extension_length
 
    return dfs(0, -1, True)
 