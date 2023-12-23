import re
from collections import deque
import matplotlib.pyplot as plt

event_q = deque()
con_list = []
ff_list = []
objects = {}
lp = 0
hp = 0

class Mod:
    def __init__(self, name):
        self.name = name
        self.destinations = []

    def __repr__(self):
        return f'{self.name}'

    def add_modules(self, module):
        self.destinations.append(module)

class FF_module(Mod):
    def __init__(self, name):
        super().__init__(name)
        self.states = {'OFF', 'ON'}
        self.transitions = {
                            'OFF': {'LOW' : 'ON'},
                            'ON' : {'LOW' : 'OFF'}
                            }

        self.current_state = 'OFF'
        global ff_list

        ff_list.append(self)

    def add_to_queue(self,pulse):
        global event_q, lp, hp
    
        if not self.destinations:
            return
   
        if self.current_state == 'OFF' and pulse == 'LOW':
            for each in self.destinations:
                event_q.append((self, 'HIGH', each))   
                hp += 1             
                # print(f"{self.name} - HIGH -> {each}")

        elif self.current_state == 'ON' and pulse == 'LOW':
            for each in self.destinations:
                event_q.append((self, 'LOW', each)) 
                lp += 1               
                # print(f"{self.name} LOW -> {each}")


    def transition(self, event):
        _,pulse,_ = event
        if pulse in self.transitions[self.current_state]:
            self.add_to_queue(pulse)
            self.current_state = self.transitions[self.current_state][pulse]
            # print(f'Transitioned {self.name} to {self.current_state}')

        # else:
            # print(f'Invalid event for current state')
            # return

        return True

class Con_module(Mod):
    def __init__(self, name):
        super().__init__(name)
        self.memory = {}
        # self.input = {}
        global con_list

        con_list.append(self)

    def add_to_queue(self):
        global event_q, lp, hp
    
        if not self.destinations:
            return
   
        if all(value == 'HIGH' for value in self.memory.values()):
            for each in self.destinations:
                event_q.append((self, 'LOW', each))  
                lp += 1              
                # print(f"{self.name} - LOW -> {each}")
        else: 
            for each in self.destinations:
                event_q.append((self, 'HIGH', each))                
                hp += 1
                # print(f"{self.name} - HIGH -> {each}")


    def transition(self, event):
        from_mod, pulse, _ = event
        self.memory[from_mod] = pulse
        self.add_to_queue()
        return True

    def add_input(self, ob):
        self.memory[ob] = 'LOW'

class B_mod(Mod):
    def __init__(self, name):
        super().__init__(name)

    def add_to_queue(self,pulse):
        global event_q, lp, hp
         

        if not self.destinations:
            return

        for each in self.destinations:
            event_q.append((self, pulse, each))

            if pulse == 'LOW':
                lp += 1
            elif pulse == 'HIGH':
                hp += 1

            # print(f"{self.name} - pulse -> {each}")


    def transition(self, pulse):
        self.add_to_queue(pulse)

class outmod(Mod):
    def __init__(self, name):
        super().__init__(name)

    def transition(self, event):
        fr, pulse, to = event
        print(pulse)
        if pulse == 'LOW':
            return False
        return True


def parse(data):
    re_pattern = f'(?<=[&%])'
    global objects


    for i in data:
        module, destination = i.strip().split('->')
        destination = destination.strip().split(', ')
        module = module.strip()
        module = re.split(re_pattern, module)
        
        if module[0] == 'broadcaster':
            objects[module[0]] = (B_mod(module[0]), destination)
        elif module[0] == '%':
            objects[module[1]] = (FF_module(module[1]), destination)
        elif module[0] == '&':
            objects[module[1]] = (Con_module(module[1]), destination)
       
        # objects['output'] = (outmod('output'), ['output'])
        objects['rx'] = (outmod('rx'), ['rx'])

     
    for v in objects.values():
        obj, lst = v
        # print(obj, lst)
        for item in lst:
            # if item == 'output':
                # obj.add_modules('output')
                # continue
            obj.add_modules(objects[item][0])
        # print(type(obj.destinations[0]))
                
    for c in con_list:
        for v in objects.values():
            obj, lst = v
            if str(c) in lst:
                c.add_input(obj)



def press_button():
    broadcaster = objects['broadcaster'][0]
    broadcaster.transition('LOW')

    while event_q:
        event = event_q.popleft()
        continue_loop = event[2].transition(event)
        if not continue_loop:
            return False
        return True

def plot_pulses(pulse_data):
    # Assuming pulse_data is a list of lists, where each sublist contains pulses at a time step
    plt.figure(figsize=(10, 6))
    
    for i, pulses in enumerate(pulse_data):
        plt.plot([i] * len(pulses), pulses, 'o')  # Plot each pulse

    plt.xlabel('Time Step')
    plt.ylabel('Pulses')
    plt.title('Pulse Simulation Over Time')
    plt.show()



def main(data):
    global lp, hp
    parse(data)
    iterations = 5

    pulse_data = []

    """ part 1 """
    for i in range(iterations):
        lp += 1
        press_button()  
        pulse_data.append((lp, hp))
    # print(lp * hp)
    # print(pulse_data)
    plot_pulses(pulse_data)

    """ part 2 """
    # count = 0

    # while True:
    #     count += 1
    #     keep_pressing = press_button()  
    #     if not keep_pressing:
    #         break
    
    # print(count)
        
 

if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_20\test_data2.txt'
    path = r'C:\AOC\2023\Day_20\data.txt'
    
    # 167_409_079_868_000
    with open(path, 'r') as file:
        input = file.read().splitlines()

      
    total = main(input)
    # print(total)

    