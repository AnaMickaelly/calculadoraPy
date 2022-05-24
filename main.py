# importando o tkinter
from tkinter import *
from tkinter import ttk 


#cores

cor1 = "#080000" #black
cor2 = "#feffff" #white
cor3 = "#38576b" #blue
cor4 = "#ECEFF1" #gray
cor5 = "#FFAB40" #orange

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


#criando frames

Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)


Frame_corpo = Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1, column=0)


#criando os botoes

b_1 = Button(Frame_corpo, text="C", width=11, height=2, bg=cor4,  relief=RAISED,  overrelief=RAISED) #botão de limpar "clean"
b_1.place(x=0, y=0)

b_2 = Button(Frame_corpo, text="%", width=11, height=2, bg=cor4) 
b_2.place(x=85, y=0)

b_1 = Button(Frame_corpo, text="/", width=11, height=2, bg=cor5, fg=cor2) 
b_1.place(x=170, y=0)







janela .mainloop()