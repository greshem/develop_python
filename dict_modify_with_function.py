

def _replace_v2_parameters(data):
    data['display_name'] = data['name']
    data['display_description'] = data['description']
    del data['name']
    del data['description']
    return data

data = {'name': 'name',
        'description': 'description',
        'volume_type': 'volume_type',
        'snapshot_id': 'snapshot_id',
        'metadata': 'metadata',
        'imageRef': 'image_id',
        'availability_zone': 'availability_zone',
        'source_volid': 'source_volid'}
data = _replace_v2_parameters(data)

import json
d4 = json.dumps(data, indent=1, sort_keys=True)
print d4

