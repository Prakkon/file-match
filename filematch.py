import rapidfuzz
import re
#import levenstein
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/match")
def match_files(file1: str, file2: str):
    salutations_pattern = r"^(Dr\.|DR\.|Mr\.|MR\.|Ms\.|MS\.|Mrs\.|MRS\.|Miss|Prof\.)\s*"
    file1 = re.sub(salutations_pattern, "", file1) # remove salutations
    file2 = re.sub(salutations_pattern, "", file2)

    
    
 
    file1 = file1.lower()
    file2 = file2.lower()

    format = r"(\.(pdf|docx|doc|txt|xlsx|xls|pptx|ppt|note|csv|json))+?$"
    file1 = re.sub(format, "", file1, flags=re.IGNORECASE)
    file2 = re.sub(format, "", file2, flags=re.IGNORECASE)


    file1 = re.sub(r'[^a-zA-Z0-9]', '', file1)
    file2 = re.sub(r'[^a-zA-Z0-9]', '', file2) 

    # file format can be ignored
    

    similarity = rapidfuzz.fuzz.ratio(file1, file2)

    return {"file1": file1, "file2": file2, "similarity": similarity}


 #   date_pattern = r"(?:\d{6}|\d{8})"

    
 #   dates1 = re.findall(date_pattern, file1) 
 #   dates2 = re.findall(date_pattern, file2)
 #   date1 = datetime.strptime(str(dates1), '%YY%mm%dd').strftime('%dd/%mm/%YY')
 #   date2 = datetime.strptime(str(dates2), '%YY%mm%dd').strftime('%dd/%mm/%YY')

    
    
 #   if dates1 != nullDate:
 #       if date1 == date2 and similarity < 90.00:
 #          similarity += 10.00 
        
    
    

#regex to ignore -
# salutations "Dr., Mr., Ms., Mrs., Miss, Prof." at the start of a sentence
# dates - if the format is different, but it is the same date, then it can be ignored
# CASE SENSITIVITY - if the case is different, but the text is the same, then it can be ignored
# Do we ignore file types too?
# surname first names - if the order is different, but the names are the same, then it can be ignored [KumarSanu vs SanuKumar...]
# PrakharSharma vs PrakharSharma123 
# Pr4kh4rSh4rm4 vs PrakharSharma
# pradeep vs prabhdeep - 92% accuracy

