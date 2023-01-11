from . import conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Programa:
    def __init__(self, id, nombre, descripcion, nacional, idCategoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.nacional = nacional
        self.idCategoria = idCategoria
        self.categoria = obtenerCategoria(idCategoria)

    def registrar(self):
        sql = "insert into programa (nombre,descripcion,nacional,idCategoria) values (%s, %s, %s, %s);"
        usuario = (self.nombre, self.descripcion, self.nacional, self.idCategoria)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

class Categoria:
    def __init__(self, id, nombre):
        self.nombre = nombre
        self.id = id

    def registrar(self):
        sql = "insert into categoria (id,nombre) values (%s, %s);"
        catego = (self.id, self.nombre)
        try:
            cursor.execute(sql, catego)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

def obtenerCategoria(id):
    sql = "SELECT * FROM categoria WHERE id=%s"
    cursor.execute(sql, (id,))
    id, nombre = cursor.fetchone()
    #print(result)
    catego = Categoria(id, nombre)
    return catego

def obtenerCategorias():
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)
    catego_tupla = cursor.fetchall()
    categorias = []
    for catego in catego_tupla:
        (id, nombre) = catego
        categorias.append(Categoria(id, nombre))

    return categorias

def obtener_programa(id):
    sql = "SELECT * FROM programa WHERE id=%s"
    cursor.execute(sql, (id,))
    (id, nombre, descripcion, nacional, idCategoria) = cursor.fetchone()
    #print(result)
    programa = Programa(id, nombre, descripcion, nacional, idCategoria)
    return programa

def listarProgramas():
    sql = "SELECT * FROM programa"
    cursor.execute(sql)
    result = cursor.fetchall()
    programas = []
    for programa in result:
        (id, nombre, descripcion, nacional, idCategoria) = programa
        programas.append(Programa(id, nombre, descripcion, nacional, idCategoria))
    return programas

def listar_nacionales():
    sql = "SELECT * FROM programa WHERE nacional=1"
    cursor.execute(sql)
    result = cursor.fetchall()
    programas = []
    for programa in result:
        (id, nombre, descripcion, nacional, idCategoria) = programa
        programas.append(Programa(id, nombre, descripcion, nacional, idCategoria))
    return programas

def listar_programs_categoria(id):
    sql = "SELECT * FROM programa WHERE idCategoria=%s"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    programas = []
    for programa in result:
        (id, nombre, descripcion, nacional, idCategoria) = programa
        programas.append(Programa(id, nombre, descripcion, nacional, idCategoria))
    return programas