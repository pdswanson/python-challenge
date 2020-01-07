# This is for PyBank
import os
import csv

budget_csv = os.path.join('budget_data.csv')

with open(budget_csv) as budget:
    reader = csv.reader(budget)
    next(reader)
    revenue = []
    date = []
    rev_chg = []
    for row in reader:
        revenue.append(int(row[1]))
        date.append(row[0])
    for x in range(1,len(revenue)):
        rev_chg.append(revenue[x] - revenue[x-1])
        avg_chg = sum(rev_chg) / len(rev_chg)
        max_chg = max(rev_chg)
        min_chg = min(rev_chg)
        max_mon = str(date[rev_chg.index(max(rev_chg))+1])
        min_mon = str(date[rev_chg.index(min(rev_chg))+1])

print("Financial Analysis")
print("----------------------------")
print("Total Months:", len(date))
print("Total: $", int(sum(revenue)))
print("Average Change: $", format(avg_chg, '.2f'))
print("Greatest Increase in Profits:", max_mon, "($", max_chg, ")")
print("Greatest Decrease in Profits:", min_mon, "($", min_chg, ")")

with open("PyBank.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print("Total Months:", len(date), file=f)
    print("Total: $", int(sum(revenue)), file=f)
    print("Average Change: $", format(avg_chg, '.2f'), file=f)
    print("Greatest Increase in Profits:", max_mon, "($", max_chg, ")", file=f)
    print("Greatest Decrease in Profits:", min_mon, "($", min_chg, ")", file=f)
