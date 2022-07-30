def policz_wpłate(podstawa, policz_premie):
    return podstawa + policz_premie (podstawa)

def zwruc_zero(podstawa):
    return 0

def policz_premie_managera (podstawa):
    return 0.5 * podstawa

print(policz_wpłate(1000, zwruc_zero))
print(policz_wpłate(2000, policz_premie_managera))