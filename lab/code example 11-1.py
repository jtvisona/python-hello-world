
from datetime import datetime, time

def main():
    input("Press Enter to start...")
    start = datetime.now()
    month = f"{start:%B}"
    day = f"{start:%d}"
    hours = f"{start:%I}"
    minutes = f"{start:%M}"
    am_pm = f"{start:%p}"
    print(f"Start time: {month} {day} at {hours}:{minutes}{am_pm}")

    input("Press Enter to stop...")   
    stop = datetime.now()
    month = f"{stop:%B}"
    day = f"{stop:%d}"
    hours = f"{stop:%I}"
    minutes = f"{stop:%M}"
    am_pm = f"{stop:%p}"
    print(f"Stop time: {month} {day} at {hours}:{minutes}{am_pm}")

    elapsed_time = stop - start
    new_days = elapsed_time.days
    new_minutes = elapsed_time.seconds // 60
    new_hours = new_minutes // 60
    new_minutes = new_minutes % 60
    print("Time elapsed: ")
    if new_days > 0:
        print(f"days: {new_days}")
    print(f"hours: {new_hours}, minutes: {new_minutes}")

if __name__ == "__main__":
    main()