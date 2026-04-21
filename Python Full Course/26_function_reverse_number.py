# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 26_function_reverse_number.py
# ============================================================

def Reverse(num,sum=0):
    while num>0:
        rem=num%10
        sum=sum*10 + rem
        num//=10
    return sum
num=123
print(Reverse(num))
