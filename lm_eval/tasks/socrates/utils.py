import re


def contains_correct(references, predictions):
    try:
        pred = predictions[0]
    except IndexError:
        print(str(predictions))
    ref = references
    for ref in references:
        if ref.lower() in pred.lower():
            return {"contains_correct": 1.0}
    # match = float(int(bool(re.search(r"("+r")|(".join(ref)+r")", pred, re.IGNORECASE))))

    return {"contains_correct": 0.0}
