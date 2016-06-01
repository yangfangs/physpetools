import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='logfile.log',
                    filemode='w')

console = logging.StreamHandler()

console.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

console.setFormatter(formatter)

logging.getLogger('').addHandler(console)


def getLogging(name):
    return logging.getLogger(name)

