#!/usr/bin/env python
from tutorial.mammals import Cat
from tutorial.mammals import Dog


x = Dog('Bo')
y = Cat('Quincy')

print(x.name)
print(y.name)

print(x.make_happy())
print(y.make_happy())
