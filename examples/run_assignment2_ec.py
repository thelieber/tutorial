#!/usr/bin/env python

from tutorial import (WriteFile,
                      CSVFormatter,
                      LogFormatter,
                      )

wcsv = WriteFile('/tmp/wcsv.csv', CSVFormatter)
wlog = WriteFile('/tmp/wlog.log', LogFormatter)

wcsv.write(['a', 'b,2', 'c', 'd'])
wlog.write('this is a log message')
wcsv.write(['1', '2', '3', '4'])
wlog.write('this is another log message')

wcsv.close()
wlog.close()