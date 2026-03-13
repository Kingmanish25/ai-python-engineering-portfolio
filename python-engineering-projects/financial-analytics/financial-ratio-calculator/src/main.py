def calculate_ratios(revenue, profit, assets, liabilities):

    profit_margin = profit / revenue
    debt_ratio = liabilities / assets

    print("Profit Margin:", profit_margin)
    print("Debt Ratio:", debt_ratio)


calculate_ratios(100000, 20000, 50000, 20000)
