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