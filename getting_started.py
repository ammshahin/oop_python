class Person:
    def total_cost(self, a, b):
        return a * b


prsn = Person()
prsn.amount = 5000
prsn.count = 42

print(prsn.total_cost(prsn.count, prsn.amount))