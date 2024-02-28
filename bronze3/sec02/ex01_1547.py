import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

y_amount = 0
m_amount = 0
for time in a:
    y_amount += 10 + (time // 30) * 10
    m_amount += 15 + (time // 60) * 15

if y_amount < m_amount:
    print("Y", min(y_amount, m_amount))
elif m_amount < y_amount:
    print("M", min(y_amount, m_amount))
else:
    print("Y M", y_amount)