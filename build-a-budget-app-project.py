import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        TITLE_LENGTH = 30
        width = TITLE_LENGTH - len(self.name)
        asterisk_length = int((width) / 2)
        title = f"{'*' * asterisk_length}{self.name}{'*' * asterisk_length}"
        items = []
        for item in self.ledger:
            amount = 0
            description = ""
            for key, value in item.items():
                if key == "amount":
                    amount = float(value)
                if key == "description":
                    description = value[:23]
            items.append(f"{description:<{23}}{amount:>{7}.2f}")
        items_output = "\n".join(items)
        total = self.get_balance()
        return f"{title}\n{items_output}\nTotal: {total}"

    def get_balance(
        self,
    ):
        balance = sum(
            [
                value
                for item in self.ledger
                for key, value in item.items()
                if key == "amount"
            ]
        )
        return balance

    def check_funds(self, amount):
        current_balance = self.get_balance()
        return amount <= current_balance

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        # current_balance = self.get_balance()
        if self.check_funds(amount):
            self.ledger.append({"amount": float(-amount), "description": description})
            return True
        return False

    def transfer(self, amount, destination):
        if self.withdraw(amount, f"Transfer to {destination.name}"):
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


def create_spend_chart(categories):
    title = "Percentage spent by category"
    percentages = [index for index in range(100, -1, -10)]
    # print(percentages)
    category_spendings = []
    # category_percentages = []
    names = []
    for category in categories:
        withdrawals = [item["amount"] for item in category.ledger if item["amount"] < 0]
        # print(withdrawals)
        category_spendings.append(sum(withdrawals))
        names.append(category.name.title())
    total_spending = sum(category_spendings)
    # print(total_spending)
    category_percentages = [
        math.floor(((c / total_spending) * 100) / 10) * 10 for c in category_spendings
    ]
    # print(category_percentages)
    details = []
    for percentage in percentages:
        amount = ""
        for index, c in enumerate(category_percentages):
            if c < percentage:
                amount += " "
            else:
                amount += "o"
        detail = f"{percentage:>{3}}| {'  '.join(amount)}"
        details.append(f"{detail}  ")
    # print(details)
    details_output = "\n".join(details)
    width = len(details[-1])
    # print("width",width)
    line = ("---" * len(categories)) + "-"
    category_output = ""
    for i in range(len(max(names, key=len))):
        category_output += "\n    "
        names_string = ""
        for n in names:
            names_string += f" {n[i] if len(n) > i else ' ':<{2}}"
        category_output += f"{names_string} "

    output = f"{title}\n{details_output}\n{line:>{width}}{category_output}"
    # for line in output.split('\n'):
    #     print(len(line))
    return output


food = Category("food")
food.deposit(100000)
food.withdraw(10)
food.withdraw(10)

not_food = Category("nots")
not_food.deposit(100000)
not_food.withdraw(10)
not_food.withdraw(10)
not_food.withdraw(10)

idk = Category("idkdda")
idk.deposit(100000)
idk.withdraw(10)
idk.withdraw(10)
idk.withdraw(10)
idk.withdraw(10)
idk.withdraw(10)

print(create_spend_chart([food, not_food, idk]))
