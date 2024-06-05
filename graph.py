import matplotlib.pyplot as plt
from data import get_data
df = get_data()


def professions_graphic():
    profession_counts = df['Profesión'].value_counts() 
    plt.figure(figsize=(10, 10))
    plt.pie(profession_counts, labels=profession_counts.index, autopct='%1.1f%%', startangle=150)
    plt.title('Distribución de Profesiones')
    plt.axis('equal')
    return plt


