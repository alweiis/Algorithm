cash = int(input())
stocks = list(map(int, input().split()))
asset_jh = [cash, 0, 0]  # 현금, 주식, 자산
asset_sm = [cash, 0, 0]
tmp_list = []

# 준현의 주식 계산
for stock in stocks:
    if asset_jh[0] >= stock:
        asset_jh[1] += (asset_jh[0] // stock)
        asset_jh[0] %= stock

# 성민의 주식 계산
for i in range(1, len(stocks)):
    if stocks[i - 1] < stocks[i]:
        tmp_list.append('+')
    elif stocks[i - 1] > stocks[i]:
        tmp_list.append('-')
    elif stocks[i - 1] == stocks[i]:
        tmp_list.append('.')

for i in range(2, len(tmp_list)):
    if asset_sm[1] and tmp_list[i - 2] == tmp_list[i - 1] == tmp_list[i] == '+':
        asset_sm[0] = stocks[i + 1] * asset_sm[1]
        asset_sm[1] = 0

    if tmp_list[i - 2] == tmp_list[i - 1] == tmp_list[i] == '-':
        asset_sm[1] += (asset_sm[0] // stocks[i + 1])
        asset_sm[0] %= stocks[i + 1]

# 자산 계산
asset_jh[2] = asset_jh[0] + (stocks[-1] * asset_jh[1])
asset_sm[2] = asset_sm[0] + (stocks[-1] * asset_sm[1])

if asset_jh[2] > asset_sm[2]:
    print('BNP')
elif asset_jh[2] < asset_sm[2]:
    print('TIMING')
elif asset_jh[2] == asset_sm[2]:
    print('SAMESAME')