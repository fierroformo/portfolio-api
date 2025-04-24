# Technical Review – Fintual Application

This repository contains a simple HTTP API for manage a stocks porfolio

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
