# Se emplearon librerias PANDAS y openxyl
import pandas as pd

def leer_archivo_encuesta():
    # Especifica la ruta al archivo .xlsx
    archivo = 'encuesta/input_encuesta.xlsx'
    # Lee el archivo usando pandas
    df = pd.read_excel(archivo, engine='openpyxl', header=None)

    list_respuestas = []
    for index, row in df.iloc[1:].iterrows(): # Ignoramos las filas de la cabecera
        # Aquí 'row' es una Serie con los valores de la fila actual.
        # Puedes acceder a los valores por su índice numérico.
        lista_aux = []
        # El arreglo tendra la estructura
        lista_aux.append(row[2]) # Edad
        lista_aux.append(row[3]) # Habilidades con productos tecnológicos
        lista_aux.append(row[4]) # Frecuencia de uso
        lista_aux.append(row[6]) # Tipo de transaccion
        lista_aux.append(row[7]) # Tamaño de fuente
        lista_aux.append(row[9]) # Diseño de pantalla
        # Metricas de interaccion Positivas
        lista_aux.append(row[11]) # Rapidez de las transacciones
        lista_aux.append(row[12]) # Facilidad de uso
        lista_aux.append(row[13]) # Intuitividad en la interfaz de uso
        # Metricas de interaccion Negativas
        lista_aux.append(row[17]) # Dificultad en la navegación por las opciones en pantalla
        lista_aux.append(row[18]) # Confusión causada por la falta de claridad en los iconos y símbolos
        lista_aux.append(row[19]) # Problemas para encontrar la información deseada en la pantalla
        lista_aux.append(row[20]) # Lentitud en la respuesta de la interfaz a tus acciones}
        # Finalmente lo añadimos al arreglo general
        list_respuestas.append(lista_aux)

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