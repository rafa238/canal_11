from . import conexion
from .programa import Programa

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Conductor:
    def __init__(self,id, nombre, apellido_pat):
        self.id = id
        self.nombre = nombre
        self.apellido_pat = apellido_pat

    def registrar(self):
        sql = "insert into conductor (nombre, apellidoPat) values (%s, %s);"
        conductor = (self.nombre, self.apellido_pat)
        try:
            cursor.execute(sql, conductor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


def obtener_por_conductor():
    cursor.callproc("dos")
    # print out the result
    results = []
    for result in cursor.stored_results():
        results = result.fetchall()
        print(result.fetchall())
    return results

def obtener_conductores():
    sql = "SELECT * FROM conductor"
    cursor.execute(sql)
    conductores_tupla = cursor.fetchall()
    conductores = []
    for conduc in conductores_tupla:
        (id, nombre, apPat) = conduc
        conductores.append(Conductor(id, nombre, apPat))
    return conductores
