import abc
import datetime

class WriteFile(object):
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, filename):
        self.filename = filename
        
    def write(self, textln):
        fh = open(self.filename, 'a')
        fh.write(textln)
        fh.close()

class Logfile(WriteFile):
    
    def write(self, textln):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        super(Logfile, self).write("{}    {}\n".format(dt_str, textln))

class Delimfile(WriteFile):
    
    def __init__(self, filename, delimeter):
        super(Delimfile, self).__init__(filename)
        self.delimeter = delimeter
        
    def write(self, alist):
        super(Delimfile, self).write("{}\n".format(self.delimeter.join(alist)))
        
    

"""
dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
print dt_str

fh = open('test.txt','w')
fh.write('blah')
fh.close()

open('test.txt', 'r').read()

"""
