NOME=['JOHNNY','SULISTA','JULIO']
IDADE=[26,41,26]
PESO=[140,98,56]
ALTURA=[1.96,1.78,1.70]
IMC=[36.443,30.93,29.45]
def getche():
    x=input("ENTER para continuar...")

def menu():
    print("*********MENU***********")
    print("Escolha uma opçao:")
    print("1 - incluir aluno")
    print("2 - listar todos alunos")
    print("3 - listar dados de alunos por idade")
    print("4 - listar dados de  um aluno ")
    print("9 - fim")

def incluir():
    nome=input("digite o nome do aluno: ")
    while(nome):
        try:
            nome=nome.upper()
            idade=int(input("digite a idade do "+nome+":"))
            peso=int(input("digite o peso do "+nome+":"))
            altura=float(input("digite a ALTURA com ponto "+nome+":"))
            imc=(peso/(altura*altura))
            NOME.append(nome)
            IDADE.append(idade)
            PESO.append(peso)
            ALTURA.append(altura)
            x=round(imc,3)
            IMC.append(x)
        except:
            print("use ponto na altura!!")
            getche()
        nome=input("digite o nome do aluno: ")

def listar():
    print("@"*15," LISTA ",len(NOME),"@"*15)
    mediaimc=.0
    for i in range(len(IDADE)):
        print(NOME[i],"|IDADE|",IDADE[i],"|PESO|:",PESO[i],"|ALTURA|",ALTURA[i],"|IMC|",IMC[i])
        mediaimc=(mediaimc+IMC[i])
    Tamanholista=len(IMC)
    MDA=(mediaimc/Tamanholista)
    print(round(MDA,3))
    print("@"*10)

def listaraluno():
    nome=input("digite o nome do aluno que deseja procurar:")
    nome=nome.upper()
    try:
        i=NOME.index(nome)
        print(NOME[i],"|IDADE|",IDADE[i],"|PESO|:",PESO[i],"|ALTURA|",ALTURA[i],"|IMC|",IMC[i])
    except:
        print("digite letras maisculas.")
        print("produto nao encontrado!")

def listaidade():
    posicao=[]
    igrup=(int(input("digite a idade que deseja: ")))
    imcidade=.0
    for i in range(len(IDADE)):
        if IDADE[i] ==igrup:
            posicao.append(i)
    for i in range (len(posicao)):
        print(NOME[posicao[i]],"|IDADE|",IDADE[posicao[i]],"|PESO|:",PESO[posicao[i]],"|ALTURA|",ALTURA[posicao[i]],"|IMC|",IMC[posicao[i]])
        imcidade=(imcidade+IMC[posicao[i]])
    print(imcidade/len(posicao))
    







op=0
while op!=9:
    menu()
    try:
        op=int(input())
    except:
        print("digite opçoes listada a cima!")
        getche()
    if op==1:
        incluir()
    elif op==2:
        listar()
    elif op==4:
        listaraluno()
    elif op==3:
        listaidade()

