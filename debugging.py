import json
import os 
import subprocess
import webbrowser
import os.path
from os import path

with open('test1.json', encoding="utf8") as f:
 data = json.load(f)

if path.exists("demo36.txt"):
    print("File already exists, create new text file!")
else:
    file = open("demo36.txt", "w+")
    file.write("@startuml\n")
    file.write("skinparam componentstyle uml2\n")
    file.write("left to right direction\n")
    file.write("skinparam component{\n")
    file.write("  BackgroundColor Moccasin\n")
    file.write("}\n")
    res=[]
    for i in data["Events"]:
        if i["EventKind"] == "StepInto":
            if i["Type"] not in res:
                res.append(i["Type"])
                file.write("package ")
                file.write("\"")
                file.write("**")
                file.write(i["Namespace"])
                file.write("**")
                file.write("\"")
                file.write(" {\n")
                file.write(" component ")
                file.write("\"")
                file.write("**")
                file.write(i["Type"])
                file.write("**")
                file.write("\"")
                file.write(" as ")
                file.write(i["Type"])
                file.write(" <<component>>\n")
                file.write("}\n")
    res1=[]
    for k in data["Events"]:
        for i in data["PathNodes"]:
            for j in data["PathNodes"]:
                if k["Id"] == i["Event_Id"]:
                    if j["Parent_Id"] == i["Id"] and j["Origin"] == "StepInto" and j["Type"] != i["Type"]:
                        a=j["Type"] + " --u(0-- " + i["Type"]
                        if a not in res1:
                            res1.append(j["Type"] + " --u(0-- " + i["Type"])
                            file.write(j["Type"])
                            file.write(" --u(0-- ")
                            file.write(i["Type"])
                            file.write("\n")
    file.write("@enduml")
    file.close()

subprocess.run("java -jar plantuml.jar -tsvg demo36.txt",capture_output=True)
if path.exists("home6.html"):
    print("File already exists, create new HTML file!")
else:
    open("home6.html","w+").write('<!DOCTYPE html>\n<html>\n<body>\n<center>\n<h1><b>Debugging Session</b></h1><br>\n<img src="demo36.svg">\n<center>\n</html>')
    webbrowser.open('file:///' + os.path.realpath("home6.html"))
