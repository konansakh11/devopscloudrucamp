from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import socket
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def show_hostname():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR')
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>01-application</title>
    </head>
    <body>
        <p>{hostname}, {ip_addr}, {author}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
