class País:
    #a. Construtor que inicialize o código ISO, o nome e a dimensão do país; 

    def __init__(self,iso,nome,populacao,dimensao,fronteira):
        self.iso = iso
        self.nome = nome
        self.populacao = populacao
        self.dimensao = dimensao
        self.fronteira = fronteira
    
    def get_ISO(self):
        return self.iso
    
    #c. Um método que permita verificar se dois objetos representam o mesmo país (isso se chama igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO; 
    def verificacao(self,iso2):
        if self.iso == iso2:
            return True
        else:
            return False
    #d. Um método que informe se outro país é limítrofe do país que recebeu a mensagem; 
    def limítrofe(self,paises):
        if self.nome in paises:
            return True
        else:
            return False
    #f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países.
    def vizinhos_comuns(self,vizinhos_1,vizinhos_2):
        vizinhos_comuns = []
        for i in range(len(vizinhos_1)):
            if vizinhos_1[i] in vizinhos_2:
                vizinhos_comuns.append(vizinhos_1[i])
        return vizinhos_comuns

    #e. Um método que retorne a densidade populacional do país;
    def calcular_DD(self,habitantes,area):
        DD = habitantes/area
        return DD

    def infos_países(self):
        print('[ISO] - ',self.iso,'\n[NOME] - ',self.nome,'\n[POPULAÇÃO] - ',self.populacao,'\n[DIMENSÃO] - ',self.dimensao,'\n[PAÍSES VIZINHOS] - ',self.fronteira)


p1_s_am = País('BRA','Brasil',214300000,8510000,['Uruguai','Bolívia','Paraguai','Argentina','Venezuela','Peru','Colômbia','Guiana','Suriname','Guiana Francesa'])
DD_BRA = p1_s_am.calcular_DD(p1_s_am.populacao,p1_s_am.dimensao)
p1_s_am.infos_países()
print('Densidade populacional = ','{:.2f}'.format(DD_BRA))
print(' ')

p2_s_am = País('URY','Uruguai',3426000,176215,['Brasil','Argentina'])
DD_URY = p2_s_am.calcular_DD(p2_s_am.populacao,p2_s_am.dimensao)
p2_s_am.infos_países()
print('Densidade populacional = ','{:.2f}'.format(DD_URY))
print(' ')

p3_s_am = País('PRY','Paraguai',6704000,406752,['Brasil','Argentina','Bolívia'])
DD_PRY = p3_s_am.calcular_DD(p3_s_am.populacao,p3_s_am.dimensao)
p3_s_am.infos_países()
print('Densidade populacional = ','{:.2f}'.format(DD_PRY))
vizinhos_c = p3_s_am.vizinhos_comuns(p3_s_am.fronteira,p2_s_am.fronteira)  #Vizinhos comuns entre Paraguai e Uruguai
print(vizinhos_c)
print(' ')


p4_s_am = País('ARG','Argentina',45081000,2780000,['Brasil','Uruguai','Paraguai','Bolívia','Chile'])
DD_ARG = p4_s_am.calcular_DD(p4_s_am.populacao,p4_s_am.dimensao)
vl = p4_s_am.limítrofe(p1_s_am.fronteira) #Verificar se um país faz fronteira com outro
if vl == True:
    print(p4_s_am.nome,'é limítrofe com',p1_s_am.nome)
else:
    print('Países não limítrofes')


p4_s_am.infos_países()
print('Densidade populacional = ','{:.2f}'.format(DD_ARG))
print(' ')

p5_s_am = País('CHL','Chile',19049000,756626,['Argentina','Bolívia','Peru'])
DD_CHL = p5_s_am.calcular_DD(p5_s_am.populacao,p5_s_am.dimensao)
p5_s_am.infos_países()
print('Densidade populacional = ','{:.2f}'.format(DD_CHL))
vl = p5_s_am.limítrofe(p1_s_am.fronteira)
if vl == True:
    print(p5_s_am.nome,'é limítrofe com',p1_s_am.nome)
else:
    print(p5_s_am.nome,' não é limítrofe com', p1_s_am.nome)
print(' ')



p1_euro = País('ITA','Itália',59011000,301230,['França','Áustria','Suiça','Eslovênia',])

p2_euro = País('FRA','França',67075000,551695,['Itália','Espanha','Luxemburgo','Bélgica','Alemanha','Mônaco','Andorra'])
p3_euro = País('LUX','Luxemburgo',640064,2586,['Alemanha','França','Bélgica'])
p4_euro = País('GRC','Grécia',10064000,131957,['Macedônia','Turquia','Albânia','Bulgária'])
p5_euro = País('NLD','Holanda',17053000,41850,['Bélgica','Alemanha'])

class Continente:
    def __init__(self,nome,paises):
        self.nome = nome
        self.paises = paises
        
    def add_paises(self,países):
        self.paises = países
    
    def população_total(self,paises):
        pop_total = 0
        for i in range(len(paises)):
            pop_total += paises[i].populacao
        return pop_total

    def dimensão_total(self,paises):
        dimensao_total = 0
        for i in range(len(paises)):
            dimensao_total += paises[i].dimensao
        return dimensao_total

    def maior_dimen_ter(self,paises):
        maior_dimensao = 0
        maior_país = str
        for i in range(len(paises)):
            if maior_dimensao < paises[i].dimensao:
                maior_dimensao = paises[i].dimensao
                maior_país = paises[i].nome
        return maior_país

    def menor_dimen_ter(self,paises):
        menor_dimensao = 0
        menor_país = str
        for i in range(len(paises)):
            if menor_dimensao > paises[i].dimensao or menor_dimensao == 0:
                menor_dimensao = paises[i].dimensao
                menor_país = paises[i].nome
        return menor_país
    
    def menor_populacao(self,paises):
        menor_populacao = 0
        menor_país = str
        for i in range(len(paises)):
            if menor_populacao > paises[i].populacao or menor_populacao == 0:
                menor_populacao = paises[i].populacao
                menor_país = paises[i].nome
        return menor_país

    def maior_populacao(self,paises):
        maior_populacao = 0
        maior_país = str
        for i in range(len(paises)):
            if maior_populacao < paises[i].populacao:
                maior_populacao = paises[i].populacao
                maior_país = paises[i].nome
        return maior_país
    
    def razao_territorial(self,paises):
        menor_dimensao = 0
        maior_dimensao = 0
        for i in range(len(paises)):
            if menor_dimensao > paises[i].dimensao or menor_dimensao == 0:
                menor_dimensao = paises[i].dimensao
            else:
                maior_dimensao = paises[i].dimensao

        r_t = maior_dimensao/menor_dimensao
        return r_t
Am_Sul = Continente('América do Sul',[])
amsul = [p1_s_am,p2_s_am,p3_s_am,p4_s_am,p5_s_am]
Am_Sul.add_paises(amsul)

Euro = Continente('Europa',[])
euro = [p1_euro,p2_euro,p3_euro,p4_euro,p5_euro]
Euro.add_paises(euro)


print("[AMÉRICA DO SUL]")
maior_populacao = Am_Sul.maior_populacao(Am_Sul.paises)
menor_populacao = Am_Sul.menor_populacao(Am_Sul.paises)
maior_dimensão = Am_Sul.maior_dimen_ter(Am_Sul.paises)
menor_dimensão = Am_Sul.menor_dimen_ter(Am_Sul.paises)
pop_total = Am_Sul.população_total(Am_Sul.paises)
di_total = Am_Sul.dimensão_total(Am_Sul.paises)
razao_ter = Am_Sul.razao_territorial(Am_Sul.paises)
print('Dimensão total do continente: ',di_total,'\nPopulação total do continente:',pop_total,'\nPaís com a maior população: ',maior_populacao,'\nPaís com a menor população: ',menor_populacao,'\nPaís com a maior dimensão territorial: ',maior_dimensão,'\nPaís com a menor dimensão territorial: ',menor_dimensão,'\nRazão territorial entre o maior e menor país do continente: {:.2f}'.format(razao_ter))
print(' ')

print('[EUROPA]')
maior_populacao = Euro.maior_populacao(Euro.paises)
menor_populacao = Euro.menor_populacao(Euro.paises)
maior_dimensão = Euro.maior_dimen_ter(Euro.paises)
menor_dimensão = Euro.menor_dimen_ter(Euro.paises)
pop_total = Euro.população_total(Euro.paises)
di_total = Euro.dimensão_total(Euro.paises)
razao_ter = Euro.razao_territorial(Euro.paises)
print('Dimensão total do continente: ',di_total,'\nPopulação total do continente:',pop_total,'\nPaís com a maior população: ',maior_populacao,'\nPaís com a menor população: ',menor_populacao,'\nPaís com a maior dimensão territorial: ',maior_dimensão,'\nPaís com a menor dimensão territorial: ',menor_dimensão,'\nRazão territorial entre o maior e menor país do continente: {:.2f}'.format(razao_ter))
print(' ')