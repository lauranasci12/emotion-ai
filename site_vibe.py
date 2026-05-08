import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Caine Vibe Check", layout="centered")

# CSS PARA O VISUAL "DIGITAL CIRCUS"
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(#1a1a1a 1px, transparent 1px), linear-gradient(90deg, #1a1a1a 1px, transparent 1px);
        background-size: 30px 30px;
    }
    .bolinha {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin: 0 auto;
        transition: all 0.5s ease;
    }
    .neon-azul { background-color: #00BFFF; box-shadow: 0 0 20px #00BFFF; }
    .neon-alegre { background-color: #FF0000; box-shadow: 0 0 30px #FF0000; }
    .neon-triste { background-color: #8A2BE2; box-shadow: 0 0 30px #8A2BE2; }
    </style>
    """, unsafe_allow_html=True)

# --- TREINAMENTO DA IA (O CÉREBRO) ---
def treinar_ia():
    # Carrega seus arquivos txt
    with open('alegre.txt', 'r', encoding='utf-8') as f:
        alegres = f.readlines()
    with open('triste.txt', 'r', encoding='utf-8') as f:
        tristes = f.readlines()
    
    frases = alegres + tristes
    rotulos = ['alegre'] * len(alegres) + ['triste'] * len(tristes)
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(frases)
    modelo = MultinomialNB()
    modelo.fit(X, rotulos)
    return vectorizer, modelo

vectorizer, modelo = treinar_ia()

# --- INTERFACE DO SITE ---
st.title("🎪 Caine Vibe Check 🎪")
st.write("Digite um trecho do seu livro para a IA analisar a vibe:")

texto_usuario = st.text_area("Seu texto aqui...", height=100)

if st.button("ANALISAR VIBE 🔮"):
    if texto_usuario:
        # IA Pensando
        vetor = vectorizer.transform([texto_usuario])
        resultado = modelo.predict(vetor)[0]
        
        # Muda a cor da bolinha baseado no resultado
        if resultado == 'alegre':
            st.markdown('<div class="bolinha neon-alegre"></div>', unsafe_allow_html=True)
            st.success("Vibe Detectada: ALEGRE! 🔴")
        else:
            st.markdown('<div class="bolinha neon-triste"></div>', unsafe_allow_html=True)
            st.info("Vibe Detectada: TRISTE... 🟣")
    else:
        st.warning("Escreva algo antes!")
else:
    # Bolinha Neutra (Azul)
    st.markdown('<div class="bolinha neon-azul"></div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("🔴 Vermelho: Alegre | 🟣 Roxo: Triste")