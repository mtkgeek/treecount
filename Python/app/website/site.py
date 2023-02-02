
import os
import shutil
from urllib import response
from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from typing import List


from config import Settings, get_settings
from functions import count_trees

from . import web_config
from pathlib import Path

from os.path import dirname, abspath

router = APIRouter()


settings: Settings = get_settings()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data = {
        "page": "Home"
    }
    return web_config.templates.TemplateResponse("home.html", {"request": request, "data": data})


@router.post("/process", response_class=HTMLResponse)
async def process(request: Request, uploaded_files: List[UploadFile] = File(...)):
    # Parent Directory path
    
    parent_dir = dirname(dirname(abspath(__file__)))
    path = os.getcwd()

  
    # Path
    datapath = os.path.join(path, "data/challenge2_WUR_S4G/")
    outputpath = os.path.join(path, "output/")

    count_trees.setup_function_r()

    try:
        for file in uploaded_files:
            with open(f"{datapath}{file.filename}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        file.file.close()
    except Exception as e:
        print("An error occurred", e)
        return web_config.templates.TemplateResponse("error.html", {"request": request,})


    
    count_trees.main_function_r()
    # head, tail = os.path.split(path_name)
    all_filepaths = os.listdir(outputpath)
    print(all_filepaths)

    data = {
        "files": all_filepaths,
        

    }

    return web_config.templates.TemplateResponse("processing_results.html", {"request": request, "data": data})


@router.get("/download/{filename}", response_class=FileResponse)
async def process(request: Request, filename: str ):
    path = os.getcwd()  
    # Path
    outputpath = os.path.join(path, "output/")
    headers = {'Access-Control-Expose-Headers': 'Content-Disposition'}
    return FileResponse(f"{outputpath}{filename}", filename=filename, headers=headers)
