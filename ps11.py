# Problem Set 11: Simulating robots
# Name: Anusika Nijher
# Collaborators: None


import math
import random
import ps11_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problem 1 
# Time: 20 min
# === Problem 2
# Time: 20 min
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

        self.width = width
        self.height = height
        self.clean = {}
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        position = (int(pos.getX()), int(pos.getY()))
        self.clean[position] = self.clean.get(position,0) + 1
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """

        possible = (int(m), int(n))
        if possible in self.clean:
            return True
        else:
            return False
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean)
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        randomWidth = random.randint(0, self.width-1)
        randomHeight = random.randint(0, self.height-1)
        return Position(randomWidth, randomHeight)
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if pos.getX() < 0 or pos.getY() < 0:
            return False
        
        if pos.getX() >= self.width or pos.getY() >= self.height:
            return False
        return True
        


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.Rroom = room
        self.Rspeed = speed
        self.Rdirection = random.randint(0,360)
        self.Rposition = room.getRandomPosition()
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.Rposition
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.Rdirection

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.Rposition = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.Rdirection = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        not_hitting_wall = True
        while not_hitting_wall:
            currently = self.getRobotPosition()
            next_position = currently.getNewPosition(self.getRobotDirection(), self.Rspeed)
            if self.Rroom.isPositionInRoom(next_position):
                self.Rposition = next_position
                self.Rroom.cleanTileAtPosition(self.Rposition)
                not_hitting_wall = False
            else:
                self.Rdirection = random.randint(0, 360)


# === Problem 3
# Time: 2 hours
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    Results = []
    list_length = 0
    avg_length = 0
    for test in range(num_trials):
        if visualize:
            anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        testing_room = RectangularRoom(width,height)
        robotsList = []
        for robot in range(num_robots):
            robotsList.append(robot_type(testing_room, speed))
        percentage = 0.0000000
        path = []
        while percentage < min_coverage:
            if visualize:
                anim.update(testing_room,robotsList)
            for robot in robotsList:
                robot.updatePositionAndClean()
            percentage = float(testing_room.getNumCleanedTiles())/float(testing_room.getNumTiles())
            path.append(percentage)
        if visualize:
            anim.done()
        Results.append(path)
    for path in Results:
        list_length = list_length + len(path)
    avg_length = list_length/len(Results)
    return avg_length

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
# Time: 2 hours
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    listofrooms = [1, 5, 10, 15, 20, 25]
    listofavgs = []
    for room in listofrooms:
        a = runSimulation(1, 1.0, room, room, 0.75, 50, Robot, False)
        listofavgs.append(int(a))
    print "for room sizes", listofrooms, "we get these average times", listofavgs
    pylab.figure()
    pylab.plot(listofrooms,listofavgs, 'ro')
    pylab.ylabel('Average Time in Clock Ticks')
    pylab.xlabel('Room Size')
    pylab.title('Time Vs. Room Size (squares) 75% Clean with 1 Robot')

#showPlot1()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    listofavgs = []
    listofrobots =[]
    for robots in range(1,11):
        listofrobots.append(robots)
        a = runSimulation(robots, 1.0, 25, 25, 0.75, 50, Robot, False)
        listofavgs.append(int(a))
    print "for robot numbers ranging from 1 - 10 we get these average times", listofavgs
    pylab.figure() 
    pylab.plot(listofrobots,listofavgs,'ro')
    pylab.ylabel('Average Time in Clock Ticks')
    pylab.xlabel('Number of Robots')
    pylab.title('Time Vs. Number of Robots in a 25x25 Room 75% Clean')
        

#showPlot2()


def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    listofavgs = []
    listofrooms = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    listofratios = []
    for rooms in listofrooms:
        listofratios.append((float(rooms[0])/float(rooms[1])))
        a= runSimulation(2, 1.0, rooms[0], rooms[1], 0.75, 150, Robot, False)
        listofavgs.append(int(a))
    print "for room ratios", listofratios, "we get these average times", listofavgs, 
    pylab.figure()
    pylab.plot(listofratios,listofavgs, 'ro')
    pylab.ylabel('Average Time in Clock Ticks')
    pylab.xlabel('Room Ratio')
    pylab.title('Time Vs. Room Ratio 75% Clean with 2 Robots')

#showPlot3()


def showPlot4():

    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    pylab.figure()
    # TODO: Your code goes here
    listofcoverage = [0.2, 0.4, 0.6, 0.8, 1.0]
    robotsandcleaning = {}
    for robots in range(1,6):
        listofavgs = []
        for coverage in listofcoverage:
            a = runSimulation(robots, 1.0, 25, 25, coverage, 50, Robot, False)
            listofavgs.append(int(a))
        robotsandcleaning[robots] = listofavgs
        pylab.plot(listofcoverage, robotsandcleaning[robots], label= 'Robots: ' + str(robots))
    print robotsandcleaning
    pylab.legend()
    pylab.ylabel('Average Cleaning Time in Clock Ticks')
    pylab.xlabel('Cleaning Percentage')
    pylab.title('Cleaning Time vs Cleaning Percentage')
    
#showPlot4()


# === Problem 5
# Time: 10mins
class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        not_hitting_wall = True
        while not_hitting_wall:
            currently = self.getRobotPosition()
            self.setRobotDirection(random.randint(0, 360))
            next_position = currently.getNewPosition(self.getRobotDirection(), self.Rspeed)
            if self.Rroom.isPositionInRoom(next_position):
                self.Rposition = next_position
                self.Rroom.cleanTileAtPosition(self.Rposition)
                not_hitting_wall = False
            else:
                self.Rdirection = random.randint(0, 360)

# === Problem 6
# Time: 45 min
def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    pylab.figure()
    listofrooms = [1, 5, 10, 15, 20, 25]
    listoftypes = [Robot, RandomWalkRobot]
    robotsandcleaning = {}
    for robots in listoftypes:
        listofavgs = []
        for room in listofrooms:
            a = runSimulation(1, 1.0, room, room, 0.75, 50, robots, False)
            listofavgs.append(int(a))
        robotsandcleaning[robots] = listofavgs
        pylab.plot(listofrooms, robotsandcleaning[robots], label= 'Robot Type: ' + str(robots))
    print robotsandcleaning
    pylab.legend()
    pylab.ylabel('Average Cleaning Time in Clock Ticks')
    pylab.xlabel('Room Width and Height')
    pylab.title('Cleaning Time vs Room Width and Height 75% Clean 1 Robot')
    
showPlot5()
pylab.show()


print runSimulation(1, 1.0, 5, 5, 1, 100, Robot, False)

