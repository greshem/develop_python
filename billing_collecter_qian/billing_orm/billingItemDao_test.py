#!/usr/bin/python 
# /root/billing/billing/db/dao/billingItemDao.py
# /root/billing/billing/db/object/models.py

if __name__=='__main__':
    import sys;

    sys.path.append("/root/billing/");
    from billing.db.dao.billingItemDao  import BillingItemDao;
    from billing.db.object.models import BillingItem;


    item=BillingItemDao();
    #'billing_item', 'billing_item_id', 'created_at', 'get', 'iteritems', 'metadata', 'next', 'price', 'region_id', 'save', 'unit', 'update', 'updated_at'

    for each in item.list(): 
        print each.billing_item;
        print each.billing_item_id;
        print each.price;
