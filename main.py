from tkinter import *
import sqlite3
import tkinter.filedialog
import tkinter.messagebox
import datetime

conn = sqlite3.connect(r"C:\Users\Victor\Documents\Projetos\store\Database\store.db")
c = conn.cursor()

data=datetime.date.today()

labels_list= []
lista_produtos =[]
preco_produtos =[]
quantidade_produtos =[]
id_produtos =[]


class Aplications:
    def __init__(self, master, *args, **kwargs):
        self.master=master

        self.left=Frame(master, width=700, height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right=Frame(master, width=660, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)
        
        #label para o titulo
        self.heading = Label(self.left, text="SuperMercado na Manha ", font=('arial 40 bold'), bg='lightblue')
        self.heading.place(x=0, y=0)
        
        #label para data
        self.date_1 = Label(self.right, text="Data: " +str(data), font=('arial 16 bold'), bg='lightblue')
        self.date_1.place(x=0, y=0)

        self.produto = Label(self.right, text="Produto ", font=('arial 18 bold'), fg='white',bg='lightblue')
        self.produto.place(x=0, y=60)

        self.quantidade = Label(self.right, text="Quantidade ", font=('arial 18 bold'), fg='white',bg='lightblue')
        self.quantidade.place(x=300, y=60)

        self.valor = Label(self.right, text="Valor ", font=('arial 18 bold'), fg='white',bg='lightblue')
        self.valor.place(x=500, y=60)
        
        #onde vai as coisas pra add no carrinho
        self.enterid = Label(self.left, text="Produto ID ", font=('arial 18 bold'),bg='white')
        self.enterid.place(x=0, y=80)

        self.enterid_e=Entry(self.left, width=25, font=('arial 18 bold'), bg='lemonchiffon')
        self.enterid_e.place(x=190, y=80)

        self.btn_pesquisar=Button(self.left, text="Pesquisar", width=22,height=1, bg='blue',fg='white', font=('arial 10 bold'), command=self.busca_id)
        self.btn_pesquisar.place(x=350, y=120)
        #------------------------

        self.product_name = Label(self.left, text="", font=('arial 27 bold'),bg='white', fg='green')
        self.product_name.place(x=0, y=250)

        self.preco = Label(self.left, text="", font=('arial 27 bold'),bg='white', fg='green')
        self.preco.place(x=0, y=290)

        self.total_carrinho = Label(self.right, text="Valor total: ", font=('arial 30 bold'),bg='lightblue', fg='black')
        self.total_carrinho.place(x=0, y=650)


    def busca_id(self, *args, **kwargs):
        self.get_id = self.enterid_e.get()
        query= "SELECT * FROM inventory WHERE id=?"

        resultado0 = c.execute(query, (self.get_id,))
        for self.resultado in resultado0:
            self.get_id = self.resultado[0] #id    
            self.get_name = self.resultado[1] #nome
            self.get_price = self.resultado[4] #preco
            self.get_stock = self.resultado[2] #estoque -- pego esses valores no banco de dados

            self.product_name.configure(text="Nome produto: "+str(self.get_name))
            self.preco.configure(text="Preço R$: "+str(self.get_price))

            self.quantidade = Label(self.left, text="Quantidade: ", font=('arial 18 bold'),bg='white', fg='black')
            self.quantidade.place(x=0, y=370)

            self.quantidade_e=Entry(self.left, width=25, font=('arial 18 bold'), bg='lemonchiffon')
            self.quantidade_e.place(x=200, y=370)
            self.quantidade_e.focus()

            self.desconto = Label(self.left, text="Desconto: ", font=('arial 18 bold'),bg='white', fg='black')
            self.desconto.place(x=0, y=420)

            self.desconto_e=Entry(self.left, width=25, font=('arial 18 bold'), bg='lemonchiffon')
            self.desconto_e.place(x=200, y=420)
            self.desconto_e.insert(END, 0) #vai setar com o valor 0 de inicio

            self.btn_add_carr=Button(self.left, text="Carrinho", width=22,height=1, bg='blue',fg='black', font=('arial 10 bold'), command=self.add_carr)
            self.btn_add_carr.place(x=350, y=470)

            self.valor_pago = Label(self.left, text="Total pago: ", font=('arial 18 bold'),bg='white', fg='black')
            self.valor_pago.place(x=0, y=550)
             
            self.valor_pago_e=Entry(self.left, width=25, font=('arial 18 bold'), bg='bisque')
            self.valor_pago_e.place(x=200, y=550)

            self.btn_calc_troco=Button(self.left, text="Calcular troco", width=22,height=1, bg='orange',fg='black', font=('arial 10 bold'), command=self.troco)
            self.btn_calc_troco.place(x=350, y=600)

            self.btn_gerar_nf=Button(self.left, text="Gerar NF", width=22,height=1, bg='blue',fg='white', font=('arial 10 bold'))
            self.btn_gerar_nf.place(x=350, y=650)
            
    def add_carr(self, *args, **kwargs):     
        self.quantidade_valor=int(self.quantidade_e.get()) 
        if self.quantidade_valor > int(self.get_stock):
            tkinter.messagebox.showinfo("victor@email", "Quantidade acima do estoque disponível")
        else: 
            self.preco_final=(float(self.quantidade_valor)* float(self.get_price)) - (float(self.desconto_e.get()))
            lista_produtos.append(self.get_name)   
            preco_produtos.append(self.preco_final)  
            quantidade_produtos.append(self.quantidade_valor)  
            id_produtos.append(self.get_id)      

            self.x_index=0
            self.y_index=100
            self.counter=0

            for self.p in lista_produtos:
                self.temp_name=Label(self.right, text=str(lista_produtos[self.counter]), font='arial 18 bold', bg='lightblue', fg='darkviolet')
                self.temp_name.place(x=0, y=self.y_index) 
                labels_list.append(self.temp_name)

                self.temp_qnt=Label(self.right, text=str(quantidade_produtos[self.counter]), font='arial 18 bold', bg='lightblue', fg='darkviolet')
                self.temp_qnt.place(x=300, y=self.y_index) 
                labels_list.append(self.temp_qnt)

                self.temp_preco=Label(self.right, text="R$ "+str(preco_produtos[self.counter]), font='arial 18 bold', bg='lightblue', fg='darkviolet')
                self.temp_preco.place(x=500, y=self.y_index) 
                labels_list.append(self.temp_preco)

                self.y_index += 40
                self.counter +=1

                self.total_carrinho.configure(text="Valor total: R$ "+str(sum(preco_produtos)))

                self.quantidade.place_forget()
                self.quantidade_e.place_forget()
                self.desconto.place_forget()
                self.desconto_e.place_forget()
                self.quantidade.place_forget()
                self.product_name.configure(text="")
                self.preco.configure(text="")
                self.btn_add_carr.destroy()

                self.enterid.focus()
                self.enterid_e.delete(0,END)


    def troco(self, *args, **kwargs):
        self.t_pago=float(self.valor_pago_e.get())
        self.total=float(sum(preco_produtos))

        self.troco_cliente=self.t_pago- self.total

        self.troco_1 = Label(self.left, text="Troco: R$ "+str(self.troco_cliente), font=('arial 25 bold'),bg='white', fg='red')
        self.troco_1.place(x=0, y=700)






        


janelaRaiz = Tk()
menubar = Menu(janelaRaiz)
banco = Aplications(janelaRaiz)
janelaRaiz.geometry("1366x768+0+0")
janelaRaiz.title("Mercadinho")
janelaRaiz.config(menu=menubar)
janelaRaiz.mainloop()