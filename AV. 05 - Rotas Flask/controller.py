from flask import Flask, flash, render_template, url_for, redirect, request

from cliente import Cliente

c1 = Cliente(1, 'Paulo Victor', 101, '123-456-789-10', 'pessoa fisica')
c2 = Cliente(2, 'Ricardo Taveira', 102, '109-876-543-21', 'pessoa fisica')
c3 = Cliente(3, 'Pablo Silva', 103, '567-891-012-34', 'pessoa fisica')

clientes = [c1, c2, c3]
id_c = 4
codigo_c = 104

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['DEBUG'] = True


@app.route('/')
def index():
    return "<h1>Bem Vindo Cliente!</h1><br><ul>"


@app.route('/create', methods=['GET', 'POST'])
def create():
    global id_c
    global codigo_c
    if request.method == 'POST':
        if not request.form['cliente'] or not request.form['cpf']:
            flash('Favor entrar todos os valores dos campos', 'error')
        else:
            cliente = Cliente(id_c, request.form['cliente'], codigo_c, request.form['cpf'], 'pessoa fisica')
            clientes.append(cliente)
            id_c += 1
            codigo_c += 1
            return redirect(url_for('show_clientes'))
    return render_template('create.html')


@app.route('/read/<int:id_cliente>')
@app.route('/read', defaults={'id_cliente': None})
def read(id_cliente):
    result = "<h1>Consulta a Clientes</h1><br><ul>"
    cliente = None
    if id_cliente:
        try:
            for c in clientes:
                if c.id == id_cliente:
                    cliente = c
            result += "<p> Id=" + str(cliente.id) + "</p>"
            result += "<p> Nome=" + cliente.nome + "</p>"
            result += "<p> CPF=" + cliente.cnpjcpf + "</p>"
        except Exception as e:
            print(e)
            result += f'<p>Erro -> Por favor Digite um ID Válido!</p>'
    else:
        result += f'<p>Digite um ID válido na url</p>'
    return result


@app.route('/update', methods=['GET', 'POST'])
def update():
    cliente = None
    if request.method == 'POST':
        if not request.form['cliente'] or not request.form['cpf'] or not request.form['id']:
            flash('Favor entrar todos os valores dos campos', 'error')
        else:
            try:
                id_cliente = int(request.form['id'])
                for c in clientes:
                    if c.id == id_cliente:
                        cliente = c
                cliente.nome = request.form['cliente']
                cliente.cnpjcpf = request.form['cpf']
                return redirect(url_for('show_clientes'))
            except Exception as e:
                flash(f'Favor entrar com um ID válido', 'error')
    return render_template('update.html')


@app.route('/delete/<int:id_cliente>')
@app.route('/delete', defaults={'id_cliente': None})
def delete(id_cliente):
    result = "<h1>Exclusão de Cliente</h1><br><ul>"
    cliente = None
    if id_cliente:
        try:
            for c in clientes:
                if c.id == id_cliente:
                    cliente = c
            clientes.remove(cliente)
            result += f'<p>Usuário -> Id= {str(cliente.id)} | Nome= {str(cliente.nome)}, Excluido!</p>'
        except Exception as e:
            print(e)
            result += f'<p>Erro -> Por favor Digite um ID Válido!</p>'
    else:
        result += f'<p>Digite um ID válido na url</p>'
    return result


@app.route('/all')
def show_clientes():
    result = '<h1>Clientes</h1><br><ul>'
    for cliente in clientes:
        result += '<p>'
        result += 'Id=' + str(cliente.id)
        result += ' Nome=' + cliente.nome
        result += ' CPF=' + cliente.cnpjcpf
        result += '</p>'
    return result


if __name__ == '__main__':
    app.run()
