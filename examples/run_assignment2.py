#!/usr/bin/env python

from tutorial import (
        Logfile,
        Delimfile,
        )

log = Logfile('/tmp/log.txt')
c = Delimfile('/tmp/text.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])




"""
>cat log.txt
2015-02-01 12:33    this is a log message
2015-02-01 12:33    this is another log message

>cat text.csv
a,b,c,d
1,2,3,4
"""