import numpy as np
import tensorflow as tf

class Classificadr():

    def __init__(self):
        self.model = tf.keras.models.load_model(r'C:\Users\joao.queiroz\Desktop\osc\scr\modelo_1.keras')
        print("Modelo carregado")
    
    def classificar(self, sinal):
        predicao = self.model.predict(sinal)
        classe_predita = np.argmax(predicao)
        print(f"A classe predita para o novo sinal é: {classe_predita}")


        

    # Carrega o modelo treinado
    # model = tf.keras.models.load_model(r'C:\Users\joao.queiroz\Desktop\osc\scr\modelo_1.keras')

    # # Exemplo de um novo sinal (substitua pelos seus dados reais)
    # novo_sinal = df.iloc[0,:-1].values.reshape(1,-1)

    # # Faz a predição
    # predicao = model.predict(novo_sinal)

    # # Obtém a classe predita (índice da maior probabilidade)
    # classe_predita = np.argmax(predicao)

    # print(f"A classe predita para o novo sinal é: {classe_predita}")