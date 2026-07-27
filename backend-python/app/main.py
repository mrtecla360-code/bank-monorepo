develop
@app.get("/api/balance/{account_number}")
def get_balance(account_number: str):
    db = read_db()
    acc = next((a for a in db["accounts"] if a["account_number"] == account_number), None)
    
    if not acc:
        raise HTTPException(status_code=400, detail="La cuenta no existe")
        
    return {
        "status": "success",
        "account_number": acc["account_number"],
        "holder": acc["holder"],
        "balance": acc["balance"]
    }
@app.get("/api/accounts")
def list_accounts():
    db = read_db()
    return {"status": "success", "accounts": db["accounts"]}

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
main
