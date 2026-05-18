from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.expense_routes import router as expense_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)


@app.get("/")
def home():
    return {"message":"Finance Tracker API Running"}