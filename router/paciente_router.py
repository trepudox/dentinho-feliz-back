from fastapi import APIRouter

from model import Paciente


router = APIRouter(tags=["paciente"])


@router.get("/paciente/{paciente_id}", tags=["paciente"])
def get_paciente_by_id(paciente_id: int):
    return {"id": paciente_id, "nome": "trepudox"}


@router.post("/paciente/", tags=["paciente"])
def cria_paciente(paciente: Paciente):
    # return service.salvar_paciente(paciente)
    return paciente
