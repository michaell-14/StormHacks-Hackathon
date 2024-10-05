import pygame
from Animations import PlayAnimation

NFC_tags = {
    34343 : "Lion",
    23223 : "Monkey"
}

currentAnimal = NFC_tags(uid)

PlayAnimation(currentAnimal)
