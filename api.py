from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autoknowmus price engine running"}

@app.get("/price")
def price(model:str, year:int, km:int, city:str):
    
    # Temporary test price
    estimated_price = 1500000

    return {
        "model": model,
        "year": year,
        "km": km,
        "city": city,
        "estimated_price": estimated_price
    }