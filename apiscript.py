#! /usr/bin/env python3

# Script to automate Contrast API calls
#
# Command Line Arguments:
#
# -h, --help:		Help screen
# -v, --verbose:	Verbose output for trouble shooting

import argparse
import sys
import re
import base64
#import requests

APP_NAME 	= "API Runner"
APP_DESCRIPTION	= "Python script to automate API requests"
APP_VERSION 	= "0.1"
CONFIG		= ""
SCRIPT		= ""

args = {
"EMAIL"		: "",
"SERVICE_KEY"	: "",
"API_KEY"	: "",
"AUTH"	: "",
"URL"		: "",
"URL_SCHEME"	: "https://",
"URL_PORT"	: "443",
"URL_SERVER"	: "apptwo.contrastsecurity.com",
"URL_PATH"	: "contrast/api/ng",
"ORG_ID"	: "",
"APP_ID"	: "",
"ENDPOINT"	: ""
}

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def readCmd(self):
    self.name = "a"

  def readCfg(self):
    self.name = "b"

  def readYaml(self):
    self.name = "c"

parser = argparse.ArgumentParser(description = APP_DESCRIPTION)
parser.parse_args()

p1 = Person("John", 36)
p1.readCfg()

print(p1.name)
print(p1.age)

