#This Algorithm is First Come First Serve Algorithm... designed for the CPU Scheduling... It is a Non-premptive Algorithm which works on the basis of First Arrived process gets executed first...
import numpy as np
# Function to set Arrival time...
def SetArrivalTime(matrix):
    for z in range(0, rows):
        print(z+1, " Process");
        a = int(input("Enter the Arrival time of Process : "));
        matrix[z][0] = a;

#Function to show matrix table...
def ShowMatrix(matrix):
    print("AT\tBT\tCT\tTAT\tWT\tRT\tChecked");
    for i in range(0, rows):
        for j in range(0, 7):
            print(matrix[i][j], "\t", end=" ");
        print();

# Function to set the Burst Time for every Process...
def SetBurstTime(matrix):
    for loop in range(0, rows):
        print(loop+1, "Process ");
        a = int(input("Enter the Burst Time of the Process : "));
        matrix[loop][1] = a;

#Printing the Gantt Chart for the Processes executed in the Waiting Queue in timely order...
def PrintGanttChart(time, process):
    print("The Gantt Chart or the Waiting Queue formed is : ");
    for c in range(0, rows):
        print(process[c], "\t", end="");
    print();
    for c in range(0, rows):
        if time[c] == 0:
            #If time is 0 then the process in not yet executed...
            print("", end="");
        else:
            print(time[c],"\t", end="");
    print();

# Sorting the Processes based on their Arrival time...
def SortProcesses(matrix):
    temp = 0;
    temp1 = 0;
    str1 = "";
    for j in range(0, rows):
        for k in range(j+1, rows):
            if(matrix[k][0] < matrix[j][0]):
                temp = matrix[k][0];
                matrix[k][0] = matrix[j][0];
                matrix[j][0] = temp;
                str1 = process[k];
                process[k] = process[j];
                process[j] = str1;
                temp1 = matrix[k][1];
                matrix[k][1] = matrix[j][1];
                matrix[j][1] = temp1;

#Evaluating Completion Time of Every Process...
def EvaluateCompletionTime(matrix, time):
    for loop in range(0, rows):
        if loop == 0:
            time[loop] = matrix[loop][0] + matrix[loop][1];
            matrix[loop][6] = 1;
            print();
            ShowMatrix(matrix);
            print();
            PrintGanttChart(time, process);
        else:
            time[loop] = time[loop-1] + matrix[loop][1];
            matrix[loop][6] = 1;
            print();
            ShowMatrix(matrix);
            print();
            PrintGanttChart(time, process);

#Function to calculate Completion Time... 
def GetCompletionTime(matrix, time):
    for loop in range(0, rows):
        matrix[loop][2] = time[loop];

#Function to get the Turn Around Time of the Process...
def GetTurnAroundTime(matrix):
    for loop in range(0, rows):
        matrix[loop][3] = matrix[loop][2] - matrix[loop][0];

#Function to get the Waiting Time of the Processes...
def GetWaitingTime(matrix):
    for loop in range(0, rows):
        matrix[loop][4] = matrix[loop][3] - matrix[loop][1];

#Function to get the Response Time of the Processes...
def GetResponseTime(matrix):
    for loop in range(0, rows):
        matrix[loop][5] = matrix[loop][4];
rows = int(input("Enter the number of processes : "));
arr = [0] * rows * 7;
time = [0] * rows;
process = ["P"] * rows;
base = 0;
Queue = [0] * rows;
rotations = 0;
# We create a data chart for the CPU Scheduling algorithm
matrix = np.array([[arr]]).reshape(rows, 7);
for i in range(0, rows):
    for j in range(0, 7):
        matrix[i][j] = 0;
        print(matrix[i][j], "\t", end=" ");
    print();

for i in range(0, rows):
    process[i] = process[i] + (str)(i+1);
#Calling arrays or matrix simply call and pass them as variables...
SetArrivalTime(matrix);
ShowMatrix(matrix);
SetBurstTime(matrix);
ShowMatrix(matrix);
SortProcesses(matrix);
EvaluateCompletionTime(matrix, time);
print();
print("The Completion Time of the Processes are updated : ");
GetCompletionTime(matrix, time);
GetTurnAroundTime(matrix);
GetWaitingTime(matrix);
GetResponseTime(matrix);
print();
ShowMatrix(matrix);
print();
PrintGanttChart(time, process);