import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha segura aleatória."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def verificar_senha(senha):
    """Analisa a força da senha e devolve nota e dicas."""
    pontuacao = 0
    dicas = []

    if len(senha) >= 8:
        pontuacao += 1
    else:
        dicas.append("Use pelo menos 8 caracteres.")

    if any(c.islower() for c in senha) and any(c.isupper() for c in senha):
        pontuacao += 1
    else:
        dicas.append("Misture letras maiúsculas e minúsculas.")

    if any(c.isdigit() for c in senha):
        pontuacao += 1
    else:
        dicas.append("Adicione pelo menos um número.")

    if any(c in string.punctuation for c in senha):
        pontuacao += 1
    else:
        dicas.append("Adicione pelo menos um símbolo (ex.: !@#$%).")

    if pontuacao == 4:
        nivel = "FORTE"
    elif pontuacao == 3:
        nivel = "MÉDIA"
    else:
        nivel = "FRACA"

    return nivel, dicas

def menu():
    print("=== GERADOR E VERIFICADOR DE SENHAS ===")
    print("1 - Gerar senha segura")
    print("2 - Verificar força de uma senha")
    print("0 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        try:
            entrada = input("Tamanho da senha (padrão 12): ")
            tamanho = int(entrada) if entrada else 12
        except ValueError:
            print("Valor inválido. Usando o padrão 12.")
            tamanho = 12
        print(f"Senha gerada: {gerar_senha(tamanho)}")

    elif opcao == "2":
        senha = input("Digite a senha para verificar: ")
        nivel, dicas = verificar_senha(senha)
        print(f"Classificação: {nivel}")
        if dicas:
            print("Dicas para melhorar:")
            for dica in dicas:
                print(f"- {dica}")
        else:
            print("Excelente! Sua senha está muito segura.")

    elif opcao == "0":
        print("Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")