# ============================================================
# TOPIC: Lambda & map() — Practice
# ============================================================

# Even or Odd using map
def f(n):
    if n % 2 == 0:
        return 'even'
    return 'odd'

print(list(map(f, range(1, 101))))


# Pattern using map + lambda with two iterables
n = 5
print('\n'.join(list(map(lambda st, sp: '* ' * st + ' ' * sp, range(1, n + 1), range(1, n + 1)))))


# Length of strings using map
l = ['1234', '567', ' ', '345']
print(tuple(map(len, l)))
