me = float(input('Digite o metro : '))
km = me * 0.001
hm = me * 0.01
dam = me * 0.1
dm = me * 10
cm = me * 100
mm = me *1000
print('\033[1;31m{}\033[m km'.format(km))
print('\033[1;32m{}\033[m hm'.format(hm))
print('\033[1;33m{}\033[m dam'.format(dam))
print('\033[1;34m{}\033[m m'.format(me))
print('\033[1;35m{}\033[m dm'.format(dm))
print('\033[1;36m{}\033[m cm'.format(cm))
print('\033[1;37m{}\033[m mm'.format(mm))
