from pyramid.view import view_config
from zeep import Client
from datetime import datetime

cliente = Client('http://localhost:7101/AplicacionServidorCancion-ProyectoServidorCancion-context-root/CancionSWPort?WSDL');
factory = cliente.type_factory('ns0')

@view_config(route_name='home', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'cancionduff'}

@view_config(route_name='cancion-nueva', renderer='templates/agregar.jinja2')
def cancion_nueva(request):
    if request.POST:
        id = request.POST['id']
        titulo = request.POST['titulo']
        nombre_artista = request.POST['nombreArtista']
        genero = request.POST['genero']
        fecha_lanzamiento = request.POST['fecha']
        fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d')
        cancion = factory.cancion(id = id, titulo = titulo, nombreArtista = nombre_artista, genero = genero, fechaLanzamiento = fecha_lanzamiento)
        try:
            cliente.service.adicionarCancion(cancion)
        except Exception as error:
            return {'error': error}
    return {}

@view_config(route_name='cancion-eliminar', renderer='templates/eliminar.jinja2')
def cancion_eliminar(request):
    return { }

@view_config(route_name='cancion-actualizar', renderer='templates/actualizar.jinja2')
def cancion_actualizar(request):
    return { }

@view_config(route_name='cancion-consultar', renderer='templates/consultar.jinja2')
def cancion_consultar(request):
    return { }

@view_config(route_name='cancion-listar', renderer='templates/listar.jinja2')
def cancion_listar(request):
    try:
        canciones = cliente.service.listarCanciones()
    except Exception as error:
        return {'canciones': []}
    else:
        return { 'canciones': canciones}

@view_config(route_name='cancion-principal', renderer='templates/index.jinja2')
def cancion_principal(request):
    return { }