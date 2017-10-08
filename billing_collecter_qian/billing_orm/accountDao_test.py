# -*- coding:utf-8 -*-

# /root/billing/billing/db/dao/ accountDao.py

import sys;
sys.path.append("/root/billing/");
from billing.db.dao.accountDao  import AccountDao;
from billing.db.object.models import Account


def add_one_user(id, name ):
    account=Account()
    account.account_id=id
    account.username=name
    account.gift_balance=999
    account.cash_balance=1999
    account.type="credt"
    account.status="normal"
    accountDao=AccountDao(account)
    accountDao.add()
    print account.created_at


if __name__=='__main__':
    add_one_user("account_333", "user_name_333");
