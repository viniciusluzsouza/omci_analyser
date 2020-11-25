#!/bin/bash

SCRIPT=$(readlink -f "$0")
PROGRAMDIR=$(dirname "$SCRIPT")

echo "# Installing Graphviz ..."
sudo apt install graphviz -y &>/dev/null

echo "# Installing python dependencies ..."
pip3 install -q -r $PROGRAMDIR/requirements.txt

echo "# Creating symbolic link ..."
sudo ln -sf $PROGRAMDIR/main.py /usr/sbin/omci_analyser
sudo chmod 777 /usr/sbin/omci_analyser

echo "Installation completed!"
