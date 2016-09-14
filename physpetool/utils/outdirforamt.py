import time


class timeformat:
    subdir = ''

    def __init__(self, sub):
        self.subdir = sub

    def __str__(self):
        timeformat = '%Y%m%d%H%M%S'
        timeinfo = str(time.strftime(timeformat))
        subdir = self.subdir + timeinfo
        return subdir






if __name__ == '__main__':
    doclu_subdir = timeformat('temp/hcp_alignment')
    print(doclu_subdir)
