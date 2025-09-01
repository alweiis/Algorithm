phone = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6,
         "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10}
alphabet = input()
time = 0
for alpha in alphabet:
    for key, val in phone.items():
        if alpha in key:
            time += val
print(time)