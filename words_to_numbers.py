def words_to_num(words):
    map={'zero':4,'one':3,'two':3,'three':5,'four':4,'five':4,'six':3,'seven':5,'eight':5,'nine':4,'ten':3,
         'eleven':6,'twelve':6,'thirteen':8,'fourteen':8,'fifteen':7,'sixteen':7,'seventeen':9,'eighteen':8,'nineteen':8,'twenty':6,
            'thirty':6,'forty':5,'fifty':5,'sixty':5,'seventy':7,'eighty':6,'ninety':6,'hundred':7,'thousand':8,'million':1000000,'and':3
        
         }
    
    # words=words.replace(' and ',' ')
    words=words.replace('-',' ')
    words=words.replace(',',' ')
    split_words=words.split()
    total_value=0
    current_value=0
    for word in split_words:
        if word == ' and ':
            continue
        
        number=map[word]
        if number==100:
            current_value *=100
            
        elif number>=1000:
            total_value +=(current_value*number)
            current_value=0
            
        else:
            current_value+=number
            
    total_value+=current_value
    return total_value

input1=input("Enter the string : ")
print(words_to_num(input1))


