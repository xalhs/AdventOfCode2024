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

## Day 5
Day 5 was the first puzzle that wasn't straightforward in its solution. Part 1 was fairly easy, for each list of numbers we just had to check a bunch of conditions on the order of its elements for whether to reject it or not. Part 2 was much more interesting. We had to reorder the list to make it fit the conditions, the conditions worked like an ordering, "a" before "b". My first idea was to take each list and check it against the conditions, each time the list failed one of the conditions (e.g. "b" was before "a") I would swap the two elements. There are small problems with this method, first one is that not every two elements in the list are directly linked to one another so we would have to run it multiple times to make it fully operational. Ideally, this would work like a bubble sort on each list of numbers. I'm sure that if run enough times on the list, it would work and I could always do something like 'while not ordered' 'run the list against the conditions', however, I didn't like this solution that much. My second idea was to take the list and create something like a "total ordering" meaning have a complete list of conditions from start to finish e.g. "a" before "b" before "c" before "d"... That was one possibility, another was having multiple "unrelated" conditions like "a" before "b" before "c" and "1" before "2" before "3", from now on I'll write "<" instead of "before". Implicitly I assumed transitivity worked globally on the set of conditions meaning that if we had "a"<"b" and "b"<"c" then "a"<"c" and so I proceeded to use Zorn's lemma to create some form of total order on the set. If you are not familiar with it Zorn's lemma basically says that if the above assumptions are true then there exists a maximal element let's call it "el" such that there is no element that is greater than that (or in our case that goes after it). Then we can separate that element and find the maximal element for the remaining list and if we do this properly we should be able to make either a totally ordered list or a bunch of totally ordered smaller lists. Unfortunately, when trying this out I discovered that in fact the conditions had loops like "a"<"b", "b"<"c", "c"<"a". This meant that transitivity didn't hold, at least not on a global level. I was sad to abandon the idea since I liked Zorn's lemma but then I realized I didn't have to trash it completely. The total order might not work on a global level but it HAS to work on a local level (i.e. for each individual list of numbers) otherwise the problem would not be solvable. So for each set of numbers, I isolated the relevant conditions (as a curated set of rules) and on those I now used my previous idea of Zorn's lemma. Finding the maximal element for each list of numbers was then easy and then I could search for the next maximal element and thus completely order them. There were a couple other technical details, for example, how to identify the next maximal element without reprocessing and re-curating the set of conditions but those are not too important. Overall pretty interesting puzzle. 

## Day 6
Day 6 was another interesting one. Part one was basically an algorithmic implementation of the description, it wasn't too complicated, it just required some creativity to add all the parameters of the description (e.g. position, direction, position of obstacles). Part 2 made the problem much more computationally intensive, now we needed to do the procedure an $n^2$ amount of times where $n$ is the size of the puzzle map. This meant that we had to optimize the algorithm from part 1. My main idea was to skip over redundant steps, we need to find the next obstacle in the path of the guard so instead of going one step forward each time and checking whether that is an obstacle, we can instead just map all obstacles in that direction and find the next one (thus skipping over many unnecessary steps). That was the main idea behind the solution, it is still not super fast but it only requires a few seconds to run instead of the hours/days it would have taken otherwise.

## Day 7
Day 7 was fairly easy, it just required basically doing all possible combinations of multiplication and addition operations between numbers in a list. I just did it the brute force way with some small optimizations. For part 2 it was almost exactly the same but now we had three operations (addition, multiplication and concatenation). I performed a very slight modification to the code and it worked immediately. All in all, an easy day.

## Day 8
Day 8 was quite easy as well, part 1 just required to find for some pairs of antennas that are in a grid, the points that are collinear with them and are twice the distance from the first antenna than from the second one (and not in between apparently). The solution was just essentially requiring some vector additions and checks to see whether the new points are in bounds. Part 2 was slightly more tricky, it required to find ALL the collinear points between each 2 antennas of the same type. To solve I just took the vector difference between the two antennas and divided it by the greater common divisor of its components (to get the smallest primitive translation vector) and then add or subtract the vector as many times as needed to stay within the bounds. Overall, pretty easy as well.

## Day 9
Day 9 was decent. It mainly involved moving elements of a string from right to left to "unoccupied" positions. Part 1 was about moving the characters of the block in the string one by one while part 2 was about moving the entire block to the first unoccupied space. It required some clever manipulations but the idea wasn't that complicated.  

## Day 10
Day 10 was a funny one. Given a height map, we had to find out how many top points we can reach from each bottom-most point using only steaps of +1 increasing height. I accidentally read the description wrong initially and solved a different problem. I thought instead it asked how many different paths are from each bottom-most point to all top points. The way I did it was by iterating over the map and assigning values to each height. Each height of "9" (the top most) would get a value of 1, then each height of "8" would get a value as the number of "9"s it neighbored. And then each subsequent height "k" would get a value based on the sum of the values of the "k+1" heights around it. Then I would just need to sum over the values of height "0". Unfortunately, that is not what the problem was asking us to do. So I modified my solution, instead of values I used a list of the possible "9"s that can be reached by each point, then for a height "k" I just had to add the lists together of all the neighboring "k+1" heights while removing the duplicate elements. Then for the height "0"s I just had to sum the lengths of their lists. That was part 1. For part 2... I had to find all the dinstinct paths... which is exactly what I solved with my wrong solution so I just inputted that answer and got it correct immediately. As I said before, pretty fun day, first time it happened to me that I "guessed" what part 2 was going to be (even by accident).   
