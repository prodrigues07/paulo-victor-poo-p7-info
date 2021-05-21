from classMovimentoFolha import MovimentoFolha
from classTipoMovimento import TipoMovimento
from classColaborador import Colaborador

class FolhaPagamento:

    def __init__(self, mes, totalDescontos, totalProventos, ano):
        self.mes = mes
        self.totalDescontos = totalDescontos
        self.totalProventos = totalProventos
        self.ano = ano
        self.movimentos = []
        self.colaboradores = []

    # QUESTAO 8
    def calcularFolha(self):
        for movimento in self.movimentos:
            if movimento.tipoMovimento == TipoMovimento.P:
                self.totalProventos += movimento.valor
            elif movimento.tipoMovimento == TipoMovimento.D:
                self.totalDescontos += movimento.valor

        totalSalarios = 0
        for colaborador in self.colaboradores:
            totalSalarios += colaborador.salarioAtual

        totalPagamento = (totalSalarios + self.totalProventos) - self.totalDescontos
        print('Total de Salários = {} Total de Proventos = {} Total de Descontos = {} Total a Pagar = {}'.format(totalSalarios, self.totalProventos, self.totalDescontos, totalPagamento))


    def inserirMovimentos(self, mov):
        if type(mov) == MovimentoFolha:
            self.movimentos.append(mov)

    def inserirColaboradores(self, colaborador : Colaborador):
        self.colaboradores.append(colaborador)
