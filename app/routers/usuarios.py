from fastapi import APIRouter

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
def listar_usuarios():
    return [{"id": 1, "nombre": "Mario"}, {"id": 2, "nombre": "Luisa"}]
