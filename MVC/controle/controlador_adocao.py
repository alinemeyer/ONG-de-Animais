from MVC.limite.tela_adocao import TelaAdocao
from MVC.entidade.adocao import Adocao


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()

    def pega_adocao_por_codigo(self, codigo: str):
        for adocao in self.__adocoes:
            if adocao.codigo == codigo:
                return adocao
        return None

    def incluir_adocao(self):
        dados_adocao = self.__tela_adocao.pega_dados_adocao()
        adocao = Adocao(dados_adocao["adotante"], dados_adocao["animal"], dados_adocao["data"], dados_adocao["codigo"])
        self.__adocoes.append(adocao)

    def altera_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        if adocao is not None:
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
            adocao.adotante = novos_dados_adocao["adotante"]
            adocao.animal = novos_dados_adocao["animal"]
            adocao.data = novos_dados_adocao["data"]
            adocao.codigo = novos_dados_adocao["codigo"]
            self.lista_adocao()
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: Adoção não existente")

    def lista_adocao(self):
        for adocao in self.__adocoes:
            self.__tela_adocao.mostra_adocao({"adotante": adocao.adotante, "animal": adocao.animal, "data": adocao.data, "codigo": adocao.codigo})

    def excluir_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(codigo_adocao)

        if adocao is not None:
            self.__adocoes.remove(adocao)
            self.lista_adocao()
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: Adoção não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao, 2: self.altera_adocao, 3: self.lista_adocao, 4: self.excluir_adocao, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()

