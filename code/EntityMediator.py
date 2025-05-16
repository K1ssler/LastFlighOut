#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code import Entity


class EntityMediator:

    @staticmethod
    def verify_collision(self, entity_list: list[Entity]):
        for entity in entity_list:
            if pygame.sprite.spritecollide(entity, self.collision_sprites, False, pygame.sprite.collide_mask) \
                    or entity.rect.top <= 0:
                for sprite in self.collision_sprites.sprites():
                    if sprite.sprite_type == 'obstacle':
                        sprite.kill()
                self.active = False
                entity.kill()
