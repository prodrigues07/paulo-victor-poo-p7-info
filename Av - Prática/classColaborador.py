from classMovimentoFolha import MovimentoFolha
from classTipoMovimento import TipoMovimento


class Colaborador:

    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioAtual):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.bairro = bairro
        self.cep = cep
        self.cpf = cpf
        self.salarioAtual = salarioAtual
        self.movimentos = []

    # QUESTAO 9
    def calcularSalario(self):
        totalProventos = 0.0
        totalDescontos = 0.0

        for movimento in self.movimentos:
            if movimento.tipoMovimento == TipoMovimento.P:
                totalProventos += movimento.valor
            elif movimento.tipoMovimento == TipoMovimento.D:
                totalDescontos += movimento.valor

        valorLiquido = (self.salarioAtual + totalProventos) - totalDescontos

        print('Codigo: {} Nome: {}\nSalário: {} Total Proventos: {} Total Descontos: {} Valor Liquido a Receber: {}'.format(
            self.codigo, self.nome, self.salarioAtual, totalProventos, totalDescontos, valorLiquido))

    def inserirMovimentosColab(self, mov):
        if type(mov) == MovimentoFolha:
            self.movimentos.append(mov)
