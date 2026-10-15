import matplotlib.pyplot as plt
def plot_profit():
    months = []
    profits = []
    for i in range(1, 13):
        profit = float(input("Enter profit for month " + str(i) + ": "))
        months.append(i)
        profits.append(profit)
    plt.plot(months, profits, marker='o')
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.title("Company ABC - Monthly Profit")
    plt.grid(True)
    plt.show()
plot_profit()