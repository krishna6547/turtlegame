# to save high score in a file

def storescore(score):
    file = open("score.txt","a")
    file.write(f"{score},")
    file.close()
                

def high_score():
    
    with open("score.txt","r") as file:
        data = file.read()
        List = list(data.split(","))
    if len(List) > 1:
        return max(List)
    else:
        return None

high_score()
