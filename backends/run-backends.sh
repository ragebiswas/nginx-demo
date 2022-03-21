#!/bin/sh
node --version > /dev/null 2>&1 || { echo 'node not found or not in PATH, aborting...' ; exit 1; }


node servers.js
