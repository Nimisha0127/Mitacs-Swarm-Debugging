import json
import os 
import subprocess
import webbrowser, os

with open('test1.json', encoding="utf8") as f:
 data = json.load(f)
file = open("demo3.txt", "w")
file.write("@startuml\n")
file.write("skinparam componentstyle uml2\n")
file.write("left to right direction\n")
file.write("skinparam component{\n")
file.write("  BackgroundColor Moccasin\n")
file.write("}\n")
res=[]
res1=[]
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
for i in data["Events"]:
    if i["callby"] != "null" and i["EventKind"] == "StepInto":
        file.write(i["Type"])
        file.write(" --u(0-- ")
        file.write(i["callby"])
        file.write("\n")
file.write("@enduml")
file.close()

file = open("demo3.txt", "r")
result = subprocess.run("java -jar plantuml.jar -tpng demo3.txt",capture_output=True)
open("home.html","w").write('<!DOCTYPE html>\n<html>\n<body>\n<center>\n<h1><b>Debugging Session</b></h1>\n<img src="demo3.png">\n</body>\n</html>')
webbrowser.open('file:///' + os.path.realpath("home.html"))
