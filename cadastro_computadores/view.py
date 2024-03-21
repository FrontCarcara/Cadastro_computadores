#importando SQLITE3
import sqlite3

#criando conexao
try:
    conexao = sqlite3.connect('cadastro_pcs.db')
    cursor = conexao.cursor()
    print('---Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print(f'---Erro ao conectar com o banco de dados: {e}')    
    
    
#Tabela de Unidade---------------------------------------------

#Criar Unidades(Inserir C) CRUD
def criar_unidades(i):
         with conexao:
             cursor = conexao.cursor()
             query = "INSERT INTO unidades (nome, sigla) VALUES (?,?)"
             cursor.execute(query, i)
             
#criar_unidades(['BASE AEREA DE SÃO PAULO','BASP','DOMBASP'])
#Ver todas as unidades (Read R) CRUD
def ver_unidades():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM unidades')
        linha = cursor.fetchall()
        
        for i in linha:
            lista.append(i)
        return lista

#Atualizar Unidades(Update U) CRUD
def atulizar_unidades(i):
         with conexao:
             cursor = conexao.cursor()
             query = "UPDATE unidades SET nome =?, unidade =? WHERE id=?"
             cursor.execute(query, i)
l = ['BASE AEREA DE SAO PAULO','BASP','DOMBASP', 1]
#atulizar_unidades(l)
#print(ver_unidades())

# Deletar as unidade (Delete D) CRUD
def deletar_unidades(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM unidades WHERE id=?"
        cursor.execute(query, i)
deletar_unidades([1])
