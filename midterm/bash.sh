#!/bin/bash

tail -10 log.txt | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" >> target.txt
nmap -iL target.txt -sV