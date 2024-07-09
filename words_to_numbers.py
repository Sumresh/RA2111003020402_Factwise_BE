def words_to_num(words):
    map={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
         'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sisteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,
            'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':9,'hundred':100,'thousand':1000,'million':1000000
        
         }
    
    words=words.replace(' and ',' ')
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