def convert(number: int) -> str:
    result = ""
    divisors = {"3": "Pling", "5": "Plang", "7": "Plong"}

    for divisor in divisors:
        if number % int(divisor) == 0:
            result += divisors[divisor]

    if result == "":
        result = str(number)

    return result
