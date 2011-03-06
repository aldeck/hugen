/*
 * Copyright ##year##, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		##author##
 */
#ifndef ##main.view.header.guard##
#define ##main.view.header.guard##

#include <View.h>

class ##main.view.class## : public BView {
public:
					##main.view.class##(BRect frame);
					~##main.view.class##();
	virtual void	Draw(BRect updateRect);
	virtual void	AttachedToWindow();
	virtual void	FrameResized(float width, float height);
};

#endif	// ##main.view.header.guard##
