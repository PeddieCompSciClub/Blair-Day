from pathlib import Path
file1 = open("athletics2.txt", "w")

events=Path('athletics1.txt').read_text().split("\n")

override=Path('athleticsOverride.txt').read_text().split("\n")

for i in range(0,len(events)-1):
    event = events[i].split("\\")

    for item in override:
        if item.split("\\")[0] == event[0]:
            for j in range(1,len(item.split("\\"))):
                if len(item.split("\\")[j]) > 0:
                    event[j-1] = item.split("\\")[j] 
    
    for k in range(len(event)):
        file1.write(event[k])
        if k+1 < len(event):
            file1.write("\\")
    file1.write("\n")


file1.close()



# athletics2.py
# overrides values in athletics1.txt with athleticsOverride.txt
# 
# athletics1.txt format:
# team - level\location\time\winner
# 
# athleticsOverride.txt format:
# team - level\teamOverride - levelOverride\locationOverride\timeOverride\winnerOverride
# 
# Blank values in athleticsOverride.txt will be ignored
# format ex: team - level\\locationOverride\\winnerOverride
# above format will only override the location and winner