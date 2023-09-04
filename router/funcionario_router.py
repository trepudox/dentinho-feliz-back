from fastapi import APIRouter

from model import Funcionario


router = APIRouter(tags=["funcionario"])


@router.get("/funcionario/{funcionario_id}", tags=["funcionario"])
def get_funcionario_by_id(funcionario_id: int):
    return {"id": funcionario_id, "nome": "trepudox"}


@router.post("/funcionario/", tags=["funcionario"])
def cria_funcionario(funcionario: Funcionario):
    # return service.salvar_funcionario(funcionario)
    return funcionario
