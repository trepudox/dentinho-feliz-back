import time
from fastapi import FastAPI, Request

from router.dentista_router import router as dentista_router
from router.funcionario_router import router as funcionario_router
from router.paciente_router import router as paciente_router


app = FastAPI()

app.include_router(dentista_router)
app.include_router(funcionario_router)
app.include_router(paciente_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = str(process_time)
    return response
