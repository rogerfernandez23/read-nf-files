🧾 Leitor de Notas Fiscais PJ
Sistema completo para leitura e processamento automatizado de notas fiscais enviadas por colaboradores Pessoa Jurídica (PJ). Compatível com arquivos XML e PDF, o sistema realiza extração de dados, validação, integração com Google Sheets, e disponibiliza uma interface gráfica intuitiva para facilitar o uso por usuários não técnicos.

🚀 Funcionalidades

✅ Leitura de notas fiscais XML (modelo NFe)
✅ Extração de dados essenciais de notas em PDF
✅ Validação automática de CNPJ e valores
✅ Verificação de duplicidade contra planilha do Google Sheets
✅ Atualização automática da planilha "Notas Processadas"
✅ Movimentação automática de arquivos processados
✅ Geração e visualização de logs
✅ Interface gráfica simples e funcional com Tkinter

📁 Estrutura de Pastas

leitor-nf/
│
├── data/
│ ├── registros # Arquivo local de apoio
|
├── src/
│ ├── automation/ # Geração de logs
│ ├── extraction/ # Leitura e extração dos arquivos XML e PDF
│ ├── google/ # Integração com Google Sheets
│ ├── integration/ # Organização de diretórios e movimentação de arquivos
│ ├── processing/ # Processamento em lote dos arquivos
│ ├── storage/ # Gerenciamento do arquivo CSV local
│ └── view/ # Interface gráfica (GUI)
│
├── logs/ # Logs gerados por processamento
├── processados/ # Arquivos XML/PDF organizados após leitura
│ ├── xml/
│ ├── pdf/
│ └── erros/
│
├── credentials.json # Configure aqui suas credenciais da conta de serviço do Google
├── main.py # Ponto de execução do sistema
└── README.md
