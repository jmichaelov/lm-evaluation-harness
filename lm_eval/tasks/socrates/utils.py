import re


def exact_match(references, predictions):
    pred = predictions[0]
    ref = references[0]

    match = float(int(bool(re.search(r"|".join(ref), pred, re.IGNORECASE))))

    return {"exact_match": match}
