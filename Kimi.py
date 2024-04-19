class Kimi:
    def __init__(self,date,bigp,placement,end,pont,kon,finish,circl,error) -> None:
        self.date = date
        self.bigp = bigp
        self.placement = placement
        self.end = end
        self.pont = pont
        self.kon = kon
        self.finish = finish
        self.circl = circl
        self.error = error

    def __str__(self) -> str:
        return self.finish
        





file = open("kimi.csv", "tr", encoding="utf-8")
kimi = []
count = 0
stat = {}

file.readline()

for row in file:
    row = row.strip().split(";")
    kimi.append(Kimi(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    count += 1

if count == len(kimi):
    print("3. feladat: ",len(kimi)) 

print("4. feladat: Magyar Nagydíj helyezései")
for i in kimi:
    if i.bigp == "Magyar Nagydíj":
        if i.placement != "":
            print(f"\t {i.date} : {i.placement}. hely")

for i in kimi:
    if i.finish == "N":
        if i.error in stat.keys():
            stat[i.error] += 1
        else:
            stat[i.error] = 1

 
print("5. feladat: Hibastatisztika")
for k,t in stat.items():
    if t > 1:
        print("\t", k, ":", t)

file.close()
print("8.feladat")

html = open("kimi.html","wt", encoding="utf-8")
html.write("doctype html")
html.write("<html>")
html.write("<head></head>")
html.write("<h1>Kimi Räikkönen</h1>")
html.write("<table>")
for i in kimi:
    html.write(f"<tr><td>{i.date}</td><td>{i.bigp}</td><td>{i.placement}</td></tr>")
html.write("</table>")
html.write("</body>")
html.write("</html>")
html.close()