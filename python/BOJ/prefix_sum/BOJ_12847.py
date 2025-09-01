n, m = map(int, input().split())
salary = list(map(int, input().split()))
salary_list = [sum(salary[:m])]
prefix_sum = salary_list[0]
for i in range(m, n):
    prefix_sum = prefix_sum + salary[i] - salary[i - m]
    salary_list.append(prefix_sum)
print(max(salary_list))