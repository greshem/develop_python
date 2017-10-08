
# /home/tmp3/pypi/django-account/django-account-0.1.9/account/utils.py 
def render_to(template_path):
    """
    Decorate the django view.

    Wrap view that return dict of variables, that should be used for
    rendering the template.
    """

    def decorator(func):
        def wrapper(request, *args, **kwargs):
            output = func(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            ctx = RequestContext(request)
            return render_to_response(template_path, output,
                                      context_instance=ctx)
        return wrapper
    return decorator


