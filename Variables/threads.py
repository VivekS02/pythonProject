import threading
t=threading.current_thread()

print("current thread:", t)
print("Thread name:",t.name)
print("Thread identifier:",t.ident)
print("is the thread alive:",t.is_alive())
t.name = 'MyThread'
print("After name change:",t.name)