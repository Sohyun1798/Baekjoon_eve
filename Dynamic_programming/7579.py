def get_input():

    N, M = map(int, input().split())
   
    mem = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    return N, M, mem, cost

def dp_7579():

    N, M, mem, cost = get_input()

    table = []
    costList = [0]*(N+1)
    ans = 1000000
    print(table)

    for i in range(N+1):
        temp = []

        for j in range(N+1):

            if i == 0:
                if j == 0:
                    m_value = 0
                    c_value = 0
                else: 
                    m_value = mem[j-1]
                    c_value = cost[j-1]
            
            else:
                if i == j:
                    m_value = table[i-1][j]
                    #c_value = costList[j]
                else:
                    m_value = table[i-1][j] + mem[i-1]
                    c_value = costList[j] + cost[i-1]

            costList[j] = c_value
            temp.append(m_value)

            if m_value >= M:
                ans = min(ans, c_value)

        if min(temp) >= M:
            break

        else: table.append(temp)
                   
    return ans


print(dp_7579())