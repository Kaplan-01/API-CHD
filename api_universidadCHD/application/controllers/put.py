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
                    bus2 = self.actionPut(self.file,matricula) 
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
    def actionPut(file, matricula):
        try:
            bus = []
            bus2 = {} 
            with open('static/csv/alumnos.csv','r') as csvfile: 
                reader = csv.DictReader(csvfile)   
                for row in reader: 
                    if(matricula==row['matricula']):
                        row['matricula'] = "123456789"
                        bus.append(row)
                        print(bus)
                        bus2['status']="200 Ok"
                        bus2['alumnos']="Elemento Insertado"
                        break
                    else: 
                        bus2={}
                        bus2['status']="Hm... Algo ha salido mal"
            return bus2 
        except  Exception as e:
            bus = {}
            bus['status'] = "Error"
            return bus 
