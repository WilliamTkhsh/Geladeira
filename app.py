from flask import Flask, render_template

class Item:
    def __init__(self, nome, preco, categoria, tipo):
        self.nome=nome
        self.preco=preco
        self.categoria=categoria
        self.tipo=tipo

app = Flask(__name__)
@app.route('/inicio')
def main():
    coca = Item('Coca-cola', '6,00', 'Refrigerante', 'Lata')
    guarana = Item('Guarana', '6,00', 'Refrigerante', 'Lata')
    suco1 = Item('Suco de Laranja', '10,00', 'Suco', 'Copo 500ml')
    return render_template('djeladera.html')

if __name__ == "__main__":
    app.run(debug=True)