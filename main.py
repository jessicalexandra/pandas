import pandas as  pd

# organizar los datos 
tabla1=pd.read_csv("./data/empleados.csv ")
from data.comidas import comidas
tabla2=pd.DataFrame(comidas,columns=['nombrePlato','precio'])
from data.medicos import crearmedicos
medicos=crearmedicos()
tabla3=pd.DataFrame(medicos)

# tabla1Modificada=tabla1.head(50)
# tabla1Modificada=tabla1.tail(10)
# tabla1Modificada=tabla1[['nombres','salario']].head(10)
# print(tabla1Modificada)
tabla1Modificada=tabla3['nombre'].head(50)
print(tabla1Modificada)