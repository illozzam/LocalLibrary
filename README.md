# Projeto LocalLibrary - JeffMudrei

Este projeto foi modificado a partir de um fork [deste repositório](https://github.com/JeffMudrei/LocalLibrary).

Desenvolvido em Python 3.7 e Django 2.2.12

Instalação:
Com o virtualenv ativado:
```
pip install -r requirements.txt
```

Lista de modificações (07/05/2020):
1. O model 'Author' deixou de ser abstrato e passou a ser um objeto relacionado ao model Book
2. Criada a pasta 'catalog' dentro dos templates do app 'catalog'. Isso facilitaria a identificação do template caso o projeto fique muito extenso e seja necessário criar mais apps.
2. Os perfis Author e Book foram criados no admin do catalog
3. Instalado o [Django Rest Framework](https://www.django-rest-framework.org/) para gerir o funcionamento da API
4. Programadas as rotinas básicas da API para Author e Book (em 'api', dentro do app 'catalog')
5. Atualizadas as URLs do projeto para o funcionamento correto da API
