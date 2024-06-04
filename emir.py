from time import time

def tree(elements, weights, max_weight=0.6, current_weight=0, current_subset=set()):
    if len(elements) == 0:
        yield current_subset, current_weight
        return
    
    first_element = elements[0]
    rest_elements = elements[1:]
    first_weight = weights[0]
    rest_weights = weights[1:]  
    
    # Apelle récursif pour le reste des éléments
    for subset, weight in tree(rest_elements, rest_weights, max_weight, current_weight, current_subset):
        if weight <= max_weight:
            yield subset, weight  # Retourne le sous-ensemble et le poids sans ajouter le premier élément
        if weight + first_weight <= max_weight:
            yield subset.union({first_element}), weight + first_weight  # Retourne le sous-ensemble avec le premier élément et le poids correspondant

elements = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
weights = [0.2, 0.1, 1, 0.2, 0.3, 0.2, 0.4, 0.2, 0.1, 0.2, 0.4, 0.4, 0.4, 0.1, 0.5, 0.4, 0.3, 0.4, 0.01, 0.05, 0.4, 0.6, 0.05]
weights.sort(reverse=True)

for subset, weight in tree(elements, weights):
    print("Objets:", subset, " Poids:", weight)
