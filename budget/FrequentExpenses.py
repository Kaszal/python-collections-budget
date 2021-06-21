from . import Expense
import collections
import matplotlib.pyplot as plt

expanses = Expense.Expenses()
expanses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expanses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
#spending_counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
categories, count = zip(*top5)

fix, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()