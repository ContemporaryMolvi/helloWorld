import sys

def default():
    print("Hello World!")
def cat():
    print("Meow!")
    
main():
    if sys.argv[1] == "cat":
        cat()
    default()

if __name__ == "__main__":
    main()
