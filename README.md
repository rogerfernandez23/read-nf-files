# 🧾 Leitor de Notas Fiscais PJ

Um Script completo para leitura, extração e processamento de notas fiscais enviadas por colaboradores PJ. Compatível com arquivos em extensão **.xml** e **.pdf**. Essa aplicação extrai os dados, valida informações cruciais e junto a integração com o Google Sheets, insere em planilha para armazenamento e tratativas. Além de ser construído com uma interface gráfica para facilitar o uso dos demais colaboradores com ou sem conhecimento técnico.

---

## 🚀 Funcionalidades

- ✅ Leitura de **Notas Fiscais XML (NFe modelo 55)**
- ✅ Extração de **dados básicos de PDFs**
- ✅ Validação de **CNPJ e valores**
- ✅ Bloqueio de **notas duplicadas**
- ✅ Registro automático em **Google Sheets**
- ✅ Organização dos arquivos (XML, PDF, Erros)
- ✅ Geração e visualização de **logs de processamento**
- ✅ **Interface gráfica** com botões intuitivos via `Tkinter`

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – Interface gráfica
- [gspread](https://github.com/burnash/gspread) – Integração com Google Sheets
- [Google API Client](https://developers.google.com/sheets/api) – Autenticação com Google
- [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) – Leitura de XML
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – Extração de dados de PDFs
- [csv](https://docs.python.org/3/library/csv.html) – Manipulação de arquivos CSV
- [shutil / os / glob](https://docs.python.org/3/library/) – Organização e movimentação de arquivos
- Estrutura modular baseada em **Clean Code**

---

## ⚙️ **Como Usar**

1. Clone este repositório:

   ```bash
   git clone https://github.com/rogerfernandez23/read-nf-files.git
   cd read-nf-files
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure suas credenciais do Google Sheets (arquivo `credentials.json`).

4. Inicie a aplicação:

   ```bash
   python main.py
   ```

5. Faça upload da NFe em formato .xml ou .pdf e visualize os dados extraídos na planilha do Google Sheets.

\*. Necessário configurar as Credenciais de sua planlha no Google Cloud. Mais sobre: https://medium.com/@matheussouza004/acessando-uma-planilha-do-google-sheets-usando-python-dc243d9803c3
