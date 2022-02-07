class TelaVoluntario:
    def tela_opcoes(self):
        print("-------- VOLUNTARIO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Voluntario")
        print("2 - Alterar Voluntario")
        print("3 - Listar Voluntario")
        print("4 - Excluir Voluntario")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_voluntario():
        print("-------- DADOS VOLUNTARIO ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        telefone = input("Telefone: ")
        genero = input("Genero: ")
        email = input("E-mail: ")
        endereco = input("Endereco: ")
        oferece_lt = input("Oferece lar temporario: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "telefone": telefone, "genero": genero,
                "email": email, "endereco": endereco, "oferece_lt": oferece_lt}

    def mostra_voluntario(self, dados_voluntario):
        print("NOME DO VOLUNTARIO: ", dados_voluntario["nome"])
        print("DATA NASCIMENTO DO VOLUNTARIO: ", dados_voluntario["data_nascimento"])
        print("TELEFONE DO VOLUNTARIO: ", dados_voluntario["telefone"])
        print("GENERO DO VOLUNTARIO: ", dados_voluntario["genero"])
        print("E-MAIL DO VOLUNTARIO: ", dados_voluntario["email"])
        print("ENDERECO DO VOLUNTARIO: ", dados_voluntario["endereco"])
        print("OFERECE LAR TEMPORARIO: ", dados_voluntario["oferece_lt"])
        print("\n")

    def seleciona_voluntario(self):
        telefone_voluntario = input("Telefone do voluntario que deseja selecionar: ")
        return telefone_voluntario

    def mostra_mensagem(self, msg):
        print(msg)
