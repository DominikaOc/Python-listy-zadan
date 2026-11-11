def evaluate_wallet(wallet, exchange_rate):
    exchange_rate['PLN'] = 1  #dodaję nowy klucz 'PLN' i jego wartość to 1
    wartość = 0
    for k in wallet:
        wartość = wartość + wallet[k] * exchange_rate[k]

    return wartość


wallet = {'PLN' : 5000 , 'EUR' : 1000 , 'USD' : 300}
exchange_rate = {'EUR': 4.25 , 'USD' : 3.63 , 'YEN': 0.02 }
print(evaluate_wallet(wallet, exchange_rate))