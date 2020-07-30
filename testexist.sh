#!/bin/bash
#OnikenX#
if which rainbowstream > /dev/null 2> /dev/null
then
    sendto='rainbowstream'
elif which tweet-client > /dev/null 2> /dev/null
then
    sendto='tweet-client'
else
	echo there is no way to send the tweet so for that yeet (or you can send it manually)
	exit 1
fi

echo $sendto