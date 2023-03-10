#file: test_my_music.py
from lib.my_music import *

'''

first test verifies add track functionailty but calls upon #list_music to verify, giving the class freedom to operate as necessary

'''
def test_add_track():
    songs = My_music()
    songs.add_track("Moth Grinder", "Grim Salvo")
    result = songs.list_music()
    assert result == "1. Moth Grinder by Grim Salvo\n"

'''
second test checks for the same as the first but with different parameters (anti hard coding)

'''
def test_add_different_track():
    songs = My_music()
    songs.add_track("Alien Boy", "Oliver Tree")
    result = songs.list_music()
    assert result == "1. Alien Boy by Oliver Tree\n"

'''

third tests checks functionality and formatting of multiple tracks being listed by #list_music

'''

def test_list_of_two_tracks():
    songs = My_music()
    songs.add_track("Moth Grinder", "Grim Salvo")
    songs.add_track("OBLITERATION", "Killstation")
    result = songs.list_music()
    assert result == "1. Moth Grinder by Grim Salvo\n2. OBLITERATION by Killstation\n"

'''

fourth test same as above but checks different entries + an extra entry

'''

def test_list_of_three_tracks():
    future_garage = My_music()
    future_garage.add_track("Archangel", "Burial")
    future_garage.add_track("Moth", "Burial & Four Tet")
    future_garage.add_track("Ready Set Loop", "SBTRKT")
    result = future_garage.list_music()
    assert result == "1. Archangel by Burial\n2. Moth by Burial & Four Tet\n3. Ready Set Loop by SBTRKT\n"