revenue: int = int(input("Введите сумму выручки :"))
costs: int = int(input("Введите сумму издержек:"))
profit: int = revenue-costs
print(f"Ваша прибыль: {profit}")
if profit > 0:
    profitability = profit/revenue
    employees: int = int(input("Введите численность сотрудников"))
    profit_empI: float = profit/employees
    print(f"Прибыль на одного сотрудника: {profit_empI}")





