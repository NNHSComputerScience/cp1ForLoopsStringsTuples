Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> var = "computer"
>>> #      01234567
>>> len(var)
8
>>> var[0]
'c'
>>> var[7]
'r'
>>> var[-1]
'r'
>>> var[len(var)]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    var[len(var)]
IndexError: string index out of range
>>> var[8]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    var[8]
IndexError: string index out of range
>>> var[7]
'r'
>>> 