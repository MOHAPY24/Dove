import dove as dv

print("DoveCLI Client, make sure to configure your session params in client/config/session.jsonc and client/config/user.jsonc!")
model = input("Model >> ")
prompt = input("Prompt >> ")

cl = dv.DoveClient()
clconf  = cl.config
cl.create_data(model=model, prompt=prompt)
cl.send_to_remote()
cl.recive_from_remote()