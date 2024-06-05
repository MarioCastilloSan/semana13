import streamlit as st 
from data import get_data, get_row
from graph import professions_graphic


def main():
    st.title('Aplicación para ver mis datos')
    df = get_data()
    st.dataframe(df)
    #row = st.text_input("Ingresa una fila a filtrar")
    row_selection = st.selectbox("Si quieres crear un solo contrato selecciona una fila:", df.index)
    if st.button('Ver fila'):
        row = get_row(df, row_selection)
        st.write(row)
    st.write('¡Gracias por usar mi aplicación!')
    if st.button('Ver gráfica de profesiones'):
        st.pyplot(professions_graphic())

    

if __name__ == '__main__':
    main()
