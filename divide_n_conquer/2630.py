def get_input():

    n = int(input())
    input_list = []

    for _ in range(n):
        input_list.append(list(map(int, input().split())))
    
    return n, input_list

def divide_conquer():
    pass