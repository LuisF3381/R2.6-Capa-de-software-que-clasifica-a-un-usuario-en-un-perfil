# Se emplearon librerias PANDAS, unittest
import pandas as pd
import unittest


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
        lista_aux.append(row[20]) # Lentitud en la respuesta de la interfaz a tus acciones
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
        perfiles["Cliente Senior"] += 14
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
    # Rapidez de las transacciones
    if (respuesta[6] >= 4):
        perfiles["Cliente Frecuente"] += 5
    # Facilidad de uso
    if (respuesta[7] >= 4):
        perfiles["Cliente Frecuente"] += 3
    # Intuitividad en la interfaz de uso
    if (respuesta[8] >= 4):
        perfiles["Cliente Frecuente"] += 2
    # Valoracion Negativa de la experiencia
    # Problemas para encontrar la información deseada en la pantalla (4: Negativo o 3: Neutral):
    if (respuesta[11] >= 4):
        perfiles["Cliente Frecuente"] += 3
    # Lentitud en la respuesta de la interfaz a tus acciones
    if (respuesta[12] >= 4):
        perfiles["Cliente Frecuente"] += 4

    ###########################################################
    # Puntos para Cliente Ocasional
    ###########################################################
    # Edad
    if respuesta[0] == '35 años a 54 años':
        perfiles["Cliente Ocasional"] += 2
    if respuesta[0] == '18 años a 34 años':
        perfiles["Cliente Ocasional"] += 4
    # Habilidades tecnologicas
    if respuesta[1] == 'Me siento muy cómodo utilizando dispositivos electrónicos y canales digitales':
        perfiles["Cliente Ocasional"] += 6
    if respuesta[1] == 'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad':
        perfiles["Cliente Ocasional"] += 4
    # Frecuencia
    if (respuesta[2] == 'Mensualmente') or (respuesta[2] == 'Ocasionalmente'):
        perfiles["Cliente Ocasional"] += 12
    # Tipo de transaccion
    if ('Retiro de efectivo' in respuesta[3]):
        perfiles["Cliente Ocasional"] += 5
    if ('Depósito de efectivo' in respuesta[3]):
        perfiles["Cliente Ocasional"] += 2
    # Diseño de interfaz
    if (respuesta[5] == 'Diseño más avanzado que agrupe opciones relacionadas.'):
        perfiles["Cliente Ocasional"] += 4
    # Valoracion Positiva de la experiencia
    # Rapidez de las transacciones
    if (respuesta[6] >= 4):
        perfiles["Cliente Ocasional"] += 4
    # Facilidad de uso
    if (respuesta[7] >= 4):
        perfiles["Cliente Ocasional"] += 3
    # Valoracion Negativa de la experiencia
    # Lentitud en la respuesta de la interfaz a tus acciones
    if (respuesta[12] >= 4):
        perfiles["Cliente Ocasional"] += 3
    # Dificultad en la navegación por las opciones en pantalla
    if (respuesta[9] >= 4):
        perfiles["Cliente Ocasional"] += 3

    # Devolver el perfil con la puntuación más alta
    return max(perfiles, key=perfiles.get)




def clasificador_perfiles(arr_respuestas):

    # Se crea el arreglo que contendra los perfiles a los que se asignaron
    perfiles_asignados = []

    for lista in arr_respuestas:
        aux = clasificar_usuario(lista)
        perfiles_asignados.append(aux)


    return perfiles_asignados


##### PRUEBAS UNITARIOS PARA CLIENTE SENIOR######

class TestClasificarUsuario(unittest.TestCase):

    def test_cliente_senior_1(self):
        respuesta = ['Mas de 54 años',
                    'Suelo tener dificultades para utilizar dispositivos electrónicos y canales digitales',
                    'Mensualmente',
                    'Retiro de efectivo',
                    'Grande',
                    'Diseño simple con opciones básicas claramente visibles',
                    5, 5, 5, 4, 4, 4, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Senior")

    def test_cliente_senior_2(self):
        respuesta = ['Mas de 54 años',
                    'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad',
                    'Ocasionalmente',
                    'Consulta de saldo',
                    'Grande',
                    'Diseño simple con opciones básicas claramente visibles',
                    4, 4, 4, 3, 3, 3, 3]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Senior")

    def test_cliente_senior_3(self):
        respuesta = ['Mas de 54 años',
                    'Suelo tener dificultades para utilizar dispositivos electrónicos y canales digitales',
                    'Mensualmente',
                    'Depósito de efectivo',
                    'Mediano',
                    'Diseño simple con opciones básicas claramente visibles',
                    4, 4, 4, 3, 3, 3, 3]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Senior")

    def test_cliente_senior_4(self):
        respuesta = ['Mas de 54 años',
                    'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad',
                    'Mensualmente',
                    'Retiro de efectivo',
                    'Mediano',
                    'Diseño simple con opciones básicas claramente visibles',
                    5, 5, 4, 3, 3, 3, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Senior")

    def test_cliente_senior_5(self):
        respuesta = ['Mas de 54 años',
                    'Suelo tener dificultades para utilizar dispositivos electrónicos y canales digitales',
                    'Ocasionalmente',
                    'Consulta de saldo',
                    'Grande',
                    'Diseño simple con opciones básicas claramente visibles',
                    4, 4, 5, 4, 4, 3, 3]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Senior")

    def test_cliente_frecuente_1(self):
        respuesta = ['Entre 35 y 54 años',
                    'Estoy completamente familiarizado con los dispositivos electrónicos y canales digitales',
                    'Semanalmente',
                    'Transferencia entre cuentas propias',
                    'Mediano',
                    'Diseño moderno con múltiples opciones',
                    3, 4, 3, 4, 3, 5, 5]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Frecuente")

    def test_cliente_frecuente_2(self):
        respuesta = ['Entre 35 y 54 años',
                    'Estoy completamente familiarizado con los dispositivos electrónicos y canales digitales',
                    'Diariamente',
                    'Pago de servicios',
                    'Pequeño',
                    'Diseño moderno con múltiples opciones',
                    3, 3, 4, 4, 4, 4, 5]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Frecuente")

    def test_cliente_frecuente_3(self):
        respuesta = ['Entre 18 y 34 años',
                    'Estoy completamente familiarizado con los dispositivos electrónicos y canales digitales',
                    'Diariamente',
                    'Transferencia a terceros',
                    'Mediano',
                    'Diseño moderno con múltiples opciones',
                    3, 4, 3, 3, 4, 5, 5]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Frecuente")

    def test_cliente_frecuente_4(self):
        respuesta = ['Entre 35 y 54 años',
                    'Estoy completamente familiarizado con los dispositivos electrónicos y canales digitales',
                    'Diariamente',
                    'Consulta de saldo',
                    'Pequeño',
                    'Diseño moderno con múltiples opciones',
                    3, 3, 3, 4, 3, 5, 4]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Frecuente")

    def test_cliente_frecuente_5(self):
        respuesta = ['Entre 18 y 34 años',
                    'Estoy completamente familiarizado con los dispositivos electrónicos y canales digitales',
                    'Semanalmente',
                    'Pago de tarjetas de crédito',
                    'Pequeño',
                    'Diseño moderno con múltiples opciones',
                    3, 3, 4, 4, 4, 4, 5]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Frecuente")

    def test_cliente_ocasional_1(self):
        respuesta = ['Entre 18 y 34 años',
                     'Tengo habilidades avanzadas en tecnología',
                     'Ocasionalmente',
                     'Consulta de saldo',
                     'Pequeño',
                     'Diseño moderno con múltiples funcionalidades',
                     3, 3, 2, 2, 2, 3, 1]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Ocasional")

    def test_cliente_ocasional_2(self):
        respuesta = ['Entre 18 y 34 años',
                     'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad',
                     'Mensualmente',
                     'Transferencia entre cuentas propias',
                     'Pequeño',
                     'Diseño moderno con múltiples funcionalidades',
                     2, 2, 2, 1, 1, 2, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Ocasional")

    def test_cliente_ocasional_3(self):
        respuesta = ['Entre 35 y 54 años',
                     'Suelo tener dificultades para utilizar dispositivos electrónicos y canales digitales',
                     'Ocasionalmente',
                     'Retiro de efectivo',
                     'Mediano',
                     'Diseño moderno con múltiples funcionalidades',
                     3, 2, 2, 3, 3, 2, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Ocasional")

    def test_cliente_ocasional_4(self):
        respuesta = ['Entre 18 y 34 años',
                     'Tengo habilidades avanzadas en tecnología',
                     'Ocasionalmente',
                     'Consulta de saldo',
                     'Pequeño',
                     'Diseño simple con opciones básicas claramente visibles',
                     3, 2, 1, 2, 2, 2, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Ocasional")

    def test_cliente_ocasional_5(self):
        respuesta = ['Entre 35 y 54 años',
                     'Tengo algunas habilidades tecnológicas y puedo utilizar dispositivos electrónicos y canales digitales con cierta facilidad',
                     'Mensualmente',
                     'Depósito de efectivo',
                     'Mediano',
                     'Diseño moderno con múltiples funcionalidades',
                     3, 2, 3, 3, 3, 2, 2]
        self.assertEqual(clasificar_usuario(respuesta), "Cliente Ocasional")


def main():
    # Se preprocesa el archivo de encuesta de los usuarios de cajeros ATM
    respuestas_usuarios = leer_archivo_encuesta()
    # Se aplica el clasificador basado en reglas para clasificar a los usuarios
    usuarios_clasificados = clasificador_perfiles(respuestas_usuarios)

    print(usuarios_clasificados)

# Si este script se ejecuta como principal, llamamos a la función main y a los test unitarios
if __name__ == "__main__":
    main()
    unittest.main()