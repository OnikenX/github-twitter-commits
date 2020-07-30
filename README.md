# github-twitter-commits

This is a simple program that uses reainbowstream (because Twitter API is a headhick to get into)

## Instalation

There is the need to put the files in somewhere in the path, if possible, put them in ~/.local/bin and add it to your PATH.

The programs that are needed are:
- `githook`
- `gitupdate` (linked with the name `gitup`)
- if you don't have rainbowstream in the repository machine add the `tweet-client.py` as `tweet-client`

## Programs

### tweet
A wrapper that gets input from stdin and tweets the input trow rainbowstream ( as i know right now, rainbowstream can't send multiline tweets).
Written in bash.

### tweettime
A little bash program that tweets the output of `date` every minute.

### test folder

a folder with python and github api tests

### gitupdate

a wrapper that: 
 - adds every staged modification, additions, etc
 - commits (by argument or default)
 - and pushes

all in one command

### githook

A man-in-the-middle program for git, that sends every command to git and if `git push` is called it sends a tweet with `tweet`.

### Client/Server

Added a client/server for a the repos that are in machines that don't have rainbowstream, like my win7 32bit machine where pip doesn't want to install it in msys2 and choco can't install pip, for that I done this server client thingy so you can make this work if you have a linux box in a vm or server or even in the host like me.

#### tweet-server.py

The server waits the client to sent the message and tweets it with rainbowstream, it shows it's local ip to be easy to copy to the client.

#### tweet-client.py

The client is needs the server ip, if it is not the default it will ask for the ip and afeter connected will ask for the tweet to send.

## TODO

- A makefile to turn the installation easier