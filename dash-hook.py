from scapy.all import *
import json
import subprocess
import atsumori


# ローカルのjsonファイル展開、返り値は辞書型
def openJSON(file):
    with open(file, 'r') as f:
        return json.load(f)


def loadMaclist():
    settings = openJSON("_settings.json")  # setting.JSON open
    dash_mac = settings["dash_button"]["macaddress"]
    return dash_mac


def arp_display(pkt):
    print("start dash hook")
    macaddress = loadMaclist()
    if pkt[ARP].op == 1:
        for i in macaddress:
            if pkt[ARP].hwsrc == i:  # メモのMACアドレス
                print("Pushed Button" + str(i))
                atsumori.playAtsumori()


print(sniff(prn=arp_display, filter="arp", store=0))
