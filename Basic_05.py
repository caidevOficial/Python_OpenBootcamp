
contacto = {
    'Nombre': 'Facundo',
    'Apellido': 'Caidev',
    'Edad': 32,
    'Email': 'correofalso@gmail.com',
    'Telefono': '123456789',
    'Casado': False,
    'Con Hijos': False,
    'Lista de amigos': ['Amigo_1', 'Amigo_2', 'Amigo_3', 'Amigo_4', 'Amigo_5'],
    'Peliculas Vistas': {
        'Pelicula_1': 'Shrek 1',
        'Pelicula_2': 'Shrek 2',
        'Pelicula_3': 'Shrek Tercero',
        'Pelicula_4': 'Shrek 4'
    }
}

print(
    f'* Nombre: {contacto["Nombre"]}',
    f'* Apellido: {contacto["Apellido"]}',
    f'* Edad: {contacto["Edad"]}',
    f'* Email: {contacto["Email"]}',
    f'* Telefono: {contacto["Telefono"]}',
    f'* Casado: {contacto["Casado"]}',
    sep='\n'
)

print('* Lista de amigos:')
for amigo in contacto['Lista de amigos']:
    print(f'** {amigo}')

print(f'* Peliculas Vistas:')
for pelicula, titulo in contacto['Peliculas Vistas'].items():
    print(f'** {pelicula} - {titulo}')
