for each in $(grep oslo.log -R ./ |awk -F: '{print $1}'  |grep py$ ); 
do 
sed 's/oslo.log/oslo_log/g' $each -i ; 
done 

