# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 30_pattern_inverted_star_triangle.py
# ============================================================

num=5
for row in range(num,0,-1):
    for col in range(1,row+1):
        print('*',end = ' ')
    print()
