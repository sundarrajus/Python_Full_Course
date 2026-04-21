# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 27_function_int_to_binary.py
# ============================================================

def Sample(num):
    rem=""
    while num >0:
        rem=str(num%2) +rem
        num//=2
    return rem
num=12
print(Sample(num))
