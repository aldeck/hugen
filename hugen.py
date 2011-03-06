#
# Copyright 2009, Alexandre Deckner, alex@zappotek.com
# Distributed under the terms of the MIT License.
#
import re, sys, os


variables = {}
variables["app.name"] = "Microbe"
variables["year"] = "2011"
variables["author"] = "Alexandre Deckner <alex@zappotek.com>"
variables["app.class"] = "App"
variables["main.view.class"] = "MainView"
variables["main.window.class"] = "MainWindow"


variables["app.signature"] = "application/x-vnd.Haiku-" + variables["app.name"]
variables["app.folder"] = variables["app.name"].lower()

def makeHeaderGuard(classname):
	return "_" + classname.upper() + "_" + "H"

variables["app.header.guard"] = makeHeaderGuard(variables["app.class"])
variables["main.view.header.guard"] = makeHeaderGuard(variables["main.view.class"])
variables["main.window.header.guard"] = makeHeaderGuard(variables["main.window.class"])

variables["class.name"] = "Div"
variables["class.headerguard"] = makeHeaderGuard(variables["class.name"])

def run(templateName, variables):
    outputFileName = variables["app.folder"]  + "/" + os.path.basename(templateName)	
    
    file = open(templateName, 'r')
    text = file.read()

    for name, value in variables.items():
    	#print name, value
    	text = text.replace("##" + name + "##", value)
    	outputFileName = outputFileName.replace("##" + name + "##", value)

    file.close()
    
    outputFileName = outputFileName.replace("###", "") # clean ## when no variable in filename but just the template tag
    print "generate " + outputFileName + " (" + templateName + ")"
    dir = os.path.dirname(outputFileName)
    if not os.path.isdir(dir):
    	os.mkdir(dir)
    outFile = open(outputFileName, 'w')
    outFile.write(text);
    outFile.close()


def runAll(templateFileSet, variables):
    for template in templateFileSet:
    	run(template, variables)


def visit(result, dir, names):
    for name in names:
        path = os.path.join(dir, name)
        if os.path.isfile(path) and os.path.basename(path).find("##") != -1:
            print "file", path
            result.append(path)


#if len(sys.argv) >= 2 and sys.argv[1] != "--help":
#    run(sys.argv[1], options)
    
if len(sys.argv) == 2 and sys.argv[1] != "--help":
    templateFiles = []
    templateDir = sys.argv[1]
    if os.path.isdir(templateDir):
        os.path.walk(templateDir, visit, templateFiles)
    runAll(templateFiles, variables)
else:
    print "Usage: python checkstyle.py file.cpp [file2.cpp] [directory]\n"
    print "Checks c++ source files against the Haiku Coding Guidelines."
    print "Outputs an html report in the styleviolations.html file.\n"
