from fastapi import APIRouter

from model import Dentista
from service import dentista_service


router = APIRouter(tags=["dentista"])


@router.get("/dentista/{dentista_id}", tags=["dentista"])
def get_dentista_by_id(dentista_id: int):
    return {"id": dentista_id, "nome": "trepudox"}


@router.post("/dentista/", tags=["dentista"])
def cria_dentista(dentista: Dentista):
    return dentista_service.salvar_dentista(dentista)
    # return dentista
