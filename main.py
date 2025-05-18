from fastapi import FastAPI
from contextlib import asynccontextmanager
import settings
import db
from controllers import router as api_router
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    print("DB initialized")

    for i in range(5):
        try:
            async with db.AsyncSessionLocal() as session:
                await session.execute(text("SELECT 1"))
            print("DB connection successful")
            break
        except OperationalError:
            print(f"DB not ready, retrying ({i+1}/5)...")
            await asyncio.sleep(2)
    else:
        print("DB connection failed after retries")
        raise RuntimeError("Database not reachable")

    yield

    print("Application shutting down")

app = FastAPI(debug=settings.DEBUG_MODE, lifespan=lifespan)

@app.get("/", tags=["Root Endpoint"])
async def root():
    return {"message": "Welcome to Magd's Task"}

app.include_router(api_router, prefix="/api")
