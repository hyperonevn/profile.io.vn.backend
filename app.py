from fastapi import FastAPI, Request
import json

app = FastAPI()

with open("data/users.json", "r", encoding="utf-8") as f:
    USERS = json.load(f)

@app.get("/")
async def get_user_by_subdomain(request: Request):
    host = request.headers.get("host", "")
    subdomain = host.split(".")[0] if "." in host else None

    if subdomain in USERS:
        return USERS[subdomain]
    else:
        return {"error": "User not found"}
