# ==============================================================================
# GERENCIADOR DE ESTOQUE DE PRODUTOS REGIONAIS (FEIRA DA BANANA / PORTO DE MANAUS)
# Curso Técnico em Inteligência Artificial - Avaliação AV4
# Componente Curricular: Programação em Python
# ==============================================================================

"""
DESCRIÇÃO TÉCNICA:
Sistema de automação de inventário focado no comércio de produtos amazônicos.
Utiliza Dicionários de Dicionários (Hash Maps aninhados) para garantir buscas 
e atualizações em tempo constante O(1). Implementa CRUD completo, tratamento 
de exceções para robustez e um Sistema Especialista Baseado em Regras (IA Simbólica).
"""

# BLOCO 1: BANCO DE DADOS EM MEMÓRIA (Indexado por ID)
estoque = {
    1: {"nome": "Açaí", "quantidade": 20, "preco": 15.00},
    2: {"nome": "Cupuaçu", "quantidade": 10, "preco": 12.50},
    3: {"nome": "Farinha", "quantidade": 30, "preco": 8.00},
    4: {"nome": "Castanha-Do-Pará", "quantidade": 5, "preco": 25.00}
}

# Controle incremental de chaves primárias automáticas
proximo_codigo = 5


# BLOCO 2: CADASTRO DE NOVOS PRODUTOS (CREATE)
def cadastrar_novo_produto(estoque_local):
    global proximo_codigo
    print("\n=== 📝 CADASTRAR NOVO PRODUTO ===")
    
    nome = input("Nome do novo produto (ex: Pirarucu): ").strip().title()
    
    # Validação de integridade para evitar nomes duplicados
    for dados in estoque_local.values():
        if dados["nome"] == nome:
            print(f"\n⚠️ [!] O produto '{nome}' já está cadastrado no sistema!")
            return

    try:
        # Sanitização de string para o padrão numérico float (Aceita ponto e vírgula)
        preco_input = input(f"Preço unitário de {nome} (R$): ").strip()
        preco_input = preco_input.replace(",", ".") 
        preco = float(preco_input)
    except ValueError:
        print("\n❌ [ERRO] Entrada inválida! Digite um preço numérico válido.")
        return

    # Inserção O(1) na tabela hash
    estoque_local[proximo_codigo] = {"nome": nome, "quantidade": 0, "preco": preco}
    print(f"\n✅ [OK] {nome} cadastrado com sucesso! CÓDIGO ATRIBUÍDO: {proximo_codigo}")
    
    proximo_codigo += 1


# BLOCO 3: MOVIMENTAÇÃO DE ENTRADA DE ESTOQUE (UPDATE)
def adicionar_estoque_por_codigo(estoque_local):
    print("\n=== 📥 ADICIONAR QTD AO ESTOQUE ===")
    try:
        codigo = int(input("Digite o CÓDIGO do produto: "))
    except ValueError:
        print("\n❌ [ERRO] O código deve ser um número inteiro!")
        return

    if codigo in estoque_local:
        produto = estoque_local[codigo]
        print(f"Produto Selecionado: {produto['nome']} (Estoque atual: {produto['quantidade']} unid.)")
        
        try:
            qtd_entrada = int(input(f"Quantidade de {produto['nome']} que está entrando: "))
            if qtd_entrada < 0:
                print("\n❌ [ERRO] A quantidade de entrada não pode ser negativa!")
                return
        except ValueError:
            print("\n❌ [ERRO] Digite uma quantidade inteira válida!")
            return
        
        # Operador de acumulação composto para atualizar o estado do inventário
        produto["quantidade"] += qtd_entrada
        print(f"\n✅ [OK] {qtd_entrada} unidades adicionadas! Novo estoque: {produto['quantidade']} unid.")
    else:
        print("\n⚠️ [!] Código de produto não cadastrado.")


# BLOCO 4: LEITURA DO INVENTÁRIO (READ)
def listar_produtos(estoque_local):
    print("\n" + "="*12 + " INVENTÁRIO ATUAL " + "="*12)
    if not estoque_local:
        print("Nenhum produto cadastrado.")
        return
    for codigo, dados in estoque_local.items():
        print(f"CÓDIGO: {codigo} | {dados['nome']}")
        print(f"Quantidade..: {dados['quantidade']} unid.")
        print(f"Preço.......: R$ {dados['preco']:.2f}")
        print("-" * 42)


# BLOCO 5: ALGORITMO HÍBRIDO DE BUSCA (READ)
def buscar_produto(estoque_local):
    print("\n=== 🔍 BUSCAR PRODUTO ===")
    opcao_busca = input("Buscar por (1) Código ou (2) Nome? ").strip()
    
    if opcao_busca == "1":
        try:
            codigo = int(input("Digite o código: "))
            if codigo in estoque_local:
                p = estoque_local[codigo]
                print(f"\n[Achou!] CÓDIGO {codigo} -> {p['nome']} | Qtd: {p['quantidade']} | Preço: R$ {p['preco']:.2f}")
            else:
                print("\n⚠️ [!] Código não encontrado.")
        except ValueError:
            print("\n❌ [ERRO] Código inválido.")
            
    elif opcao_busca == "2":
        nome = input("Digite o nome do produto: ").strip().title()
        encontrou = False
        for codigo, p in estoque_local.items():
            if p["nome"] == nome:
                print(f"\n[Achou!] CÓDIGO {codigo} -> {p['nome']} | Qtd: {p['quantidade']} | Preço: R$ {p['preco']:.2f}")
                encontrou = True
                break
        if not encontrou:
            print("\n⚠️ [!] Nome de produto não localizado.")
    else:
        print("\n❌ Opção de filtragem inválida.")


# BLOCO 6: EXCLUSÃO DE REGISTROS (DELETE)
def remover_produto(estoque_local):
    print("\n=== ❌ REMOVER PRODUTO DO SISTEMA ===")
    try:
        codigo = int(input("Digite o código do produto para remover: "))
        if codigo in estoque_local:
            removido = estoque_local.pop(codigo)
            print(f"\n✅ [OK] {removido['nome']} foi completamente excluído do sistema.")
        else:
            print("\n⚠️ [!] Código não encontrado no banco de dados.")
    except ValueError:
        print("\n❌ [ERRO] Código inválido.")


# BLOCO 7: ALERTA DE REPOSIÇÃO (LÓGICA CONDICIONAL COM LIMIAR)
def listar_estoque_baixo(estoque_local, limiar=10):
    print(f"\n======= ⚠️ ESTOQUE BAIXO (Limiar: {limiar}) =======")
    encontrou = False
    for codigo, dados in estoque_local.items():
        if dados["quantidade"] <= limiar:
            print(f"• [Cód {codigo}] {dados['nome']} -> Apenas {dados['quantidade']} unidades.")
            encontrou = True
    if not encontrou:
        print("Todos os produtos possuem níveis de estoque seguros.")


# BLOCO 8: CÁLCULO PATRIMONIAL (LAÇO COM ACUMULADOR)
def calcular_valor_total(estoque_local):
    # Uso de list comprehension e geradores com a função acumuladora nativa sum()
    total = sum(dados["quantidade"] * dados["preco"] for dados in estoque_local.values())
    print(f"\n💰 Valor Patrimonial Total em Estoque: R$ {total:.2f}")


# BLOCO 9: NÚCLEO DE INTELIGÊNCIA ARTIFICIAL (SISTEMA ESPECIALISTA)
def recomendacao_ia(estoque_local):
    print("\n======= 🧠 RECOMENDAÇÃO INTELIGENTE (SISTEMA ESPECIALISTA) =======")
    for codigo, dados in estoque_local.items():
        valor_investido = dados["quantidade"] * dados["preco"]
        qtd = dados["quantidade"]
        
        print(f"• [Cód {codigo}] {dados['nome']} ({qtd} unid.): ", end="")
        
        # Árvore de Decisão Baseada em Regras Lineares
        if dados["quantidade"] <= 5:
            print("❌ COMPRAR IMEDIATAMENTE (Risco crítico de falta)")
        elif dados["quantidade"] <= 10:
            print("⚠️ PROGRAMAR REPOSIÇÃO (Estoque preventivo)")
        elif valor_investido > 500:
            print("💰 ESTOQUE ALTO / CAPITAL RETIDO (Evitar novas compras)")
        else:
            print("✅ ESTOQUE ADEQUADO (Operação normal)")


# BLOCO 10: INTERFACE EM LOOP INTERATIVO (MAIN)
def main():
    while True:
        print("\n" + "=" * 45)
        print("     GERENCIADOR DE ESTOQUE REGIONAL     ")
        print("=" * 45)
        print("1 - Cadastrar NOVO produto (Gera Código)")
        print("2 - Adicionar QTD ao estoque (Via Código)")
        print("3 - Listar estoque completo")
        print("4 - Buscar produto")
        print("5 - Remover produto do sistema")
        print("6 - Alertas de estoque baixo")
        print("7 - Valor total do estoque")
        print("8 - Recomendação Inteligente (IA)")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1": cadastrar_novo_produto(estoque)
        elif opcao == "2": adicionar_estoque_por_codigo(estoque)
        elif opcao == "3": listar_produtos(estoque)
        elif opcao == "4": buscar_produto(estoque)
        elif opcao == "5": remover_produto(estoque)
        elif opcao == "6": listar_estoque_baixo(estoque)
        elif opcao == "7": calcular_valor_total(estoque)
        elif opcao == "8": recomendacao_ia(estoque)
        elif opcao == "0":
            print("\nObrigado por utilizar o sistema! Encerrando...")
            break
        else:
            print("\n❌ [!] Opção inválida! Digite um número válido entre 0 e 8.")

if __name__ == "__main__":
    main()