from faker import Faker

def crearmedicos():
    medicos=[]
    faker=Faker()

    for i in range (2000):
        medico={}
        cargo=faker.job()
        medico['nombre']=faker.name()
        medico['cargo']=cargo
        medicos.append(medico)

        return medicos