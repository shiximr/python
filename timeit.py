import time
from tqdm import tqdm

def myadd():
    result = 0
    for i in tqdm(range(10000000)):
        result += 1
    print(result)

if __name__ == '__main__':
    start = time.time()
    myadd()
    end = time.time()
    print(end - start)

import time
from tqdm import tqdm

def timeit(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)
def myadd():
    result = 0
    for i in tqdm(range(10000000)):
        result += 1
    print(result)

if __name__ == '__main__':

    timeit(myadd)




import time
from tqdm import tqdm

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timeit

@deco

def myadd():
    result = 0
    for i in tqdm(range(10000000)):
        result += 1
    print(result)

if __name__ == '__main__':
    #myadd() = deco(myadd)
    myadd()


[root@room9pc01 project07]# mkdir mydemo
[root@room9pc01 project07]# cd mydemo
hi = 'hello world'
>>> import mydemo.foo
>>> mydemo.foo.hi
'hello world'
>>> exit()

[root@room9pc01 project07]# vim mydemo/__init__.py
[root@room9pc01 project07]# cat mydemo/__init__.py
star = '*' * 30
>>> import mydemo
>>> mydemo.star
'******************************'
>>> mydemo.foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mydemo' has no attribute 'foo'
>>> from mydemo import foo
>>> foo.hi
'hello world'


>>> import hashlib
>>> m = hashlib.md5(b'123456')   #得到123456的md5对象，hashlib.md5(类型要是byte类型)
>>> m.hex()
>>> m.hexdigest()                #获取123456的md5值（16进制的数）
'e10adc3949ba59abbe56e057f20f883e'



>>> m = hashlib.md5()
>>> m.update(b'12')
>>> m.update(b'34')
>>> m.update(b'56')
>>> m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'


>>> with open('/tmp/passwd', 'rb') as fobj:
...     data = fobj.read()
...
>>> m = hashlib.md5(data)
>>> m.hexdigest()
'4efee2481b1327b5a909ecdf417ad332'

[root@room9pc01 project07]# md5sum /tmp/passwd
4efee2481b1327b5a909ecdf417ad332  /tmp/passwd



import sys
import hashlib
def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return  m.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))


>>> import sys
>>> sys.path
['', '/usr/local/lib/python36.zip', '/usr/local/lib/python3.6', '/usr/local/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']



>>> import os
>>> import tarfile
>>> tar = tarfile.open('/tmp/security.tar.gz', 'w:gz')
>>> tar.add('/etc/hosts')
>>> os.chdir('/etc')
>>> tar.add('security')
>>> tar.close()
[root@room9pc01 project07]# file /tmp/security.tar.gz
/tmp/security.tar.gz: gzip compressed data, was "security.tar",
last modified: Sat Jan 19 14:06:44 2019, max compression

>>> 
>>> os.mkdir('/tmp/demo')
>>> os.chdir('/tmp/demo')
>>> tar = tarfile.open('/tmp/security.tar.gz', 'r:gz')
>>> tar.extractall()
>>> tar.close()
>>> 

 = os.walk('/tmp/demo/security')
>>> a.__next__()
('/tmp/demo/security', ['namespace.d', 'console.apps', 'console.perms.d', 'limits.d'], ['pwquality.conf', 'console.handlers', 'console.perms', 'sepermit.conf', 'namespace.conf', 'time.conf', 'opasswd', 'namespace.init', 'limits.conf', 'pam_env.conf', 'group.conf', 'chroot.conf', 'access.conf'])
>>> a.__next__()
('/tmp/demo/security/namespace.d', [], [])
>>> a.__next__()
('/tmp/demo/security/console.apps', [], ['xserver', 'setup', 'liveinst', 'config-util'])
>>> a.__next__()
('/tmp/demo/security/console.perms.d', [], [])
>>> a.__next__()
('/tmp/demo/security/limits.d', [], ['20-nproc.conf'])
>>> a.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for path, folders, files in a:
...     for file in files:
...             os.path.join(path, file)
... 
>>> 
>>> for path, folders, files in os.walk('/tmp/demo/security'):
...     for file in files:
...             os.path.join(path, file)
... 
'/tmp/demo/security/pwquality.conf'
'/tmp/demo/security/console.handlers'
'/tmp/demo/security/console.perms'
'/tmp/demo/security/sepermit.conf'
'/tmp/demo/security/namespace.conf'
'/tmp/demo/security/time.conf'
'/tmp/demo/security/opasswd'
'/tmp/demo/security/namespace.init'
'/tmp/demo/security/limits.conf'
'/tmp/demo/security/pam_env.conf'
'/tmp/demo/security/group.conf'
'/tmp/demo/security/chroot.conf'
'/tmp/demo/security/access.conf'
'/tmp/demo/security/console.apps/xserver'
'/tmp/demo/security/console.apps/setup'
'/tmp/demo/security/console.apps/liveinst'
'/tmp/demo/security/console.apps/config-util'
'/tmp/demo/security/limits.d/20-nproc.conf'

class PigToy:
    def init(self, name, color):
        self.name = name
        self.color = color
        
    def show_me(self):
        print('Hi, my name is %s , I am %s' %(self.name, self.color))
        
        
piggy = PigToy()
piggy.init('Piggy', 'pink')

piggy.show_me()

george = PigToy()
george.init('George', 'red')
george.show_me()


class Vender:
    def __init__(self,company, phone):
        self.company = company
        self.phone = phone

    def call(self):
        print('Calling %s ......' % self.phone)
class PigToy:
    def __init__(self, name, color, company, phone):
        self.name = name
        self.color = color
        self.vender = Vender(company, phone)

    def show_me(self):
        print('Hi, my name is %s , I am %s' %(self.name, self.color))


piggy = PigToy('Piggy', 'pink', 'tedu', '400-800-1234')
#piggy.show_me()
print(piggy.vender.company)
piggy.vender.call()

class PigToy:
    def __init__(self, name, color, company, phone):
        self.name = name
        self.color = color
        self.vender = Vender(company, phone)

    def show_me(self):
        print('Hi, my name is %s , I am %s' %(self.name, self.color))

class NewPigToy(PigToy):  #新类继承了它父类的所有属性
    def walk(self):
        print('walking')

a = NewPigToy('piggy', 'pink')
a.show_me()
a.walk()


class PigToy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def show_me(self):
        print('Hi, my name is %s , I am %s' %(self.name, self.color))

class NewPigToy(PigToy):  #新类继承了它父类的所有属性
    def __init__(self, name, color, size):
        #PigToy.__init__(self, name, color)
        super(NewPigToy, self).__init__(name, color)
        self.size = size

    def walk(self):
        print('walking')

a = NewPigToy('piggy', 'pink', 'Middle')
print(a.name, a.size)


class A:
    def foo(self):
        print('foo')
        
class B:
    def bar(self):
        print('bar')
        
class C(A, B):
    pass

c1 = C()
c1.foo()
c1.bar()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return '<%s>' %self.title

    def __call__(self):
        print("<%s> is writed by %s" % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('Core Python', 'Wesley')  #调用__init__返回Book实例的内存地址
    print(core_py)  #打印的时候会自动调用__str__
    core_py()       #调用实例的时候会自动调用__call__


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def create_date(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

    @staticmethod
    def is_date_valid(date_str):
        year, month, day = map(int, date_str.split('-'))
        return year < 4000 and 1 <= month <= 12 and 1 <= day <= 31

if __name__ == '__main__':
    d1 = Date(2019, 1, 20)
    print(d1.month)
    d2 = Date.create_date('2019-1-21')
    print(d2.year)
    print(Date.is_date_valid('2019-13-21'))
