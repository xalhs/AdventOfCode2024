# Advent of Code 2024
These are my scripts for the puzzles at https://adventofcode.com/2024 . Same as last year, I will be uploading all days that I solve with a short commentary on thought process/description. All the puzzles (so far) have been solved without looking up any hint related to the event. Note that my naming process for the input texts is input + the date. So for the first day it was input1.txt, the second day input2.txt... etc.

## Day 1
The first days are generally fairly easy, so I didn't expect much. Part 1 was mainly about sorting 2 lists and taking the absolute differences of their elements, initially I messed up because the puzzle said to find their "distances" and I thought it meant the difference between their positions. Part 2 was similarly easy it just required a simple operation between the lists.

## Day 2
Day 2 wasn't too difficult either. It was basically a bunch of if statements to find the allowed sequences. Part 2 was just the same thing but ignoring one of the columns each time.

## Day 3
Day 3 was mostly about text parsing. It didn't have anything too special but part 1 took me a bit because I was reinitializing my result at every line and couldn't find the problem. Part 2 was easy as well, it just required a couple of extra parsing functions. 

## Day 4
Day 4 wasn't hard, the main idea for part 1 is essentially finding all the "X"s and then figuring out how many "XMAS" words they create in each of the 8 directions. The trap I fell for here was forgetting that with my loops you could go to negative indices and would cause lists to warp around so I counted a few extra words this way. Interestingly the way I figured that out was by forgetting to do another typical thing which was to remove the "\n" from every line. After I removed it I found out I was counting more words which shouldn't happen so then I realized that in fact that column of "\n" was actually protecting me from overcounting due to the horizontal warp arounds and so I added another row of dots to prevent the vertical warp arounds from happening. Part 2 was simple too, the idea here is to iterate over all the "A"s and then check if they fulfill the conditions. 
