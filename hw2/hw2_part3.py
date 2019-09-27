
"""
This program is a sentiment analysis tool, it will compute the happiness and sadness level of a sentence. 


Author: Xueqi Huang
Version: 1

"""



##define functions
def percentage_happy(sentence):
    sentence_input = sentence.strip().lower()
    total_words = int(sentence_input.count(' '))+1
    w1 = sentence_input.count('laugh')
    w2 = sentence_input.count('happiness')
    w3 = sentence_input.count('love')
    w4 = sentence_input.count('excellent')
    w5 = sentence_input.count('good')
    per_h = (w1+w2+w3+w4+w5)/total_words
    return per_h

def percentage_sad(sentence):
    sentence_input = sentence.strip().lower()
    total_words = int(sentence_input.count(' '))+1
    w1 = sentence_input.count('bad')
    w2 = sentence_input.count('sad')
    w3 = sentence_input.count('terrible')
    w4 = sentence_input.count('horrible')
    w5 = sentence_input.count('problem')
    per_s = (w1+w2+w3+w4+w5)/total_words
    return per_s   

## input sentence
sentence = input('Enter a sentence => ')
print(sentence)

## call functions
print('Percentages. happy: {0:.3f}'.format(percentage_happy(sentence)), 'sad: {0:.3f}'.format(percentage_sad(sentence)))

## give conclusion
if percentage_happy(sentence) > percentage_sad(sentence):
    print('This is a happy sentence')
elif percentage_sad(sentence) > percentage_happy(sentence):
    print('This is a sad sentence')
else:
    print('This is a neutral sentence')