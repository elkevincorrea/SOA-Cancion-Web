from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def my_view(request):
    return {'project': 'cancionduff'}

@view_config(route_name='cancion-nueva', renderer='templates/agregar.jinja2')
def cancion_nueva(request):
    return { }
