import django
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class IntrospectionView(LoginRequiredMixin, TemplateView):
    template_name = "introspect/introspect.txt"
    content_type = 'text/plain'

    def get_app_version(self, app):
        if hasattr(app, 'get_version'):
            get_version = app.get_version
            if callable(get_version):
                version = get_version()
            else:
                version = get_version
        elif hasattr(app, 'VERSION'):
            version = app.VERSION
        elif hasattr(app, '__version__'):
            version = app.__version__
        else:
            return
        if isinstance(version, (list, tuple)):
            version = '.'.join(str(o) for o in version)
        return version

    def get_context_data(self, **kwargs):
        ctx = super(IntrospectionView, self).get_context_data(**kwargs)
        ctx.update(django_version=self.get_app_version(django))
        return ctx

