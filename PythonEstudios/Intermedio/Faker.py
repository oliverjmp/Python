from faker import Faker
import pandas as pd

fake= Faker(['es_ES','en_US'])

numero_clientes=10

clientes=[]
for i in range(1,numero_clientes+1):

    cliens={

        "id": i,
        "nombre": fake.name(),
        "email": fake.email(),
        "telefono":fake.phone_number(),
    }
    clientes.append(cliens)
    df=pd.DataFrame(clientes)
    print(df.head)
    df.to_csv("clientes.csv", index=False)

