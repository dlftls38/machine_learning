import gym
from gym.envs.registration import register
from colorama import init
from kbhit import KBHit
import msvcrt as vc

init(autoreset=True)

env = gym.make('FrozenLake-v0')       # is_slippery True
env.render()                            # Show the initial board


while True:
    keyIn = vc.getch().decode('utf-8').lower()
    if keyIn in ['w', 'a', 's', 'd']:
        action = 3          # up
        if keyIn == 's':
            action = 1      # down
        elif keyIn == 'a':
            action = 0      # left
        elif keyIn == 'd':
            action = 2      # right
        
        state, reward, isDone, information = env.step(action)
        env.render()
        env.reset()
        print("state : {} \t action : {} \t reward : {} \t info : {}".format(
            state, action, reward, information))
        print() # new line
        if isDone:
            print("DONE")
            break
    else:
        break