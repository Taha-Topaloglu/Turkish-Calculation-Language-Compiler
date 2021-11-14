import re
f = open('calc')
content = f.readlines()
init_var = {}
init_value = {}
mid_var = {}
mid_value = {}
first_part = None
middle_part = None
last_part = None
t_digits = ['sifir','bir','iki','uc','dort','bes','alti','yedi','sekiz','dokuz']
content = [x.strip() for x in content]
for element in range(len(content)):
    if content[element] == 'AnaDegiskenler':
        first_part = element
    if content[element] == 'YeniDegiskenler':
        middle_part = element
    if content[element] == 'Sonuc':
        last_part = element
if last_part == None or middle_part == None or first_part == None or not last_part > middle_part > first_part :
    print('syntax')
else:
    pass
for i in range(1,middle_part):
    if re.findall('degeri',content[i]) == [] or re.findall('olsun',content[i]) == []:
        print('syntax')
    else:
        continue
for n in range(1,middle_part):
    init_var[n] = re.findall('(^[A-Za-z0-9_]{1,10})\s*\t*degeri',content[n])
for n in range(1,middle_part):
    init_value[n] = re.findall('degeri\s*\t*(.+?)\s*\t*olsun$',content[n])
for control in init_var.values():
    if control == [] or control == None:
        print('syntax')
for value in init_value.values():
    val = str(value)
    control = re.findall('\d{1}|\d{1}\.\d{1}|dogru|yanlis',val)
    if control == [] or control == None:
        if value == 'bir' or value == 'iki' or value == 'uc' or value == 'dort' or value == 'bes' or value == 'alti' or value == 'yedi' or value == 'sekiz' or value == 'dokuz':
            control = re.findall('sifir\s*nokta\s*sifir|sifir\s*nokta\s*bir|sifir\s*nokta\s*iki|sifir\s*nokta\s*uc|sifir\s*nokta\s*dort|sifir\s*nokta\s*bes|sifir\s*nokta\s*alti|sifir\s*nokta\s*yedi|sifir\s*nokta\s*sekiz|sifir\s*nokta\s*dokuz|bir\s*nokta\s*sifir|bir\s*nokta\s*bir|bir\s*nokta\s*iki|bir\s*nokta\s*uc|bir\s*nokta\s*dort|bir\s*nokta\s*bes|bir\s*nokta\s*alti|bir\s*nokta\s*yedi|bir\s*nokta\s*sekiz|bir\s*nokta\s*dokuz|iki\s*nokta\s*sifir|iki\s*nokta\s*bir|iki\s*nokta\s*iki|iki\s*nokta\s*uc|iki\s*nokta\s*dort|iki\s*nokta\s*bes|iki\s*nokta\s*alti|iki\s*nokta\s*yedi|iki\s*nokta\s*sekiz|iki\s*nokta\s*dokuz|uc\s*nokta\s*sifir|uc\s*nokta\s*bir|uc\s*nokta\s*iki|uc\s*nokta\s*uc|uc\s*nokta\s*dort|uc\s*nokta\s*bes|uc\s*nokta\s*alti|uc\s*nokta\s*yedi|uc\s*nokta\s*sekiz|uc\s*nokta\s*dokuz|dort\s*nokta\s*sifir|dort\s*nokta\s*bir|dort\s*nokta\s*iki|dort\s*nokta\s*uc|dort\s*nokta\s*dort|dort\s*nokta\s*bes|dort\s*nokta\s*alti|dort\s*nokta\s*yedi|dort\s*nokta\s*sekiz|dort\s*nokta\s*dokuz|bes\s*nokta\s*sifir|bes\s*nokta\s*bir|bes\s*nokta\s*iki|bes\s*nokta\s*uc|bes\s*nokta\s*dort|bes\s*nokta\s*bes|bes\s*nokta\s*alti|bes\s*nokta\s*yedi|bes\s*nokta\s*sekiz|bes\s*nokta\s*dokuz|alti\s*nokta\s*sifir|alti\s*nokta\s*bir|alti\s*nokta\s*iki|alti\s*nokta\s*uc|alti\s*nokta\s*dort|alti\s*nokta\s*bes|alti\s*nokta\s*alti|alti\s*nokta\s*yedi|alti\s*nokta\s*sekiz|alti\s*nokta\s*dokuz|yedi\s*nokta\s*sifir|yedi\s*nokta\s*bir|yedi\s*nokta\s*iki|yedi\s*nokta\s*uc|yedi\s*nokta\s*dort|yedi\s*nokta\s*bes|yedi\s*nokta\s*alti|yedi\s*nokta\s*yedi|yedi\s*nokta\s*sekiz|yedi\s*nokta\s*dokuz|sekiz\s*nokta\s*sifir|sekiz\s*nokta\s*bir|sekiz\s*nokta\s*iki|sekiz\s*nokta\s*uc|sekiz\s*nokta\s*dort|sekiz\s*nokta\s*bes|sekiz\s*nokta\s*alti|sekiz\s*nokta\s*yedi|sekiz\s*nokta\s*sekiz|sekiz\s*nokta\s*dokuz|dokuz\s*nokta\s*sifir|dokuz\s*nokta\s*bir|dokuz\s*nokta\s*iki|dokuz\s*nokta\s*uc|dokuz\s*nokta\s*dort|dokuz\s*nokta\s*bes|dokuz\s*nokta\s*alti|dokuz\s*nokta\s*yedi|dokuz\s*nokta\s*sekiz|dokuz\s*nokta\s*dokuz',val)
            if control == [] or control == None:
                print('syntax')
                break

print(init_var.values())
print(init_var)
print(init_value)
