# meminta input dari pengguna dalam fahrenheit
fahrenheit = float(input("masukkan temperatuer dalam fahrenheit: "))

# mengonversi fahrenheit ke celcius
celcius = (fahrenheit - 32) * 5 / 9

# menampilka hasil konversi
print(f"{fahrenheit} derajat fahrenheit sama dengan {celcius:.2f} derajat celcius.")6