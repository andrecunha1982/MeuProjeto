#Definição inicial dos vetores necessários
cultura = []
formato = []
areas = []
insumo_sementes = []
insumo_fertilizante = []
insumo_corretivo = []
insumo_defensivo = []

#Função do Menu Principal
def menu():
    print("\nBem vindo(a) a FarmTech Solutions - Soluções em Agricultura Digital\n")
    print("Digite a opção desejada:")
    print("1 - Registrar nova cultura e definir de área de plantio")
    print("2 - Consultar registros e verificar insumos Necessários")
    print("3 - Atualizar registro")
    print("4 - Excluir Registro")
    print("5 - Sair")
    opcao_inicial = int(input("\nDigite uma opção: "))
    return opcao_inicial

#Função para registrar cultura, formato e tamanho
def escolher_cultura():
    print("\nEscolha a nova cultura a ser registrada:")
    print("1 - Soja")
    print("2 - Milho")
    opcao_cultura = int(input("\nDigite uma opção: "))
    if opcao_cultura == 1:
        cultura.append("Soja")
        print("\nVamos definir as características da área de plantio. Qual o formato da área?")
        print("1 - Retangular")
        print("2 - Triangular")
        print("3 - Circular")
        opcao_formato = int(input("\nDigite uma opção: "))
        if opcao_formato == 1:
            formato.append("Retangular")
            formato_largura = float(input("\nDefina a largura da área de plantio: "))
            formato_comprimento = float(input("Defina o comprimento da área de plantio: "))
            areas.append (formato_largura * formato_comprimento)
            insumo_sementes.append(((formato_largura * formato_comprimento)/10000) * 60)
            insumo_fertilizante.append(((formato_largura * formato_comprimento)/10000) * 300)
            insumo_corretivo.append(((formato_largura * formato_comprimento)/10000) * 4000)
            insumo_defensivo.append((formato_largura * formato_comprimento)/10000)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")
        elif opcao_formato == 2:
            formato.append("Triangular")
            formato_largura = float(input("\nDefina a largura da área de plantio: "))
            formato_comprimento = float(input("Defina o comprimento máximo da área de plantio: "))
            areas.append ((formato_largura * formato_comprimento)/2)
            insumo_sementes.append(((formato_largura * formato_comprimento)/10000) * 60)
            insumo_fertilizante.append(((formato_largura * formato_comprimento)/10000) * 300)
            insumo_corretivo.append(((formato_largura * formato_comprimento)/10000) * 4000)
            insumo_defensivo.append((formato_largura * formato_comprimento)/10000)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")
        else:
            formato.append("Circular")
            formato_diametro = float(input("\nDefina o diametro da área de plantio: "))
            areas.append((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)
            insumo_sementes.append(((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000)
            insumo_fertilizante.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 300)
            insumo_corretivo.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 4000)
            insumo_defensivo.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 3)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")
    else:
        cultura.append("Milho")
        print("Vamos definir as características da área de plantio. Qual o formato da área?")
        print("1 - Retangular")
        print("2 - Triangular")
        print("3 - Circular")
        opcao_formato = int(input("\nDigite uma opção: "))
        if opcao_formato == 1:
            formato.append("Retangular")
            formato_largura = float(input("\nDefina a largura da área de plantio: "))
            formato_comprimento = float(input("Defina o comprimento da área de plantio: "))
            areas.append (formato_largura * formato_comprimento)
            insumo_sementes.append(((formato_largura * formato_comprimento)/10000) * 60)
            insumo_fertilizante.append(((formato_largura * formato_comprimento)/10000) * 300)
            insumo_corretivo.append(((formato_largura * formato_comprimento)/10000) * 4000)
            insumo_defensivo.append((formato_largura * formato_comprimento)/10000)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")

        elif opcao_formato == 2:
            formato.append("Triangular")
            formato_largura = float(input("\nDefina a largura da área de plantio: "))
            formato_comprimento = float(input("Defina o comprimento máximo da área de plantio: "))
            areas.append ((formato_largura * formato_comprimento)/2)
            insumo_sementes.append(((formato_largura * formato_comprimento)/10000) * 60)
            insumo_fertilizante.append(((formato_largura * formato_comprimento)/10000) * 300)
            insumo_corretivo.append(((formato_largura * formato_comprimento)/10000) * 4000)
            insumo_defensivo.append((formato_largura * formato_comprimento)/10000)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")
        else:
            formato.append("Circular")
            formato_diametro = float(input("\nDefina o diametro da área de plantio: "))
            areas.append((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)
            insumo_sementes.append(((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000)
            insumo_fertilizante.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 300)
            insumo_corretivo.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 4000)
            insumo_defensivo.append((((formato_diametro / 2) * (formato_diametro / 2) * 3.1415)/10000) * 3)
            wait = input("\nRegistro adicionado com sucesso. Pressione enter para continuar.")

#Função para consultar registros de maneira tabular e conferir a posição do registro no vetor
def consulta_insumos():
    dados = [
        ["\nPosição", "Cultura", "Formato", "Area (m2)", "Sementes (Kg)", "Fertilizante (Kg)", "Corretivo (Kg)", "Defensivo (Litros)"],
        ["-" * 7, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20],
        *[[str(i),
           cultura[i],
           formato[i],
           f"{areas[i]:.2f}",
           f"{insumo_sementes[i]:.2f}",
           f"{insumo_fertilizante[i]:.2f}",
           f"{insumo_corretivo[i]:.2f}",
           f"{insumo_defensivo[i]:.2f}"
           ] for i in range(len(cultura))]
    ]
    for linha in dados:
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*linha))

    wait = input("\nConsulta realizada com sucesso. Pressione enter para continuar.")

#Função para excluir o registro desejado
def excluir_registro():
    dados = [
        ["\nPosição", "Cultura", "Formato", "Area (m2)", "Sementes (Kg)", "Fertilizante (Kg)", "Corretivo (Kg)",
         "Defensivo (Litros)"],
        ["-" * 7, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20],
        *[[str(i),
           cultura[i],
           formato[i],
           f"{areas[i]:.2f}",
           f"{insumo_sementes[i]:.2f}",
           f"{insumo_fertilizante[i]:.2f}",
           f"{insumo_corretivo[i]:.2f}",
           f"{insumo_defensivo[i]:.2f}"
           ] for i in range(len(cultura))]
    ]
    for linha in dados:
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*linha))

    posicao = int(input("\nDigite a posição que deseja excluir: "))
    if posicao < 0 or posicao >= len(cultura):
        print("Posição inválida. Nenhum dado foi excluído.")
        return
    cultura.pop(posicao)
    formato.pop(posicao)
    areas.pop(posicao)
    insumo_sementes.pop(posicao)
    insumo_fertilizante.pop(posicao)
    insumo_corretivo.pop(posicao)
    insumo_defensivo.pop(posicao)
    wait = input("Registro excluído com sucesso. Pressione enter para continuar.")

#Função para atualizar o registro desejado
def atualizar_dados():
    dados = [
        ["\nPosição", "Cultura", "Formato", "Area (m2)", "Sementes (Kg)", "Fertilizante (Kg)", "Corretivo (Kg)",
         "Defensivo (Litros)"],
        ["-" * 7, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20],
        *[[str(i),
           cultura[i],
           formato[i],
           f"{areas[i]:.2f}",
           f"{insumo_sementes[i]:.2f}",
           f"{insumo_fertilizante[i]:.2f}",
           f"{insumo_corretivo[i]:.2f}",
           f"{insumo_defensivo[i]:.2f}"
           ] for i in range(len(cultura))]
    ]
    for linha in dados:
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*linha))

    #Escolher posição a ser atualizada
    posicao = int(input("\nDigite a posição do registro que deseja atualizar: "))

    #Verificar se a posição selecionada é valida
    if posicao < 0 or posicao >= len(cultura):
        print("Posição inválida. Verifique se a posição está correta.")
        return

    #Sendo válida, atualiza a cultura
    print("Selecione a nova cultura:")
    print("1 - Soja")
    print("2 - Milho")
    nova_cultura = int(input("Digite a opção desejada: "))
    if nova_cultura == 1:
        cultura[posicao] = "Soja"
    else:
        cultura[posicao] = "Milho"

    #Depois atualiza o formato da area de plantio
    print("\nSelecione o novo formato: ")
    print("1 - Retangular")
    print("2 - Triangular")
    print("3 - Circular")
    novo_formato = int(input("Digite a opção desejada: "))

    #Confirmações de metragens e ajusta os valores de area
    if novo_formato == 1:
        formato[posicao] = "Retangular"
        nova_largura = float(input("Digite a nova largura da área de plantio: "))
        novo_comprimento = float(input("Digite o novo comprimento da área de plantio: "))
        nova_area = round(nova_largura * novo_comprimento, 2)
    elif novo_formato == 2:
        formato[posicao] = "Triangular"
        nova_largura = float(input("Digite a nova largura da área de plantio: "))
        novo_comprimento = float(input("Digite o novo comprimento máximo da área de plantio: "))
        nova_area = round((nova_largura * novo_comprimento)/2, 2)
    else:
        formato[posicao] = "Circular"
        novo_diametro = float(input("Digite o novo diâmetro da área de plantio: "))
        nova_area = round((novo_diametro / 2) * (novo_diametro / 2) * 3.1415, 2)
    areas[posicao] = nova_area

    #Com a confirmação da nova área, atualiza os valores dos insumos
    if nova_cultura == 1:
        insumo_sementes[posicao] = round((nova_area / 10000) * 60, 2)
        insumo_fertilizante[posicao] = round((nova_area / 10000) * 300, 2)
        insumo_corretivo[posicao] = round((nova_area / 10000) * 4000, 2)
        insumo_defensivo[posicao] = round((nova_area / 10000) * 3, 2)
    else:
        insumo_sementes[posicao] = round((nova_area / 10000) * 20, 2)
        insumo_fertilizante[posicao] = round((nova_area / 10000) * 600, 2)
        insumo_corretivo[posicao] = round((nova_area / 10000) * 4000, 2)
        insumo_defensivo[posicao] = round((nova_area / 10000) * 3, 2)

    wait = input("Dados atualizados com sucesso! Pressione enter para continuar.")

#Menu Principal
while True:
    opcao_inicial = menu()

    if opcao_inicial == 1:
        escolher_cultura()
    elif opcao_inicial == 2:
        consulta_insumos()
    elif opcao_inicial == 3:
        atualizar_dados()
    elif opcao_inicial == 4:
        excluir_registro()
    elif opcao_inicial == 5:
        print("Obrigado por utilizar as soluções da FarmTech Solutions!")
        break
    else:
        print("Opção inválida. Tente novamente.")