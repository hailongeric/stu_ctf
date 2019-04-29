#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from pwn import *
context.log_level = "dehug"

r = process("./bbvvmm")

r.interactive()
