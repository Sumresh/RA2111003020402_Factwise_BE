def maxpoints(cardpoint,k):
    n=len(cardpoint)
    
    total_sum=sum(cardpoint)
    
    if k==n:
        return total_sum
    
    window=n-k
    current_sum = sum(cardpoint[:window])
    min_sum=current_sum
    
    for i in range(window,n):
        current_sum+=cardpoint[i]-cardpoint[i-window]
        min_sum=min(min_sum,current_sum)
        
        
    return total_sum-min_sum

cards=input("Enter the card point separated by space: ").strip().split()
card_points=list(map(int,cards))
k_value=int(input("Enter the k value: "))
print(maxpoints(card_points,k_value))
