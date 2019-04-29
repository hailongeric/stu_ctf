#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
ii
"""

from pwn import *

context.log_level = 'debug'
r = process('./bbvvmm')

payload = '286346a63cffa373'.decode('hex') 
r.sendlineafter('name:',payload)
r.recvline('000')
print r.pid

pause()
r.interactive()
