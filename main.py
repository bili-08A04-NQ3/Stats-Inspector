import os
import json

from NQLogger import NQlog


def GetUUIDs(Path: str) -> list:
    Files = os.listdir(Path)
    FinalList: list = []
    for i in Files:
        FinalList.append(i[0:-5])
    return FinalList


def readJson(Path: str, Target: list) -> int:
    with open(Path) as f:
        File = json.load(f)

    return int(File[Target[0]][Target[1]][Target[2]])


def GetFromJson(target: list):
    AfterUUIDs = GetUUIDs("AfterStats")
    NQlog("检查所有玩家的" + str(target) + "差")
    NQlog("UUID" + " " * 49 + "| 差\n" + "—" * 70)
    for i in AfterUUIDs:
        Before: str = "BeforeStats\\" + i + ".json"
        After: str = "AfterStats\\" + i + ".json"
        if os.access(Before, os.F_OK):
            try:
                a = readJson(After, ["stats", target[0], target[1]])
                b = readJson(Before, ["stats", target[0], target[1]])
                if a == b:
                    pass
                else:
                    diff = a - b
                    NQlog("老玩家UUID: " + i + "的差:  | " + str(diff))
            except:
                pass
        else:
            try:
                a = readJson(After, ["stats", target[0], target[1]])
                NQlog("新玩家UUID: " + i + "的差:  | " + str(a))
            except:
                pass


def GetFromPlayer(UUID: str):
    Before: str = "BeforeStats\\" + UUID + ".json"
    After: str = "AfterStats\\" + UUID + ".json"
    with open(After) as f:
        File = json.load(f)
        Data = dict(File["stats"])
        FirstKeys = Data.keys()
        NQlog("key" + " " * 67 + "   |  difference\n" + "—" * 80)
        for FirstKey in FirstKeys:
            SecondKeys = dict(File["stats"][FirstKey]).keys()
            for SecondKey in SecondKeys:
                a = File["stats"][FirstKey][SecondKey]
                try:
                    b = readJson(Before, ["stats", FirstKey, SecondKey])
                    if a == b:
                        pass
                    else:
                        c = str(["stats", FirstKey, SecondKey])
                        Out = c + (72 - len(c)) * " " + " | "
                        Out += str(a - b)
                        NQlog(Out)
                except:
                    print(["stats", FirstKey, SecondKey], "   ", a)


print("Type Help For Help")
while True:
    Cmd = input(">>>")
    try:
        if Cmd == "Help":
            print("""从所有统计数据中检查某一个项目: checkFromAllStats
比较某一个人的所有统计数据: getFromPlayer""")
        elif Cmd == "checkFromAllStats":
            print("输入要比较的项目,例子:\nminecraft:mined,minecraft:obsidian")
            Key = input("请输入")
            Rd = Key.split(",")
            if len(Rd) != 2:
                input("你输入的数据不对,输入回车以退出程序")
                break
            GetFromJson(Rd)
        elif Cmd == "getFromPlayer":
            UUID = Key = input("请输入UUID")
            GetFromPlayer(UUID)
    except:
        print("你输入的数据不对")




