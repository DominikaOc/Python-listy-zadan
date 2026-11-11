def best_covering_set(s, lst):
    max_moc = -1
    for set in lst:
        if len(set&s) > max_moc:
            max_moc = len(set&s)
            wynik = set

    return wynik

print(best_covering_set( {1,2,3} , [ set() , {0,1} , {2,4} , {1,3} ] ))

