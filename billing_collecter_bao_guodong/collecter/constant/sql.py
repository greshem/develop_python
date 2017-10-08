# -*- coding:utf-8 -*-
'''
Created on 2015��9��16��

@author: baoguodong.kevin
'''
class SQL(object):
    instance="SELECT `uuid` as resource_id,user_id,project_id as tenant_id,display_name as resource_name,vm_state as `status`,created_at,updated_at,deleted_at,vcpus as cpu,memory_mb as memory FROM nova.instances \
    WHERE deleted=0 AND vm_state != 'error' AND created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"
    
    disk="SELECT id as resource_id,user_id,project_id as tenant_id,size as sum,`status`,display_name as resource_name,created_at,updated_at,deleted_at FROM cinder.volumes \
    WHERE deleted=0 AND created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"
    
    snapshot="SELECT snapshots.id as resource_id,snapshots.created_at,snapshots.updated_at,snapshots.user_id,snapshots.project_id as tenant_id,snapshots.status,snapshots.display_name as resource_name,volumes.size as sum \
    FROM (SELECT id,created_at,updated_at,user_id,project_id,`status`,display_name,volume_id FROM cinder.snapshots WHERE deleted=0 AND created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')) snapshots LEFT JOIN cinder.volumes ON snapshots.volume_id=volumes.id"
    
    ip="SELECT floatingips.id as resource_id,floatingips.tenant_id,floating_ip_address as resource_name,floatingips.status as `status`,ports.created_at \
    FROM neutron.floatingips LEFT JOIN neutron.ports ON floatingips.floating_port_id=ports.id WHERE created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"
    
    router="SELECT routers.tenant_id,routers.id as resource_id,routers.name as resource_name,routers.status,ports.created_at,bandwidth \
    FROM neutron.routers LEFT JOIN neutron.ports ON routers.gw_port_id=ports.id WHERE created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"
    
    vpn="SELECT id as resource_id,tenant_id,`name` as resource_name,`status` FROM neutron.vpnservices"
    
    image="SELECT user_id,images.id as resource_id,project_id as tenant_id,`name` as resource_name,count(instance_image.uuid) as sum FROM (SELECT `uuid`, user_id,project_id,image_ref FROM nova.instances WHERE image_ref IS NOT NULL AND deleted=0 \
    AND vm_state != 'error' AND created_at <= DATE_FORMAT(DATE_ADD(UTC_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i'))\
     instance_image LEFT JOIN glance.images ON instance_image.image_ref=images.id group by images.id" 
    
    send_using="SELECT us.*,billing_resource.resource_name,billing_resource.billing_item,billing_resource.region_id,billing_resource.sum,billing_resource.parent_id,billing_resource.status,billing_resource.resource_type,billing_resource.user_id,billing_resource.tenant_id \
                 FROM (SELECT using_id,resource_id,started_at,ended_at FROM using.using WHERE tran_status IS NULL OR tran_status != 'ack') us LEFT JOIN using.billing_resource ON us.resource_id=billing_resource.resource_id"

