import numpy as np
import Margot_test as m


def question1_2():
    n_objets = [1, 2, 10, 23]
    print("Question 1 :")
    for i in n_objets:
        print("Nombre de possibilit�s pour", i, "objets:", 2**i)
    print("\nQuestion2 :\nNombre max de possibilit�s :", 2**max(n_objets))


# Question 3 :
# Utilit� maximale pour un poids inf�rieur ou �gal � 0.6 : 7.6 avec 6 objets pour un poids total de 0.6


if __name__ == '__main__':
    #question1_2()
    m.algo_sac(3)

