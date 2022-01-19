from django.contrib import messages


class DataMixin:
    """Mixin for all clases that we have to
    make they shorter and fater"""
    paginate_by = 12  # needs to be queryset in function(not import tegs '{% load menu_tags %}' )

    def __init__(self) -> None:
        self.order_list = ["newest", "most popular 👇",
                           "most popular 👆", "price 👆", "price 👇"]

    def get_user_context(self, *args, **kwargs):
        context = kwargs
        context["order_list"] = self.order_list
        return context

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)
