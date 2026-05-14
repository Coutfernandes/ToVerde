👨‍💻 Autor
Desenvolvido por Matheus CoutinhoExcelente descrição! Esse conteúdo já está muito bem estruturado. Para criar o arquivo README.md perfeito para o ToVerde no seu GitHub, vou organizar essas informações usando formatação Markdown profissional, incluindo ícones e blocos de código.

Basta copiar o conteúdo abaixo e colar no seu arquivo README.md:

🌿 ToVerde - Sistema de Monitoramento Ambiental
O ToVerde é uma plataforma full-stack desenvolvida para facilitar a denúncia e o monitoramento de crimes ambientais. O objetivo central é conectar cidadãos e autoridades para combater atividades como desmatamento, queimadas e poluição, promovendo uma fiscalização mais ágil e participativa.

🚀 Funcionalidades
Autenticação Completa: Sistema seguro de cadastro, login, logout e recuperação de senha via e-mail.

Denúncias Dinâmicas: Submissão de ocorrências com suporte para anexos (fotos/vídeos) e opção de envio anônimo.

Painel Administrativo: Interface customizada para gestão de denúncias, permitindo filtros avançados e controle de status.

Perfil do Usuário: Área exclusiva para o usuário logado acompanhar o histórico e a evolução de suas próprias denúncias.

Design Responsivo: Interface moderna construída com Bootstrap, garantindo navegabilidade em computadores e dispositivos móveis.

🛠️ Tecnologias Utilizadas
O projeto utiliza o padrão de arquitetura MTV (Model-Template-View) do Django:

Linguagem: Python

Framework Web: Django

Frontend: HTML5, CSS3, JavaScript e Bootstrap

Banco de Dados: SQLite (Ambiente de desenvolvimento)

Versionamento: Git

🔧 Como Instalar e Rodar o Projeto
Clone o repositório:

Bash
git clone [https://github.com/Coutfernandes/ToVerde.git](https://github.com/Coutfernandes/ToVerde.git)
Crie um ambiente virtual e instale as dependências:

Bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
Execute as migrações e inicie o servidor:

Bash
python manage.py migrate
python manage.py runserver
Acesse o sistema em http://127.0.0.1:8000/.
