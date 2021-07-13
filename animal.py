import sys

def default():
    print("Hello World!")
    
def cat():
    print("Meow!")
    
def dog():
	print("Woof!")
	
def main():
	if sys.argv[1] == "cat":
        	cat()
	elif sys.argv[1] == "dog":
		dog()
	else:
    		default()
>>>>>>> dog

if __name__ == "__main__":
    	main()
