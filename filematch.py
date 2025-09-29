import rapidfuzz
import re
#import levenstein
from fastapi import FastAPI
# from dateutil import parser

app = FastAPI()

@app.get("/match")
def match_files(file1: str, file2: str):
    salutations_pattern = r"^(Dr\.|DR\.|Mr\.|MR\.|Ms\.|MS\.|Mrs\.|MRS\.|Miss|Prof\.)\s*"
    file1 = re.sub(salutations_pattern, "", file1) # remove salutations
    file2 = re.sub(salutations_pattern, "", file2)
    date_pattern = r"^(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}$"
    dates1 = re.findall(date_pattern, file1) 
    dates2 = re.findall(date_pattern, file2)
    
    
    nullDate = []
 
    file1 = file1.lower()
    file2 = file2.lower()

   
    file1 = re.sub(r'[^a-zA-Z0-9]', '', file1)
    file2 = re.sub(r'[^a-zA-Z0-9]', '', file2) 



    similarity = rapidfuzz.fuzz.ratio(file1, file2)
    
    
    if dates1 != nullDate:
        if dates1 == dates2 and similarity < 90.00:
           similarity += 10.00        
    return {"file1": file1, "file2": file2, "dateifAny": dates1, "similarity": similarity}


#regex to ignore -
# salutations "Dr., Mr., Ms., Mrs., Miss, Prof." at the start of a sentence
# dates - if the format is different, but it is the same date, then it can be ignored
# CASE SENSITIVITY - if the case is different, but the text is the same, then it can be ignored
# Do we ignore file types too?
# surname first names - if the order is different, but the names are the same, then it can be ignored [KumarSanu vs SanuKumar...]
# PrakharSharma vs PrakharSharma123 
# Pr4kh4rSh4rm4 vs PrakharSharma
# pradeep vs prabhdeep - 92% accuracy

