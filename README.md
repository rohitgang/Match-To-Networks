# Match-To-Networks

## Match feed converted to networks in real time for analysis

***

If suppose, this is the match frame : 

<img width="1792" alt="image" src="imgs/match_rep.png">

The graph state of the frame generated will be something like this : 

<img width="1349" alt="image" src="imgs/graph_rep.png">

***

Higher level steps : 

1. Achieve network generation from one frame of the match.
2. Achieve network generation for each frame in the whole match.
3. Achieve network generation from match feed in real - time.

## Installation and Setup

**Run these commands**

1. pip install virtualenv
2. virtualenv mtnenv
3. source mtnenv/bin/activate

* remember to update the requirements.txt file with nay new packages using **pip freeze > requirements.txt**

4. deactivate (use once you are done using the environment)
