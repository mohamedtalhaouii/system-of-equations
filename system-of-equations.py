#Mohamed Talhaoui
import numpy as np
from fractions import Fraction

M = int(input("Combien des inconnues dans cette system? : "))


if M == 3:
    print("pour résoudre ce système {\n  ax + by + cz = d\n  ax + by + cz = d\n  ax + by + cz = d\n}")

    print("\nEntrez les coefficients de l'équation 1")
    a1 = float(Fraction(input("Entrez le premier coefficient: ")))
    b1 = float(Fraction(input("Entrez le deuxième coefficient: ")))
    c1 = float(Fraction(input("Entrez le troisième coefficient: ")))
    d1 = float(Fraction(input("Entrez le dernier coefficient: ")))


    print("\nEntrez les coefficients de l'équation 2")
    a2 = float(Fraction(input("Entrez le premier coefficient: ")))
    b2 = float(Fraction(input("Entrez le deuxième coefficient: ")))
    c2 = float(Fraction(input("Entrez le troisième coefficient: ")))
    d2 = float(Fraction(input("Entrez le dernier coefficient: ")))


    print("\nEntrez les coefficients de l'équation 3")
    a3 = float(Fraction(input("Entrez le premier coefficient: ")))
    b3 = float(Fraction(input("Entrez le deuxième coefficient: ")))
    c3 = float(Fraction(input("Entrez le troisième coefficient: ")))
    d3 = float(Fraction(input("Entrez le dernier coefficient: ")))

    #Solving
    A = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
    B = np.array([d1,d2,d3])
    C = np.linalg.solve(A,B)
    print("Les solutions de ce système est le triple (x,y,z) = ",C)
    

elif M == 2:
    print("pour résoudre ce système {\n  ax + by + cz = d\n  ax + by + cz = d\n}")

    print("\nEntrez les coefficients de l'équation 1")
    a1 = float(Fraction(input("Entrez le premier coefficient: ")))
    b1 = float(Fraction(input("Entrez le deuxième coefficient: ")))
    c1 = float(Fraction(input("Entrez le troisième coefficient: ")))
    d1 = float(Fraction(input("Entrez le dernier coefficient: ")))


    print("\nEntrez les coefficients de l'équation 2")
    a2 = float(Fraction(input("Entrez le premier coefficient: ")))
    b2 = float(Fraction(input("Entrez le deuxième coefficient: ")))
    c2 = float(Fraction(input("Entrez le troisième coefficient: ")))
    d2 = float(Fraction(input("Entrez le dernier coefficient: ")))

    #Solving
    A = np.array([[a1,b1,c1],[a2,b2,c2]])
    B = np.array([d1,d2])
    C = np.linalg.solve(A,B)
    print("Les solutions de ce système est le couple (x,y) = ",C)
