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
aguaComGas = Item('Água com gas', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_com_gas.jpg'))
aguaSaborizada = Item('Água Saborizada', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_saborizada.jpg'))
aguaTonica = Item('Água Tônica', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica.jpg'))
aguaTonicaZero = Item('Água Tônica Zero', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica_zero.jpg'))
coca = Item('Coca Cola', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_cola.jpg'))
cocaZero = Item('Coca Cola Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_zero.jpg'))
pepsi = Item('Pepsi', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'pepsi.jpg'))
pepsiZero = Item('Pepsi Black', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'pepsi_zero.jpg'))
h2o = Item('H2OH', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'h2o.jpg'))
chaLimao = Item('Chá de Limão', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_limao.jpg'))
chaPessego = Item('Chá de Pêssego ', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_pessego.jpg'))
sucoMaracuja = Item('Suco de Maracuja', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'suco_maracuja.jpg'))
sucoPesssego = Item('Suco de Pêssego', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'suco_pessego.jpg'))
redBull = Item('Red Bull', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'red_bull.jpg'))
redBullZero = Item('Red Bull Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'red_bull_zero.jpg'))
monster = Item('Monster', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'monster.jpg'))
neston = Item('neston', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'neston.jpg'))
alpino = Item('Alpino', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'alpino.jpg'))
smoovlatte = Item('Smoovlatte', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'smoovlatte.jpg'))
sprite = Item('Sprite', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'sprite.jpg'))
schweppes = Item('Schweppes', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'schweppes.jpeg'))


lista = [guarana, guaranaZero, coca, cocaZero, pepsi, pepsiZero]
lista2 = [aguaTonica, aguaTonicaZero, agua, aguaComGas, aguaSaborizada, h2o]
lista3 = [chaLimao, chaPessego, sucoMaracuja, sucoPesssego, redBull, redBullZero]
lista4 = [monster, sprite, schweppes, neston, alpino, smoovlatte]

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
    return render_template('djeladera.html', itens=lista, itens2=lista2, itens3 = lista3, itens4 = lista4)

if __name__ == "__main__":
    app.run(debug=True)