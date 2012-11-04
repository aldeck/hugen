#
# Copyright 2009, Alexandre Deckner, alex@zappotek.com
# Distributed under the terms of the MIT License.
#
import re, sys, os


def run(templateName, variables):
    outputFileName = 'generated/' + variables["app.folder"] + "/" + os.path.basename(templateName)

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
        os.makedirs(dir)
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


if len(sys.argv) == 3 and sys.argv[1] != "--help":
    templateFiles = []
    templateDir = 'templates/' + sys.argv[1]

    config = {}
    execfile('configs/' + sys.argv[2] + '.py', config)
    print config

    if os.path.isdir(templateDir):
        os.path.walk(templateDir, visit, templateFiles)
    runAll(templateFiles, config['variables'])
else:
    print "Usage: python hugen.py <template name> <config name>\n"
    print "Generates scaffolding for Haiku C++ applications."
