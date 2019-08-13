import os
import random
import string
import time
import subprocess

class pdfFile:

    def __init__(self , caminho = None ):
        
        if caminho != None:
            self.atalizaPdf(caminho)
            self.arquivoTxtCaminho()
        self._info = None
        self.arquivoSaidaTxt = None
        self._arquivoTxtCaminho = None
        
        diretorioAtual = os.getcwd()
        os.system("cd " + diretorioAtual + " ; echo " " > pdftotext.log" )
        
    def close(self ):
        if self._info != None:
            os.system("cd /tmp rm " + self._info )
    
    def arquivoTxtCaminho(self):
        if self._arquivoTxtCaminho == None:
            self._arquivoTxtCaminho = self.getCaminhoAleatorio()
        
        return self._arquivoTxtCaminho
        
    def atalizaPdf( self , caminho ):
        self.caminhoPdf =  caminho

        arq = open(caminho,"rb")
        arqBytes = arq.read(5)
        arq.close()

        if "PDF" in arqBytes.decode("ascii"):
            self.valido = True
        else:
            self.valido = False

    def getText(self, atalizaPdf = None, cont = 0):
        if atalizaPdf != None:
            self.atalizaPdf(atalizaPdf)
        if self.valido == True:
            

            caminhoSaida = self.arquivoTxtCaminho()
            
            comando = "pdftotext "+ atalizaPdf + " " + caminhoSaida + " 2>> pdftotext.log"


            
            
            os.system( comando )

            flag = False
            for i in range( 0 , 101 ):
                if os.path.isfile( caminhoSaida ):
                    flag = True
                    break
                else:
                    if i % 10 == 0:
                        print( i,  comando  )
                    time.sleep(i/500)
            
            
            if flag == True:
                arq = open(caminhoSaida, "r")
                text = arq.read()
                arq.close()

                os.system("rm " + self.arquivoTxtCaminho() )
            else:
                print("erro: log")
                arq = open(caminhoSaida, "a")
                arq.write( f"erro: {atalizaPdf}{caminhoSaida}")
                arq.close()
                return ""
            return text
    
    def getCaminhoAleatorio(self):
        s = "/tmp/"
        for i in range(0,15):
            s += random.choice(string.ascii_letters)
        
        return s
