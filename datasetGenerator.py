import pyautogui as ui
import os
import time
from os import listdir
from os.path import isfile, join
from shutil import copyfile
from xml.etree import ElementTree as et

def takeScreenShot():
    var = 0
    print("Enter Champion Name:")
    inp = input()
    try:
        os.mkdir(inp)
    except:
        pass
    while True:
        ui.screenshot("images\\" + inp + '\\' + str(var) + '.png', region=(721, 279, 388, 440))
        print(var)
        var = var + 1
        time.sleep(.4)
def generateXML(inp):
    files = [f for f in listdir("images\\" + inp) if isfile(join("images\\"+inp, f))]
    print(files)
    for file in files:
        final = file.split('.')[0]
        string = str("<?xml version='1.0' encoding='UTF-8'?><annotation><folder>Aatrox</folder><filename>" + final + '.png' + "</filename><path>C:\\Users\\sagef\\Documents\\Development\\python\\tensorLeague\\images\\" + inp + '\\' + final + '.png' + "</path><source><database>Unknown</database></source><size><width>388</width><height>440</height><depth>3</depth></size><segmented>0</segmented><object><name>Aatrox</name><pose>Unspecified</pose><truncated>1</truncated><difficult>0</difficult><bndbox><xmin>1</xmin><ymin>1</ymin><xmax>388</xmax><ymax>440</ymax></bndbox></object></annotation>")
        print(string)
        filename = "images\\" + inp + '\\' + final +'.xml'
        f = open(filename, "w")
        f.write(string)
        f.close()
        print(file)

#takeScreenShot()
generateXML("Aatrox")
