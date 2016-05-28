from physpetool.phylotree.log import getLogging

testlog = getLogging('wwww')
testlog.error("~~~~~~~~~~~~~~test1.")
testlog.info("~~~~~~~~~~~~~~test2." )
testlog.debug("~~~~~~~~~~~~~~~~~~~~~~~~~test3.")

