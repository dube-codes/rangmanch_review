from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from reviews.routes import router as review_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database Table created")
    yield
    # shutdown: cleanup here
    print("Shuting down the app")


version = "v1"
app = FastAPI(
    title="Rangmanch Review API",
    description="API for rangmanch movie and theater reviews",
    version=version,
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {"message": "Welcome to Rangmanch Review API!"}


app.include_router(review_router, prefix=f"/api/{version}/review", tags=["Review"])
