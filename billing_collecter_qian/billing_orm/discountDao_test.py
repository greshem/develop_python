#!/usr/bin/python 
# /root/billing/billing/db/dao/discountDao.py
# /root/billing/billing/db/object/models.py

if __name__=='__main__':
    import sys;

    sys.path.append("/root/billing/");
    from billing.db.dao.discountDao  import DiscountDao;
    from billing.db.object.models import Discount


    discount=DiscountDao();
    discount.list("account_id");
    row=discount.getDiscountDetail();
    for each in row: 
        print each.discount_ratio;
        print each.discount_id;
        print each.account_id;
        print each.billing_item_id;
        print each.billing_item ;

    dis=Discount();
    dis.discount_ratio=0.6;
    dis.discount_id="uuid";
    dis.account_id="uuid"
    #dis.billing_item_id=3;
    discount.add(dis);
    
    #print dir(each);

    #def list(self,account_id,region_id=None,session=None):

