from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"Mensagem" : "Acessando rota de autenticação" , "Autenticado" : False}


@auth_router.post("/criar_conta")
async def criar_conta(nome: str, email: str ,senha: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if usuario:
        return {"Mensagem" "Usuario já cadastrado!"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return("Mensagem" "Usuario cadastrado com sucesso!")