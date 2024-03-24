#importando SQLITE3
import sqlite3

#criando conexao
try:
    conexao = sqlite3.connect('cadastro_pcs.db')
    cursor = conexao.cursor()
    print('---Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print(f'---Erro ao conectar com o banco de dados: {e}')    

#criando tabela de unidade:
try:
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS unidades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sigla TEXT
        )''' )
        print('---Tabela unidades criada com sucesso!')
except sqlite3.Error as e:
    print(f'---Erro ao criar a tabela unidades: {e}')

#criando tabela de setores:
try:
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS setores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            unidade TEXT,
            ramal TEXT,
            FOREIGN KEY (unidade) REFERENCES unidades (sigla) ON UPDATE CASCADE ON DELETE CASCADE
        )''' )
        print('---Tabela Setores criada com sucesso!')
except sqlite3.Error as e:
    print(f'---Erro ao criar a tabela setores: {e}')
    
#criando tabela de pcs:
try:
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS computadores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bmp TEXT,
            setor TEXT,
            ramal REAL,
            solicitador TEXT,
            telefone TEXT,
            data_solicitado DATE,
            problema TEXT,
            pronto BOOLEAN,
            data_retirada DATE,
            retirado TEXT,
            FOREIGN KEY (setor) REFERENCES setores (nome) ON DELETE CASCADE
        )''' )
        print('---Tabela computadores criada com sucesso!')
except sqlite3.Error as e:
    print(f'---Erro ao criar a tabela computadores: {e}')  
    
