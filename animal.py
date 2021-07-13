import sys

def default():
    	print("Hello World!")

def dog():
	print("Woof!")
	
def main():
	if sys.argv[1] == "dog":
		dog()
    	default()

if __name__ == "__main__":
    	main()
