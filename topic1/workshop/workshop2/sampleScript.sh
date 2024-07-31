#!/bin/bash

echo $USER
echo $HOME
echo $SHELL

echo $0 #Name of the script
echo $@ #All of the arguments

printf 'Hello %s\n' $1
