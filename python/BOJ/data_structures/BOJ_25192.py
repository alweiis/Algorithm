n = int(input())
count = 0
records = set()
for _ in range(n):
    record = input()
    if record == 'ENTER':
        if records:
            count += len(records)
            records = set()
    else:
        records.add(record)
if records:
    count += len(records)
print(count)