from Scripts.auxiliary.gui_builder import *
from Scripts.classes.master_cipher import MasterCipher


PATH = './keys.yaml'


def run():

    # Evalúa si existe un archivo de configuraciones, en caso de que no, crea uno.
    try:
        open(PATH, 'r', encoding='utf-8')
        if len(yaml.load(open(PATH, 'r', encoding='utf8'), Loader=yaml.FullLoader)['keys']) == 1:
            raise OSError('El archivo de configuraciones es el por defecto.')
    except OSError:
        
        # Creamos un archivo nuevo de llaves
        new_keys_file(PATH)

        # Mostramos una ventana para cargar o crear una llave
        have = have_configuration()

        # Si tiene una llave, que la introduzca, si no, crearemos una nueva
        if have:
            import_configuration(PATH)
        else:
            set_configuration_params(PATH)

    # Abrimos la pestaña para cargar una configuración
    key, rails = select_configuration(PATH)

    # Abrimos la pestaña principal de la aplicación, y retornamos los valores ingresados
    # Para que la ejecución no termine a la primera vez, creamos un bucle
    while True:

        # Creamos un objeto que instancie el encriptador
        encoder = MasterCipher(key, n=rails)
        text, encode = application()

        if encode:
            result = encoder.encode(text)
        else:
            result = encoder.decode(text)

        # Devolverá True si se presiona el botón 'Ok', y False si se presiona 'Cancel', terminando la ejecución en
        # este último caso
        keep_encoding = show(result)

        if keep_encoding:
            pass
        else:
            break

    print('All works very well, keep improving')


if __name__ == '__main__':
    run()
