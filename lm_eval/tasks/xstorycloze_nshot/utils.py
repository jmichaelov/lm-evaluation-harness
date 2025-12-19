def doc_to_text(doc):
    text = (
        (
            doc["input_sentence_1"]
            + " "
            + doc["input_sentence_2"]
            + " "
            + doc["input_sentence_3"]
            + " "
            + doc["input_sentence_4"]
            + " "
            + [doc["sentence_quiz1"], doc["sentence_quiz2"]][
                int(doc["answer_right_ending"]) - 1
            ]
            + " "
        )
        * 2
        + doc["input_sentence_1"]
        + " "
        + doc["input_sentence_2"]
        + " "
        + doc["input_sentence_3"]
        + " "
        + doc["input_sentence_4"]
    )

    return text
