from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'cancionduff'}

@view_config(route_name='cancion-nueva', renderer='templates/agregar.jinja2')
def cancion_nueva(request):
    return { }

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
    return { }