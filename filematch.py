import rapidfuzz
import re
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/match")
def match_files(file1: str, file2: str):
    salutations_pattern = r"^(Dr\.|DR\.|Mr\.|MR\.|Ms\.|MS\.|Mrs\.|MRS\.|Miss|Prof\.)\s*"
    file1 = re.sub(salutations_pattern, "", file1)
    file2 = re.sub(salutations_pattern, "", file2)
    file1 = file1.lower()
    file2 = file2.lower()
    format = r"(\.(pdf|docx|doc|txt|xlsx|xls|pptx|ppt|note|csv|json))+?$"
    file1 = re.sub(format, "", file1, flags=re.IGNORECASE)
    file2 = re.sub(format, "", file2, flags=re.IGNORECASE)
    file1 = re.sub(r'[^a-zA-Z0-9]', '', file1)
    file2 = re.sub(r'[^a-zA-Z0-9]', '', file2) 
    similarity = rapidfuzz.fuzz.ratio(file1, file2)

    return {"file1": file1, "file2": file2, "similarity": similarity}
