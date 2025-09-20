Made a terminal typing app based on https://www.keybr.com/

Loops through a string and takes terminal input, highlights current character, compares input to expectation.
Correct > keeps going
Incorrect > highlights in red

Shows mistakes + accuracy at end

Usage:
just run the file 4Head
```bash
python main.py
```

to fix:
- Can't highlight a space in red, can fix by swapping in something else in render
- newline space looks a bit janky
- my way of taking terminal input surely can't be the best way to do it


ideas for next features:
- timer, wpm 
- different text, maybe something like scaling difficulty where you replay until you reach x accuracy / wpm
- serve 2/3 lines at a time for longer text
- live mistakes / accuracy count / timer
- take in a filepath, convert file to text, allow user to test ability to type that - if i can toss my .py files in there, I can use it to practice typing code faster


  
