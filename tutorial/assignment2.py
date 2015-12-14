import abc
import datetime

"""
Example using inheritance and abstract classes
"""

class WriteFile(object):
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, filename):
        self.filename = filename
        
    @abc.abstractmethod
    def write(self):
        return
        
    def write_line(self, textln):
        fh = open(self.filename, 'a')
        fh.write(textln)
        fh.close()

class Logfile(WriteFile):
    
    def write(self, textln):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line("{}    {}\n".format(dt_str, textln))

class Delimfile(WriteFile):
    
    def __init__(self, filename, delimeter):
        super(Delimfile, self).__init__(filename)
        self.delimeter = delimeter
        
    def write(self, alist):
        self.write_line("{}\n".format(self.delimeter.join(alist)))
    