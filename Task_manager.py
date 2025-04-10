import json
import os
from datetime import datetime
print("welcome to Task Management Console App")


if os.path.exists("data.json"):
    with open("data.json","r") as file:
        Tasks=json.load(file)
else:
    Tasks=[]

def save_to_json_file():
    with open("data.json","w") as file:
        json.dump(Tasks,file,indent=2)

# For adding tasks we need create function 

def Add_Task():
    task_name=input("\nEnter the TASK you want to add: ")
    task_discription=input("Enter the Task description: ")
    task_due_date=input("Enter the Due date: ")
    while True:
        priority_list=["High","Medium","Low"]
        task_priority=int(input("Enter the priority: \n 1.High \n 2.Medium \n 3.Low \n Enter option here: "))
        if task_priority>0 and task_priority<4:
            priority_opt=priority_list[task_priority-1]
            break
        else:
            print("Invalid option please choose option b/w [1-3]")


    while True:
        category_list=["Work","Personal","Others"]
        task_category=int(input("enter the category: 1.Work \n 2.Personal \n 3.others \n Enter option here: "))
        if task_category>0 and task_category<4:
            category_opt=category_list[task_category-1]
            break
        else:
            print("Invalid option please choose option b/w [1-3]")


    #task_status=input("Enter the status: ")
    Tasks.append(
        {
            "Name":task_name,
            "Discription":task_discription,
            "Due_date":task_due_date,
            "Status":"pending",
            "Priority":priority_opt,
            "category":category_opt
        }
        
    )
    save_to_json_file()
#
# to view the task are avilable in task list
def View(Tasks):
     for i in range(len(Tasks)):
            print(str(i+1)+". "+str(Tasks[i]["Name"])+" - "+str(Tasks[i]["Discription"])
                  +" - "+str(Tasks[i]["Due_date"])+" - "+str(Tasks[i]["Status"])+" - "+
                  str(Tasks[i]["Priority"])+" - "+str(Tasks[i]["category"]))
 
#2
#To update the task in the task list
def Update():
    update_task=int(input("enter the number of task you need to update :"))-1
    while True:
        update_details=int(input("\n1.Name \n 2. Description \n 3. Due_date \n 4. Status \n 5.Exit \n Enter here your option: "))
        if update_details==1:
            Tasks[update_task]["Name"]=input("enter what you need to change")
        elif update_details==2:
            Tasks[update_task]["Discription"]=input("enter what you need to change")
        elif update_details==3:
            Tasks[update_task]["Due_date"]=input("enter what you need to change")
        else:
            break
        save_to_json_file()
        View(Tasks)
        


# to do mark as completed 
def complete():
    task_num=int(input("enter the task number you completed: "))-1
    Tasks[task_num]["Status"]="completed"
    save_to_json_file()
    View(Tasks)

# to deleting the task which is unwanted
def Delete():
    task_num_del=int(input("Enter the task number you Want to delete : "))
    del Tasks[task_num_del-1]


#to filder the data according to the status or duedate
def Filter():
    filter_by=int(input("Enter the filter option \n 1.By status \n 2.By due_date \n ENTER YOUR OPTION HERE: "))
    if filter_by==1:
        
        while True:
            status_opt=input("enter the option (pending\completed): ").lower()
            if status_opt=="pending":
                
                Display(status_opt)
                break
            elif status_opt=="completed":
                
                Display(status_opt)
                break
            else:
                print("enter the valid option (pending\completed)")
                
    if filter_by==2:
        Tasks1=sorted(Tasks,key=lambda x:datetime.strptime(x["Due_date"],"%Y-%m-%d"))
        
        save_to_json_file()
        View(Tasks1)
   
    
# display
def Display(status_opt):
    for i in range(len(Tasks)):
        if Tasks[i]["Status"]==status_opt:
            print(str(i+1)+". "+str(Tasks[i]["Name"])+" - "+str(Tasks[i]["Discription"])
                  +" - "+str(Tasks[i]["Due_date"])+" - "+str(Tasks[i]["Status"])+
                  " - "+str(Tasks[i]["Priority"])+" - "+str(Tasks[i]["category"]))

while True:
    print("\n Task manager ")
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Update Tasks")
    print("4. Mark as completed")
    print("5. Delete")
    print("6. Filter")
    print("7. Exit ")
    option = int(input("Enter the option you want: "))

    if option==1:
        Add_Task()

    elif option == 2:
        View(Tasks)

    elif option ==3:
        View(Tasks)
        Update()

    elif option ==4:
        View(Tasks)
        complete()

    elif option== 5:
        Delete()
        save_to_json_file()
        

    elif option == 6:
        Filter()
    elif option == 7:
        print("Now you are exiting App")
        break

    else:
        print("invalid option please choose correct option [1-6]")