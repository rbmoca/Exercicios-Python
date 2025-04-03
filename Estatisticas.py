import statistics as st

# moda

def calc_moda(lista):
    return (st.mode(lista))

def calc_media(lista):
    return (st.mean(lista))

def calc_mediana(lista):
    return (st.median(lista))

def calc_varianca(lista):
    return (st.variance(lista))

def calc_amplitude(lista):
    return (max(lista) - min(lista))

def calc_desvio_padrao(lista):
    return (st.stdev(lista))

