from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# class Money:
#     def __str__(self):
#         return 'Money'

#     def __init__(self, *args, **kwargs):
#         self.money = args

#     def __iter__(self):
#         return MoneyIterator(self)

#     def __len__(self):
#         return len(self.money)

#     def __getitem__(self, key):
#         return self.money[key]

# class MoneyIterator:
#     def __init__(self, money):
#         self.items = money
#         self.index = 0

#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         item = self.items[self.index]
#         self.index += 1
#         return item
