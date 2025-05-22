from fastapi import APIRouter

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.get("/")
def listar_productos():
    return [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Mouse"}]
