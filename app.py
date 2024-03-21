from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from business import Business

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

business = Business()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/services")
def get_services():
    return business.get_all_services()


@app.get("/services/{id}")
def get_service(id: str):
    # return business.get_service(id)
    pass


@app.get("/calendar/{date}/hours")
def get_calendar_hours(date: str):
    return business.get_avaliable_calendar_hours(date)


@app.get("/calendar/{date}/confirm/{hour}")
def confirm_calendar_hour(date: str, hour: str):
    return business.confirm_calendar_hour(date, hour)
