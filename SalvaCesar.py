import os
import sys
import customtkinter as ctk
from tkinter import PhotoImage
from automacao import aut  

def executar_automacao():
    
    vezes = numDigitado.get();
    
    if vezes.isdigit(): 
        vezes = int(vezes);
        aut(vezes);  
    else:
        print("Por favor, insira um número válido."); 

ctk.set_appearance_mode('dark');
app = ctk.CTk();
app.title('Salva César');
app.geometry('400x300');

imagem = PhotoImage(file="image.png");
label_imagem = ctk.CTkLabel(app, image=imagem);
label_imagem.pack(pady=10);

label_usuario = ctk.CTkLabel(app, text='Quantas vezes você quer executar a tarefa?');
label_usuario.pack(pady=1);

numDigitado = ctk.CTkEntry(app, placeholder_text='Digite o número aqui');
numDigitado.pack(pady=1);

botao = ctk.CTkButton(app, text="Execute o script", command=executar_automacao);
botao.pack(pady=20);

app.mainloop();
