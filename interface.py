import customtkinter as ctk
import time
import math

class InterfaceCaineReal(ctk.CTk):
    def __init__(self):
        super().__init__()
        this = self
        this.title("Vibe Check - Digital Circus")
        this.geometry("700x750")
        this.configure(fg_color="#050505") # Fundo preto profundo

        # Cores Neon Reais
        this.cor_azul = "#00BFFF"    # Azul Neon (Neutro)
        this.cor_alegre = "#FF0000"  # Vermelho Vivo (Alegre)
        this.cor_triste = "#8A2BE2"  # Roxo Elétrico (Triste)

        # --- O GRID E A BOLA (O DESIGN DA FOTO) ---
        this.canvas = ctk.CTkCanvas(this, width=600, height=400, bg="#050505", highlightthickness=0)
        this.canvas.pack(pady=30)

        # Desenhar Grade (Linhas bem escuras e finas)
        for i in range(0, 600, 30):
            this.canvas.create_line(i, 0, i, 400, fill="#1a1a1a")
            this.canvas.create_line(0, i, 600, i, fill="#1a1a1a")

        # Criar a Bola com camadas de brilho para não ficar "feia"
        this.centro_x, this.centro_y = 300, 200
        # Camada de Brilho (Glow)
        this.brilho = this.canvas.create_oval(this.centro_x-40, this.centro_y-40, this.centro_x+40, this.centro_y+40, outline=this.cor_azul, width=2)
        # O Núcleo da Bola
        this.nucleo = this.canvas.create_oval(this.centro_x-25, this.centro_y-25, this.centro_x+25, this.centro_y+25, fill=this.cor_azul, outline=this.cor_azul, width=2)

        # --- INTERFACE DE TEXTO ---
        this.caixa_texto = ctk.CTkTextbox(this, width=500, height=150, fg_color="#111", border_color="#333", font=("Arial", 14))
        this.caixa_texto.pack(pady=10)
        this.caixa_texto.insert("1.0", "Escreva seu texto aqui...")

        this.botao = ctk.CTkButton(this, text="ANALISAR VIBE", fg_color="#222", hover_color="#333", command=this.animar)
        this.botao.pack(pady=10)

        # Legenda Colorida (Agora com as cores certas!)
        this.frame_legenda = ctk.CTkFrame(this, fg_color="transparent")
        this.frame_legenda.pack()
        
        ctk.CTkLabel(this.frame_legenda, text="● ALEGRE", text_color=this.cor_alegre, font=("Arial", 14, "bold")).pack(side="left", padx=10)
        ctk.CTkLabel(this.frame_legenda, text="● TRISTE", text_color=this.cor_triste, font=("Arial", 14, "bold")).pack(side="left", padx=10)

        this.vibrar()

    def vibrar(self):
        this = self
        t = time.time() * 12
        vibe = math.sin(t) * 2
        this.canvas.coords(this.nucleo, 275+vibe, 175+vibe, 325+vibe, 225+vibe)
        this.after(30, this.vibrar)

    def animar(self):
        this = self
        # Simula a IA decidindo (AQUI VAI A LÓGICA DEPOIS)
        # Por enquanto, ele alterna para você ver as cores!
        texto = this.caixa_texto.get("1.0", "end").lower()
        
        if "alegre" in texto or "feliz" in texto or "vitória" in texto:
            this.mudar_cor(this.cor_alegre)
        elif "triste" in texto or "dor" in texto or "sozinho" in texto:
            this.mudar_cor(this.cor_triste)
        else:
            this.mudar_cor(this.cor_azul)

    def mudar_cor(self, cor):
        this = self
        this.canvas.itemconfig(this.nucleo, fill=cor, outline=cor)
        this.canvas.itemconfig(this.brilho, outline=cor)

if __name__ == "__main__":
    app = InterfaceCaineReal()
    app.mainloop()