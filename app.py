from flask import Flask, render_template, request, redirect
import os

class Item:
    def __init__(self, nome, preco, rota):
        self.nome=nome
        self.preco=preco
        self.rota=rota

app = Flask(__name__)

imgFolder = os.path.join('static', 'sources')
app.config['UPLOAD_FOLDER'] = imgFolder

guarana = Item('Guaraná', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'guarana.jpg'))
guaranaZero = Item('Guaraná Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'guarana_zero.jpg'))
agua = Item('Água', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua.jpg'))
aguaTonica = Item('Água Tônica', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica.jpg'))
aguaTonicaZero = Item('Água Tônica Zero', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica_zero.jpg'))
coca = Item('Coca Cola', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_cola.jpg'))
cocaZero = Item('Coca Cola Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_zero.jpg'))
h2o = Item('H2OH', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'h2o.jpg'))
chaLimao = Item('Chá de Limão ', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_limao.jpg'))
chaPessego = Item('Chá de Pêssego ', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_pessego.jpg'))

lista = [guarana, guaranaZero, coca, cocaZero, agua, aguaTonica, aguaTonicaZero, h2o]
lista2 = [chaLimao, chaPessego]


@app.route('/novo_item')
def new():
    return render_template('novo-item.html', titulo='Novo Item')

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    preco = request.form['preco']
    rota = request.form['rota']
    item = Item(nome, preco, rota)
    list.append(item)
    return redirect('/')

@app.route('/')
def main():
    return render_template('djeladera.html', itens=lista, itens2=lista2)

if __name__ == "__main__":
    app.run(debug=True)