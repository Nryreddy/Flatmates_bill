class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def f_info(n):
        flatmate_info = {}

        for i in range(n):
            name = input("Name of flatmate " + str(i + 1) + " is : ")
            days_in_house = int(input("No of days in the house: "))
            flatmate_info[name] = days_in_house

        for x, y in flatmate_info.items():
            print(f"Flatmate {x} stayed for {y} days")

        return flatmate_info

    def pays(bill,info):
        ni = 0
        for i in info.values():
            ni = ni + i
        for x, y in info.items():
            dd = y / ni
            individual_amt = round(bill.amount * dd, 2)
            info[x] = individual_amt
            print(f"{x} pays ", individual_amt)