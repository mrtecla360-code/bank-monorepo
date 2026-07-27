from fastapi import APIRouter

router = APIRouter()

# Base de datos simulada
accounts = {
    "1001": {"nombre": "Juan", "saldo": 5000},
    "1002": {"nombre": "María", "saldo": 3000},
}

@router.post("/transfer")
def transferir(origen: str, destino: str, monto: float):

    if origen not in accounts:
        return {"error": "La cuenta origen no existe"}

    if destino not in accounts:
        return {"error": "La cuenta destino no existe"}

    if monto <= 0:
        return {"error": "El monto debe ser mayor que cero"}

    if accounts[origen]["saldo"] < monto:
        return {"error": "Saldo insuficiente"}

    accounts[origen]["saldo"] -= monto
    accounts[destino]["saldo"] += monto

    return {
        "mensaje": "Transferencia realizada correctamente",
        "origen": accounts[origen],
        "destino": accounts[destino]
    }