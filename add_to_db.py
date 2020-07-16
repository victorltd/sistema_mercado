from tkinter import *
import sqlite3
import tkinter.filedialog
import tkinter.messagebox


conn = sqlite3.connect(r"C:\Users\Victor\Documents\Projetos\store\Database\store.db")
c = conn.cursor()


resultado0 = c.execute("SELECT MAX(id) from inventory")
for resultado in resultado0:
    id = resultado[0]




class BancoDeDados:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.reading = Label(master, text="Cadastro de produtos", font=('arial 40 bold'), fg='steelblue')
        self.reading.place(x=400, y=0)

        self.name_1=Label(master, text="Nome do produto:", font=('arial 18 bold'))
        self.name_1.place(x=0, y=70)

        self.name_e=Entry(master, width=20, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)

        self.stock_1=Label(master, text="Estoque:", font=('arial 18 bold'))
        self.stock_1.place(x=0, y=120)

        self.stock_e=Entry(master, width=20, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_1=Label(master, text="Preço de custo:", font=('arial 18 bold'))
        self.cp_1.place(x=0, y=170)

        self.cp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)

        self.sp_1=Label(master, text="Preço de venda:", font=('arial 18 bold'))
        self.sp_1.place(x=0, y=220)

        self.sp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)

        self.vendor_1=Label(master, text="Nome do fornecedor:", font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=270)

        self.vendor_e=Entry(master, width=20, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=270)

        self.vendor_phone_1=Label(master, text="Telefone do fornecedor:", font=('arial 18 bold'))
        self.vendor_phone_1.place(x=0, y=320)

        self.vendor_phone_e=Entry(master, width=20, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=320)

        self.id_1=Label(master, text="ID:", font=('arial 18 bold'))
        self.id_1.place(x=0, y=370)

        self.id_e=Entry(master, width=20, font=('arial 18 bold'))
        self.id_e.place(x=380, y=370)

        self.btn_add=Button(master, text="Cadastrar", width=25,height=2, bg='steelblue',fg='white', font=('arial 10 bold'), command=self.get_itens)
        self.btn_add.place(x=500, y=420)

        self.btn_clear=Button(master, text="Limpar", width=15,height=2, bg='orange',fg='white', font=('arial 10 bold'), command=self.clear_all)
        self.btn_clear.place(x=320, y=420)

        self.tBox=Text(master,width=60,height=18 )
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "Ultimo cadastro ID: " +str(id))

        self.master.bind('<Return>', self.get_itens)
        self.master.bind('<Up>', self.clear_all)

    def get_itens(self, *args, **kwargs):
        self.name= self.name_e.get()
        self.stock= self.stock_e.get()
        self.cp= self.cp_e.get()
        self.sp= self.sp_e.get()
        self.vendor= self.vendor_e.get()
        self.vendor_phone= self.vendor_phone_e.get()
        #self.id= self.id_e.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)

        self.assumed_profit = float(self.totalsp) - float(self.totalcp)

        if self.name == None or self.stock == None or self.cp == None or self.sp == None :
            tkinter.messagebox.showinfo("victor@email", "FAVOR PREENCHER TODOS OS CAMPOS")
        else :
            sql= "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phone) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()

            self.tBox.insert(END, "\n\nCadastro" + str(self.name) + "no banco de dados com ID " + str(self.id_e.get()))


            tkinter.messagebox.showinfo("victor@email", "CADASTRO REALIZADO COM SUCESSO")



    def clear_all(self, *args, **kwargs):
        num = id+1
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)
        




janelaRaiz = Tk()
menubar = Menu(janelaRaiz)
banco = BancoDeDados(janelaRaiz)
janelaRaiz.geometry("1366x768+0+0")
janelaRaiz.title("Mercadinho")
janelaRaiz.config(menu=menubar)
janelaRaiz.mainloop()