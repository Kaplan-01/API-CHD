#Version 0.3.0
# EJEMPLO URL 
# http://localhost:8080/put?action=put&token=4321&matricula=1718110389&nombre=Mela&primer_apellido=Kaplan&segundo_apellido=Salmon&&carrera=DD

import web
import app
import csv
import json


class Put:
    file = "/static/csv/alumnos.csv"

    def __init__(self):
        pass

    def GET(self):
        try:
            data = web.input()
            if data['token'] == "4321":
                if data['action'] == "put":
                    matricula = data['matricula']
                    nombre = data['nombre']
                    primer_apellido = data['primer_apellido']
                    segundo_apellido = data['segundo_apellido']
                    carrera = data['carrera']
                    result2 = self.actionPut(
                        self.file, matricula, nombre, primer_apellido, segundo_apellido, carrera)
                    return json.dumps(result2)

        except Exception as e:
            result = {}
            result['status'] = "Values missing"
            return json.dumps(result)

    @staticmethod
    def actionPut(file, matricula, nombre, primer_apellido, segundo_apellido, carrera):
        try:
            result = []
            resultR = []
            result2 = {}
            resultR.append(matricula)
            resultR.append(nombre)
            resultR.append(primer_apellido)
            resultR.append(segundo_apellido)
            resultR.append(carrera)
            with open('static/csv/alumnos.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(resultR)
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
