# Version 0.3.0

import web 
import app 
import csv 
import json 


class Put:
    file="/static/csv/alumnos.csv"
    def __init__(self): 
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['token'] == "4321": 
                if data['action'] == 'put':
                    matricula=data['matricula']
                    nombre=data['nombre']
                    primer_apellido=data['primer_apellido']
                    segundo_apellido=data['segundo_apellido']
                    carrera=data['carrera']

                    bus2 = self.actionPut(self.file,matricula,nombre,primer_apellido,segundo_apellido,carrera) 
                    return json.dumps(bus2) 
                else:
                    bus2 = {} 
                    bus2['status'] = "Command not found"
                    return json.dumps(bus2) 
            else:
                bus = {} 
                bus['bus'] = "Invalid Token"
                return json.dumps(bus) 
        except Exception as e:
            bus = {} 
            bus['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(bus) 

    @staticmethod
    def actionPut(file, matricula,nombre,primer_apellido,segundo_apellido,carrera):
        try:
            busR = []
            bus = []
            bus2 = {} 
            busR.append(matricula)
            busR.append(nombre)
            busR.append(primer_apellido)
            busR.append(segundo_apellido)
            busR.append(carrera)
            with open('static/csv/alumnos.csv','n', nuevoRegistro='') as csvfile: 
                writer = csv.writer(csvfile)
                writer.writerow(busR)
            with open('static/csv/alumnos.csv','r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader: 
                    bus.append(row)
                    bus2['status']="200 Ok"
                    bus2['alumnos']=bus
            return bus2 
        except  Exception as e:
            bus = {}
            bus['status'] = "Error"
            return bus 

# http://localhost:8080/put?action=put&token=4321&matricula=1718110381&nombre=Carmn&primer_apellido=Kapan&segundo_apellido=Daz&carrera=IN
