import web 
import app 
import csv 
import json 


class Search:
    
    def __init__(self): 
        pass 

    def GET(self):
        try:
            data = web.input() 
            if data['token'] == "4321": 
                if data['action'] == 'search':
                    if data['matricula'] == "17180389": 
                        bus = self.actionSearch() 
                        return json.dumps(bus) 
                    else:
                        bus = {} 
                        bus['status'] = "Not Found It"
                        return json.dumps(bus) 
                else:
                    bus = {} 
                    bus['status'] = "Command not found"
                    return json.dumps(bus) 
            else:
                bus = {} 
                bus['bus'] = "Invalid Token"
                return json.dumps(bus) 
        except Exception as e:
            bus = {} 
            bus['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(bus) 

    @staticmethod
    def actionSearch():
        try:
            bus = {} 
            bus['status'] = "200 Ok" 
            file = 'static/csv/alumnos.csv' 
            with open(file,'r') as csvfile: 
                reader = csv.DictReader(csvfile) 
                alumnos = [] 
                for row in reader: 
                    fila = {} 
                    fila['matricula'] = row['matricula']  
                    fila['nombre'] = row['nombre'] 
                    fila['primer_apellido'] = row['primer_apellido'] 
                    fila['segundo_apellido'] = row['segundo_apellido'] 
                    fila['carrera'] = row['carrera'] 
                    alumnos.append(fila) 
                    bus['alumnos'] = alumnos 
            return bus 
        except  Exception as e:
            bus = {}
            bus['status'] = "Error"
            return bus 
