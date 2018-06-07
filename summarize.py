import pandas as pd
import re

df = pd.read_csv("report.csv")

# Remove ones that have "searchable alternative"
def original_doc(fname):
    if fname.startswith("searchable-"):
        return fname[len("searchable-"):]

df["original"] = df["fname"].apply(original_doc)
droppable = df["original"].unique()
df = df[df["fname"].apply(lambda x: x not in droppable)]

def year(original):
    if original is None: return 
    match = re.match("([0-9]){2}_.*", original)

    if match:
        return int("20" + str(match.group(1)))

df["year"] = df["original"].apply(year)
                
print ("Total rows: " + str((len(df))))
print ("Null matches: " + str((len(df[df["match"].isnull()]))))
print ("Non-null matches: " + str((len(df[df["match"].notnull()]))))

has_14 =  df[df["match"].apply(lambda x: "14" in str(x))][["fname","match"]]
print "Region 14: " + str(len(has_14))
print has_14
