import django_filters
from django.db.models import Exists, OuterRef
from remember.models import Remember
from .models import Account

class AccountFilter(django_filters.FilterSet):
  has_remembered_leaf = django_filters.BooleanFilter(method='filter_has_remembered_leaf')

  class Meta:
    model = Account
    fields = ['has_remembered_leaf']

  def filter_has_remembered_leaf(self, queryset, name, value):
    if value:
      return queryset.filter(
        Exists(Remember.objects.filter(user_id=OuterRef('user_id')))
      )
    return queryset.exclude(
      Exists(Remember.objects.filter(user_id=OuterRef('user_id')))
    )