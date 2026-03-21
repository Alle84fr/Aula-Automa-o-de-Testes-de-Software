class ProcessadorDeAcoes:
    def validar_dados(self, dados: dict) -> bool:
        return True

    def salvar_dados(self, dados: dict) -> bool:
        return True

    def executar_processo(self, dados: dict) -> str:
        if self.validar_dados(dados):
            if self.salvar_dados(dados):
                return "Processo concluído com sucesso"
        return "Falha no processo"
