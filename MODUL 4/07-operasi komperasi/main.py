# operasi komparasi

# setiap hasil komparasi selalu bertipe boolean (TRUE/FALSE)

# >, <, =, !=, >=, <=, is, dan is not

# deklarasi variabel
a = 4
b = 2

# lebih besar dari (>)
print("===lebih besar dari (>)")
hasil = a > 2 # TRUE
print(a, ">", 2, "=", hasil)
hasil = b > 3 # FLASE
print(b, ">", 3, "=", hasil)
hasil = b > 2 # FLASE
print(b, ">", 2, "=", hasil)

# kurang dari <
print("===lebih dari (<)")
hasil = a < 3 # FLASE
print(a, "<", 3, "=", hasil)
hasil = b < 3 # TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 2 # FLASE
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan >=
print("===lebih dari sama dengan(>=)")
hasil = a >= 3 # TRUE
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 # FLASE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2 #TRUE
print(b, ">=", 2, "=", hasil)

# kurang dari sama dengan <=
print("===kurang dari sama dengan(<=)")
hasil = a <= 3 # FLASE
print(a, "<=", 3, "=", hasil)
hasil = b <= 3 # TRUE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2 # TRUE
print(b, "<=", 2, "=", hasil)

# sama dengan (==)
print("===sama dengan(==)")
hasil = a == 4 # FLASE
print(a, "==", 4, "=", hasil)
hasil = a == 4 # TRUE
print(a, "==", 4, "=", hasil)

# tidak sama dengan (!=)
print("===tidak sama dengan(!=)")
hasil = a != 3 # TRUE
print(a, "!=", 3, "=", hasil)
hasil = a != 3 # FLASE
print(a, "!=", 3, "=", hasil)

# is sebagai komparasi objek indentify
print("===objek identify (is)")
x = 5 # ini adalah assignment membuat objek
y = 5
hasil = x is y # TRUE
print(x, "is", y, "=", hasil)
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))

# is not sebagai komparasi
print("===objek identify")
x = 5 # ini adalah assignment membuat objek
y = 6
hasil = x is y # FLASE
print(x, "is", y, "=", hasil)
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))

print("=== objek indentify (is not)")
x = 5 # ini adalah assignment membuat objek
y = 5
print("nilai x =", x, "id =", hex(id(x)))
print("nilai y =", y, "id =", hex(id(y)))
hasil = x is not y
print("x is not y", hasil)