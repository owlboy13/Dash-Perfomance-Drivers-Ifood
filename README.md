# Dashboard de Performance

Este repositório contém um projeto desenvolvido com **Streamlit**, **Pandas** e bibliotecas de visualização como **Altair** e **Plotly**. O objetivo é monitorar a performance de entregadores de forma interativa e dinâmica.

## 🛠️ Funcionalidades
### Página Principal
- Navegação intuitiva entre as páginas "Home" e "Performance".
- Integração com **Streamlit Navigation** para alternar entre as views.

### Página de Performance
- Exibição de dados de performance de entregadores.
- Gráficos interativos de rotas completadas, rejeitadas e ofertadas.
- Filtros personalizados para período e entregadores.
- Métricas-chave como rotas completas, rejeitadas, ofertadas e aceitas.

## 🚀 Tecnologias
- **Python 3.8+**
- **Streamlit**
- **Altair**
- **Plotly**
- **Pandas**

## 📂 Estrutura do Projeto
. ├── perfomance.py # Código para a análise de performance ├── perfomance.xlsx # Base de dados (não incluída no repositório público) └── README.md # Documentação

yaml
Copiar código

## ⚙️ Pré-requisitos
1. Instalar dependências:
    ```bash
    pip install streamlit pandas altair plotly openpyxl
    ```
2. Substituir o arquivo `perfomance.xlsx` por seu próprio dataset no mesmo formato.

## 🖥️ Executar o Projeto
1. Execute a aplicação:
    ```bash
    streamlit run perfomance.py
    ```
2. Acesse o dashboard em seu navegador em: [http://localhost:8501](http://localhost:8501)

## 🛡️ Observações de Segurança
- Os dados contidos no arquivo **perfomance.xlsx** não estão disponíveis no repositório público. Certifique-se de substituir por dados fictícios ou exemplos ao compartilhar.

## 📞 Suporte
Para dúvidas ou sugestões, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/anderson-luiz-781675153/).

---

© 2024 Desenvolvido por Anderson Luiz Ferreira de Oliveira.  
