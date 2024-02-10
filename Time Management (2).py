import time

def pomodoro_timer():
    work_duration = 5 * 60  #5 minutes in seconds
    break_duration = 3 * 60  #5 minutes in seconds

    while True:
        print("Pomodoro starts now! Work for 5 minutes.")
        time.sleep(work_duration)

        print("Time for a short break (3 minutes).")
        time.sleep(break_duration)

if __name__ == "__main__":
    pomodoro_timer()