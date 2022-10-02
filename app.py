from flask import Flask, render_template, request, redirect
import os

class Item:
    def __init__(self, nome, preco, rota, id):
        self.nome=nome
        self.preco=preco
        self.rota=rota
        self.id=id

app = Flask(__name__)

imgFolder = os.path.join('static', 'sources')
app.config['UPLOAD_FOLDER'] = imgFolder

guarana = Item('Guaraná', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'guarana.jpg'),1)
guaranaZero = Item('Guaraná Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'guarana_zero.jpg'),2)
agua = Item('Água', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua.jpg'),9)
aguaComGas = Item('Água com gas', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_com_gas.jpg'),10)
aguaSaborizada = Item('Água Saborizada', '4,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_saborizada.jpg'),11)
aguaTonica = Item('Água Tônica', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica.jpg'),7)
aguaTonicaZero = Item('Água Tônica Zero', '5,00', os.path.join(app.config['UPLOAD_FOLDER'], 'agua_tonica_zero.jpg'),8)
coca = Item('Coca Cola', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_cola.jpg'),3)
cocaZero = Item('Coca Cola Zero', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'coca_zero.jpg'),4)
pepsi = Item('Pepsi', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'pepsi.jpg'),5)
pepsiZero = Item('Pepsi Black', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'pepsi_zero.jpg'),6)
h2o = Item('H2OH', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'h2o.jpg'),12)
chaLimao = Item('Chá de Limão', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_limao.jpg'),13)
chaPessego = Item('Chá de Pêssego ', '8,00', os.path.join(app.config['UPLOAD_FOLDER'], 'cha_pessego.jpg'),14)
sucoMaracuja = Item('Suco de Maracuja', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'suco_maracuja.jpg'),15)
sucoPesssego = Item('Suco de Pêssego', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'suco_pessego.jpg'),16)
redBull = Item('Red Bull', '10,00', os.path.join(app.config['UPLOAD_FOLDER'], 'red_bull.jpg'),17)
redBullZero = Item('Red Bull Zero', '10,00', os.path.join(app.config['UPLOAD_FOLDER'], 'red_bull_zero.jpg'),18)
monster = Item('Monster', '10,00', os.path.join(app.config['UPLOAD_FOLDER'], 'monster.jpg'),19)
neston = Item('neston', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'neston.jpg'),22)
alpino = Item('Alpino', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'alpino.jpg'),23)
smoovlatte = Item('Smoovlatte', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'smoovlatte.jpg'),24)
sprite = Item('Sprite', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'sprite.jpg'),20)
schweppes = Item('Schweppes', '6,00', os.path.join(app.config['UPLOAD_FOLDER'], 'schweppes.jpeg'),21)


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