from helpers import (
    create_note,
    list_notes,
    edit_note,
    delete_note,
    search_notes
 
)

def menu():
    print(""")
 ============================
          NOTE APP CLI 
 ============================
          1.Add Note
          2.View Notes
          3.Search Notes
          4.Edit Note
          5.Delete Note
          0.Exit
          """)
    def cli():
        running = True

        while running:
            menu()
            choice = input ("Choose an option:")
            if choice == "1":
                create_note()
            elif choice == "2":
                list_notes()
            elif choice == "3":
                search_notes()
            elif choice == "4":
                edit_note()
            elif choice == "5":
                delete_note()
            elif choice == "0":
                print("\nExiting Note App. Goodbye!\n")
                running = False
            else:
                print("\nInvalid choice. Please try again.\n")

                if __name__ == "__main__":
                    cli()                 
