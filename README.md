# Talk-to-Mia
Mia é uma IA de conversa feita como parte um projeto de Desenvolvimento Back-End.
Sua lógica principal funciona a partir de receber um prompt de texto, definir um assunto de um banco de assuntos pré-definidos e devolver uma resposta baseada nesse assunto, também de um banco de respostas pré-definidas.

Essa versão da Mia foi criada usando Django e é baseada na Web.
Para começar a usar a Mia, clone o repositório e realize os seguintes comandos em um terminal:

- Criar o ambiente virtual
<pre>
python -m venv venv
</pre>

- Ativar os scripts. Se o terminal ficar verde, funcionou.
<pre>
venv/scripts/activate
</pre>

- Instalar dependências
<pre>
pip install -r ./requirements.txt
</pre>

- Iniciar o servidor web localmente.
<pre>
python manage.py runserver
</pre>

O scikit-learn é uma dependência pesada.
