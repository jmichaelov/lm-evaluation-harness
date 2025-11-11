import re


def exact_match_e2(docs, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = docs["e2_aliases"]

    match = float(int(bool(re.search(r"|".join(ref), pred, re.IGNORECASE))))

    return {"exact_match": match}


def exact_match_e3(docs, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = docs["e3_aliases"]

    match = float(int(bool(re.search(r"|".join(ref), pred, re.IGNORECASE))))

    return {"exact_match": match}
