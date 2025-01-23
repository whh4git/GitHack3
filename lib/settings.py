#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

from lib import __version__
DEBUG = False

VERSION = __version__

BANNER = """
  _____ _ _   _    _            _    ____  
 / ____(_) | | |  | |          | |  |___ \\ 
| |  __ _| |_| |__| | __ _  ___| | __ __) |
| | |_ | | __|  __  |/ _` |/ __| |/ /|__ < 
| |__| | | |_| |  | | (_| | (__|   < ___) |
 \\_____|_|\\__|_|  |_|\\__,_|\\___|_|\\_\\____/ {%s}
 A '.git' folder disclosure exploit with python3.
""" % (VERSION)

USAGE = """Usage:
  python GitHack.py http://www.target.com/.git/
"""

DEPENDS = """git was not found in $PATH"""
