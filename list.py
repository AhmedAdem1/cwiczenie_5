list1= [1,5,6,8,7,3]
list2= [2,5,8,"x"]
list3= [7,5,3,6.8]
list4= []
list5= [9,6,3.1,"as"]


def validate_list(array):

    try:

        assert len(array) !=0, "Error nie ma "

        for i in range (0, len(array)):
            if (not isinstance (array[i], int )) and (not isinstance (array[i], float)):
                raise ValueError("String error")

        array.sort ()
        min_array= array[0]
        max_array= array[-1]
        sum_array= sum(array)
        tuple1= (min_array, max_array, sum_array)
        print(tuple1)

    except AssertionError:
        print("Nie ma liczb")
    except ValueError:
        print("String error")


validate_list(list1)


