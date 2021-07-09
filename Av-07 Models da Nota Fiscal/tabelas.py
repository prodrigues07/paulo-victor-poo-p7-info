from app import db
import datetime


class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    codigo = db.Column(db.Integer)
    cnpjcpf = db.Column(db.String(20))
    tipo = db.Column(db.String(20))

    def __init__(self, nome, codigo, cnpjcpf, tipo):
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "codigo": self.codigo,
            "cnpjcpf": self.cnpjcpf,
            "tipo": self.tipo
        }


class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.String(20))
    valor_unitario = db.Column(db.Float(20))

    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor

    def to_json(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "descricao": self.descricao,
            "valor_unitario": self.valor_unitario
        }


class Item(db.Model):
    __tablename__ = "itens"
    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)

    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    produto = db.relationship('Produto', foreign_keys=produto_id, lazy='subquery')

    nota_id = db.Column(db.Integer, db.ForeignKey('notas.id'))
    nota = db.relationship('NotaFiscal', foreign_keys=nota_id)

    def __init__(self, sequencial, quantidade, produto_id, nota_id):
        self.sequencial = sequencial
        self.quantidade = quantidade
        self.produto_id = produto_id
        self.nota_id = nota_id

    def get_valor(self):
        valor = self.produto.valor_unitario * self.quantidade
        return float(valor)

    def get_produto(self):
        return str(self.produto.descricao)

    def get_quantidade(self):
        return self.quantidade

    def get_preco(self):
        return self.produto.valor_unitario

    def to_json(self):
        print()
        valor = self.produto.valor_unitario * self.quantidade
        product = Produto.query.filter_by(id=self.produto_id).first()
        note = NotaFiscal.query.filter_by(id=self.nota_id).first()
        return{
            "id": self.id,
            "sequencial": self.sequencial,
            "quantidade": self.quantidade,
            "produto": product.to_json(),
            "nota": [f'Cliente: {note.para_json()["cliente"]}', f'Valor total: {note.para_json()["valor-total"]}'],
            "valor": valor
        }


class NotaFiscal(db.Model):
    __tablename__ = "notas"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    cliente = db.relationship('Cliente', foreign_keys=cliente_id)

    data = datetime.datetime.now()

    def __init__(self, codigo, cliente_id):
        self.codigo = codigo
        self.cliente_id = cliente_id

    def para_json(self):
        client = Cliente.query.filter_by(id=self.cliente_id).first()
        cliente_json = client.to_json()

        itens_objetos = Item.query.filter_by(nota_id=self.id).all()
        total = 0
        x = 0
        itens = {}
        for item in itens_objetos:
            total += item.get_valor()
            itens[x] = [f'Quantidade: {item.get_quantidade()}', f'Descricao: {item.get_produto()}',
                        f'Valor unitario: {item.get_preco()}']
            x += 1

        return {
            "id": self.id,
            "codigo": self.codigo,
            "cliente": cliente_json["nome"],
            "itens": itens,
            "valor-total": f'{total} reais'
        }
