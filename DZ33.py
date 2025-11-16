# from jinja2 import Template
#
#
# html = """
# {% macro fun_input(type='', name='', placeholder='') %}
#     <p><input type = "{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}"></p>
# {% endmacro %}
#
# {{ fun_input('text', 'firstname', 'имя') }}
# {{ fun_input('text', 'lastname', 'фамилия') }}
# {{ fun_input('text', 'address', 'адрес') }}
# {{ fun_input('text', 'phone', 'телефон') }}
# {{ fun_input('text', 'email', 'почта') }}
#
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


from jinja2 import Environment, FileSystemLoader


inputs = [
    {"type": "text", "name": "firstname", "placeholder": "имя"},
    {"type": "text", "name": "lastname", "placeholder": "фамилия"},
    {"type": "text", "name": "address", "placeholder": "адрес"},
    {"type": "tel", "name": "phone", "placeholder": "телефон"},
    {"type": "email", "name": "email", "placeholder": "почта"},

]



file_loader = FileSystemLoader('Dom33')
env = Environment(loader=file_loader)

tm = env.get_template('base.html')
msg = tm.render()
print(msg)