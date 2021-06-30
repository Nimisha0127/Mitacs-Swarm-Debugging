import json
import os 
import subprocess
import webbrowser
import os.path
from os import path
import string    
import random  
import unittest

S = 8    
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
alpha= str(ran)

#Load Json and create the PlantUML Descriptor
def create(jsonfile):
     
    with open(jsonfile, encoding='utf-8-sig') as f:
        data = json.load(f)
    if path.exists("%s.txt"%alpha):
        print("File already exists, create new text file!")
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
    return('Descriptor Created')
    

#Execute plantuml.jar to generate diagram
def generate():
    subprocess.run("java -jar plantuml.jar -tpng %s.txt"%alpha,shell=True)
    return('Diagram Generated')
 
   
#Open the diagram in browser
def display():
    beta= "%s.png"%alpha
    if path.exists("%s.html"%alpha):
        print("File already exists, create new HTML file!")
    else:
        message = """<html>\n<center>\n<h1><b>Debugging Session</b></h1>\n<body>\n<img src="{URL}">\n</body>\n<center>\n</html>"""
        new_message = message.format(URL=beta)
        open("%s.html"%alpha,"w+").write(new_message)
        webbrowser.open('file:///' + os.path.realpath("%s.html"%alpha))
    return('Diagram displayed in browser')


#Unit Tests
class TestUml(unittest.TestCase):
    #Unit Test 1
    def test_1(self):
        self.assertEqual(create('test3.json'),'Descriptor Created')
        
    #Unit Test 2    
    def test_2(self):
        self.assertEqual(generate(),'Diagram Generated')
        
    #Unit Test 3  
    def test_3(self):
        self.assertEqual(display(),'Diagram displayed in browser')
        
 
#Main
if __name__ == '__main__':
    unittest.main()
