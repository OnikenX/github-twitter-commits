#!/bin/bash
CONT=0
for a in $@
do
	git $@
	erro=$?
	if [[ $erro != 0 ]] 
	then
		echo erro $erro ocorreu
		break
	fi
	if [[ $a == "push" ]]
	then
		git remote get-url origin | replace 'https://github.com/' '' | replace '.git' '' # getting the repo name
		echo $(git remote get-url origin | replace '.git' ''| replace 'github.com' 'api.github.com')/commits
	fi
	break;
done
