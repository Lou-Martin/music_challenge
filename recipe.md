# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

```python
# EXAMPLE

class My_music():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # initialize a (tbc) data structure to store tracks
        # Side effects:
        #   creates an empty list
        pass # No code here yet

    def add_track(self, track, artist):
        # Parameters:
        #   track: string representing a single track
        #   artist: string representing a single artist
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track and artist to the data structure
        pass # No code here yet

    def list_music(self):
        # Returns:
        #   A list of all currently stored tracks with their artists (formatted legibly) eg "1. Moth Grinder by Grim Salvo"
        # Side-effects:
        #   if #list_music is called before any tracks are added an error message is displayed eg "There is currently no music in {self} - use {self}.add_track() to add some!"
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a track and an artist
#adds the song to data structure
"""
songs = My_music()
songs.add_track("Moth Grinder", "Grim Salvo")
songs.list_music() # => "1. Moth Grinder by Grim Salvo"

"""
Given another track and artist
#adds the song to data structure
"""
songs = My_music()
songs.add_track("Moth Grinder", "Grim Salvo")
songs.add_track("OBLITERATION", "Killstation")
songs.list_music() # => "1. Moth Grinder by Grim Salvo"
#                      #"2. OBLITERATION by Killstation"  I'd like the formatting to be on new lines, I need to learn 1,How to test for that 2,How to code it... is it /n?

"""
Given #list_music before any songs are added
#return an error message
"""
songs = My_music()
songs.list_music() # => "There is currently no music in {self} - use {self}.add_track() to add some!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

