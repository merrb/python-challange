import os
import csv

#path to folder
path = "03-Python_02-Homework_Instructions_PyBank_Resources_budget_data.csv"

#variables
months = []
net_amount = []
changes = []
increase = []
decrease = []

#csvfile
with open(path) as csvfile:

    #csv reader specifies delimter and varible that holds data
    csvreader = csv.reader(csvfile)

    #header row first
    csvheader = next(csvreader)

    #python list
    data_list = [row for row in csvreader]

    #total number of months in the data set
    num_months = (len(data_list))

    #profits and losses over the entire period
    net = 0
    for _ in range(num_months):
        net = net + int(data_list[_][1])
        months.append(data_list[_])
        m_change = int(data_list[_][1]) - int(data_list[_-1][1])
        changes.append(m_change)

#an extra zero is not needed in making the list
changes.pop(0)

avg_change = round(sum(changes)/len(changes), 2)

increase = max(changes)
decrease = min(changes)

# for row in changes:
#     if row[1] == increase:
#         high = row
#     if row[1] == decrease:
#         low = row

# print(changes.index(max(changes)))

# print(net)
# print(num_months)
# print(changes)
# print(avg_change)
# print(max(changes))
# print(min(changes))
# print(data_list)

print(f'month: {num_months}')
print(f'amount: {net}')
print(f'change: {avg_change}')
print(f'increase: {increase}')
print(f'decrease: {decrease}')


 