from point import Point


def main():
    point_a, point_b = Point(1, 2), Point(1, 2)

    print(point_a==point_b)
    print("a:", point_a, "  ", "b:", point_b)
    print(point_a+point_b)



if __name__ == "__main__":
    main()
