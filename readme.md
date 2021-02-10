# Projeto Django Smarket

Este é um simples projeto em `python`/`django` que serve de teste para a Smarket, desenvolvido por Darci.

## Criando o ambiente ##
Confirmar se python e virtualenv estão instalados.

##### Python
Escrever o comando ``python --version`` e garantir que a saida é algo parecido com:

```
Python 3.8.7 
```

##### Virtualenv
Escrever o comando ``virtualenv --version`` e verificar a saida:
```
virtualenv 20.4.2
```

Caso tenha algum problema, esse link pode ajudar (https://docs.python.org/pt-br/3/tutorial/venv.html)


Após baixar o codigo fonte, entre na pasta TestDjangoSmarket pelo terminal (`cd TestDjangoSmarket`) e crie um ambiente virtual novo 

```
virtualenv venv
``` 

e o ative.
```
venv\Scripts\activate.bat
```

Instale os pacotes requiridos usando o seguinte codigo.

```
pip install -r requirements.txt
```


## Rodando o servidor ##
Para rodar o servidor basta entrar na pasta UserTask (`cd UserTask`) e executar o comando 
```
python manage.py runserver
```

Com isso, o servidor deve subir e começar a escutar os requests, para iniciar você pode entrar na seguinte url (http://127.0.0.1:8000/).