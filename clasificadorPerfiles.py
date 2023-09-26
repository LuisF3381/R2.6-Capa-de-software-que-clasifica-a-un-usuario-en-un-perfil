# Se emplearon librerias PANDAS y openxyl
import pandas as pd


# Funcion que lee las respuestas de los usuarios
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


def clasificar_usuario(respuesta):

    # Los perfiles definidos tras el analisis del informe de expectativas y necesidades del usuario de cajero ATM
    perfiles = {
        "Cliente Senior": 0,
        "Cliente Frecuente": 0,
        "Cliente Ocasional": 0
    }

    ###########################################################
    # Puntos para Cliente Senior
    ###########################################################

    if respuesta[0] == 'Mas de 54 años':
        perfiles["Cliente Senior"] += 9
    # Habilidades tecnologicas
    if respuesta[1] == 'Suelo tener dificultades para utilizar dispositivos electrónicos y canales digitales':
        perfiles["Cliente Senior"] += 5
    if respuesta[1] == 'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad':
        perfiles["Cliente Senior"] += 3
    # Frecuencia
    if (respuesta[2] == 'Mensualmente') or (respuesta[2] == 'Ocasionalmente'):
        perfiles["Cliente Senior"] += 4
    # Tipo de transaccion
    if ('Retiro de efectivo' in respuesta[3]):
        perfiles["Cliente Senior"] += 3
    if ('Depósito de efectivo' in respuesta[3]):
        perfiles["Cliente Senior"] += 2
    if ('Consulta de saldo' in respuesta[3]):
        perfiles["Cliente Senior"] += 2
    # Tamaño de la fuente
    if (respuesta[4] == 'Grande'):
        perfiles["Cliente Senior"] += 4
    if (respuesta[4] == 'Mediano'):
        perfiles["Cliente Senior"] += 3
    # Diseño de interfaz
    if (respuesta[5] == 'Diseño simple con opciones básicas claramente visibles'):
        perfiles["Cliente Senior"] += 5

    # Valoracion Positiva de la experiencia
    # Facilidad de uso
    if (respuesta[7] >= 4):
        perfiles["Cliente Senior"] += 3
    # Intuitividad en la interfaz de uso
    if (respuesta[8] >= 4):
        perfiles["Cliente Senior"] += 2

    # Valoracion Negativa de la experiencia
    # Problemas para encontrar la información deseada en la pantalla (4: Negativo o 3: Neutral):
    if (respuesta[11] >= 3):
        perfiles["Cliente Senior"] += 2

    ###########################################################
    # Puntos para Cliente Frecuente
    ###########################################################
    if respuesta[0] == '35 años a 54 años':
        perfiles["Cliente Frecuente"] += 4
    if respuesta[0] == '18 años a 34 años':
        perfiles["Cliente Frecuente"] += 3

    # Habilidades tecnologicas
    if respuesta[1] == 'Me siento muy cómodo utilizando dispositivos electrónicos y canales digitales':
        perfiles["Cliente Frecuente"] += 6
    if respuesta[1] == 'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad':
        perfiles["Cliente Frecuente"] += 5

    # Frecuencia
    if (respuesta[2] == 'Semanalmente') or (respuesta[2] == 'Diariamente'):
        perfiles["Cliente Frecuente"] += 9

    # Tipo de transaccion
    if ('Retiro de efectivo' in respuesta[3]):
        perfiles["Cliente Frecuente"] += 5
    if ('Depósito de efectivo' in respuesta[3]):
        perfiles["Cliente Frecuente"] += 3

    # Diseño de interfaz
    if (respuesta[5] == 'Diseño simple con opciones básicas claramente visibles'):
        perfiles["Cliente Frecuente"] += 2
    if (respuesta[5] == 'Diseño más avanzado que agrupe opciones relacionadas.'):
        perfiles["Cliente Frecuente"] += 3

    # Valoracion Positiva de la experiencia



    print(perfiles)

    # Devolver el perfil con la puntuación más alta
    return max(perfiles, key=perfiles.get)




def clasificador_perfiles(arr_respuestas):

    # Se crea el arreglo que contendra los perfiles a los que se asignaron
    perfiles_asignados = []

    for lista in arr_respuestas:
        clasificar_usuario(lista)


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