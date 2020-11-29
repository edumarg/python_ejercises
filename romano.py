class Romano:
    def int_to_Roman(self, num):
        val = [
            10000, 5000, 4000, 1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
           '-X', '-V','-IV', "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            print('--val[i]--')
            print(val[i])
            print('--num//val[i]--')
            print(num // val[i])
            for n in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

romano = Romano()

print(romano.int_to_Roman(10000))
