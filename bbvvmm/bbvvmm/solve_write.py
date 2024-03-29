#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
from https://www.ctfwp.com/articals/2019national.html
"""

import string

base64_charset = 'IJLMNOPKABDEFGHCQRTUVWXSYZbcdefa45789+/6ghjklmnioprstuvqwxz0123y'

def b64encode(origin_bytes):
    base64_bytes = ['{:0>8}'.format(str(bin(b)).replace('0b', '')) for b in origin_bytes]

    resp = ''
    nums = len(base64_bytes) // 3
    remain = len(base64_bytes) % 3

    integral_part = base64_bytes[0:3 * nums]
    while integral_part:
        tmp_unit = ''.join(integral_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        integral_part = integral_part[3:]

    if remain:
        remain_part = ''.join(base64_bytes[3 * nums:]) + (3 - remain) * '0' * 8
        tmp_unit = [int(remain_part[x: x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='

    return resp


def b64decode(base64_str):
    base64_bytes = ['{:0>6}'.format(str(bin(base64_charset.index(s))).replace('0b', '')) for s in base64_str if
                    s != '=']
    resp = bytearray()
    nums = len(base64_bytes) // 4
    remain = len(base64_bytes) % 4
    integral_part = base64_bytes[0:4 * nums]

    while integral_part:
        tmp_unit = ''.join(integral_part[0:4])
        tmp_unit = [int(tmp_unit[x: x + 8], 2) for x in [0, 8, 16]]
        for i in tmp_unit:
            resp.append(i)
        integral_part = integral_part[4:]

    if remain:
        remain_part = ''.join(base64_bytes[nums * 4:])
        tmp_unit = [int(remain_part[i * 8:(i + 1) * 8], 2) for i in range(remain - 1)]
        for i in tmp_unit:
            resp.append(i)

    return resp

Sbox = [
    [0xD6, 0x90, 0xE9, 0xFE, 0xCC, 0xE1, 0x3D, 0xB7, 0x16, 0xB6, 0x14, 0xC2, 0x28, 0xFB, 0x2C, 0x05],
    [0x2B, 0x67, 0x9A, 0x76, 0x2A, 0xBE, 0x04, 0xC3, 0xAA, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
    [0x9C, 0x42, 0x50, 0xF4, 0x91, 0xEF, 0x98, 0x7A, 0x33, 0x54, 0x0B, 0x43, 0xED, 0xCF, 0xAC, 0x62],
    [0xE4, 0xB3, 0x1C, 0xA9, 0xC9, 0x08, 0xE8, 0x95, 0x80, 0xDF, 0x94, 0xFA, 0x75, 0x8F, 0x3F, 0xA6],
    [0x47, 0x07, 0xA7, 0xFC, 0xF3, 0x73, 0x17, 0xBA, 0x83, 0x59, 0x3C, 0x19, 0xE6, 0x85, 0x4F, 0xA8],
    [0x68, 0x6B, 0x81, 0xB2, 0x71, 0x64, 0xDA, 0x8B, 0xF8, 0xEB, 0x0F, 0x4B, 0x70, 0x56, 0x9D, 0x35],
    [0x1E, 0x24, 0x0E, 0x5E, 0x63, 0x58, 0xD1, 0xA2, 0x25, 0x22, 0x7C, 0x3B, 0x01, 0x21, 0x78, 0x87],
    [0xD4, 0x00, 0x46, 0x57, 0x9F, 0xD3, 0x27, 0x52, 0x4C, 0x36, 0x02, 0xE7, 0xA0, 0xC4, 0xC8, 0x9E],
    [0xEA, 0xBF, 0x8A, 0xD2, 0x40, 0xC7, 0x38, 0xB5, 0xA3, 0xF7, 0xF2, 0xCE, 0xF9, 0x61, 0x15, 0xA1],
    [0xE0, 0xAE, 0x5D, 0xA4, 0x9B, 0x34, 0x1A, 0x55, 0xAD, 0x93, 0x32, 0x30, 0xF5, 0x8C, 0xB1, 0xE3],
    [0x1D, 0xF6, 0xE2, 0x2E, 0x82, 0x66, 0xCA, 0x60, 0xC0, 0x29, 0x23, 0xAB, 0x0D, 0x53, 0x4E, 0x6F],
    [0xD5, 0xDB, 0x37, 0x45, 0xDE, 0xFD, 0x8E, 0x2F, 0x03, 0xFF, 0x6A, 0x72, 0x6D, 0x6C, 0x5B, 0x51],
    [0x8D, 0x1B, 0xAF, 0x92, 0xBB, 0xDD, 0xBC, 0x7F, 0x11, 0xD9, 0x5C, 0x41, 0x1F, 0x10, 0x5A, 0xD8],
    [0x0A, 0xC1, 0x31, 0x88, 0xA5, 0xCD, 0x7B, 0xBD, 0x2D, 0x74, 0xD0, 0x12, 0xB8, 0xE5, 0xB4, 0xB0],
    [0x89, 0x69, 0x97, 0x4A, 0x0C, 0x96, 0x77, 0x7E, 0x65, 0xB9, 0xF1, 0x09, 0xC5, 0x6E, 0xC6, 0x84],
    [0x18, 0xF0, 0x7D, 0xEC, 0x3A, 0xDC, 0x4D, 0x20, 0x79, 0xEE, 0x5F, 0x3E, 0xD7, 0xCB, 0x39, 0x48]
]

CK = [
    0x00070e15L, 0x1c232a31L, 0x383f464dL, 0x545b6269L,
    0x70777e85L, 0x8c939aa1L, 0xa8afb6bdL, 0xc4cbd2d9L,
    0xe0e7eef5L, 0xfc030a11L, 0x181f262dL, 0x343b4249L,
    0x50575e65L, 0x6c737a81L, 0x888f969dL, 0xa4abb2b9L,
    0xc0c7ced5L, 0xdce3eaf1L, 0xf8ff060dL, 0x141b2229L,
    0x30373e45L, 0x4c535a61L, 0x686f767dL, 0x848b9299L,
    0xa0a7aeb5L, 0xbcc3cad1L, 0xd8dfe6edL, 0xf4fb0209L,
    0x10171e25L, 0x2c333a41L, 0x484f565dL, 0x646b7279L
]

FK = [0xA3B1BAC6L, 0x56AA3350L, 0x677D9197L, 0xB27022DCL]

def LeftRot(n, b): return (n << b | n >> 32 - b) & 0xffffffff

def t(a):
    a4=a>>4
    a3=a4>>4
    a2=a3>>8
    a1=a2>>8
    return (Sbox[a1>>4][a1&0xf] << 24) + \
           (Sbox[a2>>4&0xf][a2&0xf] << 16) + \
           (Sbox[a3>>4&0xf][a3&0xf] << 8) + \
           Sbox[a4&0xf][a&0xf]

def F(xi, rki):
    B=t(xi[1]^xi[2]^xi[3]^rki)
    return xi[0] ^ B^LeftRot(B,2)^LeftRot(B,10)^LeftRot(B,18)^LeftRot(B,24)

def T_(A):
    B=t(A)
    return B^LeftRot(B,13)^LeftRot(B,23)

def sm4(X,K,rev=0):
    tmp_K=K[4:]
    if rev==1: tmp_K=tmp_K[::-1]
    for i in xrange(32):
        X = [X[1], X[2], X[3], F(X, tmp_K[i])]
    return X[::-1]

def lbc(i):
    tmp=hex(i)[2:]
    if tmp[-1]=='L': tmp=tmp[:-1]
    if len(tmp)%2==1: tmp='0'+tmp
    tmp=tmp.decode('hex')[::-1]
    return int(tmp.encode('hex'),16)

enc = str(b64decode('RVYtG85NQ9OPHU4uQ8AuFM+MHVVrFMJMR8FuF8WJQ8Y='))
m = int(enc,16)
print hex(m)
key = 0xD60D29FD0B3A70A553B72A31DAF198DA

X=[m >> (128-32),(m >> (128-32*2))&0xffffffff,(m >> 32)&0xffffffff,m&0xffffffff]
print X
Y=[lbc(key >> (128-32)),lbc((key >> (128-32*2))&0xffffffff),lbc((key >> 32)&0xffffffff),lbc(key&0xffffffff)][::-1]
print Y
K=[Y[i]^FK[i] for i in xrange(4)]
print K
for i in xrange(32):
    K.append(K[i]^T_(K[i+1]^K[i+2]^K[i+3]^CK[i]))

X=sm4(X,K,1)
username=''
for i in xrange(4):
    username += hex(X[i])[2:-1].decode('hex').decode('hex')
print username
