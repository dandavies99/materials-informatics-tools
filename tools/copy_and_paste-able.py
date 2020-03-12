# Render dicts as json in jupyter notebooks
if get_ipython().__class__.__name__=='ZMQInteractiveShell':
    from IPython.display import JSON
    from json import JSONEncoder, loads
    class MyEncoder(JSONEncoder):
            def default(self, o):
                try:
                    return o.as_dict()
                except:
                    try:
                        return o.__dict__
                    except:
                        return str(o)
    show_json = lambda x : display(JSON(loads(MyEncoder().encode(x))))
