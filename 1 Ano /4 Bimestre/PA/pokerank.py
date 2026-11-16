# POKÉRANK RPG: EDIÇÃO DEFINITIVA - SISTEMA DE GESTÃO DA GUILDA

treinadores = []

def cabecalho(titulo):
    """Função auxiliar para exibir títulos bonitos no console"""

    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)

def ler_nota(mensagem):
    """Garante que o usuário digite um número válido entre 0 e 10"""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print(" A nota deve ser entre 0 e 10, Tenta de novo.")
        except ValueError:
            print(" Valor inválido! Digite apenas números (ex: 8.5).")

def cadastrar_treinador():
    cabecalho(" REGISTRO DE NOVA DUPLA NA ARENA ◓⃙ ")

    while True:
        nome = input("Nome do(a) Mestre(a) / Treinador(a): ").strip()
        if nome:
            break
        print(" O treinador precisa de um nome!")
        
    while True:
        pokemon = input("Nome ou Espécie do Pokémon Companheiro: ").strip()
        if pokemon:
            break
        print(" O nome do Pokémon não pode estar vazio!")
        
    tipo = input("Classe Elementar / Tipo (ex: Fogo, Psíquico, Água, Dragão): ").strip()
    if not tipo:
        tipo = "Normal" # Tipo padrão caso esqueçam de digitar
    
    print("\n--- AVALIAÇÃO NAS PROVAS DA GUILDA ---")
    nota1 = ler_nota("► Força de Combate (0 a 10): ")
    nota2 = ler_nota("► Sinergia com o Mestre (0 a 10): ")
    
    # Cálculo da média inicial de poder
    media = (nota1 + nota2) / 2
    
    # Estrutura do Dicionário (Ficha do Personagem)
    ficha = {
        "nome": nome,
        "pokemon": pokemon,
        "tipo": tipo.capitalize(),
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "treinamentos": 0 # Contador de missões/treinos realizados
    }
    
    treinadores.append(ficha)
    print(f"\n QUE AURA!!! A dupla [{pokemon} & {nome}] foi registrada com poder Base: {media:.1f}!")

def listar_ranking():
    cabecalho("TODOS OS TREINADORES E SEUS POKÉMONS!!!")
    
    if not treinadores:
        print(" Nenhum treinador foi registrado na arena ainda. Chame novos treinadores!")
        return
    
   
    hall_ordenado = sorted(treinadores, key=lambda x: x["media"], reverse=True)
    
    for posicao, t in enumerate(hall_ordenado, 1):
        print(f"[{posicao}º Lugar] Mestre: {t['nome']} | Pokémon: {t['pokemon']} ({t['tipo']}) | "
              f"Poder: {t['media']:.1f} | Treinos: {t['treinamentos']}")

def simular_treinamento():
    cabecalho(" CENTRO DE TREINAMENTO DA ARENA DE BATALHA")
    
    if not treinadores:
        print(" Não há duplas cadastradas para treinar!")
        return
    
    print("Duplas disponíveis na guilda:")
    for i, t in enumerate(treinadores, 1):
        print(f"{i}. {t['pokemon']} (Mestre: {t['nome']})")
        
    try:
        escolha = int(input("\nDigite o número da dupla que deseja enviar para o treino: ")) - 1
        if 0 <= escolha < len(treinadores):
            dupla = treinadores[escolha]
            print(f"\n {dupla['pokemon']} e {dupla['nome']} foram treinar nas montanhas difíceis")
            
          
            dupla['nota1'] = min(10.0, dupla['nota1'] + 0.5)
            dupla['nota2'] = min(10.0, dupla['nota2'] + 0.5)
            dupla['media'] = (dupla['nota1'] + dupla['nota2']) / 2
            dupla['treinamentos'] += 1
            
            print(f" O treinamento concluído! Novo poder total de [{dupla['pokemon']}]: {dupla['media']:.1f}")
        else:
            print(" Número de dupla inválido!")
    except ValueError:
        print(" Digite um número inteiro válido.")

def filtrar_por_tipo():
    cabecalho(" CONSULTA POR CLASSE ELEMENTAR")
    
    if not treinadores:
        print(" A guilda está vazia.")
        return
        
    tipo_busca = input("Digite o tipo elemental que deseja procurar (ex: Fogo, Água): ").strip().capitalize()
    

    encontrados = [t for t in treinadores if t['tipo'] == tipo_busca]
    
    if not encontrados:
        print(f"\n Nenhum pokémon do tipo '{tipo_busca}' foi encontrado na guilda.")
    else:
        print(f"\n Duplas encontradas do tipo {tipo_busca}:")
        for t in encontrados:
            print(f"- Mestre: {t['nome']} | Pokémon: {t['pokemon']} | Poder: {t['media']:.1f}")

def menu():
    while True:
        print("\n" + "=" * 50)
        print("  MENU PRINCIPAL - MUNDO POKÉRANK RPG")
        print("=" * 50)
        print("1.  Registrar Nova Dupla de Aventureiros")
        print("2.  Consultar Hall da Fama (Ranking)")
        print("3.  Enviar Dupla para Treinamento (Bônus de Poder)")
        print("4.  Filtrar Duplas por Tipo Elemental")
        print("5.  Descansar na Taverna (Sair do Jogo)")
        
        opcao = input("\nEscolha sua ação na guilda (1 a 5): ").strip()
        
        if opcao == "1":
            cadastrar_treinador()
        elif opcao == "2":
            listar_ranking()
        elif opcao == "3":
            simular_treinamento()
        elif opcao == "4":
            filtrar_por_tipo()
        elif opcao == "5":
            print("\n Salvando progresso da biqueira... Que o pcc nao atrapalhe suas batalhas!")
            break
        else:
            print("\n O que você tá tentando fazer, ein? Escolha uma opção entre 1 e 5.")


if __name__ == "__main__":
    menu()
