'''Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura'''
print('========== DESAFIO 19 ==========')
from rich import print
from time import sleep

class Livro:
    pag = 2
    def __init__(self, titulo = '', paginas = 0):
        self.titulo = titulo
        self.paginas = paginas
        print(f":open_book: [blue]Você acabou de abrir o livro '[/][red]{self.titulo}[/]' [blue]que tem [/][green]{self.paginas} páginas [/][blue]no total. Você agora está na [/][yellow]página 1[/]")

    def avancar_paginas(self, n):
        cont = 0
        for c in range(Livro.pag, Livro.pag + n):
            if Livro.pag <= self.paginas:
                print(f'Pág{Livro.pag} :arrow_forward:', end=' ', flush=True)
                sleep(0.5)
                Livro.pag += 1
                cont += 1
        print(f'[blue]Você avançou {cont} páginas e agora está na [yellow]página {Livro.pag - 1}[/]')
        if Livro.pag - 1 == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

l1 = Livro('10 Coisas que Aprendi', 34)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)