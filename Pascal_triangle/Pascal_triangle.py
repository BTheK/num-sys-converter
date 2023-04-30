def pascal(current_list):
    new_list = [0] * (len(current_list) + 1)
    new_list[0] = new_list[-1] = 1
    for j in range(1, len(new_list) - 1):
        new_list[j] = current_list[j - 1] + current_list[j]
    return new_list


n = int(input())
li = [1]
for _ in range(n):
    li = pascal(li)
for i in range(len(li)):
    if i == len(li) - 1:
        print(1)
    elif i == len(li) - 2:
        print(li[i], 'x', sep='', end=' + ')
    elif i == 0:
        print('(x ^', (len(li) - i - 1), end=') + ')
    else:
        print(li[i], '(x ^ ', (len(li) - i - 1), sep='', end=') + ')
