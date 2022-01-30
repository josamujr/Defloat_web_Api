from fastapi import FastAPI
import models
from main import engine, get_database
from routers import Content, USERS, authentication as auth, voting
from config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers =["*"],)


app.include_router(USERS.router)
app.include_router(Content.router)
app.include_router(auth.router)
app.include_router(voting.router)



