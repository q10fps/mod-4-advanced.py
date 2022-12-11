'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''
social_graph = {   
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(fromMember, toMember, social_graph):
    
    # Check if fromMember follows toMember
        if toMember in social_graph[fromMember]["following"]:
        # Check if toMember follows fromMember
            if fromMember in social_graph[toMember]["following"]:
                return "friend"
            else:
                return "follower"
    
        if fromMember in social_graph[toMember]["following"]:
            return "following"
    
        return "no relationship"
    
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Check for a winner on each row
    
    # Check for a winner on each row
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]
    
    # Check for a winner on each column
    for col in range(len(board[0])):
        column = [row[col] for row in board]
        if len(set(column)) == 1 and column[0] != " ":
            return column[0]
    
    # Check for a winner on the diagonal from top left to bottom right
    diagonal = [board[i][i] for i in range(len(board))]
    if len(set(diagonal)) == 1 and diagonal[0] != " ":
        return diagonal[0]
    
    # Check for a winner on the diagonal from top right to bottom left
    diagonal = [board[i][len(board) - i - 1] for i in range(len(board))]
    if len(set(diagonal)) == 1 and diagonal[0] != " ":
        return diagonal[0]
    
    else:
        return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_travel_time = 0

    # If the stops are the same, the total travel time is 0
    if first_stop == second_stop:
        return 0

    # Get the list of stops in the route
    stops = [leg[0] for leg in route_map.keys()]

    # Check if the second stop comes directly after the first stop in the route
    if stops.index(first_stop) + 1 == stops.index(second_stop):

        # If the second stop is directly after the first stop, return the travel time for that leg
        return route_map[(first_stop, second_stop)]["travel_time_mins"]
        
    else:

        # Otherwise, keep traversing the route until second stop is reached
        current_stop = first_stop
        while current_stop != second_stop:

            # Get the next stop in the route
            next_stop = stops[(stops.index(current_stop) + 1) % len(stops)]

            # Add the travel time for the current leg to the total travel time
            total_travel_time += route_map[(current_stop, next_stop)]["travel_time_mins"]

            # Move to the next stop in the route
            current_stop = next_stop
       
        return total_travel_time

