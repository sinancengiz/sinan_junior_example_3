import pdb

# concept of recursion is t calling function in its budy

def sinan_junior_exercise_3(dummy_list_of_list):
    # in the lines below we return the list if it is an emty list
    if dummy_list_of_list == []:
        return dummy_list_of_list

    # lines below is beening runned if first item in the given list type is a list  if it is not we go else statement, 
    #other wise we cal function with first + what we return from rest of the list code after + sign at line 14 makes we contunius  call the function for rest of the list  
    if type(dummy_list_of_list[0]) == type([]):
        print(dummy_list_of_list[0])
        return sinan_junior_exercise_3(dummy_list_of_list[0] + sinan_junior_exercise_3(dummy_list_of_list[1:]))
    else:
        # here is where all magic is done, logic here is we return first item in the situation we know it is not a list because otherwise above code will run
        # + plus what we return from the function is will be first item + what we retrun from function until there is no element left 
        # that will return us flattened list 
        # to better demonsration with given example please look at the excel screen shoot 
        print(dummy_list_of_list[0])
        return dummy_list_of_list[:1] + sinan_junior_exercise_3(dummy_list_of_list[1:])



dummy_list_of_list = ['a', ['b', 'c', ['d', 1]], 2, [3]]


print(sinan_junior_exercise_3(dummy_list_of_list))

