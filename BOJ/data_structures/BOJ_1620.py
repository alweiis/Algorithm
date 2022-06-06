import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_arr = []
pokemon_dic = {}
for i in range(N):
    pokemon_name = input().rstrip()
    pokemon_arr.append(pokemon_name)
    pokemon_dic[pokemon_name] = i+1
for _ in range(M):
    chk = input().rstrip()
    if chk.isalpha():
        print(pokemon_dic[chk])
    else:
        print(pokemon_arr[int(chk) - 1])