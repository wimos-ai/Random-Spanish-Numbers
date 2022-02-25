import json
import os

os.chdir(r'C:\Users\willm\Documents\Programming\Python\Python Projects\Spanish Project')
f = open("1-100.txt", encoding="UTF-8")
c = f.read()
c = c.split("\n")

for x in range(0, len(c)):
    c[x] = c[x].strip()

for x in range(0, len(c)):
    c[x] = c[x].split(" ", maxsplit=1)

for x in range(0, len(c)):
    c[x][0] = int(c[x][0])

n = dict()
for x in range(0, len(c)):
    n[c[x][0]] = c[x][1]

c: dict[int, str] = n

del n

c[100] = "cien"

for x in range(101, 200):
    c[x] = "ciento " + c[x - 100]

c[200] = "doscientos"

for x in range(201, 300):
    c[x] = "doscientos " + c[x - 200]

c[300] = "trescientos"

for x in range(301, 400):
    c[x] = "trescientos " + c[x - 300]

c[400] = "cuatrocientos"

for x in range(401, 500):
    c[x] = "cuatrocientos " + c[x - 400]

c[500] = "quinientos"
for x in range(501, 600):
    c[x] = "quinientos " + c[x - 500]

c[600] = "seiscientos"
for x in range(601, 700):
    c[x] = "seiscientos " + c[x - 600]

c[700] = "setecientos"
for x in range(701, 800):
    c[x] = "setecientos " + c[x - 700]

c[800] = "ochocientos"
for x in range(801, 900):
    c[x] = "ochocientos " + c[x - 800]

c[900] = "novecientos"
for x in range(901, 1000):
    c[x] = "novecientos " + c[x - 900]

c[1000] = "mil"
for x in range(1001, 2000):
    c[x] = "mil " + c[x - 1000]

c[0] = ""
for x in range(2001, 100000):
    hundreds = str(x)[-3] + str(x)[-2] + str(x)[-1]
    hundreds = int(hundreds)

    if len(str(x)) == 4:
        thousands = str(x)[0]
    if len(str(x)) == 5:
        thousands = str(x)[0] + str(x)[1]
    if len(str(x)) == 6:
        thousands = str(x)[0] + str(x)[1] + str(x)[2]
    thousands = int(thousands)
    c[x] = c[thousands] + " mill " + c[hundreds]

with  open("SpanishWords.json", 'w', encoding="utf-8") as f:
    txt = json.dumps(c, ensure_ascii=False)
    f.write(txt)


def get_c():
    return c


if __name__ == "__main__":
    print(get_c())
