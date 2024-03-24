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
             query = "UPDATE unidades SET nome =?, sigla =? WHERE id=?"
             cursor.execute(query, i)

# Deletar as unidade (Delete D) CRUD
def deletar_unidades(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM unidades WHERE id=?"
        cursor.execute(query, i)
deletar_unidades([1])

#COMANDOS DE SETOR CRUD--------------------------------------------------------------------------
#Criar Unidades(Inserir C) CRUD
def criar_setor(i):
         with conexao:
             cursor = conexao.cursor()
             query = "INSERT INTO setores (nome, unidade, ramal) VALUES (?,?,?)"
             cursor.execute(query, i)
             

#Ver todas as setores (Read R) CRUD
def ver_setores():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM setores')
        linha = cursor.fetchall()
        
        for i in linha:
            lista.append(i)
        return lista

#Atualizar setores(Update U) CRUD
def atulizar_setores(i):
         with conexao:
             cursor = conexao.cursor()
             query = "UPDATE setores SET nome =?, unidade=?, ramal =? WHERE id=?"
             cursor.execute(query, i)

# Deletar as unidade (Delete D) CRUD
def deletar_setores(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM setores WHERE id=?"
        cursor.execute(query, i)
deletar_setores([1])

#COMANDOS DE COMPUTADORES CRUD--------------------------------------------------------------------------
#Criar Unidades(Inserir C) CRUD
def criar_computadores(i):
         with conexao:
             cursor = conexao.cursor()
             query = "INSERT INTO computadores (setor, bmp, ramal, data_solicitado, data_retirada, solicitador, retirado, problema, telefone, pronto) VALUES (?,?,?,?,?,?,?,?,?,?)"
             cursor.execute(query, i)
             

#Ver todas as computadores (Read R) CRUD
def ver_computadores():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM computadores')
        linha = cursor.fetchall()
        
        for i in linha:
            lista.append(i)
        return lista

#Atualizar computadores(Update U) CRUD
def atulizar_computadores(i):
         with conexao:
             cursor = conexao.cursor()
             query = "UPDATE computadores SET setor =?, bmp=?, ramal =?, data_solicitado =?, data_retirada =?, solicitador=?, retirado=?, problema=?, telefone=?, pronto=? WHERE id=?"
             cursor.execute(query, i)

# Deletar as unidade (Delete D) CRUD
def deletar_computadores(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM computadores WHERE id=?"
        cursor.execute(query, i)
deletar_computadores([1])

#função procurar computador
def procurar_computador(solicitador):
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM computadores WHERE solicitador =?', (solicitador,))
        dados = cursor.fetchall()
                
        return dados

