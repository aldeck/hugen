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
