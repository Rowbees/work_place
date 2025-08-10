def simple_budget_tracker(list_expenses):
    total_spent = sum(list_expenses)
    average_expense = total_spent / len(list_expenses)
    largest_expense = max(list_expenses)
    return total_spent, average_expense, largest_expense


my_expenses = [12.50, 35.00, 8.45, 27.80, 15.00]
results = simple_budget_tracker(my_expenses)

print(results)