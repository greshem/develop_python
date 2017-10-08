from jinja2 import Environment as JinjaEnvironment

context = {
    'page_title': 'mitsuhiko\'s benchmark',
    'table': [dict(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)
  ,dict(a=11,b=22,c=33,d=44,e=55,f=6,g=7,h=8,i=9,j=10)
]
}

source = """\
% macro testmacro(x)
  <span>${x}</span> 
% endmacro
<!doctype html>
<html>
  <head>
    <title>${page_title|e}</title>
  </head>
  <body>
    <div class="header">
      <h1>${page_title|e}</h1>
    </div>
    <div class="table">
      <table>
      % for row in table
        <tr>
        % for cell in row
          <td>key=${testmacro(cell)}
	  </td>
  	  <td>value=${testmacro(row[cell])}
	  </td>

        % endfor
        </tr>
      % endfor
      </table>
    </div>
  </body>
</html>\
"""
jinja_template = JinjaEnvironment(
    line_statement_prefix='%',
    variable_start_string="${",
    variable_end_string="}"
).from_string(source)
#print  
jinja_template.environment.compile(source, raw=True)


print jinja_template.render(context)
