# Se emplearon librerias PANDAS y openxyl
import pandas as pd

def leer_archivo_encuesta():
    # Especifica la ruta al archivo .xlsx
    archivo = 'encuesta/input_encuesta.xlsx'
    # Lee el archivo usando pandas
    df = pd.read_excel(archivo, engine='openpyxl', header=None)

    list_respuestas = []
    for index, row in df.iterrows():
        # Aquí 'row' es una Serie con los valores de la fila actual.
        # Puedes acceder a los valores por su índice numérico.
        lista_aux = []
        # El arreglo tendra la estructura
        # Edad, Habilidades con productos tecnológicos, Frecuencia, Tipo de transaccion, Tamaño de fuente, Diseño de pantalla
        lista_aux.append(row[2])
        lista_aux.append(row[3])
        lista_aux.append(row[4])
        lista_aux.append(row[6])
        lista_aux.append(row[7])
        lista_aux.append(row[9])

        # Finalmente lo añadimos al arreglo general
        list_respuestas.append(lista_aux)
        print(lista_aux)

    return list_respuestas

def clasificador_perfiles(arr_respuestas):


    return None

def main():
    # Se preprocesa el archivo de encuesta de los usuarios de cajeros ATM
    respuestas_usuarios = leer_archivo_encuesta()

    # Se aplica el clasificador basado en reglas para clasificar a los usuarios
    usuarios_clasificados = clasificador_perfiles(respuestas_usuarios)

    print(usuarios_clasificados)

# Si este script se ejecuta como principal, llamamos a la función main
if __name__ == "__main__":
    main()