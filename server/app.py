from recive import app, init

if __name__ == '__main__':
    key = input("serv_key (INT only) > ")
    if key.isalnum == False:
        print("Non-int key!")
        quit(1)
    init(int(key))
    app.run(host="0.0.0.0")