# llama a las librerias de Flask
from flask import Flask, render_template
#Declaramos una variable para llamar una instancia de ROUTER
app=Flask(__name__)
#Crear una ruta para el index
#comilla simple alt + 39 = '
@app.route('/')
#creamos una función en python
def index():
    #return 'Hola soy de Nuevo'
    #manda a acargar la pagina principal index.html
    return render_template('index.html')
#llama a contactos html
@app.route('/somos')
def somos():
    return render_template('somos.html')
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')
# creamos una condicional con if
#para inicializar la pagina y asiganar el puerto
if __name__=='__main__':
    app.run(debug=True,port=8005)
