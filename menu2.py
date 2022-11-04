from pathlib import Path
file1 = open("menu2.txt", "w")
dates=Path('menu.txt').read_text()
dates=str(dates)
dates=dates.replace("Lunch",'\nLunch')
dates=dates.replace("Dinner",'\nDinner')
file1.write(dates)
file1.close()

#debugging:
print(__file__)