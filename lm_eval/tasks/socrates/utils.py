import re


def exact_match_e2(references, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = references
    for ref in references:
        if ref.lower() in pred.lower():
            return {"exact_match_e2": 1.0}
    # match = float(int(bool(re.search(r"("+r")|(".join(ref)+r")", pred, re.IGNORECASE))))

    return {"exact_match_e2": 0.0}


def exact_match_e3(references, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = references
    for ref in references:
        if ref.lower() in pred.lower():
            return {"exact_match_e3": 1.0}
    # match = float(int(bool(re.search(r"("+r")|(".join(ref)+r")", pred, re.IGNORECASE))))

    return {"exact_match_e3": 0.0}
