import streamlit as st

# ----------------------------------------------------------
# LINKS DE ASSETS (sua imagem de fundo, seu logo, fox etc)
# ----------------------------------------------------------
url_imagem = "https://raw.githubusercontent.com/DellaVolpe69/Images/main/AppBackground02.png"
url_logo = "https://raw.githubusercontent.com/DellaVolpe69/Images/main/DellaVolpeLogoBranco.png"

st.markdown(
    f"""
    <style>
    /* Remove fundo padrão dos elementos de cabeçalho que às vezes ‘brigam’ com o BG */
    header, [data-testid="stHeader"] {{
        background: transparent;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ----------------------------------------------------------
st.set_page_config(page_title="Central de Formulários", page_icon="🗂️", layout="wide")

# ----------------------------------------------------------
# ESTILO GLOBAL
# ----------------------------------------------------------
st.markdown(
    f"""
    <style>
        /* Fundo */
        [data-testid="stAppViewContainer"] {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                        url("{url_imagem}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Inputs */
        input, textarea {{
            border: 1px solid white !important;
            border-radius: 5px !important;
        }}

        /* Select */
        .stSelectbox div[data-baseweb="select"] > div {{
            border: 1px solid white !important;
            border-radius: 5px !important;
        }}

        /* Date */
        .stDateInput input {{
            border: 1px solid white !important;
            border-radius: 5px !important;
        }}

        a {{
            text-decoration: none !important;
        }}

        /* BOTÃO */
        .custom-btn {{
            background-color: #FF5D01 !important;
            color: white !important;
            border: 2px solid white !important;
            padding: 0.6em 1.2em;
            border-radius: 10px !important;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: 0.2s ease;
            display: block;
            width: 100%;
            text-align: center;
        }}

        .custom-btn:hover {{
            background-color: white !important;
            color: #FF5D01 !important;
            transform: scale(1.03);
            border: 2px solid #FF5D01 !important;
        }}

        /* Animação para imagens */
        .shine:hover {{
            filter: brightness(1.3);
            transform: scale(1.05);
            transition: 0.2s ease;
        }}

        /* Rodapé fixo */
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            text-align: center;
            font-size: 14px;
            padding: 8px 0;
            text-shadow: 1px 1px 2px black;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# CABEÇALHO COM LOGO
# ----------------------------------------------------------
st.markdown(
    f"""
    <div style="text-align: center; padding-top: 2em;">
        <img src="{url_logo}" style="width: 40%; max-width: 200px; margin-bottom: 10px;">
        <h1 style="color: white; text-shadow: 1px 1px 3px black;">🗂️ Central de Formulários</h1>
        <p style="color: white;">Escolha abaixo o formulário desejado:</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------------
#  FUNÇÃO DE CARD
# ----------------------------------------------------------
def criar_card(texto_botao, link):
    
    st.markdown(
        f"""
        <a href="{link}" target="_blank">
            <button class="custom-btn">{texto_botao}</button>
        </a>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------
# LISTA AUTOMÁTICA DE FORMULÁRIOS
# (⭐ Basta ADICIONAR aqui novos formulários!)
# ----------------------------------------------------------
apps = [
    {
        "nome": "Cadastro de Janelas",
        "link": "https://formulariojanelas.streamlit.app/"
    },
    {
        "nome": "Cadastro de Feriados/ Inventário",
        "link": "https://formularioferiadoinventario.streamlit.app/"
    },
    {
        "nome": "Prioridades",
        "link": "https://priorizanfs.streamlit.app/"
    },
    {
        "nome": "Formulário RNC",
        "link": "https://formulariornc.streamlit.app/"
    },
    {
        "nome": "Exame Médico",
        "link": "https://gestao-documentos-exame-medico.streamlit.app/"
    },
    {
        "nome": "Prazos Default SLA",
        "link": "https://prazosdefaultsla.streamlit.app/"
    },
    {
        "nome": "Data Início Default SLA",
        "link": "https://datainiciodefaultsla.streamlit.app/"
    },
    {
        "nome": "Expurgo OP",
        "link": "https://expurgoop.streamlit.app/"
    },
]

apps_SLA = [
    {
        "nome": "Cadastro de Janelas",
        "link": "https://formulariojanelas.streamlit.app/"
    },
    {
        "nome": "Cadastro de Feriados/ Inventário",
        "link": "https://formularioferiadoinventario.streamlit.app/"
    },
    {
        "nome": "Prioridades",
        "link": "https://priorizanfs.streamlit.app/"
    },
    {
        "nome": "Prazos Default SLA",
        "link": "https://prazosdefaultsla.streamlit.app/"
    },
    {
        "nome": "Data Início Default SLA",
        "link": "https://datainiciodefaultsla.streamlit.app/"
    },
    {
        "nome": "Expurgo OP",
        "link": "https://expurgoop.streamlit.app/"
    },
]

apps_Armazem = [
    {
        "nome": "Pendências do Inventário",
        "link": "https://pendenciainventario.streamlit.app/"
    },
]

# ----------------------------------------------------------
#  RENDERIZAÇÃO CENTRALIZADA (TUDO NO MEIO)
# ----------------------------------------------------------

st.markdown("""
<style>
/* Container das abas */
div[data-baseweb="tab-list"] {
    gap: 10px;
}

/* Aba normal */
button[data-baseweb="tab"] {
    background-color: #f0f2f6;
    border-radius: 8px 8px 0 0;
    padding: 10px 16px;
    font-weight: 600;
    color: #333;
}

/* Aba ativa */
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #1f77b4;
    color: white;
}
</style>
""", unsafe_allow_html=True)

aba_sla, aba_armazem = st.tabs(["📊 SLA", "📦 Armazém"])

with aba_sla:
    st.subheader("Aplicações de SLA")

    col_esq, col_meio, col_dir = st.columns([1, 2, 1])

    with col_meio:
        for app in apps_SLA:
            criar_card(app["nome"], app["link"])
            st.markdown("<br>", unsafe_allow_html=True)
            
with aba_armazem:
    st.subheader("Aplicações de Armazém")

    col_esq, col_meio, col_dir = st.columns([1, 2, 1])

    with col_meio:
        for app in apps_Armazem:
            criar_card(app["nome"], app["link"])
            st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------------------------------------
#  RODAPÉ
# ----------------------------------------------------------
#st.markdown("<div class='footer'>💡 Desenvolvido por Rapha — Central de Performance</div>", unsafe_allow_html=True)
# --- FUNÇÃO DE RODAPÉ ---
def rodape():
    st.markdown("""
        <div class="footer">
            © 2025 <b>Della Volpe</b> | Desenvolvido por <a href="#">Raphael Chiavegati Oliveira</a>
        </div>
    """, unsafe_allow_html=True)
    
rodape()
