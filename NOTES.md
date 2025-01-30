Notes from converting the python files to being able to handle Sadism
Disgust Study (from the Moral Disgust Study)

9978.vhdr has spaces in the filenames for its .vmrk and .eeg files
for some reason.

- What's the right way to fix this?
    - Add underscores manually and check.
    - Now it works!
- What other subjects have this issue?
    - None

- Marker timestamps = seconds * 10^4 ?
    - No. Timestamp at session start = YYYYMMDDHHmmSSssssss
    - Marker timestamp = number of samples
- 9647 only 48 minutes long?
    - No. Markers are samples. 29M samples @ 5K samples / sec 


Synchronization through start beeps.

- Can we use multiple start beeps as a way to verify accuracy for each?
- Get an average offset for better synchronization?


- What marker number corresponds with the start beep of each condition?
    - Gustatory: 5 
    - Moral: 11
    - Visual: 1
    - See `marker_info.csv` for all Markers  

- What are all the snippets of interest?
- Which markers mark the beginning and end of snippets of interest?
    - For Gustatory?
        - view 8:9
    - For Moral?
        - offer 14:15
    - For Visual?
        - spit 22:32
        - palatability 26:23
    - All
        - baseline 2:3
        - cross 6:7

- How to check for typos?
    - Look for durations < 0
    - Look for durations > some value, maybe 20 s?
    - Review all durations > some value, maybe 15 s?

- How to improve synchrony?
    - Compare spit (21) and rinse (24) sync times too
        - Added both
        - spit is much more reliable than rinse
        - drop rinse
    - Does an adjustment to the sampling rate help? Is it a constant rate?
        - Seems to be a constant rate
        - 30.00 / 29.97 frame rate error accounts for it, results in an
            apparent sampling rate of 5005.005

    - 9462 has a different offset for moral and visual
        - recording paused between conditions
        - address by using the condition start sync as the one and only sync
            for the condition


- Check for out of norm artifact durations

Current subjects
2 x's means that 
a) artifact durations are distributed as expected. obvious data entry errors
    are removed and
b) offsets and sampling rate scaling checks out
5010 x x
6466 x x 43 should be 42
6664 x x 
8576 x x 4 entries in wrong column
8827 x x 1 in the hour column
9206 x x
9462 x x
9647 x ? 53 should be 43, long talking? delete row
9978 x x


Find offset for each condition based on condition start beeps

- How to verify artifacts are removed correctly? Manually?

- 6664 has a snippet that is entirely removed. Likely to result in a nan.
