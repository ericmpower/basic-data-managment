#! /usr/bin/python2.7
#
# Author: Eric Power
# Date: August 31, 2017


class eplogData():
    """Data stored according to the .eplog filetype."""
    
    def __init__(self, dataSourceFile='null'):
        """Parses the .eplog data from a file, or creates an empty eplogData instance."""
        if dataSourceFile != 'null':
            print "eplogData.__init__() for non-empty file not implemented"
            # Implementation will be a Dictionary of dictionaries. Where the key is the dictionary name, and then there are keys and values as normal.
        else:
            self.data = {}
    
    def saveTo(self, outputFileName='null'):
        """Outputs the current eplogData.data to a save file."""
        print "eplogData.saveTo() not implemented"
    
    def addData(self, topLevelKey, lowLevelKey, newValue, updateData=True)
        """Adds the newValue to the [lowLevelKey] key of the [topLevelKey] dict. 
           If updateData=False and [lowLevelKey] already exists, don't overwrite the value."""
        print "addData() not implemented"
    
    def drawData(self, HorizontalBarGraph=True, verticalBarGraph=False, listData=False, scaleDownValues=False):
        """Draws the data in eplog.data in different ways defined by the optional arguments."""
        print "drawData() not implemented"
        
