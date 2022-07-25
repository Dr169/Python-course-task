#have a HELP command
def show_help():
    #print out instructions on how use app
    print("What should we pick up at the store? ## you shoud give a string(text) and a integer(number). ##")
    print("""
            Enter 'DONE' to stop adding items.
            Enter 'SHOW' to show your items list.
            Enter 'HELP' to show how programme does work.
            """)


#have a SHOW command
def show_list():
    print("Here's your list:")
    print(shopping_list)


def add_to_list(new_item,number_of_new_item):
    #add new items to our list
    shopping_list.update({new_item : number_of_new_item})
    print("Added {} {}. List now has {} items.".format(number_of_new_item, new_item, len(shopping_list)))


#make a list to hold onto our items
shopping_list = {}


show_help()

while True:
    #ask for new items
    new_item = input("> ")
    
    #be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    number_of_new_item = int(input("> "))

    add_to_list(new_item, number_of_new_item)

show_list()