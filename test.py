# def solution(date):
#     days_in_month = {
#         1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
#     }
 
#     def valid_date(mm, dd):
#         return 1 <= mm <= 12 and 1 <= dd <= days_in_month[mm]
#     best_date = "xx-xx"
#     for m1 in range(10):
#         for m2 in range(10):
#             for d1 in range(10):
#                 for d2 in range(10):
#                     s = list(date)
#                     if s[0] == '?': s[0] = str(m1)
#                     if s[1] == '?': s[1] = str(m2)
#                     if s[3] == '?': s[3] = str(d1)
#                     if s[4] == '?': s[4] = str(d2)
 
#                     mm = int(s[0] + s[1])
#                     dd = int(s[3] + s[4])
 
#                     if valid_date(mm, dd):
#                         candidate = f"{mm:02d}-{dd:02d}"
#                         if best_date == "xx-xx" or candidate > best_date:
#                             best_date = candidate
#     return best_date


def solution(date: str) -> str:
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def is_match(target: str, pattern: str) -> bool:
        for i in range(5): 
            if pattern[i] != '?' and pattern[i] != target[i]:
                return False
        return True

    for mm in range(12, 0, -1):
        max_day = days_in_month[mm]
        for dd in range(max_day, 0, -1):
            
            candidate_date = f"{mm:02d}-{dd:02d}"

            if is_match(candidate_date, date):
                return candidate_date

    return "xx-xx"

