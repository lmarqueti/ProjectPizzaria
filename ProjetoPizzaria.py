from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import pymysql.cursors
from tkinter import ttk

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

class AdminJanela():

    def RegistrarPedidos(self):

        self.registrar = Tk()
        self.registrar.title('Registro de Pedidos')
        self.registrar['bg'] = '#524f4f'

        nomeProdutos = []
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                produtos = cursor.fetchall()
        except:
            print('erro ao conectar db')
        for i in produtos:
            nomeProdutos.append(i['nome'])

        ingred = "minha nossa"

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                produtos = cursor.fetchall()
        except:
            print('erro ao conectar db2')

        for h in range(0, len(produtos)):
            if nomeProdutos == i['nome']:
                ingred.append(i['ingredientes'])
            break

        grup = ["comprado"]
        grup.clear()
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                produtos = cursor.fetchall()
        except:
            print('erro ao conectar db2')

        for h in range(0, len(produtos)):
            if nomeProdutos == i['nome']:
                grup.append(i['grupo'])
            break

        Label(self.registrar, text='Lançar Produtos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4,padx=5, pady=5)

        Label(self.registrar,text='Produto:', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5,pady=5)
        self.produto = ttk.Combobox(self.registrar,values=nomeProdutos, width=15)
        #pprint(dict(self.produto))
        self.produto.grid(row=1, column=1, padx=5, pady=5)
        self.produto.current()

        Label(self.registrar, text=('Ingredientes:',ingred), bg='#524f4f', fg='white').grid(row=2, column=0, padx=5)
        '''self.ingredenteR = Entry(self.registrar)
        self.ingredenteR.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        self.ingredenteR.insert(0, ingred)'''

        Label(self.registrar, text='Grupo:', bg='#524f4f', fg='white').grid(row=2, column=1, padx=5)
        '''self.grupoR = Entry(self.registrar)
        self.grupoR.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
        self.grupoR.insert(0, grup)'''

        Label(self.registrar, text='Quantidade:', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.quantidade = Entry(self.registrar)
        self.quantidade.grid(row=4, column=1, columnspan=2,padx=5, pady=5)

        Label(self.registrar, text='Observações:', bg='#524f4f', fg='white').grid(row=5, column=0, columnspan=1, padx=5,pady=5)
        self.obs = Entry(self.registrar)
        self.obs.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        Label(self.registrar, text='Local:', bg='#524f4f', fg='white').grid(row=6, column=0, columnspan=1, padx=5,pady=5)
        self.local = Entry(self.registrar)
        self.local.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

        Button(self.registrar, text='Lançar', highlightbackground='#524f4f', bg='gray', relief='flat', width=15, command=self.RegistrarPedidosBackEnd).grid(row=7, column=0, padx=5, pady=5)
        Button(self.registrar, text='Excluir', highlightbackground='#524f4f', bg='gray', relief='flat', width=15, command=self.ExcluirPedidosBackEnd).grid(row=7, column=1, padx=5, pady=5)
        Button(self.registrar, text='Limpar', highlightbackground='#524f4f', bg='gray', relief='flat',width=15, command= self.LimparRegistrosPedidos).grid(row=8, column=0,columnspan=2, padx=5, pady=5)

        self.tree = ttk.Treeview(self.registrar, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=150, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Produto')

        self.tree.column('column2', width=150, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Observações')

        self.tree.column('column3', width=150, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Local de Entrega')

        self.tree.column('column4', width=50, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='QTD')

        self.tree.grid(row=0, column=4, columnspan=2 , padx=10, pady=10, rowspan=7)

        self.MostrarPedidos()

        self.registrar.mainloop()

    def CadastrarProduto(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Cadastro de Produtos')
        self.cadastrar['bg'] = '#524f4f'


        Label(self.cadastrar, text='Cadastre os Produtos',bg='#524f4f', fg='white').grid(row=0, column=0, columnspan =4, padx=5, pady=5)

        Label(self.cadastrar, text='Nome:',bg='#524f4f', fg='white').grid(row=1, column=0, columnspan =1, padx=5, pady=5)
        self.nome=Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan =2, padx=5, pady=5)

        Label(self.cadastrar, text='Ingredientes:', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5,pady=5)
        self.ingredientes = Entry(self.cadastrar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo:', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5,pady=5)
        self.grupo = Entry(self.cadastrar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Preço:', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5,pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Inserir', highlightbackground='#524f4f', bg='gray',relief='flat',width=15, command=self.CadastrarProdutoBackEND).grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', highlightbackground='#524f4f', bg='gray', relief='flat',width=15, command=self.ExcluirProdutoBackEnd).grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', highlightbackground='#524f4f', bg='gray', relief='flat',width=15,command=self.CadastrarProdutoBackEND).grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar', highlightbackground='#524f4f', bg='gray', relief='flat',width=15,command=self.LimparCadastrosProdutos).grid(row=6, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

        self.tree.column('column1', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('column2', width=200, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('column3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('column4', width=60, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=4, columnspan=2 , padx=10, pady=10, rowspan=7)

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Painel de Administração')
        self.root.geometry('300x100')


        Button(self.root, text='Pedidos', bg='#2E4682', width=20,command=self.RegistrarPedidos).grid(row=0, column=0,padx=10,pady=10)
        Button(self.root, text='Produtos', bg='#485A88', width=20, command=self.CadastrarProduto).grid(row=1, column=0, padx=10, pady=10)

        self.root.mainloop()

    def MostrarPedidos(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                resultados = cursor.fetchall()
        except:
            print('eroou')

        self.tree.delete(*self.tree.get_children())
        linhaV = []

        for i in resultados:
            linhaV.append(i['nome'])
            linhaV.append(i['observacoes'])
            linhaV.append(i['localEntrega'])
            linhaV.append(i['qtd'])

            self.tree.insert("", END, values=linhaV, iid=i['id'], tag='1')
            linhaV.clear()

    def MostrarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultados = cursor.fetchall()
        except:
            print('eroou')

        self.tree.delete(*self.tree.get_children())
        linhaV = []

        for i in resultados:
            linhaV.append(i['nome'])
            linhaV.append(i['ingredientes'])
            linhaV.append(i['grupo'])
            linhaV.append(i['preco'])

            self.tree.insert("", END, values=linhaV, iid=i['id'], tag='1')
            linhaV.clear()

    def RegistrarPedidosBackEnd(self):

        nome = [self.produto.get()]
        localEntrega= self.local.get()
        observacoes= self.obs.get()
        qtd= self.quantidade.get()
        ingredientes = 'padrão' #self.ingredenteR.get()
        grupo = 'padrão'#self.grupoR.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu1')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values (%s, %s, %s, %s, %s, %s)',(nome, ingredientes, grupo, localEntrega, observacoes,qtd))
                conexao.commit()
        except:
            print('nao deu2')


        self.MostrarPedidos()
        self.LimparCaixaTextoR()

    def CadastrarProdutoBackEND(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')
        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
                conexao.commit()
        except:
            print('nao deu')

        self.MostrarProdutosBackEnd()
        self.LimparCaixaTexto()

    def ExcluirPedidosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')
        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('nao deu')
        self.MostrarPedidos()

    def ExcluirProdutoBackEnd(self):
        idDeletar = int(self.tree.selection()[0])
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')
        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from produtos where id = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('nao deu')
        self.MostrarProdutosBackEnd()

    def LimparRegistrosPedidos(self):
        if messagebox.askokcancel('LIMPAR','DESEJA REALMENTE APAGAR TUDO?'):
            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('nao deu')
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('truncate table pedidos')
                    conexao.commit()
            except:
                print('nao deu')
            self.MostrarPedidos()

    def LimparCadastrosProdutos(self):

        if messagebox.askokcancel('LIMPAR','DESEJA REALMENTE APAGAR TUDO?'):
            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                print('nao deu')
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('truncate table produtos')
                    conexao.commit()
            except:
                print('nao deu')
            self.MostrarProdutosBackEnd()

    def LimparCaixaTexto(self):
        self.nome.delete(0, END)
        self.ingredientes.delete(0, END)
        self.grupo.delete(0, END)
        self.preco.delete(0, END)

    def LimparCaixaTextoR(self):
            self.produto.delete(0, END)
            self.quantidade.delete(0, END)
            self.local.delete(0, END)
            self.obs.delete(0, END)

class JanelaLogin():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')

        usuario= self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('eroou')

        for linha in resultados:
            if usuario == linha['nome'] and linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel']==2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('Atenção', 'Usuário ou Senha non ecxiste')


        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()

    def CadastroBackEnd(self):
        codigoPadrao = "123abc."

        if self.codigoSeguranca.get() == codigoPadrao:
            if len(self.login.get()) <=20:
                if len(self.senha.get())<=50:
                    nome = self.login.get()
                    senha = self.senha.get()

                    try:
                        conexao = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='',
                            db='erp',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )
                    except:
                        print('nao deu')
                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)',(nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
                        self.root.destroy()
                    except:
                        print('eroou')
                else:
                    messagebox.showinfo('ERRO','Insira uma senha com menos de 50 caracteres')
            else:
                messagebox.showinfo('ERRO', 'Insira um nome com menos de 20 caracteres')
        else:
            messagebox.showinfo('ERRO', 'Erro no código de segurança')

    def Cadastro(self):
        Label(self.root, text='Código de Segurança').grid(row=3, column=0, padx=5, pady=5)
        self.codigoSeguranca = Entry(self.root, show="*")
        self.codigoSeguranca.grid(row=3, column=1, padx=5, pady=10)
        Button(self.root, text='Confirmar Cadastro', bg='blue1', width=15, command=self.CadastroBackEnd).grid(row=4, column=0,columnspan=3,padx=10, pady=5)

    def UpdateBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('nao deu')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('eroou')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for i in resultados:
            linhaV.append(i['id'])
            linhaV.append(i['nome'])
            linhaV.append(i['senha'])
            linhaV.append(i['nivel'])

            self.tree.insert("",END,values=linhaV, iid=i['id'], tag='1')
            linhaV.clear()

    def VizualizarCadastros(self):
        self.vc = Toplevel()
        self.vc.title('Vizualizar Cadastros')
        self.vc.resizable(False,False)

        self.tree = ttk.Treeview(self.vc, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'),show='headings')

        self.tree.column('column1', width=30, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column('column2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Usuário')

        self.tree.column('column3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column('column4', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Nível')

        self.tree.grid(row=0, column=0,padx=10,pady=10)

        self.UpdateBackEnd()

        self.vc.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')

        Label(self.root, text='Faça seu Login').grid(row=0, column=0,columnspan=2)

        Label(self.root, text='Usuário').grid(row=1, column=0)

        self.login = Entry(self.root)
        self.login.grid(row=1, column=1,padx=5,pady=5)
        self.login.insert(0, "admin") #apenas para teste

        Label(self.root, text='Senha').grid(row=2, column=0)
        self.senha = Entry(self.root) #,show='*')
        self.senha.grid(row=2, column=1,padx=5,pady=5)
        self.senha.insert(0, "admin")  # apenas para teste

        Button(self.root, text='Entrar',bg='green1',width=10,command=self.VerificaLogin).grid(row=5, column=0,padx=20,pady=5)
        Button(self.root, text='Cadastrar', bg='orange1', width=10, command=self.Cadastro).grid(row=5, column=1, padx=5, pady=5)
        Button(self.root, text='Visualizar Cadastros', bg='white', width=20, command=self.VizualizarCadastros).grid(row=6, column=0, columnspan=2, padx=5, pady=5)


        self.root.mainloop()

JanelaLogin()