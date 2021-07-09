from app import app, db
import json
from flask import Response, request
from tabelas import Cliente, Produto, Item, NotaFiscal


def resposta(status, nome, conteudo, mensagem="", nome_secundario='', conteudo_secundario=None):
    corpo = {nome: conteudo}

    if mensagem:
        corpo["mensagem"] = mensagem
    if conteudo_secundario:
        corpo[nome_secundario] = conteudo_secundario

    return Response(json.dumps(corpo), status=status, mimetype="api/json")


"""
===================== ROTAS DOS CLIENTES =====================
"""


# MOSTRAR TODOS OS CLIENTES
@app.route('/clientes', methods=["GET"])
def todos_clientes():
    clientes_objetos = Cliente.query.all()
    clientes_json = [cliente.to_json() for cliente in clientes_objetos]
    return resposta(200, 'Clientes', clientes_json, 'Mostrando todos os clientes')


# MOSTRAR UM CLIENTE
@app.route('/cliente/<cliente_id>', methods=["GET"])
def um_cliente(cliente_id):
    cliente = Cliente.query.filter_by(id=cliente_id).first()
    cliente_json = cliente.to_json()
    return resposta(200, 'Cliente', cliente_json, f'Mostrando cliente {cliente_id}')


# CRIAR UM CLIENTE
@app.route('/cliente', methods=['POST'])
def criar_cliente():
    body = request.get_json()

    try:
        cliente = Cliente(body["nome"], body["codigo"], body["cnpjcpf"], body["tipo"])
        db.session.add(cliente)
        db.session.commit()
        return resposta(201, 'Cliente', cliente.to_json(), 'Cliente cadastrado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Cliente', {}, 'Erro ao cadastrar')


# ATUALIZAR UM CLIENTE
@app.route('/cliente/<cliente_id>', methods=['PUT'])
def att_cliente(cliente_id):
    cliente = Cliente.query.filter_by(id=cliente_id).first()
    cliente_antigo = cliente
    dados_antigos = cliente_antigo.to_json()
    body = request.get_json()

    try:
        if "nome" in body:
            cliente.nome = body['nome']
        if "codigo" in body:
            cliente.codigo = body['codigo']
        if "cnpjcpf" in body:
            cliente.cnpjcpf = body['cnpjcpf']
        if "tipo" in body:
            cliente.tipo = body['tipo']
        db.session.add(cliente)
        db.session.commit()
        return resposta(200, "Cliente", cliente.to_json(), f"Cliente {cliente_id} atualizado com sucesso",
                        "Dados antigos", dados_antigos)
    except Exception as e:
        print('Erro', e)
        return resposta(400, "Cliente", {}, "Erro ao atualizar cliente")


# DELETAR CLIENTE
@app.route('/cliente/<cliente_id>', methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente = Cliente.query.filter_by(id=cliente_id).first()

    try:
        db.session.delete(cliente)
        db.session.commit()
        return resposta(200, 'Cliente', cliente.to_json(), f'Cliente {cliente_id} deletado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Cliente', {}, 'Erro ao deletar cliente')


"""
===================== ROTAS DOS PRODUTOS =====================
"""


# MOSTRAR TODOS OS PRODUTOS
@app.route('/produtos', methods=["GET"])
def todos_produtos():
    produtos_objetos = Produto.query.all()
    produtos_json = [produto.to_json() for produto in produtos_objetos]
    return resposta(200, 'Produtos', produtos_json, 'Mostrando todos os produtos')


# MOSTRAR UM PRODUTO
@app.route('/produto/<produto_id>', methods=["GET"])
def um_produto(produto_id):
    produto = Produto.query.filter_by(id=produto_id).first()
    produto_json = produto.to_json()
    return resposta(200, 'Produto', produto_json, f'Mostrando produto {produto_id}')


# CRIAR UM PRODUTO
@app.route('/produto', methods=['POST'])
def criar_produto():
    body = request.get_json()

    try:
        produto = Produto(body["codigo"], body["descricao"], body["valor"])
        db.session.add(produto)
        db.session.commit()
        return resposta(201, 'Produto', produto.to_json(), 'Produto cadastrado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Produto', {}, 'Erro ao cadastrar')


# ATUALIZAR UM PRODUTO
@app.route('/produto/<produto_id>', methods=['PUT'])
def att_produto(produto_id):
    produto = Produto.query.filter_by(id=produto_id).first()
    produto_antigo = produto
    dados_antigos = produto_antigo.to_json()
    body = request.get_json()

    try:
        if "codigo" in body:
            produto.codigo = body['codigo']
        if "cnpjcpf" in body:
            produto.descricao = body['descricao']
        if "valor" in body:
            produto.valor_unitario = body['valor']
        db.session.add(produto)
        db.session.commit()
        return resposta(200, "Produto", produto.to_json(), f"Produto {produto_id} atualizado com sucesso",
                        "Dados antigos", dados_antigos)
    except Exception as e:
        print('Erro', e)
        return resposta(400, "Produto", {}, "Erro ao atualizar produto")


# DELETAR PRODUTO
@app.route('/produto/<produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    produto = Produto.query.filter_by(id=produto_id).first()

    try:
        db.session.delete(produto)
        db.session.commit()
        return resposta(200, 'Produto', produto.to_json(), f'Produto {produto_id} deletado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Produto', {}, 'Erro ao deletar produto')


"""
===================== ROTAS DOS ITENS =====================
"""


# MOSTRAR TODOS OS ITENS
@app.route('/itens', methods=["GET"])
def todos_itens():
    itens_objetos = Item.query.all()
    itens_json = [item.to_json() for item in itens_objetos]
    return resposta(200, 'Item', itens_json, 'Mostrando todos os itens')


# MOSTRAR UM ITEM
@app.route('/item/<item_id>', methods=["GET"])
def um_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    item_json = item.to_json()
    return resposta(200, 'Item', item_json, f'Mostrando item {item_id}')


# CRIAR UM ITEM
@app.route('/item', methods=['POST'])
def criar_item():
    body = request.get_json()

    try:
        item = Item(body["sequencial"], body["quantidade"], body["produto_id"], body["nota_id"])
        db.session.add(item)
        db.session.commit()
        return resposta(201, 'Item', item.to_json(), 'Item cadastrado com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Item', {}, 'Erro ao cadastrar')


# ATUALIZAR UM ITEM
@app.route('/item/<item_id>', methods=['PUT'])
def att_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    item_antigo = item
    dados_antigos = item_antigo.to_json()
    body = request.get_json()

    try:
        if "sequencial" in body:
            item.sequencial = body['sequencial']
        if "quantidade" in body:
            item.quantidade = body['quantidade']
        if "produto_id" in body:
            item.produto_id = body['produto_id']
        if "nota_id" in body:
            item.nota_id = body['nota_id']
        db.session.add(item)
        db.session.commit()
        return resposta(200, "Item", item.to_json(), f"Item {item_id} atualizado com sucesso",
                        "Dados antigos", dados_antigos)
    except Exception as e:
        print('Erro', e)
        return resposta(400, "Item", {}, "Erro ao atualizar item")


# DELETAR ITEM
@app.route('/item/<item_id>', methods=['DELETE'])
def deletar_item(item_id):
    item = Item.query.filter_by(id=item_id).first()

    try:
        db.session.delete(item)
        db.session.commit()
        return resposta(200, 'Item', item.to_json(), f'Item {item_id} deletada com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Item', {}, 'Erro ao deletar item')


"""
===================== ROTAS DAS NOTAS =====================
"""


# MOSTRAR TODAS AS NOTAS
@app.route('/notas', methods=['GET'])
def todas_notas():
    notas_objetos = NotaFiscal.query.all()
    notas_json = [nota.para_json() for nota in notas_objetos]
    return resposta(200, 'Nota', notas_json, 'Mostrando todas as notas')


# MOSTRAR UMA NOTA
@app.route('/nota/<nota_id>', methods=["GET"])
def uma_nota(nota_id):
    nota = NotaFiscal.query.filter_by(id=nota_id).first()
    nota_json = nota.para_json()
    return resposta(200, 'Nota', nota_json, f'Mostrando nota fiscal {nota_id}')


# CRIAR UMA NOTA
@app.route('/nota', methods=['POST'])
def criar_nota():
    body = request.get_json()

    try:
        nota = NotaFiscal(body["codigo"], body["cliente"])
        db.session.add(nota)
        db.session.commit()
        return resposta(201, 'Nota', nota.para_json(), 'Nota Fiscal cadastrada com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Nota', {}, 'Erro ao cadastrar')


# ATUALIZAR UMA NOTA
@app.route('/nota/<nota_id>', methods=['PUT'])
def att_nota(nota_id):
    nota = NotaFiscal.query.filter_by(id=nota_id).first()
    nota_antiga = nota
    dados_antigos = nota_antiga.para_json()
    body = request.get_json()

    try:
        if "codigo" in body:
            nota.codigo = body['codigo']
        if "cliente" in body:
            nota.cliente_id = body['cliente']
        db.session.add(nota)
        db.session.commit()
        return resposta(200, "Nota", nota.para_json(), f"Nota Fiscal {nota_id} atualizada com sucesso",
                        "Dados antigos", dados_antigos)
    except Exception as e:
        print('Erro', e)
        return resposta(400, "Nota", {}, "Erro ao atualizar nota fiscal")


# DELETAR NOTA
@app.route('/nota/<nota_id>', methods=['DELETE'])
def deletar_nota(nota_id):
    nota = NotaFiscal.query.filter_by(id=nota_id).first()

    try:
        db.session.delete(nota)
        db.session.commit()
        return resposta(200, 'Nota', nota.para_json(), f'Nota Fiscal {nota_id} deletada com sucesso')
    except Exception as e:
        print('Erro', e)
        return resposta(400, 'Nota', {}, 'Erro ao deletar nota')
