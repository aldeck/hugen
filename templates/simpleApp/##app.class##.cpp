/*
 * Copyright ##year##, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		##author##
 */

#include "##app.class##.h"

#include <Alert.h>

#include "MainWindow.h"


##app.class##::##app.class##()
	:
	BApplication("##app.signature##")
{
	BRect frame(50, 50, 640 + 50, 480 + 50);
	const char *title = "##app.name##";
	fMainWindow = new MainWindow(frame, title);
}


##app.class##::~##app.class##()
{
}


void ##app.class##::AboutRequested()
{
	BAlert* alert;
	alert = new BAlert("About", "##app.name##", "ok");
	alert->Go(NULL);
}


void ##app.class##::MessageReceived(BMessage *message)
{
}


int
main(int argc, char** argv)
{
	##app.class## app;
	app.Run();
	return 0;
}
