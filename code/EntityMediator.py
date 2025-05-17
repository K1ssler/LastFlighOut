import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, KNOCKBACK_DISTANCE
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.Point import Point


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0  # enemy left the screen, dies

    @staticmethod
    def __verify_collision_entity(player: Player, enemy: Enemy):
        knockback_distance = KNOCKBACK_DISTANCE
        collision_sound = pygame.mixer.Sound('./asset/Collision.wav')
        collision_sound.set_volume(0.5)

        if player.invincibility_timer == 0:

            if player.rect.colliderect(enemy.rect):
                collision_sound.play()
                player.health -= enemy.damage
                player.last_dmg = enemy.name
                player.invincibility_timer = 1000

                # push player away on collision
                dx = player.rect.centerx - enemy.rect.centerx
                dy = player.rect.centery - enemy.rect.centery

                distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)
                norm_dx = dx / distance
                norm_dy = dy / distance

                new_x = player.rect.x + int(norm_dx * knockback_distance)
                new_y = player.rect.y + int(norm_dy * knockback_distance)

                new_x = max(0, min(new_x, WIN_WIDTH - player.rect.width))
                new_y = max(0, min(new_y, WIN_HEIGHT - player.rect.height))

                player.rect.x = new_x
                player.rect.y = new_y

    @staticmethod
    def __verify_collision_point(player: Player, enemy: Enemy ,point: Point):

        if point.name == 'Point':
            collision_sound = pygame.mixer.Sound('./asset/Coin.wav')
        else:
            collision_sound = pygame.mixer.Sound('./asset/Diamond.wav')
        collision_sound.set_volume(0.5)

        if player.rect.colliderect(point.rect):
            collision_sound.play()
            player.score += point.score
            point.health -= player.damage

        for e in enemy[:]:
            if e.rect.colliderect(point.rect):
                point.health -= e.damage



    @staticmethod
    def __give_score(enemy: Enemy, player: Player):
        player.score += enemy.score

    @staticmethod
    def verify_collision(player: Player, enemies: list[Enemy], points: list[Point]):
        for enemy in enemies:
            EntityMediator.__verify_collision_window(enemy)
            EntityMediator.__verify_collision_entity(player, enemy)

        for point in points:
            EntityMediator.__verify_collision_window(point)
            EntityMediator.__verify_collision_point(player, enemies ,point)


    @staticmethod
    def verify_health(player: Player, enemies: list[Enemy], points: list[Point], entity_list: list[Entity]):
        # Verifica se o player morreu
        if player.health <= 0 and player in entity_list:
            entity_list.remove(player)

        for enemy in enemies[:]:  # cria uma cópia da lista para evitar erro ao remover
            if enemy.health <= 0:
                EntityMediator.__give_score(enemy, player)
                enemies.remove(enemy)
                if enemy in entity_list:
                    entity_list.remove(enemy)

        for point in points[:]:
            if point.health <= 0:
                points.remove(point)
                if point in entity_list:
                    entity_list.remove(point)
