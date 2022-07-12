salar = float(input())
if salar < 1751.81:
    salar = salar * 0.08
    print(f'Desconto do INSS: R$ {salar:.2f}')
elif salar > 1751.81 and salar <= 2919.72:
    salar = salar * 0.09
    print(f'Desconto do INSS: R$ {salar:.2f}')
elif salar > 2919.72 and salar <= 5839.45:
    salar = salar * 0.11
    print(f'Desconto do INSS: R$ {salar:.2f}')
else:
    salar = 642.33
    print(f'Desconto do INSS: R$ {salar:.2f}')
("salar = float(input())\n"
 "if salar < 1751.81:\n"
 "    salar = salar * 0.08\n"
 "    print('Desconto do INSS: R$ {ro}'.format(salar))\n"
 "elif 1751.82 <= salar <= 2919.72:\n"
 "    salar = round(salar * 0.09,2)\n"
 "    print('Desconto do INSS: R$ {}'.format(salar))\n"
 "elif 2919.73 <= salar <= 5839.45:\n"
 "    salar = round(salar * 0.11,2)\n"
 "    print('Desconto do INSS: R$ {}'.format(salar))\n"
 "else:\n"
 "    salar = round(5839.45 * 0.11,2)\n"
 "    print('Desconto do INSS: R$ {}'.format(salar))")
