from pydantic import BaseModel, EmailStr
from datetime import date


class Funcionario(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    sexo: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    cep: str
    telefone: str
    celular: str
    email: EmailStr
    login: str
    senha: str


class Dentista(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    sexo: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    cep: str
    telefone: str
    celular: str
    email: EmailStr
    login: str
    senha: str
    cro: str


class Paciente(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    sexo: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    cep: str
    telefone: str
    celular: str
    email: EmailStr
    login: str
    senha: str
    convenio_medico: str
    convenio_odontologico: str


class Convenio(BaseModel):
    nome: str
    razao_social: str
    codigo: str
