class APIResourceWrapper(object):
    """Simple wrapper for api objects.

    Define _attrs on the child class and pass in the
    api object as the only argument to the constructor
    """
    _attrs = []
    _apiresource = None  # Make sure _apiresource is there even in __init__.

    def __init__(self, apiresource):
        self._apiresource = apiresource

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if attr not in self._attrs:
                raise
            # __getattr__ won't find properties
            return getattr(self._apiresource, attr)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             dict((attr, getattr(self, attr))
                                  for attr in self._attrs
                                  if hasattr(self, attr)))

    def to_dict(self):
        obj = {}
        for key in self._attrs:
            obj[key] = getattr(self._apiresource, key, None)
        return obj


class BaseCinderAPIResourceWrapper(APIResourceWrapper):

    @property
    def name(self):
        # If a volume doesn't have a name, use its id.
        return (getattr(self._apiresource, 'name', None) or
                getattr(self._apiresource, 'display_name', None) or
                getattr(self._apiresource, 'id', None))

    @property
    def description(self):
        return (getattr(self._apiresource, 'description', None) or
                getattr(self._apiresource, 'display_description', None))



class Volume(BaseCinderAPIResourceWrapper):

    _attrs = ['id', 'name', 'description', 'size', 'status', 'created_at',
              'volume_type', 'availability_zone', 'imageRef', 'bootable',
              'snapshot_id', 'source_volid', 'attachments', 'tenant_name',
              'consistencygroup_id', 'os-vol-host-attr:host',
              'os-vol-tenant-attr:tenant_id', 'metadata',
              'volume_image_metadata', 'encrypted', 'transfer']

    @property
    def is_bootable(self):
        return self.bootable == 'true'

a=Volume("www.baidu.com");
a.size="333";
#a.description="description";
#a.name="aaaaaa";
a.status="error";
print a;
print a.to_dict();
