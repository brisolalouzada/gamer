#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Entity

from code3.const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = None

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        pass
