# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):# esta linha define o nosso modelo (é um objeto).class é uma palavra-chave especial que indica que estamos definindo um objeto.
    author = models.ForeignKey('auth.User')#models.ForeignKey - este é um link para outro modelo
    title = models.CharField(max_length=200)#models.CharField - assim é como você define um texto com um número limitado de caracteres.
    text = models.TextField()#models.TextField - este é para textos longos sem um limite. Será ideal para um conteúdo de post de blog, certo?
    created_date = models.DateTimeField(#models.DateTimeField - este é uma data e hora.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Post é o nome do nosso modelo, podemos lhe dar um nome diferente (mas é preciso evitar os espaços em branco e caracteres especiais).
# Sempre comece um nome de classe com uma letra maiúscula.
#models.Model significa que o Post é um modelo de Django, então o Django sabe ele que deve ser salvo no banco de dados.

#models.CharField - assim é como você define um texto com um número limitado de caracteres.







