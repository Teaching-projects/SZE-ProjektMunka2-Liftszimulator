import building
import config
import pygame
import csv

DONE = False

Base = building.Building(config.FLOORNUMBER, config.ELEVATORNUMBER)
Base.addPassenger(config.PASSENGERNUMBER)

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            DONE = True
        if event.type == pygame.VIDEORESIZE:
            old_surface_saved = config.SCREEN
            old_size = config.SIZE
            config.SCREEN = config.pygame.display.set_mode((event.w, event.h), config.pygame.RESIZABLE)
            config.SIZE = [event.w, event.h]
            while(config.SIZE[1] % 100 != 0):
                config.SIZE = [config.SIZE[0], int(config.SIZE[1] - 1)]
            config.FLOORHEIGHT = config.SIZE[1] / config.FLOORNUMBER
            Base.resize(old_size)
            config.SCREEN.blit(old_surface_saved, (0,0))
            del old_surface_saved
    Base.simulate(config.CLOCK.tick(config.FPS))
    """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            DONE = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            POSITION = pygame.mouse.get_pos()
            for i in Base.getFloors():
                for j in i:
                    if j.getRect().getRectangle().collidepoint(POSITION) and j.getElevator().getStatus() == ["IDLE"] and j.getFloorNumber() != j.getElevator().getCurrentFloor():
                        print("clicked floor: " + str(j.getFloorNumber()))
                        j.getElevator().setStopList([j.getFloorNumber()])
                        if j.getElevator().getCurrentFloor() < j.getFloorNumber(): j.getElevator().setStatus(["UP"])
                        else: j.getElevator().setStatus(["DOWN"])
    """

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['Start', 'Destination', 'Wait', 'Finish', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for i in Base.Passengers:
        writer.writerow({'Start': i.getStartFloor(), 'Destination': i.getDestinationFloor(), 'Wait': int(i.getWaitTime() / 1000), 'Finish': int(i.getFinishTime() / 1000), 'Status': i.getStatus()})


