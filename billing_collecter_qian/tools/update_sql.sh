#append   user_id  field 
alter  table account  add  user_id varchar(64) NOT NULL; 
update account set user_id=account_id  ;
