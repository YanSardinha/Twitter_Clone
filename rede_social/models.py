from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    slug = models.SlugField('Slug', max_length=250)
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuário',
        related_name='pessoa')
<<<<<<< HEAD
    amigos = models.ManyToManyField('Pessoa', symmetrical=False, blank= True)
=======
    #amigos = models.ManyToManyField('Pessoa', symmetrical=False, blank= True)
>>>>>>> 076ec4b251c448a12cd3d9503697beb30cdeff1f

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Pessoa, self).save(*args, **kwargs)

    @property
    def qt_seguidores(self):
        "Retorna quantidade de pessoas que são seguidores."
        return Seguir.objects.filter(segue_usuario = self.user).count()

    @property
    def qt_seguindo(self):
        "Retorna quantidade de pessoas que o usuário segue."
        return Seguir.objects.filter(usuario = self.usuario).count()

class Seguir(models.Model):
    usuario = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    segue_usuario = models.ForeignKey(User, related_name='segue_usuario', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class Postagem(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa" )
<<<<<<< HEAD
    conteudo = models.TextField('Conteudo', max_length=300)
=======
    conteudo = models.TextField('Conteudo', max_length=200)
>>>>>>> 076ec4b251c448a12cd3d9503697beb30cdeff1f
    data = models.DateTimeField("Data de publicação", auto_now_add=True)

    def __str__(self):
        return self.conteudo

    @property
    def qt_comentarios(self):
        "Retorna quantidade de comentarios"
        return Comentario.objects.filter(postagem=self).count()

class Comentario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, verbose_name="Postagem")
    conteudo = models.TextField('Comentario', max_length=200)
    data = models.DateTimeField("Data de publicação", auto_now_add=True)

    def __str__(self):
        return self.conteudo

class MensagemDeContato(models.Model):
    class Meta:
        verbose_name = 'Mensagem de contato'
        verbose_name_plural = 'Mensagens de contato'

    nome = models.CharField(max_length=128)
    email = models.EmailField('E-mail', null = True, blank = True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add = True)