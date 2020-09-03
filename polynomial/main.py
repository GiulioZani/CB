
"""
    polyToStr(poly) restituisce una stringa
    che descrive il polinomio poly, usando la sintassi algebrica di Python (es. 3*x**2-10*x+5),
    senza spazi, con monomi aventi esponenti
    decrescenti (questa è forse la funzione più difficile, attenzione ai dettagli... il primo monomio ha il segno solo se è negativo,
    gli esponenti 0 e 1 non vanno scritti, se l'esponente è zero non bisogna scrivere la x, se il polinomio non ha alcun monomio bisogna scrivere 0, se un coefficiente vale 1 o -1, il numero 1 non va scritto, a meno che non sia il monomio di grado zero...)

    newPoly() genera e restituisce un nuovo polinomio vuoto, cioè privo di monomi
    newPoly(coeff, expon) genera e restituisce un nuovo polinomio contenente il solo monomio specificato dagli argomenti, invocando prima il metodo precedente, per creare un polinomio vuoto, poi il metodo seguente, per aggiungere l'unico monomio
    addTermToPoly(poly, coeff, expon) aggiunge un monomio al polinomio poly (e non restituisce niente); se nel polinomo esiste già un monomio avente quell'esponente, vengono semplicemente sommati i coefficienti (se il coefficiente risultante è uguale a zero, il monomio va eliminato dal polinomio)
    sumPoly(poly1, poly2) restituisce un nuovo polinomio che sia la somma dei polinomi poly1 e poly2 (che non vengono modificati)
    multiplyPoly(poly1, poly2) restituisce un nuovo polinomio che sia il prodotto dei polinomi poly1 e poly2 (che non vengono modificati); questa funzione deve invocare ripetutamente la funzione sumPoly descritta al punto precedente, realizzando in modo diretto soltanto la moltiplicazione tra due monomi
    i metodi che ricevono una coppia (coefficiente, exponente) devono sollevare l'eccezione ValueError se l'esponente è negativo oppure non è un numero intero, mentre devono ignorare l'inserimento del monomio (senza sollevare eccezione) se il coefficiente è uguale a zero
"""

def polyToString(poly):
    result = ''
    for expon in sorted(poly.keys()):
        coeff = poly[expon]
        if coeff >= 0:
            result += "+"
        result += f"{coeff}*x**{expon}"

    return result if result[0] != '+' else result[1:]


def newPoly():
    return {}


def addTermToPoly(poly, coeff, expon):
    if expon < 0 or int(expon) != expon:
        raise ValueError
    if coeff == 0:
        return
    poly[expon] = coeff + (poly[expon] if expon in poly else 0)


def sumPoly(poly1, poly2):
    new_poly = newPoly()
    for poly_i in [poly1, poly2]:
        for (key, val) in poly_i:
            addTermToPoly(new_poly, val, key)

    return new_poly


def main():
    poly = {
        4:5.3,
        3:-3.2,
        2:45
    }
    addTermToPoly(poly, 5.4, 6)
    print(polyToString(poly))


if __name__ == '__main__':
    ciao = [[3,5]]
    main()
