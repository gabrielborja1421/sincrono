
import psycopg2
import requests


def write(x):
    try:
        cursor1.execute("insert into pokemon (name) values ('"+x+"')")
    except Exception as err:
        print('Error en la inserción: ' + err)
    else:
        conexion.commit()
    pass

def get_services():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    r = requests.get(url)
    data = r.json().get('results')
    i=0
    for e in data:
        nombres= data[i].get('name')
        print(nombres)
        i +=1
        write(nombres)
    pass



# def get_services():
#     interaciones = 10
#     url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"
#     r = requests.get(url)
#     data = r.json().get('results')
  
#     i = 0
#     j = 10
#     print('hola1')
#     for e in data:
#         nombres= data[i].get('name')
#         print(nombres)
#         i +=1
#     pass


try:
    conexion = psycopg2.connect(database='concurrente', user='postgres', password='14211421')
    cursor1 = conexion.cursor()
    cursor1.execute('select version()')
    version = cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')


def endConexion():
    conexion.close()
    pass


if __name__ == '__main__':

    get_services()
