#longest subsequent string

def l_subs_string(s: str) -> int:
        j = list(s)
        exist = []
        counter = 0
        if len(j) == 1:
            return 1
        else:
            for i in range(len(j)):
                for k in j[i:]:
                    if k not in exist:
                        exist.append(k)
                    else:
                        if len(exist) > counter:
                            counter = len(exist)
                        exist.clear()
                        break
            return counter

m = l_subs_string("abbecabc")
print(m)

#leetcode_project_01 (8-24-2024)