#from celery import shared_task
from proyecto.celery import app
import requests
from lib2to3.pgen2 import driver
from optparse import Option
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json
#Para guardar la metadata en Postgresql
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

#@shared_task
# RPA de Chilquinta
@app.task(bind=True)
def Chilquinta():
    # Opciones de navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    #Descarga de boletas
    options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\user\\Downloads\\chilquinta", #Cambiar directorio predeterminado para descargas
    "download.prompt_for_download": False, #Para descargar automáticamente el archivo
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  #No mostrará PDF directamente en Chrome
    })
        
    driver_path = "C:\\dchrome\\chromedriver.exe"
        
    driver = webdriver.Chrome(driver_path, chrome_options=options)
        
    # Inicializamos el navegador
    driver.get('https://www.chilquinta.cl/')

    # Click en iniciar sesión
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'button.btn text-font-13 btn-sv py-1 btn-block btn-secondary'.replace(' ', '.'))))\
            .click()

    # Escribir usuario
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys('97030000-7')

        # Escribir contraseña
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        "/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/form/div[1]/div/input[2]"))).send_keys('chilquinta')

    #Click para iniciar sesión
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'button.btn btn-login text-center mt-2'.replace(' ', '.'))))\
            .click()

    # Click para cerrar (x) el cambio de contraseña
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'button.close')))\
            .click()

    # Click en pagar facturas pendientes
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'a.btn btn btn-block btn-sv font-12 font-weight-600 p-2 btn-secondary'.replace(' ', '.'))))\
            .click()

    # Click en descargar boleta
    WebDriverWait(driver, 35)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr:nth-child(1) a:nth-child(2) .svg-inline--fa"))).click()

    # Folio
    NumBoleta = driver.find_element(By.XPATH,"//*[@id='table-last-invoice-desktop']/tbody/tr[1]/td[4]/div").text
    print(NumBoleta)

    # Rut Emisor
    rutEmisor = '96813520-1'
    print(rutEmisor)

    # Rut Receptor
    rutReceptor = '97030000-7'
    print(rutReceptor)

    # Tipo de Servicio
    servicio = 'ELE'
    print(servicio)

    # Fecha emisión de boleta
    textfechaemi = driver.find_element(By.XPATH,"//*[@id='table-last-invoice-desktop']/tbody/tr[1]/td[5]/div").text
    # Año de emisión de boleta
    año = textfechaemi[-4:]
    print(año)
    # Mes de emisión de boleta
    mes = textfechaemi[3:-5]
    print(mes)
    # Dia de emisión de boleta
    dia =textfechaemi[:2]
    print(dia)

    # Subir Boleta al OpenKM
    def subirBoleta():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/document/createSimple"

        payload={'docPath': '/okm:root/Cobros/76242774-5/3/ELE/NoviembreChilquinta.pdf'}
        files=[
            ('content',('PDFServlet.pdf',open('C:\\Users\\user\Downloads\\chilquinta\\PDFServlet.pdf','rb'),'application/pdf'))
        ]
        headers = {
            'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)

    time.sleep(15)
    subirBoleta()

    # Crear Grupo de Metadata en OpenKM
    def CrearMetadata():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/addGroup?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreChilquinta.pdf&grpName=okg:encCobro"
        payload={}
        files={}
        headers = {
        'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }

        response = requests.request("PUT", url, headers=headers, data=payload, files=files)

        print(response.text)
    
    time.sleep(15)
    CrearMetadata()

    #Subir metadatos al OpenKM
    def SubirMetadatos():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/setPropertiesSimple?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreChilquinta.pdf&grpName=okg:encCobro"

        payload = json.dumps({
            "simplePropertyGroup": [
                {
                    "name": "okp:encCobro.folio",
                    "value": NumBoleta
                },
                {
                    "name": "okp:encCobro.rut_emisor",
                    "value": rutEmisor
                },
                {
                    "name": "okp:encCobro.rut_receptor",
                    "value": rutReceptor
                },
                {
                    "name": "okp:encCobro.tipo_servicio",
                    "value": servicio
                },
                {
                    "name": "okp:encCobro.anio_doc",
                    "value": año
                },
                {
                    "name": "okp:encCobro.mes_doc",
                    "value": mes
                },
                {
                    "name": "okp:encCobro.dia_doc",
                    "value": dia
                }
            ]
        })
        headers = {
            'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg=',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    time.sleep(15)
    SubirMetadatos()

    # Insertar metadata en base de datos postgresql
    comentario=""
    def intertarBoletaBD(rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario):
        conn = psycopg2.connect(dbname="paginaroda", user="postgres",
                        password="admin", host="localhost", port="5432")
        cursor = conn.cursor()
        query = """ INSERT INTO web_boleta (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario) values (%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query, (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario))
        print("Metadata insertada correctamente en PostgreSQL")
        conn.commit()
        conn.close()

    time.sleep(15)   
    intertarBoletaBD(rutEmisor,rutReceptor,servicio,año,dia,NumBoleta,mes,comentario)


# RPA de Litoral
@app.task
def Litoral():
    #Opciones de navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\user\\Downloads\\litoral", #Cambiar directorio predeterminado para descargas
    "download.prompt_for_download": False, #Para descargar automáticamente el archivo
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  #No mostrará PDF directamente en Chrome
    })
    driver_path = "C:\\dchrome\\chromedriver.exe"
        
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    driver.get("https://www.litoral.cl/empresa/resumen")

    #Ingresar Rut Empresa
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.NAME,'nr_rut_empresa'))).send_keys('970300007')
        
    #Ingresar Rut Usuario
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.NAME,'nr_rut_usuario'))).send_keys('970300007')
        
    #Ingresar contraseña
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys('bestado')
        
    #Click para iniciar sesión
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'button button-secondary button--small'.replace(' ', '.'))))\
            .click()
        
    #Ver Facturas
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'i.icon-eye-blue.icon--left')))\
            .click()
        
    #Ver todas
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
        '/html/body/main/section/div/div[5]/div[1]/div/div[1]/div[1]/table/tfoot/tr/td[4]/a')))\
            .click()
        
    #Descargar Boleta
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'i.icon-pdf')))\
            .click()
        
    # Folio
    NumBoleta = driver.find_element(By.XPATH,"//*[@id='pendientesPagoContent']/tr[1]/td[4]").text
    print(NumBoleta)

    # Rut Emisor
    rutEmisor = '91344000-5'
    print(rutEmisor)

    # Rut Receptor
    rutReceptor = '97030000-7'
    print(rutReceptor)

    # Tipo de Servicio
    servicio = 'ELE'
    print(servicio)

    # Fecha emisión de boleta
    textfechaemi = driver.find_element(By.XPATH,"//*[@id='pendientesPagoContent']/tr[1]/td[5]").text
    # Año de emisión de boleta
    año = textfechaemi[-4:]
    print(año)
    # Mes de emisión de boleta
    mes = textfechaemi[3:-5]
    print(mes)
    # Dia de emisión de boleta
    dia =textfechaemi[:2]
    print(dia)


    #Subir Boleta
    def subirboleta ():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/document/createSimple"
            
        payload={'docPath': '/okm:root/Cobros/76242774-5/3/ELE/NoviembreLitoral.pdf'}
        files=[
        ('content',('PDFServlet.pdf',open('C:\\Users\\user\Downloads\\litoral\\PDFServlet.pdf','rb'),'application/pdf'))
        ]
        headers = {
        'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }
            
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
            
        print(response.text)
        
    time.sleep(10)
    subirboleta()

    #Crear Grupo de Metadatos
    def CrearMetadata():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/addGroup?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreLitoral.pdf&grpName=okg:encCobro"
        payload={}
        files={}
        headers = {
        'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }
            
        response = requests.request("PUT", url, headers=headers, data=payload, files=files)
            
        print(response.text)
        
    time.sleep(15)
    CrearMetadata()

    #Subir metadatos al OpenKM
    def SubirMetadatos():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/setPropertiesSimple?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreLitoral.pdf&grpName=okg:encCobro"

        payload = json.dumps({
            "simplePropertyGroup": [
                {
                    "name": "okp:encCobro.folio",
                    "value": NumBoleta
                },
                {
                    "name": "okp:encCobro.rut_emisor",
                    "value": rutEmisor
                },
                {
                    "name": "okp:encCobro.rut_receptor",
                    "value": rutReceptor
                },
                {
                    "name": "okp:encCobro.tipo_servicio",
                    "value": servicio
                },
                {
                    "name": "okp:encCobro.anio_doc",
                    "value": año
                },
                {
                    "name": "okp:encCobro.mes_doc",
                    "value": mes
                },
                {
                    "name": "okp:encCobro.dia_doc",
                    "value": dia
                }
            ]
        })
        headers = {
            'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg=',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    time.sleep(15)
    SubirMetadatos()

    # Insertar metadata en base de datos postgresql
    comentario=""
    def intertarBoletaBD(rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario):
        conn = psycopg2.connect(dbname="paginaroda", user="postgres",
                        password="admin", host="localhost", port="5432")
        cursor = conn.cursor()
        query = """ INSERT INTO web_boleta (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario) values (%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query, (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario))
        print("Metadata insertada correctamente en PostgreSQL")
        conn.commit()
        conn.close()

    time.sleep(15)   
    intertarBoletaBD(rutEmisor,rutReceptor,servicio,año,dia,NumBoleta,mes,comentario)


# RPA de Enel
@app.task
def Enel():
    # Opciones de navegador
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\user\\Downloads\\enel", #Cambiar directorio predeterminado para descargas
    "download.prompt_for_download": False, #Para descargar automáticamente el archivo
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  #No mostrará PDF directamente en Chrome
    })

    driver_path = "C:\\dchrome\\chromedriver.exe"
        
    driver = webdriver.Chrome(driver_path, chrome_options=options)
        
    # Inicializamos el navegador
    driver.get('https://www.enel.cl/')
        
    # Aceptar terminos
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/button[2]")))\
            .click()
        
    # Click en ingresar a mi cuenta Enel
    time.sleep(15)
    element = driver.find_element(By.CSS_SELECTOR,
    'button.global-header__btn btn-user'.replace(' ', '.'))\
        .click()

    # Escribir usuario
    WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys('989101994')

    # Escribir contraseña
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys('Enel2020.')

    #Click en Ingresar
    WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        'button.btn-cta--pink'.replace(' ', '.'))))\
            .click()

    # Click en Mis cuentas (Se demora)
    time.sleep(20)
    element = driver.find_element(By.XPATH, "/html/body/main/div[3]/div[2]/div[1]/nav/ul/li[6]/a").click()


    # Ir a la cuenta de SANTO DOMINGO 1568 (Se demora)
    time.sleep(25)
    element = driver.find_element(By.XPATH, 
    "/html/body/main/div[3]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[4]/a").click()

    # Ir a Mis Boletas (Se demora)
    time.sleep(30)
    element = driver.find_element(By.XPATH, 
    "/html/body/main/div[3]/div[2]/div[2]/div[4]/div/section/div[1]/section/button").click()

    #Descargar Boleta
    time.sleep(30)
    element = driver.find_element(By.XPATH, 
    "/html/body/main/div[3]/div[2]/div[2]/div[4]/div/section/div[1]/section/div[1]/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()

    # Folio
    NumBoleta = driver.find_element(By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr[1]/td[1]").text
    print(NumBoleta)

    # Rut Emisor
    rutEmisor = '96800570-7'
    print(rutEmisor)

    # Rut Receptor
    rutReceptor = '91081000-6'
    print(rutReceptor)

    # Tipo de Servicio
    servicio = 'ELE'
    print(servicio)

    # Fecha emisión de boleta
    textfechaemi = driver.find_element(By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr[1]/td[2]").text
    # Año de emisión de boleta
    año = textfechaemi[-4:]
    print(año)
    # Mes de emisión de boleta
    mes = textfechaemi[3:-5]
    print(mes)
    # Dia de emisión de boleta
    dia =textfechaemi[:2]
    print(dia)
        
    #Subir boleta al OpenKM
    def subirboleta ():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/document/createSimple"
            
        payload={'docPath': '/okm:root/Cobros/76242774-5/3/ELE/NoviembreEnel.pdf'}
        files=[
        ('content',('18397c6b-51d1-442f-af70-88f843ebee17.pdf',open('C:\\Users\\user\Downloads\\enel\\18397c6b-51d1-442f-af70-88f843ebee17.pdf','rb'),'application/pdf'))
        ]
        headers = {
        'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }
            
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
            
        print(response.text)
        
    time.sleep(10)
    subirboleta()

    #Crear Grupo de Metadatos en OpenKM
    def CrearMetadata():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/addGroup?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreEnel.pdf&grpName=okg:encCobro"
        payload={}
        files={}
        headers = {
        'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg='
        }
            
        response = requests.request("PUT", url, headers=headers, data=payload, files=files)
            
        print(response.text)
        
    time.sleep(15)
    CrearMetadata()

    #Subir metadatos al OpenKM
    def SubirMetadatos():
        url = "http://65.21.188.116:8080/OpenKM/services/rest/propertyGroup/setPropertiesSimple?nodeId=/okm:root/Cobros/76242774-5/3/ELE/NoviembreEnel.pdf&grpName=okg:encCobro"

        payload = json.dumps({
            "simplePropertyGroup": [
                {
                    "name": "okp:encCobro.folio",
                    "value": NumBoleta
                },
                {
                    "name": "okp:encCobro.rut_emisor",
                    "value": rutEmisor
                },
                {
                    "name": "okp:encCobro.rut_receptor",
                    "value": rutReceptor
                },
                {
                    "name": "okp:encCobro.tipo_servicio",
                    "value": servicio
                },
                {
                    "name": "okp:encCobro.anio_doc",
                    "value": año
                },
                {
                    "name": "okp:encCobro.mes_doc",
                    "value": mes
                },
                {
                    "name": "okp:encCobro.dia_doc",
                    "value": dia
                }
            ]
        })
        headers = {
            'Authorization': 'Basic dXNyY2VuOkIqQnF5KFZJamZZWG1AOEg=',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    time.sleep(15)
    SubirMetadatos()

    # Insertar metadata en base de datos postgresql
    comentario=""
    def intertarBoletaBD(rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario):
        conn = psycopg2.connect(dbname="paginaroda", user="postgres",
                        password="admin", host="localhost", port="5432")
        cursor = conn.cursor()
        query = """ INSERT INTO web_boleta (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario) values (%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query, (rut_emisor,rut_receptor,tipo_servicio,anio_doc,dia_doc,folio,mes_doc,comentario))
        print("Metadata insertada correctamente en PostgreSQL")
        conn.commit()
        conn.close()

    time.sleep(15)   
    intertarBoletaBD(rutEmisor,rutReceptor,servicio,año,dia,NumBoleta,mes,comentario)