import re


def exact_match_e2(references, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = references

    match = float(int(bool(re.search(r"|".join(ref), pred, re.IGNORECASE))))

    return {"exact_match": match}


def exact_match_e3(references, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = references

    match = float(int(bool(re.search(r"|".join(ref), pred, re.IGNORECASE))))

    return {"exact_match": match}
