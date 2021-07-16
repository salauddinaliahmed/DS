import Queues
"""
Excerise 9, completed. 
"""

class PrinterQ:
    def __init__(self) -> None:
        
        self.q = Queues.Queue()
    
    def add_job(self, job):
        self.q.enqueue(job)
    
    def do_jobs(self):
        for _ in range(len(self.q)):
            x = self.q.dequeue()
            print(f"Doing the job : {x}")
    


if __name__ == '__main__':
    pq = PrinterQ()
    for _ in range(5):
        pq.add_job(f'job_{_+1}')

    print(pq)
    pq.do_jobs()