for each in $(grep oslo_log -R ./ |awk -F: '{print $1}'  |grep py$ ); 
do 
sed 's/oslo_log/oslo.log/g' $each -i ; 
done 

