/*
 * Copyright 2009, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		Alexandre Deckner <alex@zappotek.com>
 */

#include "##main.window.class##.h"

#include <Application.h>

#include <stdio.h>

#include "##main.view.class##.h"


##main.window.class##::##main.window.class##(BRect frame, const char* title)
	:
	BWindow(frame, title, B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, 0)
{
	f##main.view.class## = new ##main.view.class##(Bounds());
	AddChild(f##main.view.class##);
	Show();
}


##main.window.class##::~##main.window.class##()
{
}


bool
##main.window.class##::QuitRequested()
{
	be_app->PostMessage(B_QUIT_REQUESTED);
	return true;
}


void
##main.window.class##::MessageReceived(BMessage *message)
{
	switch (message->what) {
		default:
			BWindow::MessageReceived(message);
	}
}

