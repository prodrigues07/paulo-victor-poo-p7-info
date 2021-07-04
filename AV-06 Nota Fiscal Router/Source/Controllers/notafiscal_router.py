from flask import Flask
from flask_restplus import Api, Resource
from model.cliente import Cliente
from model.produto import Produto
from model.nota import NotaFiscal
from model.item import ItemNotaFiscal
from Sourcer.Server.instance import Server
from Sourcer.Controllers import objeto_json, response, select_objeto

app, api = Server.app, Server.api

# Clientes Banco de Dados
client1 = Cliente(0, "Paulo Victor", 100, '470.184.360-82', 'pessoa fisica')
client2 = Cliente(1, "Beatriz Vidal", 200, '685.065.380-53', 'pessoa fisica')
client3 = Cliente(2, "Bruno Silveira", 300, '641.036.320-40', 'pessoa fisica')
client4 = Cliente(3, "Eve Castro", 400, '448.659.850-42', 'pessoa fisica')

clientes_db = [client1, client2, client3, client4]

# Produtos Banco de Dados
product1 = Produto(0, 100, 'Arroz 101', 5.5)
product2 = Produto(1, 200, 'Feijao Real', 4.5)
product3 = Produto(2, 300, 'Batata', 6)
product4 = Produto(3, 400, 'Macarrão Tio Jorge', 8)

products_db = [product1, product2, product3]

# Notas Fiscais Banco de Dados
nf1 = NotaFiscal(0, 100, client1)
nf2 = NotaFiscal(1, 200, client2)
nf3 = NotaFiscal(2, 300, client3)
nf4 = NotaFiscal(3, 400, client4)

nf_db = [nf1, nf2, nf3, nf4]

# ItensNotaFiscal Banco de Dados
item1 = ItemNotaFiscal(0, 1, 2, product1)

item2 = ItemNotaFiscal(1, 1, 5, product1)
item3 = ItemNotaFiscal(2, 2, 3, product2)

item4 = ItemNotaFiscal(3, 1, 1, product1)
item5 = ItemNotaFiscal(4, 2, 1, product2)
item6 = ItemNotaFiscal(5, 3, 2, product3)

item7 = ItemNotaFiscal(6, 1, 5, product1)
item8 = ItemNotaFiscal(7, 2, 3, product2)
item9 = ItemNotaFiscal(8, 3, 7, product3)
item10 = ItemNotaFiscal(9, 4, 4, product4)


itens_db = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10]

# Adicionando os produtos
nf1.adicionarItem(item1)

nf2.adicionarItem(item2)
nf2.adicionarItem(item3)

nf3.adicionarItem(item4)
nf3.adicionarItem(item5)
nf3.adicionarItem(item6)

nf4.adicionarItem(item7)
nf4.adicionarItem(item8)
nf4.adicionarItem(item9)
nf4.adicionarItem(item10)


# ROTAS CLIENTES
class Clientes(Api, Resource):
    @api.route('/clients')
    def get(self):
        clientes_json = objeto_json(clientes_db)
        return response, 200, clientes_json, 'Todos os clientes'

    @api.route('/cliente/<int:id_cliente>')
    def get(self, id_cliente):
        try:
            client = select_objeto(clientes_db, id_cliente)
            cliente_json = objeto_json(client)

            return response, 200, cliente_json
        except Exception as e:
            print(e)
            return response, 400, {}, 'ID inválido'

    @api.route('/cliente')
    def post(self):
        try:
            body = request.json

            cliente = Cliente(clientes_db[-1].get_id(), body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
            clientes_db.append(cliente)
            cliente_json = objeto_json(cliente)

            return response, 200, cliente_json
        except Exception as a:
            print(a)
            return response, 400, {}, 'Cliente não criado'

    @api.route('/cliente/<int:id_cliente>')
    def put(self, id_cliente):
        try:
            body = request.json
            cliente = select_objeto(clientes_db, id_cliente)

            cliente.set_nome(body['nome'])
            cliente.set_codigo(body['codigo'])
            cliente.set_cnpjcpf(body['cpf'])

            cliente_json = objeto_json(cliente)
            return response, 200, cliente_json
        except Exception as a:
            print(a)
            return response, 400, {}, 'Cliente não atualizado'

    @api.route('/cliente/<int:id_cliente>')
    def delete(self, id_cliente):
        try:
            cliente = select_objeto(clientes_db, id_cliente)
            clientes_db.remove(cliente)

            return response, 200, 'Cliente deletado'
        except Exception as e:
            print(e)
            return response, 400, {}, 'Cliente não deletado'


# ROTAS ITENS
class Itens(Api, Resource):
    @api.route('/itensnf/<int:id_nota>')
    def get(self, id_nota):
        try:
            itens_nf = select_objeto(nf_db, id_nota).get_itens()
            itens_json = objeto_json(itens_nf)

            return response, 200, itens_json, 'Todos os itens da nota'
        except Exception as a:
            print(a)
            return response, 400, 'itens', {}, 'ID inválido'

    @api.route('/itemnf/<int:id_item>')
    def get(self, id_item):
        try:
            item = select_objeto(itens_db, id_item)
            item_json = objeto_json(item)

            return response, 200, item_json, 'Itens da nota'
        except Exception as a:
            print(a)
            return response, 400, {}, 'ID inválido'

    @api.route('/itemnf')
    def post(self):
        body = request.json
        produto = select_objeto(products_db, body['produto'])
        item = ItemNotaFiscal(itens_db[-1].get_id() + 1, body['sequencial'], body['quantidade'], produto)
        itens_db.append(item)
        item_json = objeto_json(item)
        return response, 200, item_json, 'Item criado'

    @api.route('/itemnf/<int:id_item>')
    def put(self, id_item):
        body = request.json
        item = select_objeto(itens_db, id_item)

        item.set_sequencial(body['sequencial'])
        item.set_quantidade(body['quantidade'])

        item_json = objeto_json(item)
        return response, 200, item_json, 'Item atualizado'

    @api.route('/itemnf/<int:id_item>')
    def delete(self, id_item):
        item = select_objeto(itens_db, id_item)
        itens_db.remove(item)

        item_json = objeto_json(item)
        return response, 200, item_json, 'Item deletado'


# ROTAS NOTAS FISCAIS
class Notas(Api, Resource):
    @api.route('/notasfiscais')
    def get(self):
        notas_json = objeto_json(nf_db)
        return response, 200, notas_json, 'Todos as notas'

    @api.route('/notafiscal/<int:id_nota>')
    def get(self, id_nota):
        try:
            nota = select_objeto(nf_db, id_nota)
            nota_json = objeto_json(nota)
            return response, 200, nota_json, 'Nota selecionada'
        except Exception as a:
            print(a)
            return response, 400, {}, 'ID inválido'

    @api.route('/notafiscal')
    def post(self):
        body = request.json
        cliente = select_objeto(clientes_db, body['cliente'])
        nota = NotaFiscal(nf_db[-1].get_id(), body['codigo'], cliente)
        nf_db.append(nota)
        nota_json = objeto_json(nota)
        return response(201, 'nota', nota_json, 'Nota criada')

    @api.route('/notafiscal/<int:id_nota>')
    def put(self, id_nota):
        try:
            body = request.json
            nota = select_objeto(nf_db, id_nota)
            cliente = select_objeto(clientes_db, body['cliente'])
            nota.set_codigo(body['codigo'])
            nota.setCliente(cliente)
            nota_json = objeto_json(nota)
            return response(200, 'nota', nota_json, 'Nota atualizada')
        except Exception as e:
            print(e)
            return response(400, 'nota', {}, 'Nota não atualizada')

    @api.route('/notafiscal/<int:id_nota>')
    def delete(self, id_nota):
        nota = select_objeto(nf_db, id_nota)
        nf_db.remove(nota)
        nota_json = objeto_json(nota)
        return response, 200, nota_json, 'Nota deletada'

    @api.route('/calculanf/<int:id_nota>')
    def get(self, id_nota):
        try:
            nota = select_objeto(nf_db, id_nota)
            nota.calcularNotaFiscal()

            nota_json = objeto_json(nota)
            return response, 200, nota_json
        except Exception as a:
            print(a)
            return response, 400, {}, 'Nota não calculada'

    @api.route('/imprimenf/<int:id_nota>')
    def get(self, id_nota):
        nota = select_objeto(nf_db, id_nota)
        impressao = nota.imprimirNotaFiscal()
        return response, 200, impressao, 'Nota impressa'


# ROTAS PRODUTOS
class Produtos(Api, Resource):
    @api.route('/produtos')
    def get(self):
        protudos_json = objeto_json(products_db)
        return response, 200, protudos_json, 'Todos os produtos'

    @api.route('/produto/<int:id_produto>')
    def get(self, id_produto):
        try:
            produto = select_objeto(products_db, id_produto)
            produto_json = objeto_json(produto)
            return response(200, 'produto', produto_json, 'Produto selecionado')
        except Exception as e:
            print(e)
            return response(400, 'produto', {}, 'ID inválido')

    @app.route('/produto')
    def post(self):
        body = request.json
        produto = Produto(products_db[-1].get_id() + 1, body['codigo'], body['descricao'], body['valor-unitario'])
        products_db.append(produto)
        produto_json = objeto_json(produto)
        return response(201, 'produto', produto_json, 'Produto criado')

    @app.route('/produto/<int:id_produto>')
    def put(self, id_produto):
        body = request.json
        produto = select_objeto(products_db, id_produto)
        produto.set_codigo(body['codigo'])
        produto.set_descricao(body['descricao'])
        produto.set_valor_unitario(body['valor-unitario'])
        produto_json = objeto_json(produto)
        return response, 200, produto_json, 'Produto atualizado'

    @api.route('/produto/<int:id_produto>')
    def delete(self, id_produto):
        produto = select_objeto(products_db, id_produto)
        products_db.remove(produto)

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto deletado')
