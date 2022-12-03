"""""
Discente: Henrique Sabino Teixeira
"""""

agenda = {}

def incluirNovoNome(nome, telefones):
  agenda[nome] = telefones

def incluirTelefone(nome, telefone):
  if nome in agenda:
    agenda[nome].append(telefone)
  else:
    incluirNovoNome(nome, [telefone])

def excluirNome(nome):
  if nome in agenda:
    del agenda[nome]

def excluirTelefone(nome, telefone):
  if nome in agenda:
    if telefone in agenda[nome]:
      agenda[nome].remove(telefone)
    if agenda[nome] == []:
      excluirNome(nome)

def consultarTelefone(nome):
  if nome in agenda:
    return agenda[nome]

incluirNovoNome("Ana", [8299999999, 8255555555])
print(agenda)
incluirTelefone("Ana", 8244444444)
print(agenda)
incluirTelefone("João", 8233333333)
print(agenda)
excluirNome("João")
print(agenda)
excluirTelefone("Ana", 8244444444)
print(agenda)
incluirTelefone("João", 8233333333)
print(agenda)
excluirTelefone("João", 8233333333)
print(agenda)
print(consultarTelefone("Ana"))


dicio = {}

def incluirNovoNome (nome, numeros): dicio[nome] = numeros

def incluirTelefone (nome, numero):

  if nome in dicio: dicio[nome].append(numero)

  else:

      incluirNovoNome (nome, [numero])

def excluirNome(nome): 
  
  if nome in dicio: del dicio[nome]

def excluirTelefone (nome, telefone):

  if nome in dicio:

    if telefone in dicio[nome]:

      dicio[nome].remove(telefone)