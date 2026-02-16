# RECEBENDO OS DADOS DO JOGADOR
nomeHeroi = str(input("Digite o nome do seu herói: "))

quantXp = float(input("Digite o seu xp: "))

nivel = ""

# CONDICIONAIS PARA VERIFICAÇÃO DE NÍVEL

if quantXp < 1000:
    nivel = "Ferro"
elif quantXp >= 1.001 and quantXp <= 2000:
    nivel = "Bronze"
elif quantXp <= 2.001 and quantXp <= 5000:
    nivel = "prata"
elif quantXp >= 6.001 and quantXp <=7000:
     nivel = "ouro"
elif quantXp >= 7.001 and quantXp <= 8000:
    nivel = "Platina"
elif quantXp >= 8.001 and quantXp <= 9000:
    nivel = "Ascendente"
elif quantXp >= 9.001 and quantXp <= 10000:
    nivel = "Imortal"

#OUTPUT
print(f"o Herói: {nomeHeroi} está no nível: {nivel}")