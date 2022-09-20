import time

localtime = time.asctime(time.localtime(time.time()))
Path = "Logs\\Log-" + localtime
Rd = Path.split(":")
a = ""
for i in Rd:
    a += i
    a += "-"
a += ".txt"


def NQlog(thing: str):
    f = open(a, "a", encoding="utf-8")
    f.write(thing + "\n")
    print(thing)
    f.close()
