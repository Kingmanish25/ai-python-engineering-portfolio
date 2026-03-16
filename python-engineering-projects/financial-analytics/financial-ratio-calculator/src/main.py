import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_ratios(revenue, profit, assets, liabilities):

    if revenue == 0 or assets == 0:
        raise ValueError("Revenue and assets must be greater than zero")

    profit_margin = (profit / revenue) * 100
    debt_ratio = (liabilities / assets) * 100

    logging.info("Financial ratios calculated successfully")

    print("\nFinancial Ratios:\n")

    print(f"Profit Margin : {profit_margin:.2f}%")
    print(f"Debt Ratio    : {debt_ratio:.2f}%")


def main():

    parser = argparse.ArgumentParser(description="Financial Ratio Calculator")

    parser.add_argument("--revenue", type=float, required=True, help="Total revenue")
    parser.add_argument("--profit", type=float, required=True, help="Net profit")
    parser.add_argument("--assets", type=float, required=True, help="Total assets")
    parser.add_argument("--liabilities", type=float, required=True, help="Total liabilities")

    args = parser.parse_args()

    calculate_ratios(args.revenue, args.profit, args.assets, args.liabilities)


if __name__ == "__main__":
    main()
