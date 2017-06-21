import xml.etree.ElementTree as ET

def parse(filename):
    for event, elem in iterparse(filename, events=("start", "end")):
        if event == "start":
            print "Entering element %s" % elem.tag
        elif event == "end":
            print "Leaving element %s" % elem.tag

