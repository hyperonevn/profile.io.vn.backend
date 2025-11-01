from fastapi import FastAPI, Request
import json, os

app = FastAPI()

with open("data/users.json", "r", encoding="utf-8") as f:
    USERS = json.load(f)

@app.get("/{username}")
def get_user(username: str):
    user = USERS.get(username)
    if not user:
        return {"error": "User not found"}
    return user

# 👇 THÊM ĐOẠN NÀY Ở CUỐI FILE
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
