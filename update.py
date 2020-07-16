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
        self.reading = Label(master, text="Atualizar produtos", font=('arial 40 bold'), fg='steelblue')
        self.reading.place(x=400, y=0)
        
        #vai fazer a pesquisa pelo id

        self.id_le=Label(master, text="Digite o ID:", font=('arial 18 bold'))
        self.id_le.place(x=0, y=70)
        
        self.id_box=Entry(master, width=10, font=('arial 18 bold'))
        self.id_box.place(x=380, y=70)
             
        self.btn_pesquisar=Button(master, text="Pesquisar", width=10,bg='orange',fg='black', font=('arial 10 bold'), command=self.pesquisar)
        self.btn_pesquisar.place(x=550, y=70)  

        #--------------------------fim da parte de pesquisa   

        self.name_1=Label(master, text="Nome do produto:", font=('arial 18 bold'))
        self.name_1.place(x=0, y=120)

        self.name_e=Entry(master, width=20, font=('arial 18 bold'))
        self.name_e.place(x=380, y=120)

        self.stock_1=Label(master, text="Estoque:", font=('arial 18 bold'))
        self.stock_1.place(x=0, y=170)

        self.stock_e=Entry(master, width=20, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=170)

        self.cp_1=Label(master, text="Preço de custo:", font=('arial 18 bold'))
        self.cp_1.place(x=0, y=220)

        self.cp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=220)

        self.sp_1=Label(master, text="Preço de venda:", font=('arial 18 bold'))
        self.sp_1.place(x=0, y=270)

        self.sp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=270)

        self.vendor_1=Label(master, text="Nome do fornecedor:", font=('arial 18 bold'))
        self.vendor_1.place(x=0, y=320)

        self.vendor_e=Entry(master, width=20, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=320)

        self.vendor_phone_1=Label(master, text="Telefone do fornecedor:", font=('arial 18 bold'))
        self.vendor_phone_1.place(x=0, y=370)

        self.vendor_phone_e=Entry(master, width=20, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=370)

        self.totalcp_1=Label(master, text="Total preço de custo:", font=('arial 18 bold'))
        self.totalcp_1.place(x=0, y=420)

        self.totalcp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.totalcp_e.place(x=380, y=420)

        self.totalsp_1=Label(master, text="Total preço de venda:", font=('arial 18 bold'))
        self.totalsp_1.place(x=0, y=470)

        self.totalsp_e=Entry(master, width=20, font=('arial 18 bold'))
        self.totalsp_e.place(x=380, y=470)

        

        
      
        

        self.btn_add=Button(master, text="Atualizar", width=25,height=2, bg='steelblue',fg='white', font=('arial 10 bold'), command=self.atualizar)
        self.btn_add.place(x=500, y=520)
        
        self.btn_clear=Button(master, text="Limpar", width=15,height=2, bg='orange',fg='white', font=('arial 10 bold'))
        self.btn_clear.place(x=320, y=520)
        

        self.tBox=Text(master,width=60,height=18 )
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "Ultimo cadastro ID: " +str(id))

    def pesquisar(self, *args, **kwargs):
        sql= "SELECT * FROM inventory WHERE id=?"
        resultado0 = c.execute(sql, (self.id_box.get(),))
        for resultado in resultado0:
            self.n1 = resultado[1] #nome    
            self.n2 = resultado[2] #estoque
            self.n3 = resultado[3]
            self.n4 = resultado[4]
            self.n5 = resultado[5]
            self.n6 = resultado[6]
            self.n7 = resultado[7]
            self.n8 = resultado[8]
            self.n9 = resultado[9]

        conn.commit()

        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))

        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))

        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))

        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))

        self.vendor_phone_e.delete(0,END)
        self.vendor_phone_e.insert(0,str(self.n9))

        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0,str(self.n5))

        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0,str(self.n6))

    def atualizar(self, *args, **kwargs):
        #vai pegar o valor que eu digitar la e atualizar
        self.u1 = self.name_e.get()   
        self.u2 = self.stock_e.get()  
        self.u3 = self.cp_e.get()  
        self.u4 = self.sp_e.get()  
        self.u5 = self.totalcp_e.get()  
        self.u6 = self.totalsp_e.get()  
        self.u7 = self.vendor_e.get()  
        self.u8 = self.vendor_phone_e.get()  
        
        query = "UPDATE inventory SET  name=? , stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phone=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_box.get() ))
        conn.commit()
        tkinter.messagebox.showinfo("victor@email", "Cadastro atualizado")
        






janelaRaiz = Tk()
menubar = Menu(janelaRaiz)
banco = BancoDeDados(janelaRaiz)
janelaRaiz.geometry("1366x768+0+0")
janelaRaiz.title("Mercadinho")
janelaRaiz.config(menu=menubar)
janelaRaiz.mainloop()