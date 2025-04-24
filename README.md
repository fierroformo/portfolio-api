# Technical Review – Portfolio API

This repository contains a simple HTTP API for manage a stocks portfolio

## 🛠️ Tech Stack
- Language: Python 3.9
- Frameworks: Flask

## 📦 Setup & Installation

### Clone the repository
git clone https://github.com/fierroformo/portfolio-api.git
cd portfolio-api

### Build the docker image
docker build -t porfolio-api .

### Run the docker container
docker run -p 5000:5000 porfolio-api

### Test the flask app
Open browser and visit [http://localhost:5000](http://localhost:5000)


## Endpoints

### Add stocks to my Portfolio

POST http://localhost:5000/api/portfolio

Content-Type: application/json

Request:
```
{
    "stocks": [
        {"ticker": "AMZ", "price": 167.12, "qty": 1},
        {"ticker": "AAPL", "price": 140.12, "qty": 2}
    ]
}
```
Response
```
{
    "success": true
}
 ```

### Get stocks from my Portfolio

GET http://localhost:5000/api/portfolio

Content-Type: application/json

Response
```
{
    "stocks": [
        {
            "price": 167.12,
            "qty": 1,
            "ticker": "AMZ"
        },
        {
            "price": 140.12,
            "qty": 2,
            "ticker": "AAPL"
        }
    ]
}
```

### Get earnings from my Portfolio

GET http://localhost:5000/api/portfolio/earnings?start_date={start_date}&end_date={end_date}

Content-Type: application/json

Response
```
{
    "current_value": 684.47,
    "profit": 237.11,
    "total_invested": 447.36
}
```

### Sample
![](https://github.com/fierroformo/portfolio-api/blob/main/api_sample.gif)
