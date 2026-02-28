try:
    with open('youtube.txt','w') as file:
        pass
except FileNotFoundError:
    pass

finally:
    exit('youtube.txt')