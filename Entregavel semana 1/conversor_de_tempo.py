# 3. Conversor de tempo
segundos = int(input("Segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
