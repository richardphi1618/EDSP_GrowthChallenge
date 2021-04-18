class RomanNumeral:
    def __init__ (self, num):
        self.num = num
        self.RN = self.to_RN()

    
    def to_RN (self):

        val = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        syb = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        roman_num = ""

        self.remainder = self.num
        
        for i in range(len(val)):
            count = int(self.remainder / val[i])
            roman_num += syb[i] * count
            self.remainder -= val[i] * count

        return roman_num
                


                
                