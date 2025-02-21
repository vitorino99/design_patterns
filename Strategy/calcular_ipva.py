import random

from strategy import CaminhaoIPVA, CarroIPVA, MotoIPVA, Veiculo


estrategias_ipva = [CarroIPVA(), MotoIPVA(), CaminhaoIPVA()]
valores = [10000, 20000, 30000, 40000, 50000]

estrategia = random.choice(estrategias_ipva)
valor_veiculo = random.choice(valores)

veiculo = Veiculo(valor_veiculo, estrategia)

print(f"Veículo com valor R$ {valor_veiculo:.2f}")
print(f"IPVA calculado: R$ {veiculo.calcular_ipva():.2f}")
