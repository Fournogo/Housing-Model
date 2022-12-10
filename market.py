import numpy as np

# Returns the payment for a fully amortizing loan. Assumes 12 payments per year.
def pmt(rate, term, principal):
    return (rate*principal)/(12*(1-(1+rate/12)**(-12*term)))

# Returns the principal from fully amortizing payment. Assumes 12 payments per year.
def princfrompmt(rate, term, payment):
    return (payment*(12*(1-(1+rate/12)**(-12*term))))/rate

# Determines buyer agent's willingness to pay
def wtopay(cityGrid):
    return

# Determines seller agent's preferred sale price
def sellfor(cityGrid):
    return