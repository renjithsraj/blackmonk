import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
 
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

SLUG_NAME = {
    'user': 'username',
    'product': 'title'
}


def unique_slug_generator(instance, slug, model):
    col_name = SLUG_NAME.get(model)
    Model = instance.__class__
    max_length = Model._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = model.objects.filter(slug = slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug[:max_length-5], randstr = random_string_generator(size = 4))
        return unique_slug_generator(instance, slug=slug, model=model)
    return slug