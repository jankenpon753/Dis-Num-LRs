def find_contrapositive(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Find the position of "if" and "then" in the sentence
    if_index = -1
    then_index = -1
    for i, word in enumerate(words):
        if word.lower() == "if":
            if_index = i
        elif word.lower() == "then":
            then_index = i

    # Check if both "if" and "then" were found
    if if_index != -1 and then_index != -1:
        # Identify the p (if) and q (then) parts of the statement
        p = " ".join(words[if_index + 1 : then_index])
        q = " ".join(words[then_index + 1 :])

        # Negating both the p and the q
        np = "it is not true that " + p
        nq = "it is not true that " + q

        # Form the contrapositive statement
        contrapositive = f"If {np}, then {nq}"

        return contrapositive
    else:
        return "Invalid input sentence. Please use 'if' and 'then' in your sentence."


# Example usage:
original_sentence = "If he comes then I will go."
contrapositive_sentence = find_contrapositive(original_sentence)
print("Original:", original_sentence)
print("Contrapositive:", contrapositive_sentence)
