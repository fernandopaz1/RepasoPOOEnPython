# En python ninguna variable esta libre de modificación
# La idea es que modelamos constante por convencion
# Las constantes tienen todas las letras en mayusculas
# y si tienen mas de una palabra se separan con _

MI_CONSTANTE = 'Valor'


# Se acostumbra que se definan en un modulo separado (seria este)
# y los valores se importan desde ña ptr clase
# podria modificarlo desde la otra clase pero por convencion no deberiamos


class Matematica:
    PI = 3.1416