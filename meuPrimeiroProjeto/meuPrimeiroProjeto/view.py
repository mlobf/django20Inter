from django.http import HttpResponse


def hello(response):
    return HttpResponse('Hello World')


def articles(request, year):
    return HttpResponse('O ano enviado foi ' + str(year))


def lerbanco(nome):
    lista_nomes = [
        {'nome': 'ana', 'idade': 20},
        {'nome': 'joaquim', 'idade': 25},
        {'nome': 'pedro', 'idade': 33}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Nao encontrado ', 'idade': 0}


def fname(request, nome):
    result = lerbanco(nome)
    print(result)
    return HttpResponse("A pessoa " + str(nome).capitalize() +" foi encontrada, ela tem " + str(result['idade']) + ' anos.')