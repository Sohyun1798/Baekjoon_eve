def get_input():

    n = int(input())

    return n

def dp_1463():

    n = get_input()
    ans = [0 for _ in range(n+1)]

    for i in range(1,n+1):

        if i == 1:
            ans[i] = 0
        else:
            ans[i] = ans[i-1]+1

            if(i%2 == 0):
                m = int(i/2)
                temp = ans[m] + 1
                ans[i] = min(ans[i], temp)
            
            if(i%3 == 0):
                m = int(i/3)
                temp = ans[m] + 1
                ans[i] = min(ans[i], temp)

    return ans[n]

print(dp_1463())