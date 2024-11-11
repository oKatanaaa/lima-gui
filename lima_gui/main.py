from fastapi import FastAPI
from contextlib import asynccontextmanager
from lima_gui.routers import main_router, chat_router
from lima_gui.models import init_state, init_chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_chat()
    init_state()
    print('init')
    yield
    return


app = FastAPI(lifespan=lifespan)


app.include_router(main_router)
app.include_router(chat_router)
