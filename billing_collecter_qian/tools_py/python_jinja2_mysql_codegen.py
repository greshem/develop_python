from jinja2 import Environment as JinjaEnvironment

def generator_one_table(table_name,table):
    context = {
        'name': table_name,
        'table': table
    }

    source = """\
#!/usr/bin/python  

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'mysql+mysqldb://root:password@192.168.210.31/nova?charset=utf8'
#engine = create_engine(DB_CONNECT_STRING, echo=True)
engine = create_engine(DB_CONNECT_STRING, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
for row in session.execute('select * from  ${name}   ;').fetchall():
    row=dict(zip(row.keys(), row.values()));
% for cell in table
    ${cell}=row["${cell}"];
% endfor
% for cell in table
    print "${cell}=%s"%${cell};
% endfor

 \
""";

    jinja_template = JinjaEnvironment(
        line_statement_prefix='%',
        variable_start_string="${",
        variable_end_string="}"
    ).from_string(source)
    #print   
    jinja_template.environment.compile(source, raw=True)


    str=jinja_template.render(context)
    f = open("%s.py"%table_name, "w")
    f.write("%s"%str);
    f.close();






def test():
    sample_table=dict( created_at=1, updated_at=1, deleted_at=1, id=1, internal_id=1, user_id=1, project_id=1, image_ref=1, kernel_id=1, ramdisk_id=1, launch_index=1, key_name=1, key_data=1, power_state=1, vm_state=1, memory_mb=1, vcpus=1, hostname=1, host=1, user_data=1, reservation_id=1, scheduled_at=1, launched_at=1, terminated_at=1, display_name=1, display_description=1, availability_zone=1, locked=1, os_type=1, launched_on=1, instance_type_id=1, vm_mode=1, uuid=1, architecture=1, root_device_name=1, access_ip_v4=1, access_ip_v6=1, config_drive=1, task_state=1, default_ephemeral_device=1, default_swap_device=1, progress=1, auto_disk_config=1, shutdown_terminate=1, disable_terminate=1, root_gb=1, ephemeral_gb=1, cell_name=1, node=1, deleted=1, locked_by=1, cleaned=1, ephemeral_key_uuid=1)

    generator_one_table("test", sample_table);

if __name__=="__main__":
    from   gen_dump_sql_code  import  dump_one_database;
    ret_db=dump_one_database();
    for key in  ret_db:
        print "%s"%key;
        print "%r"%ret_db[key];
        generator_one_table(key, ret_db[key]);


    #test();
