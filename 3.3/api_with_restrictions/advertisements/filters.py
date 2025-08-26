from django_filters import FilterSet, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
