import os
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN
from fastapi.responses import JSONResponse, FileResponse
import json
from pydantic import BaseModel

class FileNameRequest(BaseModel):
    filename: str

app = FastAPI()

API_KEY_NAME = "Authorization"
USERS = {
    "user1": {"api_key": "user1_api_key"},
    "user2": {"api_key": "user2_api_key"},
}
UPLOAD_DIRECTORY = "./file/"

if not os.path.exists(UPLOAD_DIRECTORY):
    print("non existent directory, exiting...")
    exit()

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header in [user["api_key"] for user in USERS.values()]:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

@app.get("/")
async def ping():
    return {"message": "pong"}

@app.post("/filelist/")
async def get_file_list(api_key: APIKey = Depends(get_api_key)):
    files = os.listdir(UPLOAD_DIRECTORY)
    return JSONResponse(content=files)

@app.post("/sendfile/")
async def get_send_file(request: FileNameRequest, api_key: APIKey = Depends(get_api_key)):
    requested_filename = request.filename
    file_path = os.path.join(UPLOAD_DIRECTORY, requested_filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        with open(file_path, "r") as f:
            file_contents = json.load(f)
    except (IOError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Error reading the file")
    
    return JSONResponse(content=file_contents)

@app.get("/latestfile/")
async def get_latest_file(api_key: APIKey = Depends(get_api_key)):
    files = os.listdir(UPLOAD_DIRECTORY)
    if not files:
        raise HTTPException(status_code=404, detail="No files found")
    
    latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(UPLOAD_DIRECTORY, x)))
    latest_file_path = os.path.join(UPLOAD_DIRECTORY, latest_file)
    
    try:
        with open(latest_file_path, "r") as f:
            file_contents = json.load(f)
    except (IOError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="Error reading the latest file")
    
    return JSONResponse(content=file_contents)

# To run the server, use the following command:
# uvicorn filename:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
