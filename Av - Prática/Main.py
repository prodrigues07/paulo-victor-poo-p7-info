from classFolhaPagamento import FolhaPagamento
from classMovimentoFolha import MovimentoFolha
from classColaborador import Colaborador
from classTipoMovimento import TipoMovimento

class Main:
    def main():
        # QUESTÃO 1
        FP = FolhaPagamento(9, 0, 0, 2019)

        # QUESTÃO 2
        CL01 = Colaborador(100, "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060" , "124543556-89", 4500.00)
        CL02 = Colaborador(200, "Carmelina da Silva", "Avenida dos Expedicionários 1200", "30351280", "Aeroporto", "60530-020" , "301789435-54", 2500.00)
        CL03 = Colaborador(300, "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "32351089", "Damas", "60330-090", "350245632-76", 3000.00)

        # QUESTÃO 3
        MF01 = MovimentoFolha(CL01, 'Gratificacao', 4500.00, TipoMovimento.P)
        MF02 = MovimentoFolha(CL01, 'Plano Saúde', 1000.00, TipoMovimento.P)
        MF03 = MovimentoFolha(CL01, 'Pensão', 600.00, TipoMovimento.D)
        MF04 = MovimentoFolha(CL02, 'Gratificacao', 2500.00, TipoMovimento.P)
        MF05 = MovimentoFolha(CL02, 'Plano Saúde', 1000.00, TipoMovimento.P)
        MF06 = MovimentoFolha(CL02, 'Faltas', 600.00, TipoMovimento.D)
        MF07 = MovimentoFolha(CL03, 'Gratificacao', 4500.00, TipoMovimento.P)
        MF08 = MovimentoFolha(CL03, 'Plano Saúde', 1000.00, TipoMovimento.P)
        MF09 = MovimentoFolha(CL03, 'Pensão', 600.00, TipoMovimento.D)

        # QUESTÃO 6
        FP.inserirMovimentos(MF01)
        FP.inserirMovimentos(MF02)
        FP.inserirMovimentos(MF03)
        FP.inserirMovimentos(MF04)
        FP.inserirMovimentos(MF05)
        FP.inserirMovimentos(MF06)
        FP.inserirMovimentos(MF07)
        FP.inserirMovimentos(MF08)
        FP.inserirMovimentos(MF09)

        # QUESTÃO 7
        CL01.inserirMovimentosColab(MF01)
        CL01.inserirMovimentosColab(MF02)
        CL01.inserirMovimentosColab(MF03)
        CL02.inserirMovimentosColab(MF04)
        CL02.inserirMovimentosColab(MF05)
        CL02.inserirMovimentosColab(MF06)
        CL03.inserirMovimentosColab(MF07)
        CL03.inserirMovimentosColab(MF08)
        CL03.inserirMovimentosColab(MF09)

        FP.inserirColaboradores(CL01)
        FP.inserirColaboradores(CL02)
        FP.inserirColaboradores(CL03)

        FP.calcularFolha()
        CL01.calcularSalario()
        CL02.calcularSalario()
        CL03.calcularSalario()

if __name__ == '__main__':
    Main.main()