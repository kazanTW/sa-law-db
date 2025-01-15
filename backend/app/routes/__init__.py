from .law import LawResource

def register_routes(api):
    api.add_resource(LawResource, '/laws')
