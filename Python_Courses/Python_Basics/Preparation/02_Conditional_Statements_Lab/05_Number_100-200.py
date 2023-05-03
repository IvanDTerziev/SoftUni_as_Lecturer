UPPER_LIMIT = 200
LOWER_LIMIT = 100

BETWEEN_LOWER_AND_UPPER_LIMIT_MESSAGE = f"Between {LOWER_LIMIT} and {UPPER_LIMIT}"
LESS_THAN_LOWER_LIMIT_MESSAGE = f"Less than {LOWER_LIMIT}"
GREATER_THAN_UPPER_LIMIT_MESSAGE = f"Greater than {UPPER_LIMIT}"

number = int(input())

if number > UPPER_LIMIT:
    print(GREATER_THAN_UPPER_LIMIT_MESSAGE)
elif number >= LOWER_LIMIT:
    print(BETWEEN_LOWER_AND_UPPER_LIMIT_MESSAGE)
else:
    print(LESS_THAN_LOWER_LIMIT_MESSAGE)
