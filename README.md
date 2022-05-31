# desafio-eureciclo
- [Sobre](#sobre)
- [Tecnologias](#techs)
- [Preview](#preview)
- [Como usar](#como-usar)
- [Entre em contato](#contato)

<h2 id="sobre">Sobre</h2>
Desafio para a vaga de desenvolvedor backend Python na empresa eureciclo.
A aplicação consiste em receber um arquivo .txt com dados de vendas e importá-las 
para o banco de dados. A interface web deve fazer o upload do arquivo, listar e 
detalhar as vendas que estão cadastradas no sistema.

Foi um projeto interessante no qual eu gostei muito de ter desenvolvido.
Já trabalhei com Django profissionalmente (manutenção e melhoria), porém foram poucos 
projetos criados do zero até hoje, e sempre projetos simples.

A principal experiência que levarei deste projeto foi: aprender tanto do Django em um 
projeto que em teoria é simples, mas que ao aplicar boas práticas e estruturação correta 
se tornou uma aplicação mais complexa e desafiadora que testou bem os meus conhecimentos.

<h2 id="tech">Tecnologias</h2>
<div style="display: flex">
  <img height="32" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png" alt="Python"/>
  <img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" alt="Javascript"/>
  <img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" alt="HTML5"/>
  <img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" alt="CSS"/>
  <img height="32" src="https://seeklogo.com/images/B/bulma-logo-45B5145BF4-seeklogo.com.png" alt="Bulma">
  <img height="32" src="https://seeklogo.com/images/D/django-logo-F46C1DD95E-seeklogo.com.png" alt="Django"/>
  <img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/postgresql/postgresql.png" alt="PostegreSQL"/>
  <img height="32" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" alt="Docker"/>
</div>

<h2 id="preview">Preview</h2>
Abaixo imagens do projeto:

### Página de importação
Página onde é feita a escolha do arquivo para importação das vendas.

<img width="auto" height="auto" src="docs/screenshots/import.png">

### Página de processamento
Página onde é mostrado o resultado da importação e parsing do arquivo enviado.
O usuário pode confirmar as informações contidas no arquivo e decidir se vai
cancelar a importação ou salvar no banco de dados.

<img width="auto" height="auto" src="docs/screenshots/processing.png">

### Página de resultado do processamento
Mostra quantas vendas foram importadas e a receita bruta das vendas.

<img width="auto" height="auto" src="docs/screenshots/result.png">

### Página de listagem de vendas
Mostra todas as vendas cadastradas no sistema.

<img width="auto" height="auto" src="docs/screenshots/sales list.png">

### Página de detalhes de uma venda
Mostra os detalhes de uma venda.

<img width="auto" height="auto" src="docs/screenshots/sale details.png">

### Aviso de erros
Quando acontece algum erro durante o processamento das vendas, a aplicação
volta para a página de importação e mostra um aviso na tela.

<img width="auto" height="auto" src="docs/screenshots/error.png">

<h2 id="como-usar">Como usar</h2>

### Iniciar a aplicação

Para rodar a aplicação é preciso ter o Docker instalado e rodar o seguinte comando na pasta raiz do projeto:

```bash
./run-server.sh
```

Caso você precise fazer o _build_ da aplicação basta rodar o script passando a opção de build:

```bash
./run-server.sh build
```

### Testes

Para executar os testes basta rodar o seguinte comando:

```bash
  ./run-tests.sh
```

Caso você deseje saber a cobertura de testes da aplicação rode o script com a opção de _coverage_:

```bash
  ./run-tests.sh coverage
```

### Como criar uma venda

Para criar uma venda será necessário obter um arquivo com a estrutura de correta para que as vendas sejam importadas com sucesso. Um arquivo exemplo está presente em _docs/example.txt_.

Obtendo o arquivo com a estrutura correta, faça o upload do arquivo e clique em iniciar. 
Caso tudo ocorra como o esperado, a tela com as informações das vendas será mostrada e bastará 
clicar em _Salvar_ para que os dados sejam salvos no banco de dados. Logo após será possível 
ver um resumo da importação na página de resultados.

<h2 id="contato">Contato</h2>

Minha redes para contato:

<div style="display: flex">
  <a href="https://www.linkedin.com/in/wagner-cardoso-dev">
    <img alt="Linkedin Wagner" width="32" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />
  </a>
  <a href="mailto:wagnerdev01@gmail.com">
    <img alt="Email Wagner" width="32" src="https://cdn4.iconfinder.com/data/icons/logos-brands-in-colors/48/google-gmail-512.png" />
  </a>
</div>