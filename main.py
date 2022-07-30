def policz_wyplate (podstawa, premia_rzandu=0, premia_klienta=0, hajs_z_youtube=0):
    return podstawa + premia_klienta + premia_rzandu + hajs_z_youtube

pensja =policz_wyplate(1000, 1500)
print(f'Zarobiłem {pensja}')

print(f'Zarobiłem, podejście drugie {policz_wyplate(1000, hajs_z_youtube=1000)}')