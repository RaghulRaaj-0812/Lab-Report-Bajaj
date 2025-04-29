from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from utils.image_processing import preprocess_image
from utils.ocr import extract_text_from_image
from utils.text_processing import parse_lab_data
import cv2
import numpy as np

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        processed = preprocess_image(image)
        text = extract_text_from_image(processed)
        results = parse_lab_data(text)
        
        return {"success": True, "data": results}
    except Exception as e:
        raise HTTPException(400, detail=str(e))