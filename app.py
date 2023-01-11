from flask import Flask, redirect, url_for
from flask.templating import render_template, request
import modelos.programa as programaModel
import modelos.conductor as conductor_model
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['nombre']
        nacional = request.form['nacional']
        categoria = request.form['categoria']
        conductor = request.form['conductor']
        descripcion = request.form['descripcion']
        newPrograma = programaModel.Programa(0, name, descripcion, nacional, categoria)
        newPrograma.registrar()
        return redirect(url_for('index'))
    conductores = conductor_model.obtener_conductores()
    categorias = programaModel.obtenerCategorias()
    return render_template("index2.html", conductores = conductores, categorias = categorias)


@app.route('/programas/')
def programas(tipo=0):
    lista = programaModel.listarProgramas()
    categorias = programaModel.obtenerCategorias()
    return render_template("blog-grid.html", programas=lista, categorias = categorias)

@app.route('/programas/<int:tipo>')
def programaTipo(tipo=0):
    print("cateogira: ", tipo)
    lista = programaModel.listar_programs_categoria(tipo)
    categorias = programaModel.obtenerCategorias()
    return render_template("blog-grid.html", programas = lista, categorias = categorias)


@app.route('/programasConductor')
def programas_conductor():
    lista = conductor_model.obtener_por_conductor()
    #print(lista)
    return render_template("conductor.html", programas = lista)


@app.route('/programasNacionales')
def programas_nacionales():
    lista = programaModel.listar_nacionales()
    print(lista)
    return render_template("blog-grid.html", programas = lista)


@app.route('/horarios')
def horarios():
    return render_template("blog-grid.html")


@app.route('/programa/<tipo>')
def programa(tipo=0):
    program = programaModel.obtener_programa(tipo)
    conductores = []
    conductores_programas = conductor_model.obtener_por_conductor()
    print(conductores_programas)
    for cp in conductores_programas:
        (id_p, _, id, nom, ap) = cp
        if id_p == int(tipo):
            conductores.append(conductor_model.Conductor(id, nom, ap))
    print(conductores)
    categorias = programaModel.obtenerCategorias()
    return render_template("blog-single.html", programa = program, conductores = conductores, categorias=categorias)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
