import relojes

reloj1 = relojes.reloj()

print(reloj1.getTiempo())
reloj1.setTiempo(23, 59, 46)
print(reloj1.getTiempo())

while True:
    print(reloj1.iniciarReloj())