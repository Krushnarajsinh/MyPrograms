#Dividing A big task into a small small task is called as thread
#thread is a light-weight process it is a small program that runs before An Application open or runs
#our CPU given to all the apps or tasks that are running at a same time Actually CPU is simultaneously goes to all the tasks but it's done in very high speed
#Execution have one default Thread which is called as Main Thread, when we not create any thread then by default main thread is run
from threading import *
from time import sleep
class A(Thread):
     def run(self):
         for i in range(5):
             print("Hello by A",i)
             sleep(2)   #sleep for 2 seconds

class B(Thread):
    def run(self):
        for i in range(5):
            print("Hello by B", i)
            sleep(1)  #sleep for 1 sec
a1=A()
a2=B()

a1.start()
sleep(1)
a2.start()
  #here join() method is responsible to stop the exection of main thread and that's why print("bye") statement executed at last after a1 and a2 threads are executes
a1.join()
a2.join()
print("bye")  #execution of this statement is done by main thread
#here their is colision between task at same time CPU get them. to stop that we do following:-
#here task are executed in very fast way there for we can use sleep() to keep a gap between them for execution
#here actually there are 3 threads a1,a2 and main thread
