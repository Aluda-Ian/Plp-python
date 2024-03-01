http_status = 200

if http_status == 200 or http_status == 201:
    print("success")
elif http_status == 400:
    print("bad request")
elif http_status == 404:
    print("Not found") 
elif http_status == 501 or http_status == 501:
    print("server error")
else:
    print("unkown")

#match case refactor
match http_status:
    case 200 | 201:
        print("Sucess!")
    case 400:
        print("bad request !")    
    case 401:
        print("not found")  
    case 500 | 501 :
        print('server error') 
    case _:
        print('unkown')        