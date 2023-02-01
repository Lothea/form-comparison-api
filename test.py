from src.compare import similarity

result = similarity("I like pie",  "what is death?")

for item in result:
    print("Comparing '{}' with '{}'. Similarity {}".format(item[0], item[1], item[2].item()))


