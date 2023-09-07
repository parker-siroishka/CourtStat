from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.player import router as PlayerRouter

app = FastAPI()
origins = [
   "http://localhost:3000"
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

app.include_router(PlayerRouter, tags=["Player"], prefix="/player")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
