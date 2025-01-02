# import GerarPulso

# esp = GerarPulso.Esp32Pwm("COM5")
# # esp.conectar()
# esp.enviar_dados(frequencia=100, dutycycle=52)
# esp.desconectar()


import Osciloscopio
# from time import sleep

dado = Osciloscopio.Capturar()
dado.config()

for i in range(900):

    dado.Run()
    
    dado.FormaDeOnda(diretorio=r"C:/Users/joao.queiroz/Desktop/Sinais_/180min/", nome_arquivo="Sinal_IFBA_" + str(i) , salvar=1)

    if dado.FormaDeOnda(diretorio=r"C:/Users/joao.queiroz/Desktop/Sinais_/180min/", nome_arquivo="Sinal_IFBA_" + str(i) , salvar=1) == False:
        i = i - 1

    dado.Run()

dado.FecharConexao()
