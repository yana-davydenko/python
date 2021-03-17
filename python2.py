def function(sentence, letter):
    i=0
    for x in sentence:
        if x == letter:
            i +=1
    print('letter', i)
function('never never never', 'e')