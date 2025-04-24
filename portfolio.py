import random
from typing import List


class StockBuy(object):
    ticker: str
    price: float
    qty: int

    def __init__(self, ticker: str, price: float, qty: int) -> None:
        self.ticker = ticker
        self.price = price
        self.qty = qty

    def __str__(self) -> str:
        return f"Stock: {self.ticker} with price {self.get_price}"

    def get_price(self, _date: str) -> float:
        # _date unused because the price is random for example porpuses
        # Historical prices can be obtained with diferent services/libraries
        # https://www.linkedin.com/posts/jos%C3%A9-alejandro-betancourt-montellano-4477065b_fintech-stocks-python-activity-7306064418457464833-TAIy?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAy9rvcBIHJim4Zftl6-Yvhj5U2mNek4Ozs
        return self.price + (random.random() * self.price)


class Portfolio(object):
    stocks: List[StockBuy]
    current_value: float

    def __init__(self, stocks=[]) -> None:
        self.stocks = stocks

    def __str__(self) -> str:
        return f"Porfolio with {len(self.stocks)} stocks"

    def add_stock(self, stock: StockBuy) -> None:
        self.stocks.append(stock)

    def get_total_invested(self) -> float:
        return round(sum(stock.price * stock.qty for stock in self.stocks), 2)

    def get_profit(self, start_date: str, end_date: str) -> float:
        start_amount: float = self.get_total_invested()
        final_amount: float = sum(
            stock.get_price(end_date) * stock.qty for stock in self.stocks
        )
        self.current_value = round(final_amount, 2)
        return round(final_amount - start_amount, 2)

    def get_annualized_return(self, start_date: str, end_date: str) -> float:
        total_invested: float = self.get_total_invested()

        if total_invested:
            return round(
                self.get_profit(start_date, end_date) / self.get_total_invested() * 100,
                2
            )

        return 0.0
