#! /usr/bin/python2.7
#
# Author: Eric Power
# Date: August 31, 2017

"""Main file for testing the .eplog filetype classes"""
import sys
from eplog import eplogData

def main():
    """Main entry point for the script."""
    data = eplogData('Test')

if __name__ == '__main__':
    sys.exit(main())
