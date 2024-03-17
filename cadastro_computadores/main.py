#importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#importando pillow
from PIL import ImageTk, Image


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


#Criando janela
janela = Tk()
janela.title("")
janela.geometry("850x620")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('cadastro_computadores/imagens/BASP-DOM.ico')

style = Style(janela)
style.theme_use("clam")

#Criando frames

#frame azul do topo
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row= 0, column=0, pady= 0, padx= 0, sticky=NSEW)

#separador do frame
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

#frame branco apos o azul
frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row= 2, column=0, pady= 0, padx= 0, sticky=NSEW)

#separador do frame
ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

#frame detalhes
frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4,column=0,padx=10,pady=0,sticky=NSEW)

#frame tabela
frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5,column=0,padx=10,pady=0,sticky=NSEW)


#Trabalhando no frame logo ------------------------------------
app_lp = Image.open('cadastro_computadores/imagens/logo.png')
app_lp = app_lp.resize((50,50))
app_lp = ImageTk.PhotoImage(app_lp)
app_logo = Label(frame_logo, image=app_lp, text='Sistema de cadastro de computadores', width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), background=co6, fg=co1, padx=10)
app_logo.place(x=0, y=0)

#Função para cadastrar computadores
def computadores():
    print('Compudores')

#detalhes da unidade --------------------------------------------------------------------
#Função para adicionar unidades e setores FRAMES
def adicionar():
    #Criando frames para tabela---------
    frame_tabela_unidade = Frame(frame_tabela, width=300,height=200,bg=co1)
    frame_tabela_unidade.grid(row=0,column=0,pady=0,padx=0,sticky=NSEW)
    
    #linha divisoria 
    frame_tabela_linha= Frame(frame_tabela, width=30,height=200,bg=co1)
    frame_tabela_linha.grid(row=0,column=1,pady=0,padx=10,sticky=NSEW)
    
    frame_tabela_setores = Frame(frame_tabela, width=300,height=200,bg=co4)
    frame_tabela_setores.grid(row=0,column=2,pady=0,padx=0,sticky=NSEW)
    
    #inserir unidade botão
    l_nome = Label(frame_detalhes, text="Nome da Unidade", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4,y=10)
    e_nome_unidade = Entry(frame_detalhes, width=35, justify='left', relief='solid')    
    e_nome_unidade.place(x=7, y=40) 
    
     #inserir sigla botão
    l_sigla = Label(frame_detalhes, text="Sigla da Unidade", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_sigla.place(x=4,y=70)
    e_sigla_unidade = Entry(frame_detalhes, width=20, justify='left', relief='solid')    
    e_sigla_unidade.place(x=7, y=100) 
    
    #inserir dom botão
    l_dom = Label(frame_detalhes, text="Dom da Unidade", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_dom.place(x=4, y=130)

# Função para selecionar imagem
    def selecionar_imagem():
        filename = filedialog.askopenfilename()  # Abre uma janela para o usuário selecionar uma imagem
        if filename:
            carregar_imagem(filename)

    def carregar_imagem(filename):
        global imagem_label
        imagem = Image.open(filename)
        imagem = imagem.resize((100, 100), Image.ANTIALIAS)  # Redimensiona a imagem conforme necessário
        imagem = ImageTk.PhotoImage(imagem)
        imagem_label.configure(image=imagem)
        imagem_label.image = imagem  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector

    # Botão para selecionar imagem
    btn_selecionar_imagem = Button(frame_detalhes, text="Selecionar Imagem", command=selecionar_imagem)
    btn_selecionar_imagem.place(x=7, y=160)

    # Label para exibir a imagem selecionada
    imagem_label = Label(frame_detalhes)
    imagem_label.place(x=120, y=160)

    #botões carregar, salvar, deletar
    
    #botão salvar
    botao_salvar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=147, y=160)
    
    #botão atualizar
    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=227, y=160)
    
    #botão Deletar
    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=307, y=160)
   
    
    #Tabela unidades
    def mostrar_unidades():
        app_nome = Label(frame_tabela_unidade, text="Tabela de unidades", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','Sigla','Unidade','Dom']

        df_list = []

        global tree_unidade

        tree_unidade = ttk.Treeview(frame_tabela_unidade, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_unidade, orient="vertical", command=tree_unidade.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_unidade, orient="horizontal", command=tree_unidade.xview)

        tree_unidade.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_unidade.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_unidade.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[90,150,80,60]
        n=0

        for col in list_header:
            tree_unidade.heading(col, text=col.title(), anchor=NW)
        #adjust the column's width to the header string
            tree_unidade.column(col, width=h[n],anchor=hd[n])

        n+=1

        for item in df_list:
            tree_unidade.insert('', 'end', values=item)

    mostrar_unidades()


    #Linha separadora / parte de cima ----------------------------------------------------------
    
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=410, y=5)    
    
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=408, y=5)  
    
    
    #Linha separadora / parte de baixo / tabela----------------------------------------------------------
    
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=150, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=22, y=0)    
    
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=150, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=20, y=0) 
    
    #detalhes do setor -----------------------------------------------------------------
    
    #entrada de setor
    l_nome = Label(frame_detalhes, text="Nome do Setor", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=424,y=10)
    e_nome_setor = Entry(frame_detalhes, width=35, justify='left', relief='solid')    
    e_nome_setor.place(x=427, y=40) 
    
    #entrada de setor
    l_setor = Label(frame_detalhes, text="Setor", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_setor.place(x=424,y=10)
    
#Funçâo para salvar
def salvar():
    print('Salvar')



#Função de controle ------------------------------------------------
def control(i):
    #cadastro de computador
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
            
    #chamando a fução computadores    
        computadores()
    
    #adicionar     
    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
    
    #chamando a função de adicionar        
        adicionar()  
    
    #salvar   
    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
    
    #chamando a função de salvar      
        salvar()
        
#Criando botões

#botão de cadastro
app_img_cadastro = Image.open('cadastro_computadores/imagens/plus.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command= lambda:control('cadastro'), image=app_img_cadastro, text='Cadastro', width=80, compound=LEFT, overrelief= RIDGE, font=('Ivy 11'), background=co1, fg=co0, padx=7)
app_cadastro.place(x=10, y=30)

#botão de adicioar
app_img_adicinar = Image.open('cadastro_computadores/imagens/plus.png')
app_img_adicinar = app_img_adicinar.resize((18,18))
app_img_adicinar = ImageTk.PhotoImage(app_img_adicinar)
app_adicionar = Button(frame_dados, command= lambda:control('adicionar'), image=app_img_adicinar, text='Adicionar', width=80, compound=LEFT, overrelief= RIDGE, font=('Ivy 11'), background=co1, fg=co0, padx=7)
app_adicionar.place(x=123, y=30)


#botão de salvar
app_img_salvar = Image.open('cadastro_computadores/imagens/save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command= lambda:control('salvar'), image=app_img_salvar, text='Salvar', width=80, compound=LEFT, overrelief= RIDGE, font=('Ivy 11'), background=co1, fg=co0, padx=7)
app_salvar.place(x=237, y=30)




















janela.mainloop()
