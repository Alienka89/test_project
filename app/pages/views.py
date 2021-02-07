from rest_framework import (generics, mixins)
from rest_framework.response import Response

from .models import (Page, )
from .serializers import (PageSerializer, PageShortSerializer)
from .tasks import update_counter


class PageListView(generics.ListAPIView):
    queryset = Page.objects.filter(hide=False)
    serializer_class = PageShortSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)


class PageView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Page.objects.filter(hide=False)
    lookup_url_kwarg = 'pk'
    serializer_class = PageSerializer

    def get(self, request, pk, *args, **kwargs):
        response = self.retrieve(request, pk, *args, **kwargs)
        update_counter.delay(pk)
        return response
