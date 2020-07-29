# github-twitter-commits

This is a simple program that uses reainbowstream (because Twitter API is a headhick to get into)

## tweet
A wrapper that gets input from stdin and tweets the input trow rainbowstream ( as i know right now, rainbowstream can't send multiline tweets).
Written in bash.

## tweettime
A little bash program that tweets the output of `date` every minute.

## test folder

a folder with python and github api tests

## gitupdate

a wrapper that: 
 - adds every staged modification, additions, etc
 - commits (by argument or default)
 - and pushes
all in one command

## githook

A man-in-the-middle program for git, that sends every command to git and if `git push` is called it sends a tweet with `tweet`.
