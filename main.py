from fastapi import FastAPI
import database
from routers import user_router

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(user_router.router)


@app.get("/")
async def root():
    return {"message": "Go to OpenAPI documentation --> localhost:8000/docs"}
