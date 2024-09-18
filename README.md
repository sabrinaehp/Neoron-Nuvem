# Nuvem - Gerenciador de Voos

## 1. Descrição
O **Nuvem** é um sistema feito para ajudar uma empresa de aviação a gerenciar seus voos, trocando o uso de planilhas Excel por algo mais fácil e acessível na nuvem. Ele foi criado como um desafio da **empresa Neoron**, com o objetivo de melhorar a organização e o controle dos voos de forma mais rápida e eficiente.

## 2. Estrutura do Projeto
- **app.exe**: O arquivo que executa o sistema.
- **db.sqlite3**: Banco de dados que guarda todas as informações dos voos.
- **static/**: Pasta com arquivos como CSS e imagens.
- **views/**: Parte visual e APIs do sistema.
- **db_requests.py**: Arquivo que faz as operações no banco de dados (como cadastrar, apagar e consultar voos).
- **utils.py**: Funções extras para ajudar no funcionamento do sistema.

## 3. Funcionalidades
- Permite cadastrar voos (com informações como código do voo, origem, destino, data e horário).
- Segue algumas regras de negócio, como a diferença de pelo menos 30 minutos entre voos e não ter dois voos para o mesmo destino no mesmo dia.
- Consultar os voos que já estão cadastrados.
- Excluir voos.

## 4. Como Executar
1. Abra a pasta onde está o arquivo **app.exe**.
2. Clique duas vezes em **app.exe** para abrir o sistema e começar a gerenciar os voos.

## 5. Banco de Dados
O **Nuvem** usa um banco de dados SQLite, que fica no arquivo **db.sqlite3**, onde são guardadas todas as informações dos voos cadastrados.
