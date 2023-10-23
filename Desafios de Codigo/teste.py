# 1
# print('Saldo atualizado na conta:',float(input())+float(input())-float(input()))
# print(f'Saldo atualizado na conta: {eval(input()+"+"+input()+"-"+input()):.1f}')


# 2
# print('\n'.join(sorted(input() for _ in range(int(input())))))
# print(*sorted(input()for _ in range(int(input()))),sep='\n')

# 3
# s,v=int(input()),int(input())
# print(f'Saque realizado com sucesso. Novo saldo: {s-v}'if v<=s else'Saldo insuficiente. Saque nao realizado!')

# 4
# print(f'Valor final do investimento: R$ {eval(input()+"*(1+"+input()+")**"+input()):.2f}')

# 5
# v=float(input())
# print(f'Deposito realizado com sucesso!\nSaldo atual: R$ {v:.2f}'if(v>0)else'Encerrando o programa...'if(v==0)else'Valor invalido! Digite um valor maior que zero.')
# def c(v):return f'Deposito realizado com sucesso!\nSaldo atual: R$ {v:.2f}'if(v>0)else'Encerrando o programa...'if(v==0)else'Valor invalido! Digite um valor maior que zero.'
# print(c(float(input())))