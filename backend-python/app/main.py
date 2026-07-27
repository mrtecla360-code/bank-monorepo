class WithdrawRequest(BaseModel):
    account_number: str
    amount: float

@app.post("/api/withdraw")
def withdraw(req: WithdrawRequest):
    db = read_db()
    acc = next((a for a in db["accounts"] if a["account_number"] == req.account_number), None)

    if not acc:
        raise HTTPException(status_code=400, detail="La cuenta no existe")
    
    if acc["balance"] < req.amount:
        raise HTTPException(status_code=400, detail="Fondos insuficientes para el retiro")

    acc["balance"] -= req.amount
    db["transactions"].append({
        "type": "WITHDRAWAL",
        "account": req.account_number,
        "amount": req.amount
    })

    write_db(db)
    return {"status": "success", "message": "Retiro exitoso", "nuevo_saldo": acc["balance"]}