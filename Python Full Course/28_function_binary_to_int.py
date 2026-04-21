# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 28_function_binary_to_int.py
# ============================================================

def sample(num,sum=0):
    power=1
    while num>0:
        rem=num%10
        sum+=rem*power
        power*=2
        num//=10
    return sum
num=1010
print(sample(num))
