#ПР-9 Машкін Петро

def main(): 
	while True: 
		prompt_user()
		
def prompt_user():
        a=float(input('Введіть сторону квадрата:'))
        if a > 0:
            S=a**2
            print('Площа =',S)
        
            P=4*a
            print('Периметр =',P)
            
        else:
            print('Це не може бути стороною дійсної фігури. Введіть, будь ласка, значення при якому задовільняється рівність a>0.')
            
        
if __name__ == '__main__': main() 
