# operasi aritmatika

# variabel dengan nilai awal
a = 10
b = 3

# operasi penjumlahan (+)
hasil = a + b
print (a, "+", b, "=", hasil)

# operasi pengurangan (-)
hasil = a - b
print (a, "-", b, "=", hasil)

# operasi perkalian (*)
hasil = a * b
print (a, "*", b, "=", hasil)

# operasi pembagian (/)
hasil = a / b
print (a, "/", b, "=", hasil)

# operasi pemangkatan (**)
hasil = a ** b
print (a, "**", b, "=", hasil)

# operasi modulus (%)
hasil = a % b
print (a, "%", b, "=", hasil)

# operasi floor division (//)
hasil = a // b
print (a, "//", b, "=", hasil)

# perioritas operasi 

"""
    1. ()
    2. perkalian pembagian, dll -> * / ** % //
    3. penjumlahan dan pengurangan +-
"""   
x = 3
y = 2
z = 4

hasil = x ** z + X / (y - y) % z // x
print(X, "**", y, "**", z, "+", x, "/", y,"-", y, "%", z,"//", x, hasil )


hasil = (z + y) * z
print(x, "+", y, "*", z, "=", hasil)
# kurung akan mengambil langkah paling pertama 
hasil = (x + y) * z
print("(", x, "+", y,") * ", z, "=", hasil)