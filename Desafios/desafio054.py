import datetime
atual = datetime.date.today().year
totmai = 0
totmen = 0 
for pess in range(1,8):
    nasc = int(input('Em que ano a pessoa nasceu? ').format(pess))
    idade = atual - nasc
    if idade >= 21:
        totmai = totmai + 1
    else:
        totmen = totmen + 1
print('Ao fim tivemos no total de \033[1;32m{}\033[0m pessoas de menor\n e \033[1;31m{}\033[0m pessoas de maior'.format(totmen,totmai))
