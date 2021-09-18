def macthingWords (sentence1,sentence2):
    score = 0
    word1 = sentence1.strip().split(" ")
    word2 = sentence2.strip().split(" ")
    for words1 in word1:
        for words2 in word2:
            if words1.lower() == words2.lower():
                score+=1
    return score
if __name__ == '__main__':       
    sentences = ["Python is cool", "python is good", "python is not python snake","lol"]
    search = input()
    score = [macthingWords(search,sentence)for sentence in sentences]
    results = [ele for ele in sorted(zip(score,sentences),reverse=True) if  ele[0] != 0]
    print(f"{len(results)} result/s are found!")
    for n,sent in results:
        print(sent)
    
