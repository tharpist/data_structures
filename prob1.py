#INT
#

def recur_sum(n):
    if n == 0:
        return 0
    else:
        return n + recur_sum(n-1)

print(recur_sum(4))