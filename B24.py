from bitrix24 import *
URL = 'https://bitrix24.kelast.ru/kuratovru/rest/tasks/otk/create/'
TOKEN_ACCESS = '4a9018b8-25af-4111-a4e6-d1103317032f'


bx24 = Bitrix24(URL)

print(bx24.callMethod('crm.product.list'))

result = bx24.callMethod('im.message.add',fields ={
    'DIALOG_ID': 'chat25759',
    'MESSAGE': 'test',
})

print('')