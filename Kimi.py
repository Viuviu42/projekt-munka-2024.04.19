class Kimi:
    def __init__(self,date,bigp,placement,pont,kon,finish,circl,error) -> None:
        self.date = date
        self.bigp = bigp
        self.placement = placement
        self.pont = pont
        self.kon = kon
        self.finish = finish
        self.circl = circl
        self.error = error
        





file = open("kimi.csv", "tr", encoding="utf-8")
kimi = []

file.readline()

for row in file:
    row = row.strip().split(";")
    kimi.append(Kimi(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
