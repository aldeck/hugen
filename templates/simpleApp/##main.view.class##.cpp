/*
 * Copyright ##year##, Haiku Inc. All rights reserved.
 * Distributed under the terms of the MIT License.
 *
 * Authors:
 * 		##author##
 */


#include "##main.view.class##.h"

#include <stdio.h>


##main.view.class##::##main.view.class##(BRect frame)
	:
	BView(frame, "##main.view.class##", B_FOLLOW_ALL, B_WILL_DRAW)
{
}


##main.view.class##::~##main.view.class##()
{
}


void
##main.view.class##::AttachedToWindow()
{
	BView::AttachedToWindow();
}


void
##main.view.class##::Draw(BRect updateRect)
{
	StrokeLine(BPoint(0,0), BPoint(100,100));
}


void
##main.view.class##::FrameResized(float width, float height)
{
}
