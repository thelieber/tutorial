import datetime

class WriteFile(object):
    def __init__(self, filename, cformatter):
        self.fh = open(filename, 'a')
        self.formatter = cformatter()
    
    def write(self, fileline):
        self.fh.write(self.formatter.get_str(fileline))
    
    def close(self):
        self.fh.close()

class CSVFormatter(object):
    def __init__(self):
        self.delimeter = ','
        
    def get_str(self, my_list):
        textline = ''
        while my_list:
            element = my_list.pop(0)
            if ',' in element:
                textline += '\"{}\"'.format(element)
            else:
                textline += '{}'.format(element)
            if my_list:
                textline += '{}'.format(self.delimeter)
        return ("{}\n".format(textline))

class LogFormatter(object):
    
    def get_str(self, my_line):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return ( "{}    {}\n".format(dt_str, my_line) )
