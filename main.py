# Question : 1
def romanToInt(s):
    res = 0
    hashMap = {"I":1 , "V":5, "X":10 , "L":50, 'C':100, "D":500, "M":1000}
    for i in range(len(s)-1):
        if hashMap[s[i]] <  hashMap[s[i+1]]:
            res-= hashMap[s[i]]
        else:
            res += hashMap[s[i]]
    return res + hashMap[s[-1]]

print(romanToInt('MCMXCIV'))

# Question : 2

# Join Emplyee Table and Bonus Table on empId column then
# select columns "name" and "bonus" where bonus < 1000
