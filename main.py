from mindstorms import MSHub, DistanceSensor
from mindstorms.control import Timer
import math

# Inicializa o hub do LEGO MINDSTORMS.
hub = MSHub()

# Emite um sinal sonoro para indicar o início do programa.
hub.speaker.beep()

# Inicializa o primeiro sensor ultrassônico na porta A.
ultra1 = DistanceSensor('A')

# Inicializa o segundo sensor ultrassônico na porta B.
ultra2 = DistanceSensor('B')

# Cria um temporizador para medir o tempo entre
# a detecção do objeto pelos dois sensores.
tempo = Timer()


# Função responsável por realizar as medições e os cálculos.
def calculos():
    while True:

        # Aguarda o objeto chegar a menos de 10 cm do primeiro sensor.
        ultra1.wait_for_distance_closer_than(10, 'cm')

        # Reinicia o cronômetro quando o objeto passa pelo primeiro sensor.
        tempo.reset()

        # Aguarda o objeto chegar a menos de 10 cm do segundo sensor.
        ultra2.wait_for_distance_closer_than(10, 'cm')

        # Obtém o tempo decorrido entre as duas detecções.
        tn = tempo.now()

        # Exibe o tempo medido em segundos.
        print(tn, 's')

        # Calcula a velocidade média:
        # velocidade = distância / tempo
        vm = 24.5 / tn

        # Exibe a velocidade média em metros por segundo.
        print('velocidade_media:', vm, 'm/s')

        # Define o ângulo utilizado no cálculo da aceleração.
        angulo = 60

        # Converte o ângulo de graus para radianos,
        # unidade utilizada pela função seno.
        radianos = math.radians(angulo)

        # Calcula o seno do ângulo.
        seno = math.sin(radianos)

        # Exibe o valor do seno calculado.
        print('seno de', angulo, 'é', seno)

        # Define o valor da aceleração da gravidade.
        grav = 9.81

        # Calcula a aceleração:
        # aceleração = gravidade × seno do ângulo
        acel = grav * seno

        # Exibe a aceleração calculada em m/s².
        print('aceleração:', acel, 'm/s²')