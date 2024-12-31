import inspect


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    info['methods'] = [met for met in dir(obj) if met.startswith('__')]
    if inspect.getmodule(obj) is None:
        info['module'] = '__main__'
    else:
        info['module'] = inspect.getmodule(obj)
    return info

number_info = introspection_info(52)
print(number_info)
