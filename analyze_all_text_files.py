

import os
import re
import pandas as pd

txt_dir = "txt"

rows = []

has_14 = []

for fname in os.listdir(txt_dir):

    if "txt" not in fname.lower(): continue

    obj ={
        "fname":fname
    }

    # print fname
    
    fpath = os.path.join(txt_dir, fname)

    txt = open(fpath).read()

    txt = re.sub(r"\s+"," ",txt).upper()

    towns = ["WOODBURY","BETHLEHEM"]

    if "REGION 14" in txt\
       or "REGIONAL SCH.*OOL DISTRICT 14" in txt\
       or "REGIONAL SCH.*OOL DISTRICT NO. 14" in  txt\
       or "REGIONAL SCH.*OOL DISTRICT # 14" in  txt\
       or "WOODBURY" in txt\
       or "BETHLEHEM" in txt:
        has_14.append(fname)
        print "has 14: " + fname

    obj["first150"] = txt.upper()[:150]

    terms = [
        r".*STUDENT.* V. ([A-Z0-9 ]*) BOARD[S]{0,1} OF EDUCATION.*",
        r".*STUDENT.* V. (REGION [0-9]+).*",
        r".*STUDENT.* V. (REGIONAL SCHOOL DISTRICT [0-9]+).*",
        r".*STUDENT.* V. (REGIONAL SCHOOL DISTRICT NO. [0-9]+).*",
        r".*STUDENT.* V. (REGIONAL SCHOOL DISTRICT # [0-9]+).*",
        r".*EDUCATION ([A-Z0-9 ]*) BOARD OF EDUCATION V. .*STUDENT\.*",
        r".*EDUCATION (REGION [0-9 ]*) V. .*STUDENT\.*",
        r".*EDUCATION (REGIONAL SCHOOL DISTRICT [0-9]+) V. STUDENT\.*",
        r".*EDUCATION (REGIONAL SCHOOL DISTRICT NO. [0-9]+) V. STUDENT\.*",           
        r".*EDUCATION (REGIONAL SCHOOL DISTRICT # [0-9]+) V. STUDENT\.*",
        r".*(REGIONAL SCH.*OOL DISTRICT [0-9]+)\.*",
        r".*(REGIONAL SCH.*OOL DISTRICT NO. [0-9]+)\.*",           
        r".*(REGIONAL SCH.*OOL DISTRICT # [0-9]+)\.*",
        
    ]                 

    match = None
    district = None

    for t in terms:
        match = re.match(
            t,
            txt
        )
        if match:
            district = match.group(1)
            break

    obj["match"] = district
    rows.append(obj)

df = pd.DataFrame(rows).sort_values(by="fname")
df .to_csv("report.csv")
