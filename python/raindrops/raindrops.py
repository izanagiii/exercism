def convert(number: int) -> str:
    result = ""
    divisors = {5: "Plang", 3: "Pling", 7: "Plong"}

    # used sorted() to make sure python vers less than 3.7
    # still respect the precedence of the key ordering
    for divisor in sorted(divisors):
        if number % divisor == 0:
            result += divisors[divisor]

    if result == "":
        result = str(number)

    return result
