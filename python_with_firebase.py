from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-7a2ea-default-rtdb.firebaseio.com/", None)
# data = {
#       'Name': 'Tom Jerry'
#     , 'Email': 'tom@jerry.com'
#     , 'Phone': 222333444

# }

# data = {
#       'Name': 'Wiedźmin'
#     , 'Email': 'wiesiek@saplw.pl'
#     , 'Phone': 111222333

# }

# result = firebase.post('/pythonDB_text/Customer', data)
result = firebase.del('/pythonDB_text/Customer/-NROJbrYlDozNg8LEtn4', '')
print(result)

