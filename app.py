from typing import Dict
from flask import Flask, abort, request
from portfolio import Portfolio, StockBuy

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_400_BAD_REQUEST = 400

app = Flask(__name__)
portfolio = Portfolio()


@app.route('/')
def home():
    return "Welcome to portfolio API"


@app.route("/api/portfolio", methods=("POST",))
def add_stocks_portfolio():
    [
        portfolio.add_stock(StockBuy(**stock_data))
        for stock_data in request.get_json()["stocks"]
    ]
    return {"success": True}, HTTP_201_CREATED


@app.route("/api/portfolio", methods=("GET",))
def get_portfolio():
    response_data: Dict = {"stocks": []}
    [
        response_data["stocks"].append(stock.__dict__)
        for stock in portfolio.stocks
    ]
    return response_data, HTTP_200_OK


@app.route("/api/portfolio/earnings", methods=("GET",))
def get_portfolio_earnings():
    start_date: str = request.args.get("start_date")
    end_date: str = request.args.get("end_date")

    if not start_date or not end_date:
        abort(
            HTTP_400_BAD_REQUEST, description="start_date and end_date are required"
        )

    response_data: Dict = {
        "total_invested": portfolio.get_total_invested(),
        "profit": portfolio.get_profit(start_date, end_date),
        "current_value": portfolio.current_value
    }
    return response_data, HTTP_200_OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
