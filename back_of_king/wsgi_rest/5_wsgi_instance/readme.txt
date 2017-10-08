curl -X GET -H "X-Auth-Token:open-sesame"  192.168.82.173:8088/instances
curl -X GET -H "X-Auth-Token:open-sesame"  192.168.82.173:8088/instances?action=print


#action show, instances/d733b3fc-c83d-4e1e-833c-19429a693adf
#匹配了这条记录.
#self.mapper.connect("/instances/{instance_id}",
#                           controller=controller, action="show",
#                           conditions=dict(method=["GET"]))


curl -X GET -H "X-Auth-Token:open-sesame"  192.168.82.173:8088/instances/d733b3fc-c83d-4e1e-833c-19429a693adf



(3)、GET /instances/{instance_id} 
curl -H 'X-Auth-Token:open-sesame' -X GET  127.0.0.1:8000/instances/c81e83fe-ae90-44a3-89e7-20918dfa9aef  
{instance_id}是要查询的虚拟机的id，需要根据自己的实际情况修改。可以通过GET /instances来查看所有虚拟机记录的id

(4)、PUT /instances/{instance_id} 

curl -H 'X-Auth-Token:open-sesame' -X PUT --data 'name=new-inst2' > 127.0.0.1:8000/instances/c81e83fe-ae90-44a3-89e7-20918dfa9aef  

(5)、DELETE /instances/{instance_id}
curl -H 'X-Auth-Token:open-sesame' -X DELETE  > 127.0.0.1:8000/instances/c81e83fe-ae90-44a3-89e7-20918dfa9aef  
