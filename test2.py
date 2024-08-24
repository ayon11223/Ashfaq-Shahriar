#palindrome checking

def isPalindrome(x: int) -> bool:
        j = list(str(x))
        if x > 9:
            for i in range(len(j) // 2):
                if j[i] != j[-i - 1]:
                    return False
            return True
        elif x in range(0, 10):
            return True
        else:
            return False

h = isPalindrome(1201)
print(h)

#leetcode_project_03 (8-24-2024)