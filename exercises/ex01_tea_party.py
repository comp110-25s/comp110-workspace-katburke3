"""Exercise 01! Finding tea bags, treats, and cost based on number of guests!"""

__author__: str = "730558066"


def main_planner(guests: int) -> None:
    """put in #guests, get out amount of treats, amount of tea, and cost"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=(tea_bags(people=guests)), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """finding number of tea bags needed based on guests"""
    return people * 2


def treats(people: int) -> int:
    """finding number of treats needed based on guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """finding cost based on tea count and treat count"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
