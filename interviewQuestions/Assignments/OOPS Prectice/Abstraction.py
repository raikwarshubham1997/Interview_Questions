"""
Abstraction :- abstraction is a simple hiding the implementation of the method and showing out
               only the function of the methods. we can define what methods needed to be included and excluded too.
"""

# Example of Abstraction is Juice Machine

from abc import ABC, abstractmethod

class JuiceMachine(ABC):
    @abstractmethod
    def extract_juice(self, fruit):
        """यह एक Abstract Method है, जिसे Child Class में define किया जाएगा।"""
        pass

# Step 2: Child Class बनाना जो Abstract Class को Implement करेगी
class AppleJuice(JuiceMachine):
    def extract_juice(self, fruit):
        if fruit.lower() == "apple":
            return "Apple juice ready!"
        else:
            return "This juicer only makes apple juice!"

class OrangeJuice(JuiceMachine):
    def extract_juice(self, fruit):
        if fruit.lower() == "orange":
            return "Orange juice ready!"

        else:
            return "This juicer only makes orange juice"

apl = AppleJuice()
orng = OrangeJuice()

print(apl.extract_juice("Apple"))
print(orng.extract_juice("Orange"))
print(apl.extract_juice("banana"))

print("==================Example 2====================")
'''
🎵 Example 1: Music Player (Abstract Class) 🎵
मान लो, तुमने एक Music Player बनाया है। इसमें अलग-अलग फॉर्मेट (MP3, WAV, FLAC) के गाने प्ले हो सकते हैं, लेकिन User को यह जानने की ज़रूरत नहीं कि अंदर कैसे प्ले हो रहा है!
'''

from abc import ABC, abstractmethod

class MusicPlayer(ABC):
    @abstractmethod
    def play_music(self, file_name):
        pass

class MP3Player(MusicPlayer):
    def play_music(self, file_name):
        return f"Playing MP3 file : {file_name}.mp3"

class WAVPlayer(MusicPlayer):
    def play_music(self, file_name):
        return f"playing WAV file: {file_name}.wav"


mp3 = MP3Player()
wav = WAVPlayer()

print(mp3.play_music("song1"))
print(wav.play_music("song2"))

print("==================Example 3====================")
'''
🚗 Example 2: Car (Abstract Class) 🚗
तुम्हें कार चलाना आता है, लेकिन तुम इंजन के अंदर का सिस्टम नहीं जानते। चलो इसे Python में लिखते हैं:
'''
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def Start(self):
        pass

    def Stop(self):
        pass

class Tesla(Car):
    def Start(self):
        return "Tesla Car Started with Electric Power!"

    def Stop(self):
        return "Tesla car stopped with sensor Break!"

class BMW(Car):
    def Start(self):
        return "BMW started with Petrol Engine!"

    def Stop(self):
        return "BMW stopped with Mannual Break!"



tesla =Tesla()
bmw = BMW()

print(tesla.Start())
print(bmw.Start())
print(tesla.Stop())
print(bmw.Stop())



print("==================Example 4====================")
# TV Remote
from abc import ABC, abstractmethod

class Remote(ABC):
    @abstractmethod
    def press(self, button):
        pass

class ChannelChange(Remote):
    def press(self, button):
        if button.lower() == "next":
            return "You pressed Next button!"
        elif button.lower() == "pre":
            return "You pressed Pre button!"

        else:
            return "Press a valid button!!!"

class Volume(Remote):
    def press(self, button):
        if button.lower() == "up":
            return "You pressed volume Up button!"
        elif button.lower() == "down":
            return "You pressed volume Down button!"

        else:
            return "Press a valid button!!!"

cc = ChannelChange()
vol = Volume()

print(cc.press("Next"))
print(vol.press("Up"))
print(cc.press("Pre"))
print(vol.press("Down"))
print(cc.press("Menu"))