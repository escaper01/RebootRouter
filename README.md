# Router Reboot

I made this python script to reboot my Huawei Router b612s-25d programmatically using Selenium.

### Setup:

```bash
git clone https://github.com/escaper01/router_reboot.git
```

Before installing the requirements, it’s better to create a virtual environment for the needed packages and activated it

```bash
virtualenv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

to execute the script:

```bash
python bot.py
```

For my use case, my internet connection gets a slower during the night, so I have to reboot my router every time it happens as an edge solution 😎 I have made this script run every time using task scheduler under Windows OS (for Linux users CRON job would do the trick flawlessly).
Before setting up the task, we should create a BATCH script(Already in the repo).

```bash
CD C:\Users\escaper\OneDrive\Bureau\projects\RebootRouterBot
CALL .\venv\Scripts\activate
CALL python "bot.py"
```

The script is self-explanatory, now what’s left is the Task Scheduler:

![Untitled](media/Untitled.png)

Create Task:

![Untitled](media/Untitled%201.png)

![Untitled](media/Untitled%202.png)

As for the Triggers settings:

![Untitled](media/Untitled%203.png)

That would make the script executed every 30 minutes.

![Untitled](media/Untitled%204.png)

And the Action would to run the BATCH script (Set up the full path for the **script.bat)**

Once you hit **OK,** the script will run as scheduler.

![Untitled](media/Untitled%205.png)

![https://media0.giphy.com/media/3oEjI8Kq5HhZLCrqBW/giphy.gif?cid=ecf05e47u0pv3ktu8q0mb4kpdsk3lcwz3yi09epvusjk43yl&rid=giphy.gif&ct=g](https://media0.giphy.com/media/3oEjI8Kq5HhZLCrqBW/giphy.gif?cid=ecf05e47u0pv3ktu8q0mb4kpdsk3lcwz3yi09epvusjk43yl&rid=giphy.gif&ct=g)
