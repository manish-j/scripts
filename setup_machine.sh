#!/bin/bash
shopt -s expand_aliases
alias update='sudo apt-get update '
alias install='sudo apt-get install -y '
alias pinstall='sudo pip install '
update
install youtube-dl
install python-pip
install python-dev
pinstall pip -U
pinstall youtube-dl -U
install nmap
install axel
install aria2
