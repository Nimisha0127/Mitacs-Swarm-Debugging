import json
import os 
import subprocess
import webbrowser
import os.path
from os import path
import string    
import random  

S = 8    
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
alpha= str(ran)

#Load Json
with open('test1.json', encoding="utf8") as f:
 data = json.load(f)

#Check if text file exists
if path.exists("%s.txt"%alpha):
    print("File already exists, create new text file!")
    
#Else create new text file and write the PlantUML Descriptor
else:
    file = open("%s.txt"%alpha, "w+")
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
                    if j["Type"] in res and i["Type"] in res:
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
    
    #Execute plantuml.jar to generate diagram
    subprocess.run("java -jar plantuml.jar -tpng %s.txt"%alpha,shell=True)
    
    #Open the diagram in browser
    beta= "%s.png"%alpha
    if path.exists("%s.html"%alpha):
        print("File already exists, create new HTML file!")
    else:
        message = """<html>\n<center>\n<h1><b>Debugging Session</b></h1>\n<body>\n<img src="{URL}">\n</body>\n<center>\n</html>"""
        new_message = message.format(URL=beta)
        open("%s.html"%alpha,"w+").write(new_message)
        webbrowser.open('file:///' + os.path.realpath("%s.html"%alpha))
