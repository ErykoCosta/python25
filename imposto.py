# %%
def calc_imposto(preco: float, tx_imposto: float, **kwargs) -> float:
    imposto =  preco * (1 + tx_imposto)
    
    for i in kwargs:
        print(f'{i}: {kwargs[i]}')
        imposto += preco * kwargs[i]
    return imposto

# %%
imppostos_gerais = {'ICMS': 0.18, 'IPI': 0.04, 'PIS': 0.018, 'COFINS': 0.085}
calc_imposto(100, 0.18, **imppostos_gerais)


