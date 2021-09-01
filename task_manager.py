import datetime
from datetime import *

login = False 

# Ask the user for their credentials
# Infinate loop of while log in equal false
# program to ask for log ins again.

while login == False:
  my_list = []
  with open("user.txt") as f:
    for line in f:
      #unpacking user file into 2 dimensional list
      line = line.replace("\n", "")
      line_list = line.split(", ")
      my_list.append(line_list)
  print(my_list)
  #getting user input
  username = input("Enter your username: ")
  password = input("Enter your password: ")
#loop through all the data in column 0 and 1 and assign it to a variable called 'col0/col1'
  col0 = [x[0] for x in my_list]
  col1 = [x[1] for x in my_list]

  if username in col0:
# iterate through the list for the length of the list
    for k in range (0, len(col0)):
# checks if username matches the password in the corresponding column
      if col0[k] == username and col1[k] == password:
        print("Successfully logged in.")
        login = True

  else:
        print("Incorrect details! Please enter a valid username and password.")

def main_menu():

    print("++===== Menu =====++" + "\n" +
  "r - register user" + "\n" +
  "a - add task" + "\n" + 
  "va - view all tasks" + "\n" +
  "vm - view my tasks" + "\n" +
  "gr - generate reports" + "\n" +
  "ds - display stats" + "\n"
  "e - exit" + "\n")


def add_task():

  import datetime
  from datetime import date

#Getting user input
  tasks_file = open("tasks.txt", "a+")
  
  user = input("Please enter username of person \
the task is being assigned to: ")

  title_of_task = input("Please insert title of task: ")

  description_of_task = input("Please insert \
description of task: ")

  current_date = datetime.date.today()

  start_date = current_date.strftime('%d %b %Y')

  due_date = input("Please insert due date of the task eg. (dd-mm-yyyy): ")

  date_list = due_date.split("-")

  numbers_date = [int(x) for x in date_list]

  due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime('%d %b %Y') 

  task_completed = "No"

# writing to task.txt file

  tasks_file.write(f"\n{user}, {title_of_task}, \
{description_of_task}, {start_date}, \
{due_date}, {task_completed}")

  print("Task successfully written to file")

  tasks_file.close()


def view_all():

    # open file in read mode

  tasks_file = open("tasks.txt", "r")

    # iterate over tasks.txt file

  for line in tasks_file:

    user, title_of_task, description_of_task, start_date, due_date, enter_n = line.split(", ")

    print(f"""
Name: {user}
Title of task: {title_of_task}
Description of task: {description_of_task}
Start date: {start_date}
Due date: {due_date}
Is completed: {enter_n}
       """)

  Check = False

  while Check == False:

    backward = input("Enter '-1' to return to main menu: ")

    if backward == "-1":
      Check = True
      

    if Check == False:
      print("Invalid selection")
    
    tasks_file.close()
  

def view_mine():

    # open file in read mode

  tasks_file = open("tasks.txt", "r")
    # adding task number to file lines in chronological order
  lines=tasks_file.readlines()
  tasks_file.close()
  outtext = ['%d, %s' % (i, line) for i, line in enumerate(lines)]
  # writes data to temp file which includes task numbers that are going to be used for identification purposes
  outfile = open("temp.txt","w")
  outfile.writelines(str("".join(outtext)))
  outfile.close()
   
  outfile = open("temp.txt", "r")
  # iterate over the outfile file that includes task number
  for line in outfile:

    task_number, user, title_of_task, description_of_task,\
start_date, due_date, enter_n = line.split(", ")

    if username == user:

      print(f"""
  Task Number: {task_number}
Name: {user}
Title of task: {title_of_task}
Description of task: {description_of_task}
Start date: {start_date}
Due date: {due_date}
Enter N: {enter_n}
            """)

  my_2d_list = []

  with open("temp.txt", "r+") as outfile:

    for line in outfile:

      
      line = line.replace("\n", "")
      line_list = line.split(", ")
      my_2d_list.append(line_list)

    print(my_2d_list)

  Check = False

  while Check == False:

    backward = int(input("\n" + "Please enter task number to edit or '-1' to return to main menu: "))

    if backward == "-1":
      Check = True
      main_menu()

    if backward != "-1":

      userline = my_2d_list[backward]
    
      print(userline)

      choice = input("Please select from one of the following options for the task number selected: " + "\n" +
      "m - mark the task as complete" + "\n" +
      "e - edit Task" + "\n")

          # conditional statement to mark task as complete
      if choice == "m":

        userline[-1] = "Yes"

        print(userline)
        my_2d_list[backward] = userline
        print(my_2d_list)
        #iterate and deleting task numbers from list my_2d_list
        for sublist in my_2d_list:
          del sublist[0]
        print(my_2d_list)

        #write output to tasks file
        with open('tasks.txt', 'w') as file_output:
          file_output.write('\n'.join(', '.join(map(str, row)) for row in my_2d_list))

      if choice == "e":

        choice_e = input("Please select from one of the following options for the task number selected: " + "\n" +
      "u - change username of task" + "\n" +
      "d - change due date of task" + "\n")

        if choice_e == "u":
           #conditional statement to assess task complete or not in order to execute edit
          
          if userline[-1] == "No":

            change_of_name = input("Please provide new username to assign the task with: ")
            userline[1] = change_of_name
            print(userline)
            #inserting change of name into my_2d_list
            my_2d_list[backward] = userline
            print(my_2d_list)
            #iterate and deleting task numbers from list my_2d_list
            for sublist in my_2d_list:
              del sublist[0]
            print(my_2d_list)

            #write output to tasks file
            with open('tasks.txt', 'w') as file_output:
              file_output.write('\n'.join(', '.join(map(str, row)) for row in my_2d_list))
          else:
            print("Can not edit task because it has been completed.") 
        
        elif choice_e == "d":

          if userline[-1] == "No":
            
            change_of_date = input("Please provide the new due date to assign the task eg. (01 Jan 2000): ")
            userline[5] = change_of_date
            print(userline[5])
            #inserting change of name into my_2d_list
            my_2d_list[backward] = userline
            print(my_2d_list)
            #iterate and deleting task numbers from list my_2d_list
            for sublist in my_2d_list:
              del sublist[0]
            print(my_2d_list)

            #write output to tasks file
            with open('tasks.txt', 'w') as file_output:
              file_output.write('\n'.join(', '.join(map(str, row)) for row in my_2d_list))    
          else:
            print("Can not edit task because it been completed.")    

        else:
          print("Please choose either 'u' or 'd'.")
      
      else:
        print("Executed to file.")

    else:
      Check = False
      print("Invalid selection.")   


def reg_user():

    if username == "admin":
   
    # assigning boelean variable to registration loop
      reg = False

    # creating loop to ask for user input
      # with open("user.txt") as user_file:

      while reg == False:
      
        twod_list = []

        with open("user.txt") as user_file:

          for line in user_file:

            line = line.replace("\n", "")   
            line_list = line.split(", ")
            twod_list.append(line_list)
            print(twod_list)
        #loop through all the data in column 0 and 1 and assign it to a variable called 'col0/col1'
        col0 = [x[0] for x in twod_list]
        col1 = [x[1] for x in twod_list]
 

        
        for pair in col0:
          
          new_username = input("Please insert new username: ")

          if new_username not in col0: 

            new_password = input("Please insert new password: ")

            confirm_password = input("Please confirm new password: ")

            if new_password == confirm_password:
              reg = True
              twod_list.append([f"{new_username}, {new_password}"])
              print("Username & password successfully registered")
              print(twod_list)
              #write output to user file
              with open('user.txt', 'w') as      file_output:
                file_output.write('\n'.join(', '.join(map(str, row)) for row in twod_list)) 
            
            if reg == False:

              print("Passwords do not match! Please make sure passwords match.")

          else:
            print("That username exists. Please try another username.")

    else:

          print("Only admin may register users")

def admin_stats():
  # Calling function generate files in case they do no exist yet.
  print(gen_reports()) 

  print("""\n++===== Task overview report =====++\n""")  
  # Opening the task_overview file to get info from it.
  with open('task_overview.txt', 'r+') as task_overview_file:  

      for line in task_overview_file:

          print(line)  

  print("""\n++===== User overview report =====++\n""")  
  # Opening user_overview file.
  with open('user_overview.txt', 'r+') as user_overview_file:  

      for line in user_overview_file:

          print(line)  


def over_due_check(due_date):

    over_due = False  # Setting Boolean variable for the task as over_due.  

    # Importing datetime and dates to enable the comparison and to retrieve the current date.
    import datetime
    from datetime import date

    # The dates in this task are in the format '10 Dec 2015' as a string.
    # So, this needs to be converted to integers to compare dates.
    # First, the variable is split into a list.
    list_dates = due_date.split()
    
    day = int(list_dates[0])  # The first item is cast into an integer and stored in the 'day' variable.
    year = int(list_dates[2])  # The second item is cast into an integer and stored in the 'year' variable.

    # A month dictionary with number values is set to enable calculation of string month into an integer. 
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    # The corresponding value of the key in months_dict which is equal to list_dates[1] (i.e. 'Dec', 'Oct' etc.) is stored in 'month'.
    # This will be a number value from the appropriate key in months_dict.
    month = months_dict[list_dates[1][0:3]]

    # Getting the current date using the datetime module and formatting it into the same format at the due date initially was.
    date_now = datetime.date.today().strftime('%d %b %Y')

    # The same process is repeated for the current date.
    # Firstly, it is split into a list of items.
    date_now_list = date_now.split()
     # The first item is stored as an integer in day_2.
    day_2 = int(date_now_list[0])  
      # Second item is stored as an integer in year_2.
    year_2 = int(date_now_list[2])  
     # The corresponding integer value from months_dict at appropriate key is stored in month_2.
    month_2 = months_dict[date_now_list[1]] 

    # With integers for year, day and month, two dates can be created in the correct format for comparison.
    # date_1 is the due date and date_2 is the current date.
    date_1 = date(year, month, day)
    date_2 = date(year_2, month_2, day_2)
     # If current date is greater than set due date, over_due is changed to 'True'
    if date_2 > date_1:  
        # over_due value is returned
        over_due = True
        return(over_due)  
      # If set due date is greater than current date, over_due is 'False'.
    elif date_1 > date_2 or date_1 == date_2:  
        # over_due value is returned.
        over_due = False
        return(over_due) 



def gen_reports():
     # Setting blank strings to store info in to be written to the generated text files.
    task_overview = "" 
    user_overview = ""

    tasks_total = len(tasks_dict)  
        
    # Adding a string with the total tasks number to the tas_overview string. 
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    # Setting variables for integers
    complete_tasks = 0  
    incomplete_tasks = 0
    overdue_tasks = 0
    
        
    for key in tasks_dict:

        if tasks_dict[key][5] == "Yes":  # Checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict.

            complete_tasks += 1  # If the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1.     

        elif tasks_dict[key][5] == "No":  # Checking for which tasks are complete by finding the 'No' string in each key of tasks_dict.
          # If the task is incomplete, variable is increased by 1.
           incomplete_tasks += 1   
            # If the over_due_check function returns 'True', a task is overdue and incomplete.
           if over_due_check(tasks_dict[key][4]):   
                 # Integer is increased by 1 to count the incomplete, overdue tasks.
               overdue_tasks += 1 
            
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(complete_tasks)}." + f"\nThe total number of incomplete tasks is {str(incomplete_tasks)}."
    task_overview = task_overview + f"\nThe total number of incomplete and overdue tasks is {str(overdue_tasks)}."
    task_overview = task_overview + f"\nThe percentage of incomplete tasks is {str(round((incomplete_tasks / len(tasks_dict)) * 100, 2))}%."
    task_overview = task_overview + f"\nThe percentage of tasks that are overdue {str(round((overdue_tasks / len(tasks_dict)) * 100, 2))}%."

    # Generating a 'task_overview' file.
    # The task_overview string is then written to the file in an easy to read format.
    with open('task_overview.txt', 'w') as f3:

        f3.write(task_overview)

    # Setting variables to store information
    total_users = 0
    complete_task_for_user = 0
    incomplete_task_for_user = 0
    incomplete_and_overdue_for_user = 0

    for key in tasks_dict:
         # Counting the number of tasks assigned to the user by identifying the first list item.
        if tasks_dict[key][0] == username: 
            # Integer is increased by 1 if the task is for the user.
            total_users += 1  
         # Checking if the task for the user is complete.
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes": 
            # Integer is increased by 1 if the task is complete.
           complete_task_for_user += 1       
        # Checking if the task for the user is incomplete.
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No": 
            # Integer is increased by 1 if the task is incomplete.
            incomplete_task_for_user += 1    
            # Checking if the task is incomplete and overdue.
            if over_due_check(tasks_dict[key][4]): 
                # If overdue, integer is increased by 1.
                incomplete_and_overdue_for_user += 1  
         
    # Writing all the information calculated above into sentence strings which are built into the user_overview string variable.
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {str(len(user_details))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username} is {str(total_users)}."
    user_overview = user_overview + f"\nThe percentage of the total number of tasks assigned to {username} is {str(round((total_users / len(tasks_dict)) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks assigned to {username} that have been completed is {str(round((complete_task_for_user / total_users) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of tasks still to be completed by {username} is {str(round((incomplete_task_for_user / total_users) * 100, 2))}%."
    user_overview = user_overview + f"\nThe percentage of incomplete and overdue tasks assigned to {username} is {str(round((incomplete_and_overdue_for_user / total_users) * 100, 2))}%."

    # Generating a 'user_overview' file.
    # The user_overview string is written to the file 
    with open('user_overview.txt', 'w') as f4:

        f4.write(user_overview)        


    return("Reports have been generated successfully.")


user_details = {}
usernames_list = []
passwords_list = []
# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as f:

    for line in f:

        newline = line.rstrip('\n')
        split_line = newline.split(", ") 
        usernames_list.append(split_line[0])  
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list   
        user_details["Passwords"] = passwords_list 
  
tasks_dict = {}

count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as task_dict:

    for line in task_dict:

        
        newline = line.rstrip('\n') 
        split_line = newline.split(", ") 
        tasks_dict[f"Task {count} details:"] = split_line # Assigning each list of items to a key in tasks_dict.
        
        count += 1  # Count used to change key value for each list of info.


main_menu()

choice = input("Enter your option from the menu: ")
#while loop to keep asking user for menu options until exit is entered. 
while choice != "e":
  if choice == "r":
    reg_user()
  elif choice == "a":
    add_task()
  elif choice == "va":
    view_all()
  elif choice == "vm":
    view_mine()
  elif choice == "ds":
    admin_stats()
  elif choice == "gr":
    gen_reports()
  else:
    print("Invalid option")

  print()
  main_menu()
  choice = input("Enter your option from the menu: ")

print("Thank you for using the program, Good bye.")

