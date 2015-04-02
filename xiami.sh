#!/bin/bash

startup()
{
	chromium-browser --app="http://www.xiami.com/radio" &
	wid=`xdotool search --sync --name 虾小米打碟`
	xdotool windowsize $wid 740 180
	xdotool windowactivate --sync $wid key Home Down Down Down Down mousemove --window $wid 20 80 click 1
	xdotool windowminimize $wid 
}

playctr()
{
	xdotool windowactivate --sync $1 key space windowminimize $1
}

next()
{
	xdotool windowactivate --sync $1 key Right windowminimize $1
}

wid=`xdotool search --name 虾小米打碟中` 

case "$1" in
	-n) if [ -n "$wid" ] ; then next $wid ; fi ;;
	*) if [ -n "$wid" ] ; then playctr $wid ;
	   else startup; fi ;;
esac

exit 0
