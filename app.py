from flask import Flask, render_template, redirect, url_for, request

from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)
app.config['SECRET_KEY'] = 'llave_secreta_123'

titulo_app = 'Zona Fit (Gym)'

@app.route('/') # url
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de Inicio')
    # recuperamos clientes de la base de datos
    clientes_db = ClienteDAO.seleccionar()
    # creamos un objeto de cliente vacio para conectarlo al formulario
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    # creamos los objetos de cliente inicialmente objetos vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(request.form)  # ✅ Cambiado: usar request.form en lugar de obj=cliente
    if cliente_forma.validate_on_submit():
        # llenamos el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente) #tambien se recupera el id oculto del form
        if not  cliente.id :
            # guardar el nuevo cliente en la base de datos
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
        app.logger.info('Cliente guardado exitosamente')
    else:
        app.logger.warning('Error en validación del formulario')
        app.logger.warning(cliente_forma.errors)  # ✅ Ver errores de validación
    # redirigir a la pagina de inicio (SIEMPRE, dentro o fuera del if)
    return redirect(url_for('inicio'))  # ✅ Movido FUERA del if
@app.route('/limpiar')
def limpiar():
    return  redirect(url_for('inicio'))


@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    #recuperar el listado de ckientes para volver a mostrarlo
    clientes_db = ClienteDAO.seleccionar()
    return  render_template('index.html', titulo=titulo_app, clientes=clientes_db , forma=cliente_forma)

@app.route('/eliminar/<int:id>') #peticion para eliminar
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)