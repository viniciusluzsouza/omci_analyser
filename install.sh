#!/bin/bash

SCRIPT=$(readlink -f "$0")
PROGRAMDIR=$(dirname "$SCRIPT")

echo -e "\n# Installing Graphviz ...\n"
sudo apt install graphviz -y

echo -e "\n# Installing PIP3 ...\n"
sudo apt install python3-pip -y

echo -e "\n# Installing python dependencies ...\n"
pip3 install -r $PROGRAMDIR/requirements.txt

echo -e "\n# Creating symbolic link ...\n"
sudo ln -sf $PROGRAMDIR/main.py /usr/sbin/omci_analyser
sudo chmod 777 /usr/sbin/omci_analyser

echo -e "Installation completed!"
