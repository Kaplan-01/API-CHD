# Version 0.4.0

import web 
import app 
import csv 
import json 


class Delete:
    file="/static/csv/alumnos.csv"
    def __init__(self): 
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['token'] == "4321": 
                if data['action'] == 'delete':
                    matricula=data['matricula']
                    bus2 = self.actionDelete(self.file,matricula) 
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
    def actionDelete(file, matricula):
        try:
            bus = []
            bus2 = {} 
            with open('static/csv/alumnos.csv','r') as csvfile: 
                reader = csv.DictReader(csvfile)   
                for row in reader: 
                    if(matricula==row['matricula']):
                        bus.append(row)
                        bus.remove(row)
                        print(bus)
                        bus2['status']="200 Ok"
                        bus2['alumnos']="Elemento borrado"
                        break
                    else: 
                        bus2={}
                        bus2['status']="Ese elemento no existe"
            return bus2 
        except  Exception as e:
            bus = {}
            bus['status'] = "Error"
            return bus 
