from django import template
from django.db.models import Count

from ..models import Post, Tags

register = template.Library()

@register.simple_tag()
def get_favorite_posts():
    return Post.objects.annotate(num_likes=Count('views')).order_by('-num_likes')[:5]

