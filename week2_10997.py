#n = int(input())

## 시도했던 풀이

# if n == 1:
#     print ('*')

# else: 
#     #row_num = 7 + 4 * (n-2)
#     print('*' * (5 + ((n-1)*4)))
#     print('*')
#     print('*' + ' ' + '*' * (3 + ((n-1)*4)))

#     for i in range(n-1): #n 개만큼의 줄이 생겨야 함 최소 range(1)부터 시작
#         print('* *' + ' '*(1 + ((n-1)*4)) + '*')

#     print('* ' * n + '*' + ' *' * n)
#     print('* ' * n + '*' + ' *' * n)


#     #for i in 

#     print('*' + ' '*(3 + ((n-1)*4)) + '*')
#     print('*' * (5 + ((n-1)*4)))


### 풀이 1 (재귀 미사용)

# print("*"*(4*n-3))
# for i in range(n-1):
#     print(("* "*(i+1)+" "*(4*n-4*i-5)+" *"*i).strip())
#     print("* "*(i+1)+"*"*(4*n-4*i-5)+" *"*i)
# if n != 1:
#     print("* "*(2*n-1))
#     print("* "*(2*n-1))
# for i in range(n-1):
#     print("* "*(n-1-i)+" "*(4*i+1)+" *"*(n-1-i))
#     print("* "*(n-2-i)+"*"*(4*i+5)+" *"*(n-2-i))


### 풀이 2 (재귀 사용)

def expand_space(star_output: list) -> list: 

    for x in range(len(star_output)):
        star_output[x].insert(0, " ")
        star_output[x].insert(0, "*")
        star_output[x].append(" ")
        star_output[x].append("*")
    
    star_output.insert(0, ["*"] + [" "] * (len(star_output[0]) - 1))
    star_output.insert(0, ["*"] * len(star_output[0]))
    star_output.append(["*"] + [" "] * (len(star_output[0]) - 2) + ["*"])
    star_output.append(["*"] * len(star_output[0]))
    return star_output


def print_star(x: int) -> list:

    if x == 1:
        return [["*"]]
    elif x == 2:
        return [
            ["*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " "],
            ["*", " ", "*", "*", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*"],
        ]

    prev_star_output: list = print_star(x - 1)
    prev_star_output = expand_space(prev_star_output)
    prev_star_output[2][-2] = "*"
    return prev_star_output


N = int(input())

star_list = print_star(N)

for line in map("".join, star_list):
    print(line.rstrip())
