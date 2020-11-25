#!/bin/bash

SCRIPT=$(readlink -f "$0")
PROGRAMDIR=$(dirname "$SCRIPT")

sudo apt install graphviz -y
pip3 install -q -r $PROGRAMDIR/requirements.txt

sudo ln -sf $PROGRAMDIR/main.py /usr/sbin/omci_analyser
sudo chmod 777 /usr/sbin/omci_analyser

