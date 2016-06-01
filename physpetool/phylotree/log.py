import logging
import os
def setlogdir(logdir):
    ldir = os.path.dirname(logdir)
    writelog = os.path.join(ldir, 'log.log')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=writelog,
                        filemode='w')

    console = logging.StreamHandler()

    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)


def getLogging(name):
    return logging.getLogger(name)
