from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://pagina-web-mv-electromedicina.onrender.com/</loc>
    </url>
</urlset>"""

    
@app.route('/robots.txt')
def robots():
    return Response(
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "Sitemap: https://pagina-web-mv-electromedicina.onrender.com/sitemap.xml\n",
        mimetype="text/plain"
    )

    return Response(contenido, mimetype="application/xml")


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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
