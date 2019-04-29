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

elf  = ELF("./bbvvmm")

addr = 0x406a81

elf.write(addr,'\x00')

elf.save('new')
