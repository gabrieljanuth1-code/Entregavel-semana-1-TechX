# 4. Calculadora de desconto
preco = float(input("Preço: "))
desconto = float(input("Desconto (%): "))

preco_final = preco - (preco * desconto / 100)

print(f"Preço final: R$ {preco_final:.2f}")
