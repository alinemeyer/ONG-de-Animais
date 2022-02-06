from MVC.limite.tela_adocao import TelaAdocao
from MVC.entidade.adocao import Adocao

class ControladorAdocoes():
    def __init__(self, controlador_sistema):
        self.__adocoes = []
        self.__tela_adocoes = TelaAdocao
        self.__controlador_sistema = controlador_sistema

    def pega_adocao_por_codigo(self, codigo: int):
        for adocao in self.__adocoes:
            if(adocao.codigo == codigo):
                return adocao
        return None

    def incluir_adocao(self):
        self.__controlador_sistema.controlador_adotantes.lista_adotantes()
        self.__controlador_sistema.controlador_adocoes.lista_adocao()
        dados_adocao = self.__tela_adocoes.pega_dados_adocao()

    def excluir_adocao(self):
        self.lista_adocao()
        codigo_adocao = self.__tela_adocoes.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(int(codigo_adocao))

        if adocao is not None:
            self.__adocoes.remove(adocao)
            self.lista_adocao()
        else:
            self.__tela_adocoes.mostra_mensagem("ATENCAO: Adoção não existente")

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao(), 2: self.altera_adocao(), 3: self.lista_adocao,
                        4: self.excluir_adocao(), 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_adocoes.tela_opcoes()]()
