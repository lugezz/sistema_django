from sistema.wsgi import *
from erp.models import *
#import random

# Ejecutar en postgresql
# delete from erp_product;
# ALTER SEQUENCE erp_product_id_seq RESTART WITH 1;
# delete from erp_category;
# ALTER SEQUENCE erp_category_id_seq1 RESTART WITH 1; (Ver que tiene seq1 - Ver nombre del registro de secuencia correcto)

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))

