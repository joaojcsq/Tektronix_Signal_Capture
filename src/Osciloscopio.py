import pyvisa as visa
import numpy as np
import rede

class Capturar():

    def __init__(self):

        self.rm = visa.ResourceManager()
        # Open a connection to the oscilloscope
        # self.scope = self.rm.open_resource("USB0::0x0699::0x03C4::C023657::INSTR", timeout=20000) #SENAI
        self.scope = self.rm.open_resource("USB0::0x0699::0x03A6::C019892::INSTR", timeout=20000) #IFBA
        self.classi = rede.Classificadr()

        print("Conectado")
    
    def config(self):
        self.scope.write("DAT:ENC RPB")
        self.scope.write("DAT:WID 1")
        self.scope.write("DAT:SOU CH1")
        self.scope.write("DAT:STAR 1")
        self.scope.write("DAT:STOP 2500")
        self.scope.write("ACQ:STOPA SEQ")
        self.scope.write("ACQ:AVER ON")
        self.scope.write("ACQ:NUMAV 16")
        
        # Get the waveform parameters
        self.scope.write("WFMPRE:XZE?")
        self.xzero = float(self.scope.read())
        self.scope.write("WFMPRE:XIN?")
        self.xincr = float(self.scope.read())
        self.scope.write("WFMPRE:YZE?")
        self.yzero = float(self.scope.read())
        self.scope.write("WFMPRE:YMU?")
        self.ymult = float(self.scope.read())
        self.scope.write("WFMPRE:YOF?")
        self.yoff = float(self.scope.read())


    def FormaDeOnda(self,diretorio=None, nome_arquivo=None, salvar=None):
        # self.scope.write("DAT:ENC RPB")
        # self.scope.write("DAT:WID 1")
        # self.scope.write("DAT:SOU CH1")
        # self.scope.write("DAT:STAR 1")
        # self.scope.write("DAT:STOP 2500")
        # self.scope.write("ACQ:STOPA SEQ")
        # self.scope.write("ACQ:AVER ON")
        # self.scope.write("ACQ:NUMAV 16")

        # Get the waveform parameters
        # self.scope.write("WFMPRE:XZE?")
        # self.xzero = float(self.scope.read())
        # self.scope.write("WFMPRE:XIN?")
        # self.xincr = float(self.scope.read())
        # self.scope.write("WFMPRE:YZE?")
        # self.yzero = float(self.scope.read())
        # self.scope.write("WFMPRE:YMU?")
        # self.ymult = float(self.scope.read())
        # self.scope.write("WFMPRE:YOF?")
        # self.yoff = float(self.scope.read())


        # Read the waveform data from the oscilloscope
        waveform_data = self.scope.query_binary_values("CURV?", datatype="B")

        # Convert the binary data to a numpy array
        waveform_array = np.array(waveform_data)

        # Scale the waveform data
        waveform_array = (waveform_array - self.yoff) * self.ymult + self.yzero

        # Create a time array to match the waveform data
        time_array = np.arange(len(waveform_data)) * self.xincr + self.xzero
        


        if max(waveform_array) >= 1:
            if salvar == 1:
                # Save the waveform data and time array as a CSV file
                data = np.column_stack((time_array, waveform_array))
                header = "Time,Amplitude"
                path = diretorio + nome_arquivo + ".csv"
                np.savetxt(path, data, delimiter=",", header=header)
                self.classi.classificar(sinal=waveform_array.reshape(1,-1))
            else:
                return waveform_array, time_array
        else:
            print("Sinal com baixa amplitude")
            return False
        
    def FecharConexao(self):
        self.scope.close()
        self.rm.close()
    
    def Run(self):
        # self.scope.write("FPANEL:PRESS AUTOSET")
        # self.scope.write(":RUN")
        # print(self.scope.write("ACQUIRE:STATE?"))
        # import time
        # # self.scope.write(":ACQUIRE:STOPAfter RUNSTop")
        # time.sleep(0.5)
        self.scope.write("ACQUIRE:State RUN")
        # teste = self.scope.write("MEASUREMENT?")
        # print(teste)
        # print("RUN")


# if __name__ == "__main__":
#     dado = Capturar()
#     dado.FormaDeOnda()
