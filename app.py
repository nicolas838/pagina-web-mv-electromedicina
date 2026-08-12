from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/solicitud', methods=['GET', 'POST'])
def solicitud():

    if request.method == 'POST':

        cliente = request.form['cliente']
        empresa = request.form['empresa']
        correo = request.form['correo']
        telefono = request.form['telefono']
        equipo = request.form['equipo']
        marca = request.form['marca']
        serie = request.form['serie']
        falla = request.form['falla']
        prioridad = request.form['prioridad']

        print("===== NUEVA SOLICITUD =====")
        print("Cliente:", cliente)
        print("Empresa:", empresa)
        print("Equipo:", equipo)
        print("Marca:", marca)
        print("Serie:", serie)
        print("Prioridad:", prioridad)
        print("Falla:", falla)

    return render_template("solicitud.html")


if __name__ == "__main__":
    app.run(debug=True)