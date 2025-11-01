from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    host = request.headers.get("host", "")
    sub = host.split(".")[0] if "." in host else None

    if sub and sub != "profile":
        return f"<h1>Trang hồ sơ: {sub}</h1><p>Đây là subdomain độc lập!</p>"
    return "<h1>Trang chính của profile.io.vn</h1>"
