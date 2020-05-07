import pygame
from pygame.locals import *
from datetime import datetime

open_sans_path = 'assets/fonts/Open_Sans/OpenSans-Light.ttf'

#Initial config
pygame.init()
pygame.font.init()
pygame.display.set_caption("Life Countdown")
pygame_icon = pygame.image.load("assets/images/logo_black.png")
pygame.display.set_icon(pygame_icon)
display = pygame.display.set_mode([500,300])

white = (255, 255, 255)

#Return total seconds from datetime.datetime object
def getSeconds(date):
    today = date
    years = today.year
    months = today.month
    days = today.day
    hours = today.hour
    seconds = today.second

    total_seconds = seconds
    total_seconds += hours * 3600
    total_seconds += days * 24 * 3600
    total_seconds += months * 30 * 24 * 3600
    total_seconds += years * 365 * 24 * 3600

    return total_seconds

def main():
    #Get main rect
    display_rect = display.get_rect()
    
    #Generate main fonts
    font = pygame.font.Font(open_sans_path, 72)
    medium_font = pygame.font.Font(open_sans_path, 36)


    #Create advice text
    advice_text = medium_font.render("REMAINING SECONDS",1,(194,68,68))
    advice_text_rect = advice_text.get_rect()
    advice_text_rect.centerx = display_rect.centerx
    advice_text_rect.centery = display_rect.centery + 100

    while True:
        #Check if there is a quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        #Getting actual and last seconds from actual and las date
        my_last_date = datetime(2030,12,25,23,0,0,0)
        actual_date = datetime.now()

        remaining_seconds = getSeconds(my_last_date) - getSeconds(actual_date)


        #Display remaining seconds
        seconds_text = font.render("{:,}".format(remaining_seconds),1,(10,10,10))
        seconds_text_rect = seconds_text.get_rect()
        seconds_text_rect.centerx = display_rect.centerx
        seconds_text_rect.centery = display_rect.centery
        display.fill(white)
        display.blit(seconds_text,seconds_text_rect)
        display.blit(advice_text,advice_text_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()