#!/usr/bin/python

g_resource_keys=  ["resource_id","resource_name","billing_item","region_id","sum","parent_id","status","account_id","created_at","updated_at","deleted_at","resource_type","user_id", "tenant_id" ];

def keys_must_exist(resource_dict):
    global g_resource_keys;

    assert(isinstance(resource_dict, dict)) ;

    assert('resource_id'    in  resource_dict.keys());
    assert('resource_name'  in  resource_dict.keys());
    assert('billing_item'   in  resource_dict.keys());
    assert('region_id'      in  resource_dict.keys());
    assert('sum'            in  resource_dict.keys());
    assert('parent_id'            in  resource_dict.keys());
    assert('resource_type'  in  resource_dict.keys());
    assert('status'         in  resource_dict.keys());

    assert('user_id'      in  resource_dict.keys());
    assert('tenant_id' in  resource_dict.keys());

    assert('created_at' in  resource_dict.keys());
    assert('deleted_at' in  resource_dict.keys());
    assert('updated_at' in  resource_dict.keys());
    assert('resource_type' in  resource_dict.keys());


def keys_must_exist2(resource_dict):
    global  g_resource_keys;
    for each in resource_dict.keys():
        assert( [each in  g_resource_keys] );

def  check_resource_item_dict(resource_dict): 
    global g_resource_keys
    items_from_dict=resource_dict.keys();
    #items=g_resource_keys;

    items_from_dict.sort(); 
    g_resource_keys.sort();
    assert( items_from_dict == g_resource_keys); 
    if not( items_from_dict == g_resource_keys):
        return True;
    else: 
        return False;


if __name__=="__main__":
    a={ 
    "sum":4,
    "sum33":4,
};

    b={"resource_id": "aa",
    "resource_name": "bb",
    "billing_item": "item",
    "region_id":  "region",
    "sum":  4,
    "parent_id": "parent",
    "status":    "active",
    "account_id": "account_id",
    "created_at": "created_at",
    "updated_at": "updated_at",
    "deleted_at": "deleted_at",
    "resource_type": "resource_type", 
    "user_id": "user_id", 
    "tenant_id": "tenant_id", 
    };

    #keys_must_exist2(a);
    #print a;
    keys_must_exist(b);
    check_resource_item_dict(b);
