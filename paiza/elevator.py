N = int(input())

floor = 1
count = 0 
for i in range(N):
    m_floor = int(input())
    count += abs(m_floor - floor)
    floor = m_floor

print(count)