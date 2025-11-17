import dove as dv

print("DoveCLI Client, make sure to configure your session params in client/config/session.jsonc and client/config/user.jsonc!")
authkey = input("Password >> ")
if authkey.isalnum():
    authkey = int(authkey)
else:
    print("Authkey cannot be text. please enter an integer value.")
    exit(1)
model = input("Model >> ")
prompt = input("Prompt >> ")

cl = dv.DoveClient()
clconf  = cl.config
cl.create_data(model=model, prompt=prompt)
if cl.send_to_remote(authkey) == "Invalid AUTHkey":
    print("Invalid AUTH password")
    exit(1)
cl.recive_from_remote()