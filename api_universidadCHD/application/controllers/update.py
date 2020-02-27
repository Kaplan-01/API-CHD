# Version 0.5.0
# EJEMPLO URL 
# http://localhost:8080/update?action=update&token=1234&matricula=8&matriculaNueva=1&nombre=Jhon&apellido1=Carter&apellido2=Earth&carrera=TI

import web
import app
import json
import csv


class Update:
    file = "/static/csv/alumnos.csv"

    def __init__(self):
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "1234":
                if data['action'] == "update":
                    matricula = data['matricula']
                    matriculaNueva = data['matriculaNueva']
                    nombre = data['nombre']
                    primer_apellido = data['apellido1']
                    segundo_apellido = data['apellido2']
                    carrera = data['carrera']
                    result2 = self.actionUpdate(
                        self.file, matricula, matriculaNueva, nombre, primer_apellido, segundo_apellido, carrera)
                    return json.dumps(result2)
                else:
                    result2 = {}
                    result2['status'] = "Command not found"
                    return json.dumps(result2)
            else:
                result = {}
                result['status'] = "Invalid Token"
                return json.dumps(result)
        except Exception as e:
            result = {}
            result['status'] = "Values missing"
            return json.dumps(result)

    @staticmethod
    def actionUpdate(file, matricula, matriculaNueva, nombre, primer_apellido, segundo_apellido, carrera):
        try:
            result = []
            result2 = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if(row['matricula'] != matricula):
                        result2['status'] = "200 Ok"
                        result.append(row)
                        result2['alumnos'] = result

            longi = (len(result))
            with open('static/csv/alumnos.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                bye = []
                bye.append("matricula")
                bye.append("nombre")
                bye.append("primer_apellido")
                bye.append("segundo_apellido")
                bye.append("carrera")
                writer.writerow(bye)
                data = []
                for x in range(0, longi):
                    data.append(result[x]['matricula'])
                    data.append(result[x]['nombre'])
                    data.append(result[x]['primer_apellido'])
                    data.append(result[x]['segundo_apellido'])
                    data.append(result[x]['carrera'])
                    writer.writerow(data)
                    data = []
                save = []
                save.append(matriculaNueva)
                save.append(nombre)
                save.append(primer_apellido)
                save.append(segundo_apellido)
                save.append(carrera)
                writer.writerow(save)

            result = []
            result2 = {}
            with open('static/csv/alumnos.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    result.append(row)
                    result2['status'] = "200 Ok"
                    result2['alumnos'] = result
            return result2
        except Exception as e:
            result = {}
            result['status'] = "Error"
        return result

# TODO revisar el codigo
# Componentes de un diccionario una key y un value
 # REPL Read, execute, print and loop

 # https://repl.it
 # Seleccionamos Python
