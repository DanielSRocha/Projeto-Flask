# Estilo Único - Sistema de Gestão de Loja de Roupas

Bem-vindo ao Estilo Único, uma aplicação web desenvolvida em Python com o framework Flask, projetada para ajudar donos de lojas de roupas a gerenciar seu inventário de forma eficiente. Este projeto utiliza o PostgreSQL como banco de dados para armazenar informações sobre os produtos disponíveis na loja.

## Visão Geral

Estilo Único é uma loja de roupas online que visa proporcionar aos clientes uma experiência única e personalizada ao comprar roupas de moda. Com este sistema de gestão, os proprietários de lojas podem facilmente adicionar, editar e excluir produtos do seu inventário, garantindo que sempre tenham os itens mais recentes disponíveis para seus clientes.

## Funcionalidades Principais

- **Cadastro de Produtos**: Os usuários podem adicionar novos produtos ao inventário, incluindo informações como nome, descrição, preço e quantidade disponível.

- **Edição de Produtos**: É possível atualizar as informações dos produtos existentes, como preço e quantidade disponível, para refletir mudanças no estoque ou nas especificações do produto.

- **Exclusão de Produtos**: Caso um produto não esteja mais disponível para venda, os usuários podem removê-lo do inventário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.

- **Flask**: Framework web utilizado para construir a aplicação web.

- **PostgreSQL**: Banco de dados relacional utilizado para armazenar informações sobre os produtos da loja.

## Como Usar

1. **Pré-requisitos**: Certifique-se de ter o Python e o PostgreSQL instalados em seu sistema.

2. **Clonar o Repositório**: Clone este repositório em sua máquina local usando o seguinte comando:

    ```
    git clone https://github.com/seu-usuario/estilo-unico.git
    ```

3. **Configurar o Ambiente**: Instale as dependências do projeto executando o seguinte comando no terminal:

    ```
    pip install -r requirements.txt
    ```

4. **Configurar o Banco de Dados**: Crie um banco de dados PostgreSQL chamado `estilo_unico` e configure as credenciais de acesso no arquivo `config.py`.

5. **Executar a Aplicação**: Inicie o servidor Flask executando o seguinte comando no terminal:

    ```
    python app.py
    ```

6. **Acessar a Aplicação**: Abra o navegador da web e acesse `http://localhost:5000` para usar a aplicação.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novas funcionalidades ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Este projeto foi desenvolvido por [Daniel Servino da Rocha](https://github.com/DanielSRocha).
