RULES = {
    "uber": "Travel",
    "ola": "Travel",

    "pizza": "Food",
    "burger": "Food",
    "zomato": "Food",
    "swiggy": "Food",

    "amazon": "Shopping",
    "flipkart": "Shopping",

    "electricity": "Bills",
    "rent": "Bills",
    "internet": "Bills",

    "netflix": "Entertainment",
    "spotify": "Entertainment"
}


def detect_category(title: str):

    text = title.lower()

    for key, value in RULES.items():

        if key in text:

            return value

    return "Other"