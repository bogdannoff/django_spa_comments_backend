
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin, CreateModelMixin, PaginatedModelListMixin, \
    UpdateModelMixin, DeleteModelMixin, PatchModelMixin

from djangochannelsrestframework.pagination import WebsocketLimitOffsetPagination

from comments.models import Comments
from comments.serializers import CommentsSerializer


class CommentsPagination(WebsocketLimitOffsetPagination):

    default_limit = 10
    max_limit = 100

    def paginate_queryset(self, queryset, scope, view=None, ** kwargs):
        parents = super().paginate_queryset(queryset, scope, view, ** kwargs)
        children = list(Comments.objects.filter(parent_first_level__in=parents))
        return parents+children


class CommentsConsumer(
        PaginatedModelListMixin,
        CreateModelMixin,
        PatchModelMixin,
        DeleteModelMixin,
        GenericAsyncAPIConsumer,
):

    queryset = Comments.objects.filter(parent=None)
    serializer_class = CommentsSerializer
    pagination_class = CommentsPagination

    def get_queryset(self, **kwargs):
        # queryset = super().get_queryset(**kwargs)
        if kwargs.get('action') == 'list':
            queryset = Comments.objects.filter(parent=None)
        else:
            queryset = Comments.objects.all()
        return queryset
