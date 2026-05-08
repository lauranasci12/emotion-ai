import os
import sys

# 1. PEÇAS DA NOSSA IA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 2. FUNÇÃO PARA LER OS ARQUIVOS
def carregar_dados(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado!")
        return []
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        # Lê cada linha e remove espaços vazios
        return [linha.strip() for linha in f.readlines() if linha.strip()]

print("Carregando frases de treinamento...")

# 3. ENDEREÇOS DOS SEUS ARQUIVOS (Ajustados para o seu computador)
caminho_alegre = r"C:\Users\laura_zx5x7ap\OneDrive\Área de Trabalho\classificador_vibe\treinamento\alegre.txt"
caminho_triste = r"C:\Users\laura_zx5x7ap\OneDrive\Área de Trabalho\classificador_vibe\treinamento\triste.txt"

frases_alegres = carregar_dados(caminho_alegre)
frases_tristes = carregar_dados(caminho_triste)

# Verifica se os arquivos não estão vazios
if not frases_alegres or not frases_tristes:
    print("Ops! Verifique se você salvou as frases nos arquivos .txt corretamente.")
    sys.exit()

# 4. TREINAMENTO DA IA
# Juntamos as frases e criamos os rótulos na ordem CORRETA
frases = frases_alegres + frases_tristes
rotulos = ['alegre'] * len(frases_alegres) + ['triste'] * len(frases_tristes)

# Criamos o "tradutor" de palavras para números
vectorizer = CountVectorizer(stop_words=['a', 'o', 'e', 'do', 'da', 'um', 'uma', 'os', 'as', 'eu', 'me', 'meu', 'minha', 'esta', 'estou'])
X_treino = vectorizer.fit_transform(frases)

# Criamos e treinamos o modelo
modelo = MultinomialNB()
modelo.fit(X_treino, rotulos)

print("IA Treinada com sucesso! ✅")
print("-" * 30)

# 5. INTERAÇÃO COM VOCÊ
while True:
    entrada = input("\nDigite uma frase para a IA analisar (ou 'sair'): ")
    
    if entrada.lower() == 'sair':
        break
        
    # Transforma a sua frase no formato que a IA entende
    frase_vetorizada = vectorizer.transform([entrada])
    
    # A IA faz a previsão
    resultado = modelo.predict(frase_vetorizada)[0]
    
    print(f"Vibe detectada: {resultado.upper()} ✨")