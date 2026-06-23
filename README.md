# Projeto_Python---Gerenciador-de-Estoque-de-Produtos-Regionais-Feira-da-Banana-Porto
# Dicionário global para armazenar o estoque: {ID: {nome, quantidade, preco}}
estoque = {
    1: {"nome": "Açaí (Litro)", "quantidade": 50, "preco": 18.00},
    2: {"nome": "Polpa de Cupuaçu (Kg)", "quantidade": 15, "preco": 20.00},
    3: {"nome": "Farinha do Uarini (Kg)", "quantidade": 80, "preco": 12.00},
    4: {"nome": "Castanha-do-Pará (Kg)", "quantidade": 8, "preco": 35.00}
}
proximo_id = 5

def adicionar_produto():
    global proximo_id
    nome = input("\nNome do produto: ").strip()
    try:
        quantidade = float(input("Quantidade inicial (em kg/l): "))
        preco = float(input("Preço unitário (R$): "))
        estoque[proximo_id] = {"nome": nome, "quantidade": quantidade, "preco": preco}
        print(f"Produto '{nome}' adicionado com sucesso!")
        proximo_id += 1
    except ValueError:
        print("Entrada inválida. Digite apenas números para quantidade e preço.")

def atualizar_quantidade():
    mostrar_estoque()
    try:
        id_prod = int(input("\nDigite o ID do produto que deseja atualizar: "))
        if id_prod in estoque:
            nova_quant = float(input(f"Nova quantidade para {estoque[id_prod]['nome']}: "))
            estoque[id_prod]['quantidade'] = nova_quant
            print("Quantidade atualizada com sucesso!")
        else:
            print("ID não encontrado.")
    except ValueError:
        print("ID ou quantidade inválida.")

def remover_produto():
    mostrar_estoque()
    try:
        id_prod = int(input("\nDigite o ID do produto que deseja remover: "))
        if id_prod in estoque:
            removido = estoque.pop(id_prod)
            print(f"Produto '{removido['nome']}' removido do estoque.")
        else:
            print("ID não encontrado.")
    except ValueError:
        print("ID inválido.")

def mostrar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    if not estoque:
        print("Nenhum produto cadastrado.")
    for id_prod, info in estoque.items():
        print(f"ID: {id_prod} | {info['nome']} | Qtd: {info['quantidade']} | R$ {info['preco']:.2f}")

def verificar_estoque_baixo():
    try:
        limiar = float(input("\nInforme o limiar de quantidade (ex: abaixo de 10): "))
        print(f"\n--- PRODUTOS COM ESTOQUE ABAIXO DE {limiar} ---")
        encontrou = False
        for info in estoque.values():
            if info['quantidade'] < limiar:
                print(f"{info['nome']} - Quantidade atual: {info['quantidade']}")
                encontrou = True
        if not encontrou:
            print("Nenhum produto abaixo do limiar informado.")
    except ValueError:
        print("Valor de limiar inválido.")

def calcular_valor_total():
    valor_total = 0.0
    for info in estoque.values():
        valor_total += info['quantidade'] * info['preco']
    print(f"\nO valor total de todo o estoque é de: R$ {valor_total:.2f}")

# --- Menu Interativo ---
while True:
    print("\n==============================")
    print(" GESTÃO DE ESTOQUE - FEIRA DA BANANA")
    print("==============================")
    print("1. Exibir Estoque")
    print("2. Adicionar Produto")
    print("3. Atualizar Quantidade")
    print("4. Remover Produto")
    print("5. Verificar Estoque Baixo")
    print("6. Calcular Valor Total")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        adicionar_produto()
    elif opcao == "3":
        atualizar_quantidade()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        verificar_estoque_baixo()
    elif opcao == "6":
        calcular_valor_total()
    elif opcao == "0":
        print("\nSaindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
