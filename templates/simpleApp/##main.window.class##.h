/*
 * Copyright ##year##, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		##author##
 */
#ifndef ##main.window.header.guard##
#define ##main.window.header.guard##

#include <Window.h>

class ##main.view.class##;

class ##main.window.class## : public BWindow {
public:
								MainWindow(BRect frame, const char* title);
								~MainWindow();

	virtual	bool				QuitRequested();
	virtual	void				MessageReceived(BMessage *message);

protected:
			##main.view.class##*			f##main.view.class##;
};

#endif	// ##main.window.header.guard##
