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

    def getText(self, atalizaPdf = None, cont = 0):
        
        if atalizaPdf != None:
            self.atalizaPdf(atalizaPdf)

        caminhoSaida = self.arquivoTxtCaminho()
        diretorioAtual = os.getcwd()
        os.system( "pdftotext "+ atalizaPdf + " " + caminhoSaida + " 2>> pdftotext.log" )


        arq = open(caminhoSaida, "r")
        text = arq.read()
        arq.close()

        os.system("rm " + self.arquivoTxtCaminho() )

        return text
    
    def getCaminhoAleatorio(self):
        s = "/tmp/"
        for i in range(0,15):
            s += random.choice(string.ascii_letters)
        
        return s