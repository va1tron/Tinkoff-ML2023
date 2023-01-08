import argparse
import tokenize
import io


def lev_distance(text1, text2):
    m, n = len(text1), len(text2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(
                    table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]
                )

    return table[-1][-1]


def text_tokenizer(text):
    tokens = tokenize.generate_tokens(text.readline)
    edited_text = ""
    for token in tokens:
        if token.type == tokenize.COMMENT:
            continue
        edited_text += token.string
    edited_text = edited_text.replace("'''", '"""')
    edited_text = edited_text.split('"""')
    edited_text = edited_text[::2] if text.startswith('"""') else edited_text[1::2]
    edited_text = edited_text.replace(" ", "").replace("\n", "")
    return "".join(edited_text).lower()


def compare(text1, text2):
    text1, text2 = text_tokenizer(text1), text_tokenizer(text2)
    distance = lev_distance(text1, text2)
    return 1 - distance / max(len(text1), len(text2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="2 texts")
    parser.add_argument("input_f", type=str, help="1.txt")
    parser.add_argument("output_f", type=str, help="2.txt")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as input_file, open(
        args.output_file, "x", encoding="utf-8")\
            as output_file:
        input_text = input_file.read()
        tests = input_text.split("\n")

        for test in tests:
            original, plagiarized = test.split()
            with open(original, "r", encoding="utf-8") as original_file, open(
                plagiarized, "r", encoding="utf-8")\
                    as plagiarized_file:
                result = compare(original_file, plagiarized_file)
                output_file.write(f"{result:.2f}\n")
