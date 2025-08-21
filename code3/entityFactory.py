#!/usr/bin/python
# -*- coding: utf-8 -*-
from code3.background import Background
from code3.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        global list_bg
        match entity_name:
            case "level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", position(0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", position(WIN_WIDTH, 0)))
        return list_bg
