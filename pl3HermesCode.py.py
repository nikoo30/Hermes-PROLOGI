# function for separator
def sep():
    print("-----------------------------------")

# Function to store book titles
def books():
    math_books = [
        "\"The Princeton Companion to Mathematics\" by Timothy Gowers",
        "\"How to Solve It\" by George Polya",
        "\"The Art of Mathematics\" by Jerry P. King",
        "\"Calculus Made Easy\" by Silvanus P. Thompson",
        "\"A Mathematician's Lament\" by Paul Lockhart",
        "\"Godel, Escher, Bach: An Eternal Golden Braid\" by Douglas Hofstadter",
        "\"The Music of the Primes\" by Marcus du Sautoy",
        "\"The Theory of Everything\" by Stephen Hawking",
        "\"The Mathematical Universe\" by Max Tegmark",
        "\"The Nature of Mathematics\" by Keith Devlin"
    ]
    sci_books = [
        "\"A Brief History of Time\" by Stephen Hawking",
        "\"The Selfish Gene\" by Richard Dawkins",
        "\"The Structure of Scientific Revolutions\" by Thomas S. Kuhn",
        "\"The Double Helix\" by James D. Watson",
        "\"The Origin of Species\" by Charles Darwin",
        "\"The Elegant Universe\" by Brian Greene",
        "\"The Demon-Haunted World: Science as a Candle in the Dark\" by Carl Sagan",
        "\"The Physics of the Impossible\" by Michio Kaku",
        "\"The Gene: An Intimate History\" by Siddhartha Mukherjee",
        "\"The Emperor's New Mind: Concerning Computers, Minds, and the Laws of Physics\" by Roger Penrose"
    ]
    eng_books = [
        "\"The Elements of Style\" by William Strunk Jr. and E.B. White",
        "\"A Guide to the Project Management Body of Knowledge\" by Project Management Institute",
        "\"The Oxford English Grammar\" by Sidney Greenbaum",
        "\"The Chicago Manual of Style\" by University of Chicago Press Staff",
        "\"The Power of Now\" by Eckhart Tolle",
        "\"The Lean Startup\" by Eric Ries",
        "\"The Art of Learning\" by Josh Waitzkin",
        "\"How to Read a Book\" by Mortimer Adler and Charles Van Doren",
        "\"The Practice of Statistics\" by Daren S. Starnes, Dan Yates, and David S. Moore",
        "\"The Oxford Handbook of Political Science\" edited by Robert E. Goodin"
    ]
    nonf_books = [
        "\"The Immortal Life of Henrietta Lacks\" by Rebecca Skloot",
        "\"Into Thin Air\" by Jon Krakauer",
        "\"The New Jim Crow\" by Michelle Alexander",
        "\"A People's History of the United States\" by Howard Zinn",
        "\"Thinking, Fast and Slow\" by Daniel Kahneman",
        "\"Sapiens: A Brief History of Humankind\" by Yuval Noah Harari",
        "\"The Sixth Extinction: An Unnatural History\" by Elizabeth Kolbert",
        "\"The Soul of an Octopus\" by Sy Montgomery",
        "\"The Power of Now\" by Eckhart Tolle",
        "\"The Man Who Mistook His Wife for a Hat\" by Oliver Sacks"
    ]
    fict_books = [
        "\"The Lord of the Rings\" by J.R.R. Tolkien",
        "\"The Hitchhiker's Guide to the Galaxy\" by Douglas Adams",
        "\"The Harry Potter Series\" by J.K. Rowling",
        "\"The Chronicles of Narnia\" by C.S. Lewis",
        "\"The Handmaid's Tale\" by Margaret Atwood",
        "\"The Hunger Games\" by Suzanne Collins",
        "\"The Road\" by Cormac McCarthy",
        "\"Beloved\" by Toni Morrison",
        "\"The Color Purple\" by Alice Walker",
        "\"The Kite Runner\" by Khaled Hosseini"
    ]
    return math_books, sci_books, eng_books, nonf_books, fict_books

# Function to choose book from genre
def choose_book(genre_books):

    #print book list from selected genre
    print("\n")
    sep()
    print("Books in selected genre:")
    for i, book in enumerate(genre_books, 1):
        print(f"{i}. {book}")

    # while loop to repeat the statement if user did not input a number in the choices
    while True:
    #input choice of user
        choice = input("\nChoose a book by entering its number (1-10): ")
        #if user did not input a digit
        if choice.isdigit():
            #will determine what book from the list is chosen
            choice = int(choice)
            if choice >= 1 and choice <= 10:
                return genre_books[choice - 1]
        print("Invalid choice. Please try again.")
    
# Function to borrow or return a book
def borrow_or_return_book(book):
    borrow_count = 1  # variable to keep track of number of borrowed books
    return_count = 1  # variable to keep track of number of returned books
    
    while True:
        choice = input(f"Choose what to do with the book (Borrow/Return/Quit) \n{book}\nChoice: ")
        choice = choice.lower()
        
        #borow option
        if choice == 'borrow':
            sep()
            print(f"Please provide the following information:")
            date = input("Date today (DD/MM/YYYY): ")
            name = input("Your name: ")
            contact_number = input("Contact number: ")
            address = input("Address: ")
            sep()

            # Write data to a file
            file_name = f"user_borrow{borrow_count}.txt"  # specify the file name
            with open(file_name, "w") as file:
                file.write(f"Book Borrowed: {book}")
                file.write("\nName: " + name + "\n")
                file.write("Contact Number: " + contact_number + "\n")
                file.write("Address: " + address + "\n")
                file.write("Date: " + date)

            print(f"\nYou have borrowed the book {book}.")
            
            #loop to repeat if user did not answer yes/no
            while True:
                    # ask user if they want to view file. if yes, program will display file. if no, program will go back to choices.
                    ans = input("Would you like to view the file? (yes/no): ")
                    ans = ans.lower()
                    if ans == 'yes':
                        # code to read and display the contents of the file
                        with open(file_name, "r") as file:
                            file_contents = file.read()
                            print("------------Information----------") 
                            print(file_contents)
                        break

                    elif ans == 'no':
                        print("\nYour info has been saved. Thank you for using this program.\n")
                        break

                    else:
                        print("\nPlease enter a valid input.\n")

            borrow_count += 1  # increment the borrow_count after each borrow operation
            break

        #return option
        elif choice == 'return':
            sep()
            print(f"Please provide the following information:")
            date = input("Date today (DD/MM/YYYY): ")
            name = input("Your name: ")
            contact_number = input("Contact number: ")
            sep()

            # Write data to a file
            file_name = f"user_return{return_count}.txt" 
            with open(file_name, "w") as file:
                file.write(f"Book Borrowed: {book}")
                file.write("\nName: " + name + "\n")
                file.write("Contact Number: " + contact_number + "\n")
                file.write("Date: " + date)

            print(f"\nYou have returned the book {book}.")

            #loop to repeat if user did not answer yes/no
            while True:
                    # ask user if they want to view file. if yes, program will display file. if no, program will go back to choices.
                    ans = input("Would you like to view the file? (yes/no): ")
                    ans = ans.lower()
                    if ans == 'yes':
                        # code to read and display the contents of the file
                        with open(file_name, "r") as file:
                            file_contents = file.read()
                            print("------------Information----------") 
                            print(file_contents)
                        break

                    elif ans == 'no':
                        print("\nYour info has been saved. Thank you for using this program.\n")
                        break

                    else:
                        print("Please enter a valid input.")
            return_count += 1  # increment the return_count after each return operation
            break

        #elif to quit
        elif choice == 'quit':
            print("\nThank you for using the book management program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Main program
def main():
    math_books, sci_books, eng_books, nonf_books, fict_books = books()


    #while loop to repeat the program until user inputs 6
    while True:

        #print menu
        sep()
        print("Library System Program\n")
        print("Welcome! Choose a genre:")
        print("\n1. Math Books")
        print("2. Science Books")
        print("3. English Books")
        print("4. Non-Fiction")
        print("5. Fiction")
        print("6. Quit")
        sep()

        #choice for genres
        choice = input("\nEnter your choice (1-6): ")

        #if-elseif statements for choosing genres
        if choice == '1':
            selected_book = choose_book(math_books)
            print(f"\nYou selected: {selected_book}\n")
            borrow_or_return_book(selected_book)
        elif choice == '2':
            selected_book = choose_book(sci_books)
            print(f"\nYou selected: {selected_book}\n")
            borrow_or_return_book(selected_book)
        elif choice == '3':
            selected_book = choose_book(eng_books)
            print(f"\nYou selected: {selected_book}\n")
            borrow_or_return_book(selected_book)
        elif choice == '4':
            selected_book = choose_book(nonf_books)
            print(f"\nYou selected: {selected_book}\n")
            borrow_or_return_book(selected_book)
        elif choice == '5':
            selected_book = choose_book(fict_books)
            print(f"\nYou selected: {selected_book}\n")
            borrow_or_return_book(selected_book)

        #conditional statement to stop the loop
        elif choice == '6':
            print("Thank you for using the book selection program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()