class PySolution:
    def int_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "S"
        ]
        roman_num = ''
        n1 = num
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return f'your result for {n1} is {roman_num}'


p = PySolution()
print(p.int_roman(int(input("enter number: "))))
# print(py_solution().int_to_Roman(4000))
