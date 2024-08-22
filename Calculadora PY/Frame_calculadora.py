import tkinter
from tkinter import *
from tkinter import ttk 

#cores
co1 = '#dac9df' #lilas
co2 = '#ffffff' #branco
co3 = '#81638b' #lilas escuro 
co4 = '#000000' 

janela = Tk()
janela.geometry("400x310")
janela.title('')
janela.configure(bg = co2)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row= 0, columnspan=1, ipadx = 190)



# dividindo a janela em dois frames 

frame_cima = Frame(janela, width = 400, bg=co2, height = 60, pady = 0, padx=0)
frame_cima.grid(row =1, column = 0)

frame_baixo = Frame(janela, width = 400, bg=co2, height = 300, pady = 12, padx=20)
frame_baixo.grid(row =2, column = 0, sticky = NW)

# configurando frame cima 

app_nome = Label(frame_cima, text="Conversor de Base Numerica", relief=FLAT, anchor='center', font=('System 20'), bg = co1, fg = co2)
app_nome.place(x=10, y=15)

 #função converter
def converter():
# para converter qualquer numero em uma base para o seu correspondente em decimal
    def numero_para_decimal(numero, base):
        decimal = int(numero, base)
        binario = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        l_binario['text'] = str(binario[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:].upper())
    numero = e_valor.get()
    base = combo.get()

    #definindo o valor da base
    if base == 'BINÁRIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    else:
        base = 16

#chamando função
    numero_para_decimal(numero, base)
# configurando frame baixo 

bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']

combo = ttk.Combobox(frame_baixo, width= 12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x= 35, y = 10)

e_valor = Entry(frame_baixo, width = 9, justify='center', font=("", 13), highlightthickness=1, relief= 'solid')
e_valor.place(x = 160, y = 10)

b_converter = Button (frame_baixo, command=converter, text="CONVERTER", relief=RAISED, overrelief=RIDGE, font=('Ivy 8'), bg = co2, fg = co1)
b_converter.place(x= 247, y = 10)

l_binario = Label(frame_baixo, text="BINÁRIO", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg = co3, fg = co2)
l_binario.place(x=35, y=60)
l_binario = Label(frame_baixo, text="", width=12, relief=FLAT, anchor='center', font=('Verdana 13'), fg = co4)
l_binario.place(x = 170, y = 60 )

l_decimal = Label(frame_baixo, text="DECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg = co3, fg = co2)
l_decimal.place(x=35, y=140)
l_decimal = Label(frame_baixo, text="", width=12, relief=FLAT, anchor='center', font=('Verdana 13'), fg = co4)
l_decimal.place(x = 170, y = 140 )


l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg = co3, fg = co2)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_baixo, text="", width=12, relief=FLAT, anchor='center', font=('Verdana 13'), fg = co4)
l_hexadecimal.place(x = 170, y = 180 )

l_octal = Label(frame_baixo, text="OCTAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg = co3, fg = co2)
l_octal.place(x=35, y=100)
l_octal = Label(frame_baixo, text="", width=12, relief=FLAT, anchor='center', font=('Verdana 13'), fg = co4)
l_octal.place(x = 170, y = 100 )

janela.mainloop() 