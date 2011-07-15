/*
 * Copyright ##year##, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		##author##
 */
#ifndef ##app.header.guard##
#define ##app.header.guard##


#include <Application.h>


class BWindow;


class ##app.class## : public BApplication {

public:
								##app.class##();
								~##app.class##();

	virtual	void				AboutRequested();
	virtual void				MessageReceived(BMessage *message);

protected:
	BWindow*					fMainWindow;
};


#endif	// ##app.header.guard##
