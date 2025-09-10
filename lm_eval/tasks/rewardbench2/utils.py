import numpy as np


def process_results(doc, results):
    ll, _ = zip(*results)
    ll = np.array(ll)

    lengths = np.array([float(len(x.encode("utf-8"))) for x in doc["responses"]])

    ll_norm = ll / lengths

    ll_correct = ll[: doc["correct"][-1] + 1]
    ll_incorrect = ll[doc["correct"][-1] + 1 :]
    acc = float(np.greater(ll_correct, ll_incorrect[:, np.newaxis]).mean() == 1)

    ll_norm_correct = ll_norm[: doc["correct"][-1] + 1]
    ll_norm_incorrect = ll_norm[doc["correct"][-1] + 1 :]
    acc_norm = float(
        np.greater(ll_norm_correct, ll_norm_incorrect[:, np.newaxis]).mean() == 1
    )

    return {"acc": acc, "acc_norm": acc_norm}
