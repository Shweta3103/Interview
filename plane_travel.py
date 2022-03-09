
def convert2int(x=None):
    return int(x)

def get_input():
    group_num = int(input())
    temp = input().strip().split()
    # temp is list with string value, convert it to int list
    num_list = list(map(convert2int, temp))

    if len(num_list) != group_num:
        print("error in given input")
        raise("please provide correct input")

    return (group_num,num_list)

def set_default_status(strength_list, default_status):
    # keep dictionary form for status
    for i in strength_list:
        d = {"strength":i, "location":"source"}
        default_status.append(d)

def find_possible_plane(psg, plane_status):
    total = psg['strength']
    location = psg['location']
    result = []
    if location != 'destination':
        for plane in plane_status:
            if plane['strength'] >= total:
                result.append(plane)
    return result


if __name__ == "__main__":
    # 1. take input argument in give format
    """
        4
        8 1 6 9
        3
        7 2 3
    """
    #ps_num, ps_num_list = get_input()
    #plane_num, plane_num_list = get_input()
    ps_num, ps_num_list = (4, [8,2,5,9])
    plane_num, plane_num_list = (3, [7,2,9])

    print("The total passenger group: {}".format(ps_num))
    print("The number of passenger in each group: {}\n".format(ps_num_list))

    print("The total plane: {}".format(plane_num))
    print("The strength of each plane: {}\n".format(plane_num_list))

    # take care of flight location and group location
    # use dictionary in list
    passenger_status = []
    plane_status = []

    # se default status to source location
    set_default_status(ps_num_list, passenger_status)
    set_default_status(plane_num_list, plane_status)

    # debug information
    print("passenger: {}".format(passenger_status))
    print("plane: {}".format(plane_status))

    time_unit = 0
    for psg in passenger_status:
        #find possible plane that can carry passenger group to destinations
        possible_plane = find_possible_plane(psg, plane_status)

        # if no plane is available to carry print erro message
        if len(possible_plane) == 0:
            print("cannot move passenger group: {} as no plane can accomodate this capacity".format(psg['strength']))
            continue
        print("passenger: {} possible plane: {}".format(psg, possible_plane))

        # find plane matching minimum capacity
        plane = min(possible_plane, key=lambda x:x['strength'])

        #update time taken to reach to destination
        if plane['location'] == 'source':
            time_unit += 1
        else:
            time_unit += 2

        # update passenger status to destination
        idx = passenger_status.index(psg)
        passenger_status[idx]['location'] = 'destination'

        # update plane status to destination
        idx = plane_status.index(plane)
        plane_status[idx]['location'] = 'destination'

    #print total time taken to reach
    print("Total time: {}".format(time_unit))




