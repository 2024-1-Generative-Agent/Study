from fastapi import FastAPI, File, UploadFile
import shutil
import json

app = FastAPI()





ABSOLUTE_PATH = "."

@app.post("./dalle/")
async def get_image_url():
    
    with open(f"{ABSOLUTE_PATH}/image2url.json","r") as reader:
        image2url = json.load(reader) #
    
    return image2url