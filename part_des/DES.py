
    
class DES:
        
    # initial permutation IP
    __ip = [
        57, 49, 41, 33, 25, 17, 9,  1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
        56, 48, 40, 32, 24, 16, 8,  0,
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6
    ]

    # final permutation IP^-1
    __fp = [
        39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25,
        32,  0, 40,  8, 48, 16, 56, 24
    ]

    # Expansion table for turning 32 bit blocks into 48 bits
    __expansion_table = [
        31,  0,  1,  2,  3,  4,
        3,  4,  5,  6,  7,  8,
        7,  8,  9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31,  0
    ]

    # 32-bit permutation function P used on the output of the S-boxes
    __p = [
        15, 6, 19, 20, 28, 11,
        27, 16, 0, 14, 22, 25,
        4, 17, 30, 9, 1, 7,
        23,13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10,
        3, 24
    ]

    # Permutation and translation tables for DES
    __pc1 = [
        56, 48, 40, 32, 24, 16,  8,
        0, 57, 49, 41, 33, 25, 17,
        9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36, 28,
        20, 12,  4, 27, 19, 11,  3
    ]

    # permuted choice key (table 2)
    __pc2 = [
        13, 16, 10, 23,  0,  4,
        2, 27, 14,  5, 20,  9,
        22, 18, 11,  3, 25,  7,
        15,  6, 26, 19, 12,  1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31
    ]

    # number left rotations of pc1
    __left__rotations = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
    ]

    # The (in)famous S-boxes
    __sboxTable = [
        # S1
        [
            [14,  4, 13, 1,  2, 15, 11, 8,  3, 10,  6, 12,  5,  9, 0, 7],
            [0, 15,  7, 4, 14,  2, 13, 1, 10,  6, 12, 11,  9,  5, 3, 8],
            [4,  1, 14, 8, 13,  6, 2, 11, 15, 12,  9,  7,  3, 10, 5, 0],
            [15, 12,  8, 2,  4,  9, 1,  7,  5, 11,  3, 14, 10,  0, 6, 13]
        ],

        # S2
        [
            [15,  1,  8, 14,  6, 11,  3,  4,  9, 7,  2, 13, 12, 0,  5, 10],
            [3, 13,  4,  7, 15,  2,  8, 14, 12, 0,  1, 10,  6, 9, 11,  5],
            [0, 14,  7, 11, 10,  4, 13,  1,  5, 8, 12,  6,  9, 3,  2, 15],
            [13,  8, 10,  1,  3, 15,  4,  2, 11, 6,  7, 12,  0, 5, 14,  9]
        ],

        # S3
        [
            [10,  0,  9, 14, 6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
            [13,  7,  0,  9, 3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
            [13,  6,  4,  9, 8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
            [1, 10, 13,  0, 6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]
        ],

        # S4
        [
            [7, 13, 14, 3,  0,  6,  9, 10,  1, 2, 8,  5, 11, 12,  4, 15],
            [13,  8, 11, 5,  6, 15,  0,  3,  4, 7, 2, 12,  1, 10, 14,  9],
            [10,  6,  9, 0, 12, 11,  7, 13, 15, 1, 3, 14,  5,  2,  8,  4],
            [3, 15,  0, 6, 10,  1, 13,  8,  9, 4, 5, 11, 12,  7,  2, 14]
        ],

        # S5
        [
            [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13, 0, 14, 9],
            [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3, 9,  8, 6],
            [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6, 3,  0, 14],
            [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10, 4,  5, 3]
        ],

        # S6
        [
            [12,  1, 10, 15, 9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
            [10, 15,  4,  2, 7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
            [9, 14, 15,  5, 2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
            [4,  3,  2, 12, 9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8,  13]
        ],

        # S7
        [
            [4, 11,  2, 14, 15, 0,  8, 13,  3, 12, 9,  7,  5, 10, 6, 1],
            [13,  0, 11,  7,  4, 9,  1, 10, 14,  3, 5, 12,  2, 15, 8, 6],
            [1,  4, 11, 13, 12, 3,  7, 14, 10, 15, 6,  8,  0,  5, 9, 2],
            [6, 11, 13,  8,  1, 4, 10,  7,  9,  5, 0, 15, 14,  2, 3, 12]
        ],

        # S8
        [
            [13,  2,  8, 4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
            [1, 15, 13, 8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
            [7, 11,  4, 1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
            [2,  1, 14, 7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
        ],
    ]

    def hex2bin(self, hex):
        if hex[-1] == 'L':
            hex=hex[:-1]
        return (bin(int(hex, 16))[2:]).zfill(len(hex)*4)

    def bin2hex(self, bin):
        h =  hex(int(''.join(bin), 2)).upper()[2:].zfill(int(len(bin)/4))
        if h[-1] == 'L':
            h=h[:-1]
        return h
    
    def applyPerm(self, key, perm):
        output = [] 
        for i in perm:
            #print i
            #print key
            output.append(key[int(i)])
        return ''.join(output)

    def sBoxLookup(self, key, sBox):
        if not len(key) == 6:
            raise('SBox Lookup key length not valid')
        row = int(key[0]+key[5],2)
        col = int(key[1:5],2)
        return sBox[row][col]

    def applySBox(self, key):
        if not len(key) == 48:
            raise('SBox Lookup key length not valid')
        keyDiv = [key[i:i+6] for i in range(0,len(key), 6)]
        output = []
        for i in range(8):
            output.append('{0:04b}'.format(self.sBoxLookup(keyDiv[i], self.__sboxTable[i])))
        return ''.join(output)

    def xor(self, x, y):
        return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

    def F(self, inp, key):
        expOut = self.applyPerm(inp, self.__expansion_table)
        xorOut = self.xor(expOut, key)
        sBoxOut = self.applySBox(xorOut)
        pBoxOut = self.applyPerm(sBoxOut, self.__p)
        return pBoxOut
    
    def leftCircShift56(self, key, n):
        left = key[:28]
        right = key[28:]
        return left[n:]+left[0:n]+right[n:]+right[0:n]

    def keyGen(self, key, round):
        keys = []
        rotations = []
        if round <= 16:
            rotations = self.__left__rotations[:round]
        else:
            div = int(round/16)
            rem = int(round%16)
            rotations = self.__left__rotations*div+self.__left__rotations[:rem]
        #key = self.applyPerm(self.hex2bin(key), self.__pc1)
        #for i in rotations:
        #    key = self.leftCircShift56(key, i)
        #    keys.append(self.applyPerm(key, self.__pc2))
        m =  list(map(self.bin2hex, keys))
        m= ['e0be661032d5','f0b676f82095','e4d67623628f','e6d376363183','aed373a60167','af537b46abc2','af53d9748559','1f5bd94b944a','3f49d94897ea',
        '1f699d1cdc29','1f2d9d4a5c70','5f2cad89e938','dbacaca15e10','d8aeaed90236','f0be2e954a8c','f0bea6112e84']
        return m 

    def encryptOneRoud(self, key, msg):
        key = self.hex2bin(key)
        msg = self.hex2bin(msg)
        left = msg[:32]
        right = msg[32:]
        fOut = self.F(right, key)
        prevRight = right
        right = self.xor(left, fOut)
        left = prevRight
        return self.bin2hex(left+right)

    def encryptOneTime(self, key, msg, times,decrypt):
        keys = self.keyGen(key, 16)
        if decrypt:
            keys.reverse()
        initPerm = self.applyPerm(self.hex2bin(msg), self.__ip)
        # print type(initPerm)
        #msg = self.bin2hex(initPerm)
        msg = msg
        for i in range(16):
            msg = self.encryptOneRoud(keys[(i+times)%16], msg)
            e = msg[8:]+msg[:8]
            print e.decode('hex')
            h= self.applyPerm(self.hex2bin(e), self.__fp)
            print h.decode('hex')
        msgSwap = msg[8:]+msg[:8]
        #print msgSwap.decode('hex')
        cipher = self.applyPerm(self.hex2bin(msgSwap), self.__fp)
        return self.bin2hex(cipher)

    def encrypt(self, key, msg, times,ts ,decrypt=False):
        cipher = msg
        for t in range(times):
            cipher = self.encryptOneTime(key, cipher,ts, decrypt)
            print cipher.decode('hex')
        return cipher

D = DES()
for i in range(5,6):
    D.encrypt('12345678','92d915250119e12b',16,i,True)
