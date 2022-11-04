from pathlib import Path
file1 = open("score.txt", "w")
events=Path('athletics2.txt').read_text().split("\n")
oScore=Path('scoreOverride.txt').read_text().split("\\")

pScore=0
bScore=0

for event in events:
    event = event.split("\\")
    event = event[len(event)-1]
    if(len(event)>0):
        if(event[0]=="P"): pScore+=1
        if(event[0]=="B"): bScore+=1

if (len(oScore[0])>0): pScore = oScore[0]
if (len(oScore[1])>0): bScore = oScore[1]

file1.write(str(pScore) + "\\" + str(bScore))