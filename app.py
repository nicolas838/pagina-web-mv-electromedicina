from flask import Flask, render_template, request, Response
import os

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/sitemap.xml")
def sitemap():
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://pagina-web-mv-electromedicina.onrender.com/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""

    return Response(contenido, content_type="application/xml")


@app.route("/solicitud", methods=["GET", "POST"])
def solicitud():

    if request.method == "POST":

        cliente = request.form.get("cliente", "")
        empresa = request.form.get("empresa", "")
        correo = request.form.get("correo", "")
        telefono = request.form.get("telefono", "")
        equipo = request.form.get("equipo", "")
        marca = request.form.get("marca", "")
        serie = request.form.get("serie", "")
        falla = request.form.get("falla", "")
        prioridad = request.form.get("prioridad", "")

        print("===== NUEVA SOLICITUD =====")
        print("Cliente:", cliente)
        print("Empresa:", empresa)
        print("Correo:", correo)
        print("Teléfono:", telefono)
        print("Equipo:", equipo)
        print("Marca:", marca)
        print("Serie:", serie)
        print("Prioridad:", prioridad)
        print("Falla:", falla)

    return render_template("solicitud.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False), 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
