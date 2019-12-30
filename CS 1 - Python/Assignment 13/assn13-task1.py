"""
Parker Jackman
Assignment 13
Task 1
"""

from polygon import Polygon

def main():
    polygon1 = int(input("How many sides does the first polygon have? "))
    polygon2 = int(input("How many sides does the second polygon have? "))

    poly1 = Polygon(polygon1)
    poly2 = Polygon(polygon2)

    print("Add:", poly1 + poly2)
    print("Subtract:", poly1 - poly2)
    print("Less Than:", poly1 < poly2)
    print("Greater Than:", poly1 > poly2)
    print("Equal to:", poly1 == poly2)
    print("Polygon 1 Len:", len(poly1))
    print("Polygon 2 Len:", len(poly2))
    print("Polygon 1 String: " + str(poly1))
    print("Polygon 2 String: " + str(poly2))


main()