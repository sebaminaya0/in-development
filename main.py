# Aqui importamos las librerias a utilizar.

import requests
import os
from datetime import datetime, tzinfo, time, timezone, timedelta

# Aqui estan todas las conexiones a API's.

BINANCE = "https://api.binance.com"

COIN_MARKET_API_KEY = "2dbe87e5-1763-426d-800b-a989be228099"

headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': COIN_MARKET_API_KEY }

data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers = headers).json()

# Aqui estan todas las funciones necesarias para el funcionamiento del programa principal.

def esmoneda(moneda):
    return moneda in monedas

def _url(api):
    return BINANCE + api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol=" + cripto))

def escontacto(codigo):
    return codigo in codigosContactos.keys()

# Aqui aloje la informacion en tiempo real de las monedas que son validas, la informacion del usuario, sus contactos y la direccion a la carpeta en la que trabajamos para que todo archivo que se lea, genere o modifique permaneza en esta misma carpeta con mayor facilidad.

monedas = ()

monedas_dict = {}

for cripto in data["data"]:
    monedas_dict[cripto["symbol"]] = cripto["name"]

monedas = monedas_dict.keys()

codigoUsuario = 2909985647382910

codigosContactos = {1503021029384756:"Peter",2005994729105638:"Marcus",3009955638104729:"Leo"}

monedasUsuario = ["BTC","ETH","BNB"]

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)

# Aqui cree los archivos iniciales con el saldo inicial y log de transacciones vacio. De estos se crearan archivos de cada moneda dentro del programa. Se coloca como comentario para que no se sobreescriban nuevamente al correr el programa.

"""

transacciones = open(dir_path + "/RegistroTransacciones.txt","w")

transacciones.write(f"Registro de transacciones de usuario {codigoUsuario}: \n")

transacciones.close()

btc_name = monedas_dict['BTC']

eth_name = monedas_dict['ETH']

bnb_name = monedas_dict['BNB']

btc = get_price("BTC"+"USDT").json()

btc_price = float(btc["price"]) 

eth = get_price("ETH"+"USDT").json()

eth_price = float(eth["price"])

bnb = get_price("BNB"+"USDT").json()

bnb_price = float(bnb["price"])

saldosGeneral = open(dir_path + "/SaldosUsuario.txt","w")

saldosGeneral.write(f"Saldos totales de usuario {codigoUsuario} : \n1) BTC - Name: {btc_name} Q: 2000 USD: {2000*btc_price}\n2) ETH - Name: {eth_name} Q: 3000 USD: {3000*eth_price}\n3) BNB - Name: {bnb_name} Q: 500 USD: {500*bnb_price}")

saldosGeneral.close()

"""

# Este es el programa principal donde se daran las opciones de operaciones de nuestra billetera digital.

def digWallet():
    
    # Utilizamos un while loop pues le damos al usuario la opcion de mantenerse en el programa hasta que el prefiera. Utilizamos un break en la ultima opcion para dar esa opcion.
    
    n = 1  
    
    today = datetime.now()
    
    req = "RegistroTransacciones.txt"
    
    file = os.path.join(dir_path,req)
    
    print("\nBienvenido a su billetera digital!")

    with open(file,"a") as outputFile:
        outputFile.write(f"\nFecha y hora de inicio de sesion: {today}\n")           
    
    while(True):
        act = int(input("\nPorfavor seleccione una de las siguientes opciones:\n1) Recibir Dinero\n2) Transferir Dinero\n3) Mostrar Balance de una Moneda\n4) Mostrar Balance General\n5) Mostrar Transacciones\n6) Salir\n\nColoca el # de la opcion para continuar: "))
        while act < 0 & act > 6:
            print(f"Error: No existe opcion #{act}")
            act = int(input("\nPorfavor seleccione una de las siguientes opciones:\n1) Recibir Dinero\n2) Transferir Dinero\n3) Mostrar Balance de una Moneda\n4) Mostrar Balance General\n5) Mostrar Transacciones\n6) Salir\n\nColoca el # de la opcion para continuar: "))
        if act == 1:
            mon = input("Indicar moneda a recibir: ")
            while not esmoneda(mon):
                while mon not in monedasUsuario :
                    print("Moneda invalida\n")
                    mon = input("Indicar moneda nuevamente: ")
            cant = float(input("Indicar cantidad a recibir de la moneda: "))
            while cant < 0 :
                print("No se puede recibir cantidades negativas\n")
                cant = float(input("Indicar cantidad nuevamente: "))
            cont = int(input("Indicar contacto emisor de transaccion: "))
            while not escontacto(cont):
                print("Codigo invalido. No se encuentra en lista de contactos\n")
                cont = int(input("Indicar contacto nuevamente: "))
            nomb_cont = codigosContactos[cont]
            dummy = get_price(mon+"USDT").json()
            cambio = float(dummy["price"])
            print(f"\nTransaccion Confirmada:\nSe recibieron {cant} {mon} con un valor de {cant*cambio} USD del emisor {nomb_cont}")
            req = "RegistroTransacciones.txt"
            file = os.path.join(dir_path,req)
            with open(file,"a") as outputFile:
                outputFile.write(f"\nTransaccion de sesion #{n}\nSe recibieron {cant} {mon} con un valor de {cant*cambio} USD del emisor {nomb_cont}\n")
            req = "SaldosUsuario.txt"
            file = os.path.join(dir_path,req)
            with open(file,"r") as outputFile:
                a = outputFile.readlines()
                if mon == "BTC":
                    b = a[1].split()
                    b[6] = str(float(b[6]) + cant)
                    b[-1] = str(float(b[6])*cambio)
                    b.append("\n")
                    a[1] = " ".join(b)
                elif mon == "ETH":
                    c = a[2].split()
                    c[6] = str(float(c[6]) + 200)
                    c[-1] = str(float(c[6])*cambio)
                    c.append("\n")      
                    a[2] = " ".join(c)
                elif mon == "BNB":
                    d = a[3].split()
                    d[7] = str(float(d[7]) + 200)
                    d[-1] = str(float(d[7])*cambio)
                    d.append("\n")
                    a[3] = " ".join(d)
            with open(file,"w") as outputFile:
                outputFile.writelines(a)                     
        elif act == 2:
            mon = input("Indicar moneda a transferir: ")
            while not esmoneda(mon):
                while mon not in monedasUsuario :
                    print("Moneda invalida\n")
                    mon = input("Indicar moneda nuevamente: ")
            req = "SaldosUsuario.txt"
            file = os.path.join(dir_path,req)
            with open(file,"r") as outputFile:
                a = outputFile.readlines()
                b = a[1].split()
                c = a[2].split()
                d = a[3].split()
            cant = float(input("Indicar cantidad a transferir de la moneda: "))
            while cant < 0 :
                if mon == "BTC":
                    while cant > b[6]:
                        print("No se puede transferir cantidades negativas\n")
                        cant = float(input("Indicar cantidad nuevamente: "))
                elif mon == "ETH":
                    while cant > c[6]:
                        print("No se puede transferir cantidades negativas\n")
                        cant = float(input("Indicar cantidad nuevamente: "))
                elif mon == "BNB":
                    while cant > d[7]:
                        print("No se puede transferir cantidades negativas\n")
                        cant = float(input("Indicar cantidad nuevamente: "))
            cont = int(input("Indicar contacto receptor de transaccion: "))
            while not escontacto(cont):
                print("Codigo invalido. No se encuentra en lista de contactos\n")
                cont = int(input("Indicar contacto nuevamente: "))
            nomb_cont = codigosContactos[cont]
            dummy = get_price(mon+"USDT").json()
            cambio = float(dummy["price"])
            print(f"\nTransaccion Confirmada:\nSe transfirieron {cant} {mon} con un valor de {cant*cambio} USD al receptor {nomb_cont}")
            req = "RegistroTransacciones.txt"
            file = os.path.join(dir_path,req)
            with open(file,"a") as outputFile:
                outputFile.write(f"\nTransaccion de sesion #{n}\nSe transfirieron {cant} {mon} con un valor de {cant*cambio} USD al receptor {nomb_cont}\n")
            req = "SaldosUsuario.txt"
            file = os.path.join(dir_path,req)
            with open(file,"r") as outputFile:
                a = outputFile.readlines()
                if mon == "BTC":
                    b = a[1].split()
                    b[6] = str(float(b[6]) - cant)
                    b[-1] = str(float(b[6])*cambio)
                    b.append("\n")
                    a[1] = " ".join(b)
                elif mon == "ETH":
                    c = a[2].split()
                    c[6] = str(float(c[6]) - cant)
                    c[-1] = str(float(c[6])*cambio)
                    c.append("\n")      
                    a[2] = " ".join(c)
                elif mon == "BNB":
                    d = a[3].split()
                    d[7] = str(float(d[7]) - cant)
                    d[-1] = str(float(d[7])*cambio)
                    d.append("\n")
                    a[3] = " ".join(d)
            with open(file,"w") as outputFile:
                outputFile.writelines(a)       
        elif act == 3:
            mon = input("Indicar moneda: ")
            while not esmoneda(mon):
                while mon not in monedasUsuario :
                    print("Moneda invalida\n")
                    mon = input("Indicar moneda nuevamente: ")
            req = "SaldosUsuario.txt"
            file = os.path.join(dir_path,req)
            if mon == "BTC":    
                with open(file,"r") as outputFile:
                    a = outputFile.readlines()    
                b = a[1]
                print(b)
            elif mon == "ETH":
                with open(file,"r") as outputFile:
                    a = outputFile.readlines()    
                c = a[2]
                print(c)
            elif mon == "BNB":
                with open(file,"r") as outputFile:
                    a = outputFile.readlines()    
                d = a[3]
                print(d)
        elif act == 4:
            req = "SaldosUsuario.txt"
            file = os.path.join(dir_path,req)
            with open(file,"r") as outputFile:
                a = outputFile.read()
                print(a)
        elif act == 5:
            req = "RegistroTransacciones.txt"
            file = os.path.join(dir_path,req)
            with open(file,"r") as outputFile:
                a = outputFile.read()
                print(a)
        elif act == 6:
            print("Ten un buen dia!")
            req = "RegistroTransacciones.txt"
            file = os.path.join(dir_path,req)
            with open(file,"a") as outputFile:
                outputFile.write(f"Fin de sesion.\n")   
            break
        n += 1

digWallet()