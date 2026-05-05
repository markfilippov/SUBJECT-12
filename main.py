import pygame
import sys
import os
from enum import Enum

pygame.init()
pygame.mixer.init()

# Константы
FPS = 60
WIDTH = 1920
HEIGHT = 1080

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 60, 60)
LIGHT_BLUE = (100, 200, 255)
OLD_PAPER = (210, 190, 160)
CHALK_WHITE = (245, 245, 220)
CHALK_GRAY = (180, 180, 160)
MAX_COLOR = (100, 120, 100)
KAIL_COLOR = (120, 140, 150)
SILVER_GRAY = (192, 192, 192)
DARK_GRAY = (80, 80, 80)
TEACHER_COLOR = (100, 100, 100)
YELLOW = (255, 255, 100)
LIGHT_CYAN = (150, 255, 255)
GREEN = (100, 255, 100)


# Состояния
class State(Enum):
    BOOT = 0
    LOGO = 1
    DISCLAIMER = 2
    MENU = 3
    PROLOGUE = 4
    PROLOGUE_WAKE = 5
    THOUGHTS = 6
    ACT1_TRANSITION = 7
    ACT1_MORNING = 8
    ACT1_CORRIDOR = 9
    ACT1_LESSON = 10
    ACT1_CANTEEN = 11
    ACT1_LUCIA = 12
    ACT1_EVENING = 13
    ACT1_NIGHT = 14
    ACT1_EMPTY_CORRIDOR = 15
    ACT1_INSOMNIA = 16
    ACT1_DAY2_TRANSITION = 17
    ACT2_MORNING = 18
    ACT2_CORRIDOR = 19
    ACT2_LECTURE = 20
    ACT2_POST_LECTURE = 21
    ACT2_CLOSED_WING = 22
    ACT2_LIBRARY = 23
    ACT2_NIGHT = 24
    ACT2_DAY3_TRANSITION = 25
    ACT3_MORNING = 26
    ACT3_MATH_EXAM = 27
    ACT3_CORRIDOR_SAILAS = 28
    ACT3_LIBRARY_EVENING = 29
    ACT3_AWAKENING = 30
    ACT3_NIGHT = 31
    ACT3_DAY4_TRANSITION = 32
    ACT4_MORNING = 33
    ACT4_MATH_TEST = 34
    ACT4_CORRIDOR_WARNING = 35
    ACT4_OLD_LIBRARY = 36
    ACT4_SECRET_ROOM = 37
    ACT4_DAY5_TRANSITION = 38
    ACT5_MORNING = 39
    ACT5_CORRIDOR_RULES = 40
    ACT5_SECRET_MEETING = 41
    ACT5_MEDICAL_INFILTRATION = 42
    ACT5_ARCHIVE_FIND = 43
    ACT5_VIDEO_PROCEDURE = 44
    ACT5_MEETING_KREIN = 45
    ACT5_DAY6_TRANSITION = 46
    ACT6_MORNING = 47
    ACT6_CORRIDOR = 48
    ACT6_SECRET_ROOM_TRAITOR = 49
    ACT6_ROOF_CONFRONTATION = 50
    ACT6_CORRIDOR_RETURN = 51
    ACT6_INSOMNIA = 52
    ACT6_DAY7_TRANSITION = 53
    ACT7_MORNING = 54
    ACT7_CORRIDOR_MAX = 55
    ACT7_SECRET_PLANNING = 56
    ACT7_ABANDONED_TRAP = 57
    ACT7_SECRET_RETURN = 58
    ACT7_INSOMNIA = 59
    ACT7_DAY8_TRANSITION = 60
    ACT8_MORNING = 64
    ACT8_CORRIDOR_OBSERVE = 65
    ACT8_LIBRARY_ANALYSIS = 66
    ACT8_DORMITORY_CLUES = 67
    ACT8_PREPARATION = 68
    ACT8_DAY9_TRANSITION = 69
    ACT9_MORNING = 70
    ACT9_GYM_CONFRONTATION = 71
    ACT9_CONFESSION_CHOICE = 72
    ACT9_SECRET_MESSAGE = 73
    ACT9_INSOMNIA = 74
    ACT9_DAY10_TRANSITION = 75
    ACT10_MORNING = 76
    ACT10_CORRIDOR_BRANCH = 77
    ACT10_SECRET_PLANNING = 78
    ACT10_MEDICAL_PATH = 79
    ACT10_HART_LAB = 80
    ACT10_INSOMNIA = 81
    ACT10_DAY11_TRANSITION = 82
    ACT11_MORNING = 83
    ACT11_CORRIDOR_FOLLOW = 84
    ACT11_LIBRARY_ANALYSIS = 85
    ACT11_SAILAS_ROOM = 86
    ACT11_PREPARATION = 87
    ACT11_DAY12_TRANSITION = 88
    ACT12_REVELATION = 89
    ACT12_SILENCE_BEFORE_STORM = 90
    ACT12_HART_OFFICE = 91
    ACT12_CHASE = 92
    ACT12_LUCIA_CONFESSION = 93
    ACT12_SAILAS_MADNESS = 94
    ACT12_SAILAS_CHOICE = 95
    ACT12_ENDING = 96
    ACT12_FINAL_BLACK = 97
    PAUSE = 61


# ============================================================================
# ЗАГРУЗОЧНЫЙ ЭКРАН
# ============================================================================

class BootScreen:
    def __init__(self):
        self.timer = 0
        self.duration = 90

    def update(self):
        self.timer += 1
        return self.timer >= self.duration

    def draw(self, screen):
        screen.fill(BLACK)


# ============================================================================
# ЛОГОТИП
# ============================================================================

class LogoScreen:
    def __init__(self, path):
        self.logo = None
        if os.path.exists(path):
            try:
                self.logo = pygame.image.load(path)
            except:
                pass
        self.alpha = 0
        self.state = 0
        self.timer = 0
        self.complete = False

    def update(self):
        if self.complete:
            return
        if self.state == 0:
            self.alpha += 4
            if self.alpha >= 255:
                self.alpha = 255
                self.state = 1
        elif self.state == 1:
            self.timer += 1
            if self.timer >= 120:
                self.state = 2
        elif self.state == 2:
            self.alpha -= 4
            if self.alpha <= 0:
                self.alpha = 0
                self.complete = True

    def draw(self, screen):
        screen.fill(BLACK)
        if self.logo and self.alpha > 0:
            img = self.logo.copy()
            img.set_alpha(self.alpha)
            rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(img, rect)


# ============================================================================
# ДИСКЛЕЙМЕР
# ============================================================================

class DisclaimerScreen:
    def __init__(self, font):
        self.font = font
        self.text = """ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ

Все персонажи, события и локации, представленные в игре,
являются полностью вымышленными.

Любые совпадения с реальными людьми, живыми или умершими,
а также с реальными событиями и организациями — случайны.

В игре присутствуют сцены с упоминанием смерти
Рекомендуемый возраст — 16+.

Автор не поддерживает и не пропагандирует насилие.
Все действия персонажей продиктованы сюжетом.

© 2026 — Все права защищены"""
        self.lines = self.text.split('\n')

    def draw(self, screen):
        screen.fill(BLACK)
        visible = [l for l in self.lines if l.strip()]
        h = self.font.get_height()
        total_h = len(visible) * h
        y = (HEIGHT - total_h) // 2
        for i, line in enumerate(visible):
            surf = self.font.render(line, True, RED)
            rect = surf.get_rect(center=(WIDTH // 2, y + i * h))
            screen.blit(surf, rect)


# ============================================================================
# ГЛАВНОЕ МЕНЮ
# ============================================================================

class MainMenu:
    def __init__(self, font, bg):
        self.font = font
        self.bg = bg
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        cx = WIDTH // 2
        y = HEIGHT // 2 - 80
        texts = ["НОВАЯ ИГРА", "ВЫХОД"]
        for i, t in enumerate(texts):
            self.buttons.append({
                "text": t,
                "y": y + i * 70,
                "hover": False
            })

    def update(self, pos):
        for b in self.buttons:
            text_surf = self.font.render(b["text"], True, CHALK_WHITE)
            text_rect = text_surf.get_rect(center=(WIDTH // 2, b["y"]))
            b["hover"] = text_rect.collidepoint(pos)

    def click(self, pos):
        for b in self.buttons:
            text_surf = self.font.render(b["text"], True, CHALK_WHITE)
            text_rect = text_surf.get_rect(center=(WIDTH // 2, b["y"]))
            if text_rect.collidepoint(pos):
                return b["text"]
        return None

    def draw(self, screen):
        if self.bg:
            screen.blit(self.bg, (0, 0))
        else:
            screen.fill(BLACK)
        title_font = pygame.font.Font(None, 72)
        title = title_font.render("Субъект No 12", True, CHALK_WHITE)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title, title_rect)
        for b in self.buttons:
            color = CHALK_WHITE if b["hover"] else CHALK_GRAY
            text = self.font.render(b["text"], True, color)
            text_rect = text.get_rect(center=(WIDTH // 2, b["y"]))
            screen.blit(text, text_rect)
# ============================================================================
# СЦЕНА ПРОБУЖДЕНИЯ (НОЧЬ)
# ============================================================================

class WakeUpScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.fade_alpha = 0
        self.fade_active = True
        self.fade_in = True
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.text_timer = 0
        self.skip_fade = False

        self.texts = [
            ("Я просыпаюсь в холодном поту", WHITE),
            ("Сердце колотится", WHITE),
            ("В ушах всё ещё звучит его голос", WHITE),
            ("«Экзамен скоро начнётся»", LIGHT_BLUE)
        ]
        self.current_text = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path, skip_fade=False):
        self.load_background(bg_path)
        self.skip_fade = skip_fade
        if skip_fade:
            self.fade_active = False
            self.fade_alpha = 0
            self.show_text = True
            self.current_text = self.texts[0][0]
            self.current_color = self.texts[0][1]
            self.can_click = True
            self.text_timer = 0
        else:
            self.fade_alpha = 0
            self.fade_active = True
            self.fade_in = True
            self.show_text = False
            self.can_click = True
            self.text_timer = 0
        self.text_index = 0
        self.complete = False
        self.current_text = "" if not skip_fade else self.texts[0][0]
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_color = self.texts[self.text_index][1]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.complete = True
                return True
        return False

    def update(self):
        if self.skip_fade:
            return
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_in = False
            else:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.text_timer = 30
        else:
            if self.text_timer > 0:
                self.text_timer -= 1
                if self.text_timer == 0:
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_color = self.texts[0][1]
                    self.can_click = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.show_text and self.current_text:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            text_y = box_y + box_h // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))
        if not self.skip_fade and self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete


# ============================================================================
# СЦЕНА РАЗМЫШЛЕНИЙ
# ============================================================================

class ThoughtsScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.skip_animation = False

        self.texts = [
            ("Академия «Ксилон»", WHITE),
            ("Первый день семестра", WHITE),
            ("Я здесь уже второй год, но до сих пор чувствую себя чужим", WHITE),
            ("Сегодня всё начнётся", WHITE),
            ("Я ещё не знаю, что именно", WHITE),
            ("Но чувствую — что-то изменится", WHITE)
        ]
        self.current_text = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path, skip_animation=False):
        self.load_background(bg_path)
        self.skip_animation = skip_animation
        self.text_index = 0
        self.show_text = True
        self.can_click = True
        self.complete = False
        self.current_text = self.texts[0][0]
        self.current_color = self.texts[0][1]

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_color = self.texts[self.text_index][1]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.complete = True
                return True
        return False

    def update(self):
        pass

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.show_text and self.current_text:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            text_y = box_y + box_h // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# ПЕРЕХОД К ДНЮ 1
# ============================================================================

class Act1Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 30
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 1", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition_to_morning(self):
        return self.transition_complete


# ============================================================================
# СЦЕНА 1 - УТРО (ДЕНЬ 1)
# ============================================================================

class MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False

        self.texts = [
            ("Я открываю глаза", WHITE),
            ("Сердце всё ещё колотится после того сна", WHITE),
            ("Пустой зал, сотни парт", WHITE),
            ("Он", WHITE),
            ("Я встаю с кровати", WHITE),
            ("Голова тяжёлая — ночью почти не спал", WHITE),
            ("За окном — парк", WHITE),
            ("Академия встречает меня своей тишиной", WHITE),
            ("Сегодня первый день семестра, второй год в «Ксилон»", WHITE),
            ("И я до сих пор чувствую себя чужим", WHITE)
        ]
        self.current_text = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_color = self.texts[self.text_index][1]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_color = self.texts[0][1]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            text_y = box_y + box_h // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# СЦЕНА 2 - КОРИДОР (ДЕНЬ 1)
# ============================================================================

class CorridorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я выхожу из комнаты", WHITE),
            ("Коридор пуст", WHITE),
            ("Мои шаги отдаются эхом от стен", WHITE),
            ("Высокие потолки давят", WHITE),
            ("Всё здесь кажется чужим", WHITE),
            ("Первый урок — история", WHITE),
            ("Говорят, мистер Крейн — странный", WHITE),
            ("Но его лекции никто не пропускает", WHITE)
        ]
        self.current_text = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_color = self.texts[self.text_index][1]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_color = self.texts[0][1]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            text_y = box_y + box_h // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 3 - УРОК ИСТОРИИ (КРЕЙН)
# ============================================================================

class LessonScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.class_bg = None
        self.class_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.krein_portrait = None
        self.krein_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.krein_visible = False

        self.texts = [
            ("Академия «Ксилон» создана не для того, чтобы делать из вас гениев", "Крейн", OLD_PAPER),
            ("Она создана, чтобы отсеивать лишнее", "Крейн", OLD_PAPER),
            ("Его взгляд задерживается на мне", None, WHITE),
            ("Секунда, и уже смотрит дальше", None, WHITE),
            ("Но я чувствую — он заметил меня", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.class_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.class_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.class_bg_scaled = None
        else:
            self.class_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.krein_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.krein_portrait_scaled = None
        else:
            self.krein_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.krein_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.krein_visible = True
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.class_bg_scaled:
            self.screen.blit(self.class_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.krein_visible and self.krein_portrait_scaled:
            self.screen.blit(self.krein_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 4 - СТОЛОВАЯ (ПАДЕНИЕ ПОДНОСА)
# ============================================================================

class CanteenScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.canteen_bg = None
        self.canteen_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.max_portrait_offset_x = 0
        self.max_portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.crash_triggered = False
        self.waiting_for_crash = False
        self.text_timer = 0
        self.max_visible = False
        self.max_appeared = False
        self.crash_sound_played = False

        self.texts = [
            ("Обеденный перерыв", None, WHITE),
            ("Большой зал гудит голосами", None, WHITE),
            ("Я взял поднос и начал искать свободное место, пробираясь между столами", None, WHITE),
            ("Вдруг, чьё-то плечо задевает меня", None, WHITE),
            ("Поднос выскальзывает и тарелка летит на пол, тишина", None, WHITE),
            ("Кровь приливает к лицу, я смотрю в пол, лишь бы не видеть их взглядов", None, WHITE),
            ("Кто-то приседает рядом", None, WHITE),
            ("Крупный парень, тёмные волосы, усталые глаза", None, WHITE),
            ("Он помогает собрать осколки", None, WHITE),
            ("Я Макс", "Макс", MAX_COLOR),
            ("Спасибо", "Кайл", KAIL_COLOR),
            ("Здесь все смотрят, но никто не видит", "Макс", MAX_COLOR),
            ("Он встаёт и уходит, а я остаюсь стоять с пустым подносом", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.canteen_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.canteen_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.canteen_bg_scaled = None
        else:
            self.canteen_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.max_portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.max_portrait_offset_y = self.screen_height - portrait_height
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def start(self, bg_path, max_portrait_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.crash_triggered = False
        self.waiting_for_crash = False
        self.text_timer = 0
        self.max_visible = False
        self.max_appeared = False
        self.crash_sound_played = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click and not self.waiting_for_crash:
            self.can_click = False
            if self.text_index == 3 and not self.crash_triggered:
                self.crash_triggered = True
                self.waiting_for_crash = True
                self.text_timer = 30
                return False
            self.text_index += 1
            if self.text_index == 6 and not self.max_appeared:
                self.max_appeared = True
                self.max_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.waiting_for_crash:
            self.text_timer -= 1
            if self.text_timer <= 0:
                self.waiting_for_crash = False
                self.text_index += 1
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True

    def draw(self):
        if self.canteen_bg_scaled:
            self.screen.blit(self.canteen_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.max_visible and self.max_portrait_scaled:
            self.screen.blit(self.max_portrait_scaled, (self.max_portrait_offset_x, self.max_portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready
# ============================================================================
# СЦЕНА 5 - ПЕРВЫЙ ВЗГЛЯД ЛЮЦИИ
# ============================================================================

class LuciaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.lucia_visible = False

        self.texts = [
            ("После неудачного обеда я шел по коридору", None, WHITE),
            ("И тут я вижу ее", None, WHITE),
            ("Люция Вейн, президент школьного совета", None, WHITE),
            ("Она идёт навстречу, окружённая другими", None, WHITE),
            ("Но кажется, что она одна в целом мире", None, WHITE),
            ("Холодные глаза, светлые волосы", None, WHITE),
            ("Она проходит мимо, даже не посмотрев в мою сторону", None, WHITE),
            ("Как будто меня не существует", None, WHITE),
            ("Стоп..", None, WHITE),
            ("Почему я вообще на неё смотрю?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def start(self, bg_path, lucia_portrait_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.lucia_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 2 and not self.lucia_visible:
                self.lucia_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.lucia_visible and self.lucia_portrait_scaled:
            self.screen.blit(self.lucia_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 6 - ВЕЧЕР (ВОЗВРАЩЕНИЕ)
# ============================================================================

class EveningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.dorm_bg = None
        self.dorm_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.key_sound_played = False
        self.key_sound_requested = False

        self.texts = [
            ("После занятий я решил вернуться в комнату", None, WHITE),
            ("День прошёл как в тумане", None, WHITE),
            ("Крейн, Макс, Люция", None, WHITE),
            ("Слишком много новых лиц", None, WHITE),
            ("Я открываю дверь, темнота", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.dorm_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.dorm_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.dorm_bg_scaled = None
        else:
            self.dorm_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.key_sound_played = False
        self.key_sound_requested = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 4 and not self.key_sound_played:
                self.key_sound_requested = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.dorm_bg_scaled:
            self.screen.blit(self.dorm_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready

    def should_play_key_sound(self):
        if self.key_sound_requested:
            self.key_sound_requested = False
            self.key_sound_played = True
            return True
        return False


# ============================================================================
# СЦЕНА 7 - НОЧЬ (СТРАННЫЕ ЗВУКИ)
# ============================================================================

class NightScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.scratch_requested = False

        self.texts = [
            ("Поздняя ночь, Я уже почти заснул", None, WHITE),
            ("Но вдруг...", None, WHITE),
            ("Царапанье", None, WHITE),
            ("Из-за стены", None, WHITE),
            ("Может, показалось?", None, WHITE),
            ("Не показалось", None, WHITE),
            ("Я встал и подошел к двери", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.scratch_requested = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 1 or self.text_index == 2 or self.text_index == 4:
                self.scratch_requested = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready

    def should_play_scratch(self):
        if self.scratch_requested:
            self.scratch_requested = False
            return True
        return False


# ============================================================================
# СЦЕНА 8 - ПУСТОЙ КОРИДОР
# ============================================================================

class EmptyCorridorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я приоткрыл дверь", None, WHITE),
            ("Коридор пуст", None, WHITE),
            ("Только тусклый свет бра и длинные тени", None, WHITE),
            ("Но на полу — свежие следы обуви, они ведут к старому книжному шкафу в конце коридора", None, WHITE),
            ("Я подошел поближе", None, WHITE),
            ("Шкаф как шкаф", None, WHITE),
            ("Тёмное дерево", None, WHITE),
            ("Пыль", None, WHITE),
            ("Следы обрываются прямо перед ним", None, WHITE),
            ("Как будто тот, кто их оставил, прошёл сквозь стену", None, WHITE),
            ("Может, мне всё показалось?", None, WHITE),
            ("Я вернулся в комнату и запер дверь", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 9 - БЕССОННИЦА
# ============================================================================

class InsomniaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Не могу заснуть", None, WHITE),
            ("Лежу, смотрю в потолок", None, WHITE),
            ("Крейн и его взгляд: «Отсеивать лишнее»", None, OLD_PAPER),
            ("Люция, её холодные глаза, даже не посмотрела в мою сторону", None, WHITE),
            ("Макс - «Здесь все смотрят, но никто не видит»", None, MAX_COLOR),
            ("Так еще и странные звуки", None, WHITE),
            ("может завтра будет лучше?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 10 - ПЕРЕХОД К ДНЮ 2
# ============================================================================

class Day2Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 2", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# СЦЕНА 1 (ДЕНЬ 2) - УТРО (ПРОБУЖДЕНИЕ)
# ============================================================================

class Day2MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False

        self.texts = [
            ("Мне снова снился этот сон", None, WHITE),
            ("Тот же зал", None, WHITE),
            ("Та же улыбка", None, WHITE),
            ("Вчерашний день прошёл как в тумане", None, WHITE),
            ("Сегодня утром я снова проверил шкаф", None, WHITE),
            ("Ничего необычного", None, WHITE),
            ("Может, мне действительно показалось?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# СЦЕНА 2 (ДЕНЬ 2) - КОРИДОР (ПУТЬ НА ФАКУЛЬТАТИВ)
# ============================================================================

class Day2CorridorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я вышел из комнаты", None, WHITE),
            ("Коридор как обычно пуст", None, WHITE),
            ("Сегодня первый факультатив — «Психология выживания»", None, WHITE),
            ("Ведёт его доктор Эмма Харт", None, WHITE),
            ("Говорят, её занятия странные", None, WHITE),
            ("Но пропускать нельзя", None, WHITE),
            ("Пока я шел по коридору, в голове крутились вчерашние события", None, WHITE),
            ("Крейн сказал: «Академия создана, чтобы отсеивать лишнее»", None, OLD_PAPER),
            ("Что это значит?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 3 (ДЕНЬ 2) - ФАКУЛЬТАТИВ ДОКТОРА ХАРТ
# ============================================================================

class LectureScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.lecture_bg = None
        self.lecture_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.hart_portrait = None
        self.hart_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.hart_visible = False

        self.texts = [
            ("Кабинет психологии", None, WHITE),
            ("Белые стены", None, WHITE),
            ("Стулья расставлены полукругом", None, WHITE),
            ("Холодный свет флуоресцентных ламп", None, WHITE),
            ("Добро пожаловать на факультатив «Психология выживания»", "Харт", SILVER_GRAY),
            ("Академия «Ксилон» — это не просто школа", "Харт", SILVER_GRAY),
            ("Это испытание", "Харт", SILVER_GRAY),
            ("Те, кто не готов — отсеиваются", "Харт", SILVER_GRAY),
            ("Её взгляд скользит по аудитории", None, WHITE),
            ("Останавливается на мне", None, WHITE),
            ("На секунду дольше, чем на других", None, WHITE),
            ("Чистота разума — залог успеха", "Харт", SILVER_GRAY),
            ("Запомните это", "Харт", SILVER_GRAY),
            ("Её голос спокойный, слишком спокойный", None, WHITE),
            ("Как у гипнотизёра", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.lecture_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.lecture_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.lecture_bg_scaled = None
        else:
            self.lecture_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.hart_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.hart_portrait_scaled = None
        else:
            self.hart_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.hart_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 4 and not self.hart_visible:
                self.hart_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.lecture_bg_scaled:
            self.screen.blit(self.lecture_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.hart_visible and self.hart_portrait_scaled:
            self.screen.blit(self.hart_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 4 (ДЕНЬ 2) - КОРИДОР (ПОСЛЕ ФАКУЛЬТАТИВА)
# ============================================================================

class PostLectureScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Факультатив закончился", None, WHITE),
            ("Я вышел в коридор", None, WHITE),
            ("В голове — слова Харт", None, WHITE),
            ("«Чистота разума»", None, SILVER_GRAY),
            ("Что-то здесь не так", None, WHITE),
            ("Слишком много намёков", None, WHITE),
            ("Слишком много взглядов", None, WHITE),
            ("Крейн, Харт, Макс", None, WHITE),
            ("Все они что-то знают", None, WHITE),
            ("А я — нет", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 5 (ДЕНЬ 2) - ЗАКРЫТОЕ КРЫЛО
# ============================================================================

class ClosedWingScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.closed_bg = None
        self.closed_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.security_portrait = None
        self.security_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.security_visible = False

        self.texts = [
            ("Я решаю исследовать Академию", None, WHITE),
            ("На втором этаже — табличка «ВОСТОЧНОЕ КРЫЛО ЗАКРЫТО НА РЕМОНТ»", None, WHITE),
            ("Дверь приоткрыта", None, WHITE),
            ("Я заглянул внутрь", None, WHITE),
            ("Тёмный коридор", None, WHITE),
            ("Старые стены", None, WHITE),
            ("Пыль", None, WHITE),
            ("В воздухе — запах запустения", None, WHITE),
            ("Стоять", "Охранник", DARK_GRAY),
            ("Сюда нельзя", "Охранник", DARK_GRAY),
            ("Я обернулся и увидел охранника", None, WHITE),
            ("Проход закрыт, убирайся", "Охранник", DARK_GRAY),
            ("Я решил обойтись без лишних неприятностей и спокойно ушел", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.closed_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.closed_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.closed_bg_scaled = None
        else:
            self.closed_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.security_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.security_portrait_scaled = None
        else:
            self.security_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.security_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 8 and not self.security_visible:
                self.security_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.closed_bg_scaled:
            self.screen.blit(self.closed_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.security_visible and self.security_portrait_scaled:
            self.screen.blit(self.security_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 6 (ДЕНЬ 2) - БИБЛИОТЕКА
# ============================================================================

class LibraryScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.library_bg = None
        self.library_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.iina_visible = False

        self.texts = [
            ("Вечером я зашел в библиотеку", None, WHITE),
            ("Нужно подготовиться к завтрашним занятиям", None, WHITE),
            ("В зале тихо", None, WHITE),
            ("Только шелест страниц и тиканье часов", None, WHITE),
            ("В углу замечаю девушку", None, WHITE),
            ("Короткая стрижка, тёмный свитер", None, WHITE),
            ("В ушах наушники", None, WHITE),
            ("Перед ней — ноутбук", None, WHITE),
            ("Ийна", None, WHITE),
            ("Кажется, так её зовут", None, WHITE),
            ("Мы никогда не говорили", None, WHITE),
            ("Она подняла голову", None, WHITE),
            ("И наши взгляды встретились", None, WHITE),
            ("Она молча отвернулась", None, WHITE),
            ("Ее пальцы продолжили бегать по клавишам", None, WHITE),
            ("Странная", None, WHITE),
            ("Но что-то в ней есть", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.library_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.library_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.library_bg_scaled = None
        else:
            self.library_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.iina_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 4 and not self.iina_visible:
                self.iina_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.library_bg_scaled:
            self.screen.blit(self.library_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.iina_visible and self.iina_portrait_scaled:
            self.screen.blit(self.iina_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 7 (ДЕНЬ 2) - КОМНАТА ГГ (НОЧЬ)
# ============================================================================

class Day2NightScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Поздняя ночь", None, WHITE),
            ("Я сижу за столом", None, WHITE),
            ("Передо мной — учебники", None, WHITE),
            ("Но мысли не об учёбе", None, WHITE),
            ("Крейн, Харт", None, WHITE),
            ("Закрытое крыло", None, WHITE),
            ("Макс и его слова", None, WHITE),
            ("Что происходит в этой Академии?", None, WHITE),
            ("Что они скрывают?", None, WHITE),
            ("И почему мне кажется, что я — часть этого?", None, WHITE),
            ("Завтра новый день", None, WHITE),
            ("Может, я найду ответы", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 8 (ДЕНЬ 2) - ПЕРЕХОД К ДНЮ 3
# ============================================================================

class Day3Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 3", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# СЦЕНА 1 (ДЕНЬ 3) - УТРО (ПРОБУЖДЕНИЕ)
# ============================================================================

class Day3MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False

        self.texts = [
            ("Сегодня контрольная по математике", None, WHITE),
            ("Готовился всю ночь", None, WHITE),
            ("Но в голове — каша", None, WHITE),
            ("Формулы смешиваются с образами из сна зала и двойника", None, WHITE),
            ("Я встал с кровати, голова тяжёлая", None, WHITE),
            ("Если завалю контрольную — отчислят", None, WHITE),
            ("Харт сказала: «Те, кто не готов — отсеиваются»", None, SILVER_GRAY),
            ("Нельзя провалиться", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# СЦЕНА 2 (ДЕНЬ 3) - КОНТРОЛЬНАЯ ПО МАТЕМАТИКЕ
# ============================================================================

class MathExamScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.math_bg = None
        self.math_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Передо мной — лист с формулами", None, WHITE),
            ("Цифры плывут перед глазами", None, WHITE),
            ("Недосып даёт о себе знать", None, WHITE),
            ("Осталось 20 минут", "Преподаватель", TEACHER_COLOR),
            ("Я пытаюсь сосредоточиться", None, WHITE),
            ("Но в голове — пустота", None, WHITE),
            ("Я посмотрел на лист", None, WHITE),
            ("Строчки", None, WHITE),
            ("Ни одной знакомой формулы", None, WHITE),
            ("Я бросил ручку", None, WHITE),
            ("Всё, провалился", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.math_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.math_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.math_bg_scaled = None
        else:
            self.math_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.math_bg_scaled:
            self.screen.blit(self.math_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 3 (ДЕНЬ 3) - КОРИДОР (ВСТРЕЧА С САЙЛАСОМ)
# ============================================================================

class SailasCorridorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.sailas_visible = False

        self.texts = [
            ("Я выхожу из класса", None, WHITE),
            ("Контрольная провалена", None, WHITE),
            ("Что дальше?", None, WHITE),
            ("В конце коридора я заметил парня", None, WHITE),
            ("Худой, чёрные волосы, очки в тонкой оправе", None, WHITE),
            ("В руках — блокнот", None, WHITE),
            ("Он смотрит на меня", None, WHITE),
            ("Что-то записывает в блокнот", None, WHITE),
            ("Я отвел взгляд и начал уходить", None, WHITE),
            ("Но чувствую его взгляд на спине", None, WHITE),
            ("Сайлас Вонг", None, WHITE),
            ("Гений, сын технологического магната", None, WHITE),
            ("Никогда с ним не говорил", None, WHITE),
            ("Но почему он смотрит на меня?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.sailas_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 3 and not self.sailas_visible:
                self.sailas_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.sailas_visible and self.sailas_portrait_scaled:
            self.screen.blit(self.sailas_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 4 (ДЕНЬ 3) - БИБЛИОТЕКА (ВЕЧЕР)
# ============================================================================

class Day3LibraryScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.library_bg = None
        self.library_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.portrait_offset_x = 0
        self.portrait_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.iina_visible = False

        self.texts = [
            ("Вечером я снова зашел в библиотеку", None, WHITE),
            ("Нужно подготовиться к пересдаче", None, WHITE),
            ("Иначе — отчисление", None, WHITE),
            ("Я сел за стол и открыл учебник", None, WHITE),
            ("Формулы, теоремы, доказательства", None, WHITE),
            ("прошло: час, два, три", None, WHITE),
            ("Ничего не понимаю", None, WHITE),
            ("Отчаяние нарастает", None, WHITE),
            ("Ийна сидит в углу, как всегда", None, WHITE),
            ("Наушники, ноутбук", None, WHITE),
            ("Она иногда поднимает голову, смотрит на меня", None, WHITE),
            ("Потом снова утыкается в экран", None, WHITE),
            ("На столе появляется банка с холодным кофе", None, WHITE),
            ("Я не заказывал", None, WHITE),
            ("Я поднимаю голову, Ийна уже смотрит на меня", None, WHITE),
            ("В её взгляде — что-то странное", None, WHITE),
            ("Знает? О чём?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.library_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.library_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.library_bg_scaled = None
        else:
            self.library_bg_scaled = None

    def load_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
                self.portrait_offset_x = (self.screen_width - portrait_width) // 2
                self.portrait_offset_y = self.screen_height - portrait_height
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, portrait_path):
        self.load_background(bg_path)
        self.load_portrait(portrait_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.iina_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 8 and not self.iina_visible:
                self.iina_visible = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.library_bg_scaled:
            self.screen.blit(self.library_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.iina_visible and self.iina_portrait_scaled:
            self.screen.blit(self.iina_portrait_scaled, (self.portrait_offset_x, self.portrait_offset_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 5 (ДЕНЬ 3) - ПРОБУЖДЕНИЕ ДАРА
# ============================================================================

class AwakeningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corner_bg = None
        self.corner_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.glow_alpha = 0
        self.glow_active = False

        self.texts = [
            ("Глубокая ночь, библиотека пуста", None, WHITE),
            ("Передо мной — лист с формулами", None, WHITE),
            ("Глаза слипаются, веки тяжелеют", None, WHITE),
            ("Рука дрожит", None, WHITE),
            ("Я роняю холодный кофе", None, WHITE),
            ("Жидкость растекается по бумаге", None, WHITE),
            ("Чернила плывут", None, WHITE),
            ("Но формулы не исчезают", None, WHITE),
            ("Они начинают светиться", None, WHITE),
            ("Холодный голубой свет струится от страницы", None, WHITE),
            ("Формулы перестраиваются", None, WHITE),
            ("Складываются в структуру", None, WHITE),
            ("Я вижу скелет решения", None, WHITE),
            ("Каждая переменная становится прозрачной", None, WHITE),
            ("Я взял ручку и записал ответ", None, WHITE),
            ("Без усилий", None, WHITE),
            ("Без раздумий", None, WHITE),
            ("Я посмотрел на свои руки", None, WHITE),
            ("Ничего не изменилось", None, WHITE),
            ("Но мир стал чуть более плоским", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corner_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corner_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corner_bg_scaled = None
        else:
            self.corner_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 8:
                self.glow_active = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.glow_active:
            self.glow_alpha += 5
            if self.glow_alpha > 100:
                self.glow_alpha = 100

    def draw(self):
        if self.corner_bg_scaled:
            self.screen.blit(self.corner_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.glow_active and self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.screen_width, self.screen_height))
            glow_surface.fill(LIGHT_BLUE)
            glow_surface.set_alpha(self.glow_alpha)
            self.screen.blit(glow_surface, (0, 0))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 6 (ДЕНЬ 3) - КОМНАТА ГГ (НОЧЬ)
# ============================================================================

class Day3NightScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вернувшись в комнату", None, WHITE),
            ("Я снова посмотрел на свои руки", None, WHITE),
            ("Ничего не изменилось", None, WHITE),
            ("Но я чувствую, что-то изменилось внутри", None, WHITE),
            ("Мир стал другим", None, WHITE),
            ("Прозрачным", None, WHITE),
            ("Я не знаю, что это было", None, WHITE),
            ("Галлюцинация? Усталость?", None, WHITE),
            ("Или… что-то большее?", None, WHITE),
            ("Никому не скажу об этом", None, WHITE),
            ("Пока не разберусь сам", None, WHITE),
            ("Но завтра я проверю", None, WHITE),
            ("Решу ещё одну задачу", None, WHITE),
            ("И посмотрю, что произойдёт", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# СЦЕНА 7 (ДЕНЬ 3) - ПЕРЕХОД К ДНЮ 4
# ============================================================================

class Day4Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 4", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 4 - СЦЕНА 1: УТРО — ПРОВЕРКА ДАРА
# ============================================================================

class Day4MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.glow_alpha = 0
        self.glow_active = False
        self.transition_ready = False

        self.texts = [
            ("Ночью я не спал", None, WHITE),
            ("Думал о том, что случилось в библиотеке", None, WHITE),
            ("Светящиеся формулы и решение за секунду", None, WHITE),
            ("Это не галлюцинация", None, WHITE),
            ("Я достал учебник и открыл случайную страницу", None, WHITE),
            ("Смотрю на уравнение", None, WHITE),
            ("И вижу ответ", None, WHITE),
            ("Сразу", None, WHITE),
            ("Полностью", None, WHITE),
            ("Без усилий", None, WHITE),
            ("Формулы складываются в структуру", None, WHITE),
            ("Я не знаю, что это", None, WHITE),
            ("Но это реально", None, WHITE),
            ("Сегодня тест", None, WHITE),
            ("Я напишу его", None, WHITE),
            ("И посмотрю, что будет дальше", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 10:
                self.glow_active = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.glow_active:
            self.glow_alpha += 3
            if self.glow_alpha > 80:
                self.glow_alpha = 80

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.glow_active and self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.screen_width, self.screen_height))
            glow_surface.fill(LIGHT_BLUE)
            glow_surface.set_alpha(self.glow_alpha)
            self.screen.blit(glow_surface, (0, 0))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 4 - СЦЕНА 2: ТЕСТ ПО МАТЕМАТИКЕ
# ============================================================================

class Day4MathTestScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.math_bg = None
        self.math_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.glow_alpha = 0
        self.glow_active = False

        self.texts = [
            ("Передо мной — тест", None, WHITE),
            ("Пять задач", None, WHITE),
            ("Сложные", None, WHITE),
            ("Раньше я бы не решил ни одной", None, WHITE),
            ("Смотрю на первую задачу", None, WHITE),
            ("Формулы светятся, перестраиваются", None, WHITE),
            ("Ответ приходит сам", None, WHITE),
            ("Записываю ответ", None, WHITE),
            ("Задача за задачей", None, WHITE),
            ("Через 20 минут я закончил", None, WHITE),
            ("Я поднимаю голову", None, WHITE),
            ("Все ещё пишут", None, WHITE),
            ("Преподаватель смотрит на меня с удивлением", None, WHITE),
            ("Не говорит ничего", None, WHITE),
            ("Но я вижу", None, WHITE),
            ("Он что-то заметил", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.math_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.math_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.math_bg_scaled = None
        else:
            self.math_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 5:
                self.glow_active = True
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.glow_active:
            self.glow_alpha += 3
            if self.glow_alpha > 80:
                self.glow_alpha = 80

    def draw(self):
        if self.math_bg_scaled:
            self.screen.blit(self.math_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.glow_active and self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.screen_width, self.screen_height))
            glow_surface.fill(LIGHT_BLUE)
            glow_surface.set_alpha(self.glow_alpha)
            self.screen.blit(glow_surface, (0, 0))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 4 - СЦЕНА 3: КОРИДОР — РЕЗУЛЬТАТЫ И ПРЕДУПРЕЖДЕНИЕ
# ============================================================================

class Day4CorridorWarningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.sailas_visible = False
        self.max_visible = False
        self.sailas_shown = False
        self.max_shown = False

        self.texts = [
            ("После занятий объявили результаты", None, WHITE),
            ("У меня — 98%", None, WHITE),
            ("Лучший в классе", None, WHITE),
            ("Я вышел в коридор", None, WHITE),
            ("И почувствовал на себе взгляд", None, WHITE),
            ("Сайлас стоит у стены", None, WHITE),
            ("Смотрит в упор", None, WHITE),
            ("Что-то записывает в свой блокнот", None, WHITE),
            ("Я отвел взгляд", None, WHITE),
            ("И ускорил шаг", None, WHITE),
            ("Но мой путь преграждал Макс", None, WHITE),
            ("Сайлас заметил тебя", "Макс", MAX_COLOR),
            ("Он сказал, что твоё решение слишком чистое", "Макс", MAX_COLOR),
            ("Лицо Макса — спокойное, но в глазах — тревога", None, WHITE),
            ("Будь осторожен", "Макс", MAX_COLOR),
            ("Он захочет поговорить", "Макс", MAX_COLOR),
            ("Макс уходит", None, WHITE),
            ("А я остаюсь стоять", None, WHITE),
            ("Что значит «слишком чистое»?", None, WHITE),
            ("Что им нужно?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def start(self, bg_path, sailas_path, max_path):
        self.load_background(bg_path)
        self.load_sailas_portrait(sailas_path)
        self.load_max_portrait(max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.sailas_visible = False
        self.max_visible = False
        self.sailas_shown = False
        self.max_shown = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 5 and not self.sailas_shown:
                self.sailas_visible = True
                self.sailas_shown = True
            if self.text_index == 10:
                self.sailas_visible = False
            if self.text_index == 10 and not self.max_shown:
                self.max_visible = True
                self.max_shown = True
            if self.text_index == 16:
                self.max_visible = False
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.sailas_visible and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        if self.max_visible and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 4 - СЦЕНА 4: СТАРАЯ БИБЛИОТЕКА — ОЖИДАНИЕ
# ============================================================================

class Day4OldLibraryScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.old_library_bg = None
        self.old_library_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вечером я пришел в старую библиотеку", None, WHITE),
            ("Люция сказала прийти сюда в 22:00", None, WHITE),
            ("Не объяснила зачем", None, WHITE),
            ("Просто сказала: «Не опаздывай»", None, WHITE),
            ("Вокруг — пыльные стеллажи", None, WHITE),
            ("Запах старых книг", None, WHITE),
            ("Тишина", None, WHITE),
            ("Только мои шаги", None, WHITE),
            ("Что ей нужно? Почему я здесь?", None, WHITE),
            ("И почему я согласился?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.old_library_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.old_library_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.old_library_bg_scaled = None
        else:
            self.old_library_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.old_library_bg_scaled:
            self.screen.blit(self.old_library_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 4 - СЦЕНА 5: ТАЙНАЯ КОМНАТА — ПЕРВОЕ СОБРАНИЕ ГРУППЫ
# ============================================================================

class Day4SecretRoomScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Слышу щелчок", None, WHITE),
            ("Книжный шкаф отъезжает в сторону", None, WHITE),
            ("За ним — комната", None, WHITE),
            ("Карты на стенах", None, WHITE),
            ("Доска, исписанная именами и датами", None, WHITE),
            ("За круглым столом — четверо", None, WHITE),
            ("Ты проснулся", "Люция", YELLOW),
            ("Мы ждали", "Люция", YELLOW),
            ("Садись", "Люция", YELLOW),
            ("Я сел на свободный стул", None, WHITE),
            ("Смотрю на них", None, WHITE),
            ("Люция", None, WHITE),
            ("Макс", None, WHITE),
            ("Сайлас", None, WHITE),
            ("Ийна", None, WHITE),
            ("Все здесь", None, WHITE),
            ("То, что с тобой случилось в библиотеке — не галлюцинация", "Люция", YELLOW),
            ("Это дар", "Люция", YELLOW),
            ("Пробуждение", "Люция", YELLOW),
            ("Это пробуждённые", "Люция", YELLOW),
            ("Люция — эмпатия", None, WHITE),
            ("Видит желания, страхи, намерения людей", None, WHITE),
            ("Макс — детектор лжи", None, WHITE),
            ("Чувствует ложь, опасность, фальшь", None, WHITE),
            ("Сайлас — вычисление вероятностей", None, WHITE),
            ("Видит исход событий с точностью до процента", None, WHITE),
            ("Ийна — информационный шум", None, WHITE),
            ("Слышит данные, видит потоки сигналов, «читает» электронику", None, WHITE),
            ("Сайлас открывает блокнот и показывает мне", None, WHITE),
            ("На листе — список имён", None, WHITE),
            ("Восемь имён", None, WHITE),
            ("Четыре перечёркнуты", None, WHITE),
            ("Это пробуждённые", "Сайлас", LIGHT_CYAN),
            ("Те, кто был до тебя", "Сайлас", LIGHT_CYAN),
            ("Четверо живы", "Сайлас", LIGHT_CYAN),
            ("Четверо… исчезли", "Сайлас", LIGHT_CYAN),
            ("Я посмотрел на список", None, WHITE),
            ("Внизу — пустая строка", None, WHITE),
            ("И номер", None, WHITE),
            ("12", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, lucia_path, max_path, sailas_path, iina_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_max_portrait(max_path)
        self.load_sailas_portrait(sailas_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 6:
                self.current_portrait_visible = "lucia"
            if self.text_index == 9:
                self.current_portrait_visible = None
            if self.text_index == 11:
                self.current_portrait_visible = "lucia"
            if self.text_index == 12:
                self.current_portrait_visible = None
            if self.text_index == 12:
                self.current_portrait_visible = "max"
            if self.text_index == 13:
                self.current_portrait_visible = None
            if self.text_index == 13:
                self.current_portrait_visible = "sailas"
            if self.text_index == 14:
                self.current_portrait_visible = None
            if self.text_index == 14:
                self.current_portrait_visible = "iina"
            if self.text_index == 15:
                self.current_portrait_visible = None
            if self.text_index == 16:
                self.current_portrait_visible = "lucia"
            if self.text_index == 28:
                self.current_portrait_visible = None
            if self.text_index == 28:
                self.current_portrait_visible = "sailas"
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 4 - ПЕРЕХОД К ДНЮ 5
# ============================================================================

class Day5Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 5", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 5 - СЦЕНА 1: УТРО — ПРОБУЖДЕНИЕ
# ============================================================================

class Day5MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера я узнал, что не один", None, WHITE),
            ("Есть другие", None, WHITE),
            ("Такие же, как я", None, WHITE),
            ("Пробуждённые", None, WHITE),
            ("Люция сказала: «Мы — те, кто проснулся»", None, YELLOW),
            ("Макс, Сайлас, Ийна", None, WHITE),
            ("И я — двенадцатый", None, WHITE),
            ("Четверо до меня… исчезли", None, WHITE),
            ("Охотник", None, WHITE),
            ("Он убивает нас", None, WHITE),
            ("Сегодня первое задание", None, WHITE),
            ("Мы идём в медицинское крыло", None, WHITE),
            ("Нужны ответы", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 2: КОРИДОР — ПУТЬ НА ВСТРЕЧУ
# ============================================================================

class Day5CorridorRulesScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("В голове — вчерашние слова Люции", None, WHITE),
            ("«Кодекс Пробуждённого»", None, WHITE),
            ("Четыре правила", None, WHITE),
            ("Не используй дар публично", None, WHITE),
            ("Не доверяй учителям", None, WHITE),
            ("Не ищи Охотника в одиночку", None, WHITE),
            ("Если тебя нашли — ты не знаешь нас", None, WHITE),
            ("Звучит просто", None, WHITE),
            ("Но я чувствую — это вопрос жизни и смерти", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 3: ТАЙНАЯ КОМНАТА — ВТОРОЕ СОБРАНИЕ
# ============================================================================

class Day5SecretMeetingScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Все уже в сборе", None, WHITE),
            ("Люция стоит у доски", None, WHITE),
            ("На доске — схема медицинского крыла", None, WHITE),
            ("Сегодня ночью проникаем в медкрыло", "Люция", YELLOW),
            ("Ийна перехватила переписку", "Люция", YELLOW),
            ("Там что-то есть", "Люция", YELLOW),
            ("Вероятность успеха — 78%", "Сайлас", LIGHT_CYAN),
            ("Если не тупить", "Сайлас", LIGHT_CYAN),
            ("Макс молчит", None, WHITE),
            ("Смотрит на карту", None, WHITE),
            ("Ийна не отрывается от ноутбука", None, WHITE),
            ("Твоя задача — найти скрытые системы", "Люция", YELLOW),
            ("Твой дар видит структуру", "Люция", YELLOW),
            ("Ты найдёшь то, чего мы не видим", "Люция", YELLOW),
            ("Я киваю", None, WHITE),
            ("Внутри — страх", None, WHITE),
            ("Но и азарт", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, lucia_path, max_path, sailas_path, iina_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_max_portrait(max_path)
        self.load_sailas_portrait(sailas_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 3:
                self.current_portrait_visible = "lucia"
            if self.text_index == 6:
                self.current_portrait_visible = None
                self.current_portrait_visible = "sailas"
            if self.text_index == 8:
                self.current_portrait_visible = None
            if self.text_index == 11:
                self.current_portrait_visible = "lucia"
            if self.text_index == 14:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 4: МЕДИЦИНСКОЕ КРЫЛО — ПРОНИКНОВЕНИЕ
# ============================================================================

class Day5MedicalInfiltrationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.medical_bg = None
        self.medical_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Ночь", None, WHITE),
            ("Медицинское крыло", None, WHITE),
            ("Коридор пуст", None, WHITE),
            ("Только тусклый свет ламп", None, WHITE),
            ("И тишина", None, WHITE),
            ("Давящая", None, WHITE),
            ("Всё чисто", "Макс", MAX_COLOR),
            ("Опасности нет", "Макс", MAX_COLOR),
            ("Ийна отключает камеры", None, WHITE),
            ("Пальцы бегают по клавишам", None, WHITE),
            ("Экран ноутбука светится зелёным", None, WHITE),
            ("Система слежения отключена", "Ийна", GREEN),
            ("У вас 15 минут", "Ийна", GREEN),
            ("Мы идём по коридору", None, WHITE),
            ("Сердце колотится", None, WHITE),
            ("Но я чувствую — мы близки", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.medical_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.medical_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.medical_bg_scaled = None
        else:
            self.medical_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, max_path, iina_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 6:
                self.current_portrait_visible = "max"
            if self.text_index == 8:
                self.current_portrait_visible = None
            if self.text_index == 11:
                self.current_portrait_visible = "iina"
            if self.text_index == 13:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.medical_bg_scaled:
            self.screen.blit(self.medical_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 5: АРХИВ — НАХОДКА
# ============================================================================

class Day5ArchiveFindScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.archive_bg = None
        self.archive_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_portrait_visible = None

        self.texts = [
            ("Архив", None, WHITE),
            ("Металлические шкафы", None, WHITE),
            ("Папки с делами", None, WHITE),
            ("Пыль", None, WHITE),
            ("Холодный свет ламп", None, WHITE),
            ("Я закрыл глаза", None, WHITE),
            ("Использую дар", None, WHITE),
            ("Вижу структуру комнаты", None, WHITE),
            ("Стены, бетон, арматура", None, WHITE),
            ("И пустота", None, WHITE),
            ("За третьим шкафом", None, WHITE),
            ("Я открываю глаза и указываю на стену", None, WHITE),
            ("Здесь сейф", "Кайл", KAIL_COLOR),
            ("Макс подходит", None, WHITE),
            ("Взламывает замок", None, WHITE),
            ("Щелчок", None, WHITE),
            ("Дверца открылась", None, WHITE),
            ("Внутри лежит флешка", None, WHITE),
            ("Ийна, проверь", "Люция", YELLOW),
            ("Ийна вставляет флешку в ноутбук", None, WHITE),
            ("Экран мигает", None, WHITE),
            ("Начинается видео", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.archive_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.archive_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.archive_bg_scaled = None
        else:
            self.archive_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def start(self, bg_path, lucia_path, max_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_max_portrait(max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 6:
                self.glow_active = True
            if self.text_index == 11:
                self.glow_active = False
            if self.text_index == 18:
                self.current_portrait_visible = "lucia"
            if self.text_index == 19:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.glow_active:
            self.glow_alpha += 5
            if self.glow_alpha > 100:
                self.glow_alpha = 100

    def draw(self):
        if self.archive_bg_scaled:
            self.screen.blit(self.archive_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.glow_active and self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.screen_width, self.screen_height))
            glow_surface.fill(LIGHT_BLUE)
            glow_surface.set_alpha(self.glow_alpha)
            self.screen.blit(glow_surface, (0, 0))
        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 6: ВИДЕО — ПРОЦЕДУРА СТИРАНИЯ
# ============================================================================

class Day5VideoProcedureScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.archive_bg = None
        self.archive_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("На экране — доктор Харт", None, WHITE),
            ("Рядом — парень", None, WHITE),
            ("Наш ровесник", None, WHITE),
            ("К его голове подсоединены провода", None, WHITE),
            ("Субъект No 4", "Харт", SILVER_GRAY),
            ("Твои показатели превышают норму", "Харт", SILVER_GRAY),
            ("Мы должны провести коррекцию", "Харт", SILVER_GRAY),
            ("Пожалуйста, не стирайте меня", "Парень", WHITE),
            ("Я больше не буду использовать дар", "Парень", WHITE),
            ("Я всё отдам, просто оставьте меня…", "Парень", WHITE),
            ("Харт нажимает кнопку", None, WHITE),
            ("Парень кричит", None, WHITE),
            ("Потом замолкает", None, WHITE),
            ("Глаза пустые", None, WHITE),
            ("Запись для отчёта", "Харт", SILVER_GRAY),
            ("Процедура успешна", "Харт", SILVER_GRAY),
            ("Субъект больше не представляет угрозы", "Харт", SILVER_GRAY),
            ("Тишина", None, WHITE),
            ("Никто не говорит", None, WHITE),
            ("Это не исключение", "Сайлас", LIGHT_CYAN),
            ("Это пыточная", "Сайлас", LIGHT_CYAN),
            ("Я смотрю на экран", None, WHITE),
            ("На пустые глаза парня", None, WHITE),
            ("И понимаю — мы не просто боремся за правду", None, WHITE),
            ("Мы боремся за жизнь", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.archive_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.archive_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.archive_bg_scaled = None
        else:
            self.archive_bg_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def start(self, bg_path, sailas_path):
        self.load_background(bg_path)
        self.load_sailas_portrait(sailas_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 19:
                self.current_portrait_visible = "sailas"
            if self.text_index == 21:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.archive_bg_scaled:
            self.screen.blit(self.archive_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - СЦЕНА 7: ВСТРЕЧА С КРЕЙНОМ
# ============================================================================

class Day5MeetingKreinScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.krein_portrait = None
        self.krein_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Мы вышли из медкрыла", None, WHITE),
            ("В конце коридора стоит фигура", None, WHITE),
            ("Все замерли", None, WHITE),
            ("Крейн", None, WHITE),
            ("Он смотрит на нас", None, WHITE),
            ("Без удивления", None, WHITE),
            ("Я знал, что вы придёте", "Крейн", OLD_PAPER),
            ("Макс сжимает кулаки", None, WHITE),
            ("Люция делает шаг вперёд", None, WHITE),
            ("Но вы ошибаетесь", "Крейн", OLD_PAPER),
            ("Харт — не охотник", "Крейн", OLD_PAPER),
            ("Она жертва, как и вы", "Крейн", OLD_PAPER),
            ("Охотник — тот, кого вы меньше всего подозреваете", "Крейн", OLD_PAPER),
            ("Он поворачивается и уходит", None, WHITE),
            ("Тени поглощают его фигуру", None, WHITE),
            ("Не верьте ему", "Люция", YELLOW),
            ("Он играет с нами", "Люция", YELLOW),
            ("Но я смотрю вслед Крейну", None, WHITE),
            ("Что, если он говорит правду?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_krein_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.krein_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.krein_portrait_scaled = None
        else:
            self.krein_portrait_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def start(self, bg_path, krein_path, lucia_path):
        self.load_background(bg_path)
        self.load_krein_portrait(krein_path)
        self.load_lucia_portrait(lucia_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 3:
                self.current_portrait_visible = "krein"
            if self.text_index == 13:
                self.current_portrait_visible = None
            if self.text_index == 15:
                self.current_portrait_visible = "lucia"
            if self.text_index == 17:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "krein" and self.krein_portrait_scaled:
            portrait_x = (self.screen_width - self.krein_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.krein_portrait_scaled.get_height()
            self.screen.blit(self.krein_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 5 - ПЕРЕХОД К ДНЮ 6
# ============================================================================

class Day6Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 6", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 6 - СЦЕНА 1: УТРО — ПРОБУЖДЕНИЕ
# ============================================================================

class Day6MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера мы нашли видео", None, WHITE),
            ("После того как мы его просмотрели", None, WHITE),
            ("Я не мог спать", None, WHITE),
            ("Всю ночь перед глазами — пустые глаза того парня", None, WHITE),
            ("Харт нажимает кнопку", None, WHITE),
            ("Он кричит", None, WHITE),
            ("А она смотрит", None, WHITE),
            ("Спокойно", None, WHITE),
            ("Как на экспериментальную крысу", None, WHITE),
            ("Крейн сказал: «Харт — не охотник»", None, OLD_PAPER),
            ("Тогда кто?", None, WHITE),
            ("Кто-то из своих?", None, WHITE),
            ("Сегодня собрание", None, WHITE),
            ("Нужны ответы", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - СЦЕНА 2: КОРИДОР — ПУТЬ НА ВСТРЕЧУ
# ============================================================================

class Day6CorridorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я иду по коридору", None, WHITE),
            ("Вокруг — обычная жизнь", None, WHITE),
            ("Ученики смеются", None, WHITE),
            ("Кто-то спешит на пару", None, WHITE),
            ("А у меня в голове — крик того парня", None, WHITE),
            ("Они не знают", None, WHITE),
            ("Не знают, что происходит за этими стенами", None, WHITE),
            ("Что Академия — не школа", None, WHITE),
            ("А лаборатория", None, WHITE),
            ("Я ускорил шаг", None, WHITE),
            ("Нужно в тайную комнату", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - СЦЕНА 3: ТАЙНАЯ КОМНАТА — ПРЕДАТЕЛЬ
# ============================================================================

class Day6SecretRoomTraitorScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.lucia_pain_portrait = None
        self.lucia_pain_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Все уже здесь", None, WHITE),
            ("Напряжение висит в воздухе", None, WHITE),
            ("Сайлас сидит с блокнотом", None, WHITE),
            ("Стучит ручкой по столу", None, WHITE),
            ("Я просчитал вероятности", "Сайлас", LIGHT_CYAN),
            ("Вероятность того, что в группе есть предатель — 43%", "Сайлас", LIGHT_CYAN),
            ("Тишина", None, WHITE),
            ("Все смотрят друг на друга", None, WHITE),
            ("Макс отводит взгляд", None, WHITE),
            ("Я замечаю это", None, WHITE),
            ("Ты не можешь это знать", "Люция", YELLOW),
            ("Это просто паранойя", "Люция", YELLOW),
            ("Это математика", "Сайлас", LIGHT_CYAN),
            ("И цифры не врут", "Сайлас", LIGHT_CYAN),
            ("Ийна поднимает голову от ноутбука", None, WHITE),
            ("Лицо бледное", None, WHITE),
            ("Я кое-что нашла", "Ийна", GREEN),
            ("Она разворачивает экран", None, WHITE),
            ("Аудиозапись", None, WHITE),
            ("Голос Люции", None, WHITE),
            ("И голос Харт", None, WHITE),
            ("Вы уверены, что он готов?", "Харт", SILVER_GRAY),
            ("Да", "Люция", YELLOW),
            ("Он нам нужен", "Люция", YELLOW),
            ("Все смотрят на Люцию", None, WHITE),
            ("Макс сжимает кулаки", None, WHITE),
            ("Сайлас застыл", None, WHITE),
            ("Это не то, что вы думаете", "Люция", YELLOW),
            ("Я… я могу объяснить", "Люция", YELLOW),
            ("Она смотрит на меня", None, WHITE),
            ("В её глазах — страх", None, WHITE),
            ("Впервые", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_lucia_pain_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_pain_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_pain_portrait_scaled = None
        else:
            self.lucia_pain_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, sailas_path, lucia_path, lucia_pain_path, iina_path):
        self.load_background(bg_path)
        self.load_sailas_portrait(sailas_path)
        self.load_lucia_portrait(lucia_path)
        self.load_lucia_pain_portrait(lucia_pain_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 4:
                self.current_portrait_visible = "sailas"
            if self.text_index == 6:
                self.current_portrait_visible = None
            if self.text_index == 10:
                self.current_portrait_visible = "lucia"
            if self.text_index == 12:
                self.current_portrait_visible = None
                self.current_portrait_visible = "sailas"
            if self.text_index == 14:
                self.current_portrait_visible = None
            if self.text_index == 16:
                self.current_portrait_visible = "iina"
            if self.text_index == 17:
                self.current_portrait_visible = None
            if self.text_index == 27:
                self.current_portrait_visible = "lucia_pain"
            if self.text_index == 29:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia_pain" and self.lucia_pain_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_pain_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_pain_portrait_scaled.get_height()
            self.screen.blit(self.lucia_pain_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - СЦЕНА 4: КРЫША — КОНФРОНТАЦИЯ С ЛЮЦИЕЙ
# ============================================================================

class Day6RoofConfrontationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.roof_bg = None
        self.roof_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_pain_portrait = None
        self.lucia_pain_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("После собрания я нахожу Люцию на крыше", None, WHITE),
            ("Она стоит у края, смотрит вдаль", None, WHITE),
            ("Ветер развевает её волосы", None, WHITE),
            ("Ты использовала меня?", "Кайл", KAIL_COLOR),
            ("Она медленно поворачивается", None, WHITE),
            ("Да, я сотрудничала с Харт", "Люция", YELLOW),
            ("Но это было до того, как я узнала правду", "Люция", YELLOW),
            ("Я думала, что спасаю нас", "Люция", YELLOW),
            ("Что если я буду давать ей имена — она оставит остальных в покое", "Люция", YELLOW),
            ("Я не знала, что их убивают", "Люция", YELLOW),
            ("Я думала… их просто исключат", "Люция", YELLOW),
            ("Я смотрю на неё", None, WHITE),
            ("Хочу злиться", None, WHITE),
            ("Но не могу", None, WHITE),
            ("Почему ты не сказала?", "Кайл", KAIL_COLOR),
            ("Потому что я боялась", "Люция", YELLOW),
            ("Боялась, что вы посмотрите на меня так же, как смотрят все", "Люция", YELLOW),
            ("Как на монстра", "Люция", YELLOW),
            ("Она отворачивается", None, WHITE),
            ("Её голос дрожит", None, WHITE),
            ("Я не прошу прощения", "Люция", YELLOW),
            ("Я просто хочу, чтобы ты знал — всё, что между нами было… это не ложь", "Люция", YELLOW),
            ("Я молчу", None, WHITE),
            ("Что я могу сказать", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.roof_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.roof_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.roof_bg_scaled = None
        else:
            self.roof_bg_scaled = None

    def load_lucia_pain_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_pain_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_pain_portrait_scaled = None
        else:
            self.lucia_pain_portrait_scaled = None

    def start(self, bg_path, lucia_pain_path):
        self.load_background(bg_path)
        self.load_lucia_pain_portrait(lucia_pain_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 5:
                self.current_portrait_visible = "lucia_pain"
            if self.text_index == 23:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.roof_bg_scaled:
            self.screen.blit(self.roof_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "lucia_pain" and self.lucia_pain_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_pain_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_pain_portrait_scaled.get_height()
            self.screen.blit(self.lucia_pain_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - СЦЕНА 5: КОРИДОР — ВОЗВРАЩЕНИЕ
# ============================================================================

class Day6CorridorReturnScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Спускаюсь с крыши", None, WHITE),
            ("В голове — её слова", None, WHITE),
            ("«Я думала, что спасаю нас»", None, YELLOW),
            ("Она ошибалась", None, WHITE),
            ("Но разве я поступил бы иначе?", None, WHITE),
            ("Разве я не хотел бы защитить своих любой ценой?", None, WHITE),
            ("Не знаю", None, WHITE),
            ("Слишком много вопросов", None, WHITE),
            ("Слишком мало ответов", None, WHITE),
            ("И теперь — предатель среди нас", None, WHITE),
            ("Кто именно..", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - СЦЕНА 6: КОМНАТА ГГ — БЕССОННИЦА
# ============================================================================

class Day6InsomniaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я сижу за столом", None, WHITE),
            ("Передо мной — блокнот", None, WHITE),
            ("Список имён", None, WHITE),
            ("Четыре перечёркнуты", None, WHITE),
            ("Субъект No 1, Субъект No 4, Субъект No 7, Субъект No 11", None, WHITE),
            ("Они мертвы", None, WHITE),
            ("А мы — следующие.", None, WHITE),
            ("Крейн сказал: «Охотник — тот, кого вы меньше всего подозреваете»", None, OLD_PAPER),
            ("Сайлас сказал: «Вероятность предательства — 43%»", None, LIGHT_CYAN),
            ("Люция сказала: «Я не знала»", None, YELLOW),
            ("Кому верить?", None, WHITE),
            ("Никому", None, WHITE),
            ("Завтра новый день", None, WHITE),
            ("Я должен узнать правду", None, WHITE),
            ("Иначе мы все умрём", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 6 - ПЕРЕХОД К ДНЮ 7
# ============================================================================

class Day7Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 7", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 7 - СЦЕНА 1: УТРО — РЕШИМОСТЬ
# ============================================================================

class Day7MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера Люция призналась", None, WHITE),
            ("Она работала на Харт", None, WHITE),
            ("Думала, что спасает нас", None, WHITE),
            ("А они убивали таких как мы", None, WHITE),
            ("Я не знаю, могу ли я ей верить", None, WHITE),
            ("Но сейчас не до этого", None, WHITE),
            ("Слишком много вопросов", None, WHITE),
            ("И слишком мало времени", None, WHITE),
            ("Сайлас сказал — в группе предатель", None, WHITE),
            ("Кто-то сливает информацию Охотнику", None, WHITE),
            ("Сегодня мы идём по следу", None, WHITE),
            ("Я должен быть готов ко всему", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - СЦЕНА 2: КОРИДОР — ВСТРЕЧА С МАКСОМ
# ============================================================================

class Day7CorridorMaxScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.max_visible = False

        self.texts = [
            ("Я вышел из комнаты", None, WHITE),
            ("В коридоре — Макс", None, WHITE),
            ("Стоит у окна", None, WHITE),
            ("Смотрит в никуда", None, WHITE),
            ("Ты тоже не спал?", "Макс", MAX_COLOR),
            ("Нет", "Кайл", KAIL_COLOR),
            ("Слишком много мыслей", "Кайл", KAIL_COLOR),
            ("В глазах Макса — усталость", None, WHITE),
            ("И что-то ещё", None, WHITE),
            ("Что-то, чего я раньше не замечал", None, WHITE),
            ("Сегодня мы идём по адресу", "Макс", MAX_COLOR),
            ("Ийна нашла координаты", "Макс", MAX_COLOR),
            ("Сказала, что там база Охотника", "Макс", MAX_COLOR),
            ("Будь осторожен, я чувствую… что-то не так", "Макс", MAX_COLOR),
            ("Он уходит", None, WHITE),
            ("А я остаюсь стоять", None, WHITE),
            ("Что значит «что-то не так»?", None, WHITE),
            ("Он знает больше, чем говорит?", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def start(self, bg_path, max_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.max_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 4 and not self.max_visible:
                self.max_visible = True
            if self.text_index == 14:
                self.max_visible = False
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.max_visible and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - СЦЕНА 3: ТАЙНАЯ КОМНАТА — ПЛАНИРОВАНИЕ
# ============================================================================

class Day7SecretPlanningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Все в сборе", None, WHITE),
            ("Люция стоит у карты", None, WHITE),
            ("Показывает точку на окраине города", None, WHITE),
            ("Ийна перехватила координаты", "Люция", YELLOW),
            ("Здесь может быть база Охотника", "Люция", YELLOW),
            ("Сегодня идём туда", "Люция", YELLOW),
            ("Вероятность успеха — 65%", "Сайлас", LIGHT_CYAN),
            ("Если ничего не пойдёт не так", "Сайлас", LIGHT_CYAN),
            ("Я проверю периметр", "Макс", MAX_COLOR),
            ("Если там опасно — мы уходим", "Макс", MAX_COLOR),
            ("Ийна молчит", None, WHITE),
            ("Пальцы бегают по клавишам", None, WHITE),
            ("Она не поднимает головы", None, WHITE),
            ("Сбор в 20:00", "Люция", YELLOW),
            ("У заднего входа", "Люция", YELLOW),
            ("Не опаздывайте", "Люция", YELLOW),
            ("Я смотрю на Макса", None, WHITE),
            ("Он отводит взгляд", None, WHITE),
            ("Что-то не так", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, lucia_path, sailas_path, max_path, iina_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_sailas_portrait(sailas_path)
        self.load_max_portrait(max_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index == 3:
                self.current_portrait_visible = "lucia"
            if self.text_index == 6:
                self.current_portrait_visible = None
                self.current_portrait_visible = "sailas"
            if self.text_index == 8:
                self.current_portrait_visible = None
                self.current_portrait_visible = "max"
            if self.text_index == 10:
                self.current_portrait_visible = None
            if self.text_index == 13:
                self.current_portrait_visible = "lucia"
            if self.text_index == 16:
                self.current_portrait_visible = None
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - СЦЕНА 4: ЗАБРОШЕННОЕ КРЫЛО — ЗАПАДНЯ
# ============================================================================

class Day7AbandonedTrapScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.abandoned_bg = None
        self.abandoned_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("20:00", None, WHITE),
            ("Мы у заброшенного здания на окраине", None, WHITE),
            ("Стены обшарпаны", None, WHITE),
            ("Окна выбиты", None, WHITE),
            ("Внутри — темнота", None, WHITE),
            ("Всё чисто", "Макс", MAX_COLOR),
            ("Опасности нет", "Макс", MAX_COLOR),
            ("Идём", "Макс", MAX_COLOR),
            ("Мы заходим внутрь", None, WHITE),
            ("Тишина", None, WHITE),
            ("Только наши шаги", None, WHITE),
            ("И скрип половиц", None, WHITE),
            ("Мы поднялись на второй этаж", None, WHITE),
            ("Впереди дверь", None, WHITE),
            ("За ней — свет", None, WHITE),
            ("Открывай", "Люция", YELLOW),
            ("Макс толкает дверь", None, WHITE),
            ("Внутри — пустота", None, WHITE),
            ("Ничего", None, WHITE),
            ("Ни оборудования", None, WHITE),
            ("Ни бумаг", None, WHITE),
            ("Ловушка", "Сайлас", LIGHT_CYAN),
            ("Сзади доносится звук шагов", None, WHITE),
            ("Много шагов", None, WHITE),
            ("Уходим!", "Кайл", KAIL_COLOR),
            ("Бежим вниз", None, WHITE),
            ("Сердце колотится", None, WHITE),
            ("Кто-то предал нас", None, WHITE),
            ("Кто-то знал, что мы придём", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.abandoned_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.abandoned_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.abandoned_bg_scaled = None
        else:
            self.abandoned_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def start(self, bg_path, max_path, lucia_path, sailas_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.load_lucia_portrait(lucia_path)
        self.load_sailas_portrait(sailas_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index == 5:
                self.current_portrait_visible = "max"
            if self.text_index == 8:
                self.current_portrait_visible = None
            if self.text_index == 15:
                self.current_portrait_visible = "lucia"
            if self.text_index == 16:
                self.current_portrait_visible = None
            if self.text_index == 21:
                self.current_portrait_visible = "sailas"
            if self.text_index == 22:
                self.current_portrait_visible = None

            if self.text_index == 12:
                if os.path.exists("assets/backgrounds/ZKVnut.png"):
                    try:
                        original = pygame.image.load("assets/backgrounds/ZKVnut.png")
                        orig_width = original.get_width()
                        orig_height = original.get_height()
                        scale_x = self.screen_width / orig_width
                        scale_y = self.screen_height / orig_height
                        scale = max(scale_x, scale_y)
                        new_width = int(orig_width * scale)
                        new_height = int(orig_height * scale)
                        self.abandoned_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                        self.bg_offset_x = (new_width - self.screen_width) // 2
                        self.bg_offset_y = (new_height - self.screen_height) // 2
                    except:
                        pass

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.abandoned_bg_scaled:
            self.screen.blit(self.abandoned_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - СЦЕНА 5: ТАЙНАЯ КОМНАТА — ВОЗВРАЩЕНИЕ
# ============================================================================

class Day7SecretReturnScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.lucia_gnev_portrait = None
        self.lucia_gnev_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.sailas_ras_portrait = None
        self.sailas_ras_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Мы вернулись в тайную комнату", None, WHITE),
            ("Все тяжело дышат", None, WHITE),
            ("Тишина", None, WHITE),
            ("Все молчат", None, WHITE),
            ("Кто-то слил информацию", "Люция", YELLOW),
            ("Охотник знал, что мы придём", "Люция", YELLOW),
            ("Она смотрит на каждого по очереди", None, WHITE),
            ("Макс отводит взгляд", None, WHITE),
            ("Сайлас спокоен — слишком спокоен", None, WHITE),
            ("Ийна сжимает ноутбук", None, WHITE),
            ("Вероятность того, что предатель среди нас, теперь — 89%", "Сайлас", LIGHT_CYAN),
            ("Я смотрю на них", None, WHITE),
            ("Все под подозрением", None, WHITE),
            ("Даже Люция", None, WHITE),
            ("Даже Макс", None, WHITE),
            ("Мы найдём его", "Кайл", KAIL_COLOR),
            ("И тогда он ответит", "Кайл", KAIL_COLOR)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_lucia_gnev_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_gnev_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_gnev_portrait_scaled = None
        else:
            self.lucia_gnev_portrait_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_sailas_ras_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_ras_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_ras_portrait_scaled = None
        else:
            self.sailas_ras_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def start(self, bg_path, lucia_path, lucia_gnev_path, max_path, sailas_path, sailas_ras_path, iina_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_lucia_gnev_portrait(lucia_gnev_path)
        self.load_max_portrait(max_path)
        self.load_sailas_portrait(sailas_path)
        self.load_sailas_ras_portrait(sailas_ras_path)
        self.load_iina_portrait(iina_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index == 4:
                self.current_portrait_visible = "lucia_gnev"
            if self.text_index == 6:
                self.current_portrait_visible = None
            if self.text_index == 7:
                self.current_portrait_visible = "max"
            if self.text_index == 8:
                self.current_portrait_visible = None
            if self.text_index == 8:
                self.current_portrait_visible = "sailas"
            if self.text_index == 9:
                self.current_portrait_visible = None
            if self.text_index == 9:
                self.current_portrait_visible = "iina"
            if self.text_index == 10:
                self.current_portrait_visible = None
            if self.text_index == 10:
                self.current_portrait_visible = "sailas_ras"
            if self.text_index == 11:
                self.current_portrait_visible = None

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "lucia_gnev" and self.lucia_gnev_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_gnev_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_gnev_portrait_scaled.get_height()
            self.screen.blit(self.lucia_gnev_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas_ras" and self.sailas_ras_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_ras_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_ras_portrait_scaled.get_height()
            self.screen.blit(self.sailas_ras_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - СЦЕНА 6: КОМНАТА ГГ — БЕССОННИЦА
# ============================================================================

class Day7InsomniaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я сижу за столом", None, WHITE),
            ("Передо мной — список имён", None, WHITE),
            ("Четыре перечёркнуты", None, WHITE),
            ("Остальные — вопрос времени", None, WHITE),
            ("Макс сказал «всё чисто»", None, MAX_COLOR),
            ("Мы попали в ловушку", None, WHITE),
            ("Он ошибся? Или… нет?", None, WHITE),
            ("Сайлас слишком спокоен", None, WHITE),
            ("Слишком быстро считает вероятности", None, WHITE),
            ("Он знает больше, чем говорит?", None, WHITE),
            ("Люция уже однажды солгала", None, WHITE),
            ("Может, она всё ещё работает на Харт?", None, WHITE),
            ("Ийна", None, WHITE),
            ("Тихая", None, WHITE),
            ("Незаметная", None, WHITE),
            ("У неё доступ ко всей информации", None, WHITE),
            ("Она могла всё подстроить", None, WHITE),
            ("Кто из них?", None, WHITE),
            ("Или… все?", None, WHITE),
            ("Завтра я начну расследование", None, WHITE),
            ("И узнаю правду", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 7 - ПЕРЕХОД К ДНЮ 8
# ============================================================================

class Day8Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 8", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 8 - СЦЕНА 1: УТРО — НАЧАЛО РАССЛЕДОВАНИЯ
# ============================================================================

class Day8MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера мы чуть не погибли", None, WHITE),
            ("Кто-то слил информацию Охотнику", None, WHITE),
            ("Кто-то из нас", None, WHITE),
            ("Сегодня я начинаю расследование", None, WHITE),
            ("Буду смотреть", None, WHITE),
            ("Слушать", None, WHITE),
            ("Анализировать", None, WHITE),
            ("Мой дар видит структуру", None, WHITE),
            ("Может, я увижу то, что другие не замечают", None, WHITE),
            ("Предатель среди нас", None, WHITE),
            ("И я его найду", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 8 - СЦЕНА 2: КОРИДОР — НАБЛЮДЕНИЕ
# ============================================================================

class Day8CorridorObserveScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Весь день я наблюдаю", None, WHITE),
            ("Смотрю на каждого", None, WHITE),
            ("Ищу странности", None, WHITE),
            ("Макс", None, WHITE),
            ("Он слишком тихий сегодня", None, WHITE),
            ("Обычно он спокоен, но сейчас — будто избегает меня", None, WHITE),
            ("Не смотрит в глаза", None, WHITE),
            ("Сайлас", None, WHITE),
            ("Как всегда — с блокнотом", None, WHITE),
            ("Записывает", None, WHITE),
            ("Но сегодня он записывает слишком часто", None, WHITE),
            ("Будто фиксирует каждое наше движение", None, WHITE),
            ("Люция", None, WHITE),
            ("Она старается держаться как обычно", None, WHITE),
            ("Но я вижу — она напряжена", None, WHITE),
            ("Её взгляд иногда замирает на Максе", None, WHITE),
            ("Слишком долго", None, WHITE),
            ("Ийна", None, WHITE),
            ("Как обычно сидит в библиотеке", None, WHITE),
            ("Пальцы бегают по клавишам", None, WHITE),
            ("Но сегодня она не просто работает", None, WHITE),
            ("Она что-то ищет", None, WHITE),
            ("Или скрывает", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 8 - СЦЕНА 3: БИБЛИОТЕКА — АНАЛИЗ
# ============================================================================

class Day8LibraryAnalysisScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.library_bg = None
        self.library_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вечер", None, WHITE),
            ("Библиотека", None, WHITE),
            ("Я сижу за столом", None, WHITE),
            ("Передо мной — блокнот", None, WHITE),
            ("Я выписываю всё, что заметил", None, WHITE),
            ("Слишком много подозреваемых", None, WHITE),
            ("Нужны доказательства", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.library_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.library_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.library_bg_scaled = None
        else:
            self.library_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.library_bg_scaled:
            self.screen.blit(self.library_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 8 - СЦЕНА 4: КОРИДОР ОБЩЕЖИТИЯ — УЛИКИ
# ============================================================================

class Day8DormitoryCluesScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.dorm_bg = None
        self.dorm_bg_scaled = None
        self.room_max_bg = None
        self.room_max_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.bg_changed = False

        self.texts = [
            ("Поздняя ночь", None, WHITE),
            ("Все спят", None, WHITE),
            ("А я иду к комнате Макса", None, WHITE),
            ("К первому подозреваемому", None, WHITE),
            ("Дверь не заперта", None, WHITE),
            ("Захожу", None, WHITE),
            ("В комнате темно", None, WHITE),
            ("Он спит", None, WHITE),
            ("На столе — телефон", None, WHITE),
            ("Я взял телефон", None, WHITE),
            ("Экран загорается", None, WHITE),
            ("Немного поискав я нашел зашифрованные сообщения", None, WHITE),
            ("Отправитель неизвестен", None, WHITE),
            ("«Твоя мать жива. Пока ты делаешь, что я говорю»", None, WHITE),
            ("«Если откажешься — она умрёт»", None, WHITE),
            ("Я посмотрел на Макса", None, WHITE),
            ("Он спит", None, WHITE),
            ("Но лицо — напряжённое", None, WHITE),
            ("Ему снятся кошмары", None, WHITE),
            ("Я положил телефон на место и вышел из комнаты", None, WHITE),
            ("Макс — предатель", None, WHITE),
            ("Но он не хотел им быть", None, WHITE),
            ("Его шантажируют", None, WHITE),
            ("Его слабость — мать", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.dorm_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.dorm_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.dorm_bg_scaled = None
        else:
            self.dorm_bg_scaled = None

    def load_room_max_background(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_max_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
            except:
                self.room_max_bg_scaled = None
        else:
            self.room_max_bg_scaled = None

    def start(self, bg_path, room_max_path):
        self.load_background(bg_path)
        self.load_room_max_background(room_max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.bg_changed = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index == 5 and not self.bg_changed:
                self.bg_changed = True

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.bg_changed and self.room_max_bg_scaled:
            self.screen.blit(self.room_max_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        elif self.dorm_bg_scaled:
            self.screen.blit(self.dorm_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 8 - СЦЕНА 5: КОМНАТА ГГ — ПОДГОТОВКА К РАЗГОВОРУ
# ============================================================================

class Day8PreparationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Я вновь сижу за столом", None, WHITE),
            ("Передо мной — блокнот", None, WHITE),
            ("На чистом листе — одно слово:", None, WHITE),
            ("«Макс»", None, WHITE),
            ("Он не враг", None, WHITE),
            ("Он жертва", None, WHITE),
            ("Охотник держит его мать", None, WHITE),
            ("Если Макс откажется — она умрёт", None, WHITE),
            ("Но это не оправдание", None, WHITE),
            ("Из-за него мы чуть не погибли", None, WHITE),
            ("Из-за него Охотник всегда на шаг впереди", None, WHITE),
            ("Завтра я поговорю с ним", None, WHITE),
            ("Наедине", None, WHITE),
            ("Он должен признаться", None, WHITE),
            ("А дальше.. я не знаю", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 8 - ПЕРЕХОД К ДНЮ 9
# ============================================================================

class Day9Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 9", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 9 - СЦЕНА 1: УТРО — РЕШЕНИЕ
# ============================================================================

class Day9MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера я нашёл доказательства", None, WHITE),
            ("Макс — предатель", None, WHITE),
            ("Он сливает информацию Охотнику", None, WHITE),
            ("Я собирался поговорить с ним наедине", None, WHITE),
            ("Я встал и направился в спортзал", None, WHITE),
            ("По утрам он всегда там", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 9 - СЦЕНА 2: СПОРТЗАЛ — КОНФРОНТАЦИЯ
# ============================================================================

class Day9GymConfrontationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.gym_bg = None
        self.gym_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.max_visible = False

        self.texts = [
            ("Спортзал пуст", None, WHITE),
            ("Только Макс", None, WHITE),
            ("Он бьёт грушу", None, WHITE),
            ("Сильно", None, WHITE),
            ("Будто вымещает злость", None, WHITE),
            ("Я подошел ближе", None, WHITE),
            ("Он не оборачивается", None, WHITE),
            ("Но я вижу — он знает, что я здесь", None, WHITE),
            ("Макс", "Кайл", KAIL_COLOR),
            ("Нам нужно поговорить", "Кайл", KAIL_COLOR),
            ("Он замер", None, WHITE),
            ("Опустил руки и медленно повернулся ко мне", None, WHITE),
            ("О чём?", "Макс", MAX_COLOR),
            ("Я достаю его телефон", None, WHITE),
            ("Показываю экран", None, WHITE),
            ("Я всё знаю", "Кайл", KAIL_COLOR),
            ("Макс смотрит на телефон", None, WHITE),
            ("Потом на меня", None, WHITE),
            ("Его лицо бледнеет", None, WHITE),
            ("Откуда…", "Макс", MAX_COLOR),
            ("Не важно", "Кайл", KAIL_COLOR),
            ("Теперь скажи правду", "Кайл", KAIL_COLOR),
            ("Он долго молчит", None, WHITE),
            ("Потом закрывает лицо руками", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.gym_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.gym_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.gym_bg_scaled = None
        else:
            self.gym_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def start(self, bg_path, max_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.max_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index >= 12 and not self.max_visible:
                self.max_visible = True

            if self.text_index >= 23:
                self.max_visible = False

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.gym_bg_scaled:
            self.screen.blit(self.gym_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.max_visible and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 9 - СЦЕНА 3: ПРИЗНАНИЕ И ВЫБОР
# ============================================================================

class Day9ConfessionChoiceScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.gym_bg = None
        self.gym_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.stid_max_portrait = None
        self.stid_max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.choice_shown = False
        self.choice_made = None
        self.branch_complete = False
        self.current_portrait_visible = "stid_max"
        self.branch_texts = []
        self.branch_text_index = 0
        self.choice_buttons = []
        self.hover_index = -1
        self.waiting_for_choice = False
        self.showing_branch = False

        self.texts = [
            ("Макс опускается на скамейку", None, WHITE),
            ("Голову вниз", None, WHITE),
            ("Голос дрожит", None, WHITE),
            ("Он нашёл меня месяц назад", "Макс", MAX_COLOR),
            ("Прислал фото матери", "Макс", MAX_COLOR),
            ("Сказал, что если я не буду помогать — она умрёт", "Макс", MAX_COLOR),
            ("Я не хотел, но что мне оставалось?", "Макс", MAX_COLOR),
            ("Она — единственное, что у меня есть", "Макс", MAX_COLOR),
            ("Он поднимает голову", None, WHITE),
            ("В глазах — слёзы", None, WHITE),
            ("Я передавал ему информацию", "Макс", MAX_COLOR),
            ("Где мы будем", "Макс", MAX_COLOR),
            ("Что планируем", "Макс", MAX_COLOR),
            ("Я знал, что вы идёте в ловушку", "Макс", MAX_COLOR),
            ("Но я не мог… не мог её бросить", "Макс", MAX_COLOR),
            ("Тишина", None, WHITE),
            ("Я смотрю на него", None, WHITE),
            ("Внутри — гнев", None, WHITE),
            ("Но есть и жалость", None, WHITE),
            ("Почему ты не сказал? Мы бы помогли", "Кайл", KAIL_COLOR),
            ("Вы бы помогли?", "Макс", MAX_COLOR),
            ("И что бы вы сделали?", "Макс", MAX_COLOR),
            ("Пошли бы спасать мою мать, пока Охотник убивает здесь?", "Макс", MAX_COLOR),
            ("Вы бы пытались сделать и то, и другое", "Макс", MAX_COLOR),
            ("И все бы погибли", "Макс", MAX_COLOR),
            ("Он встаёт", None, WHITE),
            ("Смотрит мне в глаза", None, WHITE),
            ("Я знаю, что заслуживаю", "Макс", MAX_COLOR),
            ("Делай, что должен", "Макс", MAX_COLOR),
            ("Я смотрю на него", None, WHITE),
            ("И принимаю решение", None, WHITE)
        ]

        self.forgive_texts = [
            ("Макс смотрит на меня с недоверием", None, WHITE),
            ("Ты остаёшься", "Кайл", KAIL_COLOR),
            ("Но теперь ты работаешь на меня", "Кайл", KAIL_COLOR),
            ("Будешь передавать Охотнику то, что скажу я", "Кайл", KAIL_COLOR),
            ("Мы подставим его", "Кайл", KAIL_COLOR),
            ("Макс молчит", None, WHITE),
            ("Потом кивает", None, WHITE),
            ("Ты доверяешь мне? После всего?", "Макс", MAX_COLOR),
            ("Нет", "Кайл", KAIL_COLOR),
            ("Но я даю тебе шанс", "Кайл", KAIL_COLOR),
            ("Не подведи", "Кайл", KAIL_COLOR),
            ("Он смотрит на меня", None, WHITE),
            ("В его глазах — благодарность", None, WHITE),
            ("И надежда", None, WHITE)
        ]

        self.exclude_texts = [
            ("Макс смотрит на меня", None, WHITE),
            ("Его лицо ничего не выражает", None, WHITE),
            ("Ты уходишь", "Кайл", KAIL_COLOR),
            ("Я расскажу всё группе", "Кайл", KAIL_COLOR),
            ("Если я увижу тебя рядом с кем-то из нас — я не буду сдерживаться", "Кайл", KAIL_COLOR),
            ("Макс медленно кивает", None, WHITE),
            ("Забирает вещи", None, WHITE),
            ("Идёт к выходу", None, WHITE),
            ("У двери останавливается", None, WHITE),
            ("Ты поступил правильно", "Макс", MAX_COLOR),
            ("Я… я не заслуживаю", "Макс", MAX_COLOR),
            ("Он не заканчивает", None, WHITE),
            ("Уходит", None, WHITE)
        ]

        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE
        self.choice = None

    def load_background(self, path):
        if not path:
            self.gym_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.gym_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.gym_bg_scaled = None
        else:
            self.gym_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_stid_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.stid_max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.stid_max_portrait_scaled = None
        else:
            self.stid_max_portrait_scaled = None

    def start(self, bg_path, max_path, stid_max_path):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.load_stid_max_portrait(stid_max_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.choice_shown = False
        self.choice_made = None
        self.branch_complete = False
        self.current_portrait_visible = "stid_max"
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE
        self.choice = None
        self.branch_texts = []
        self.branch_text_index = 0
        self.choice_buttons = []
        self.hover_index = -1
        self.waiting_for_choice = False
        self.showing_branch = False

    def handle_click(self):
        if self.showing_branch and self.can_click:
            self.can_click = False
            self.branch_text_index += 1
            if self.branch_text_index < len(self.branch_texts):
                text_data = self.branch_texts[self.branch_text_index]
                self.current_text = text_data[0]
                self.current_speaker = text_data[1]
                self.current_color = text_data[2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return None

        if self.show_text and self.can_click and not self.choice_shown and not self.showing_branch:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.choice_shown = True
                self.show_text = False
                self.waiting_for_choice = True
                return None
        return None

    def make_choice(self, choice):
        self.choice_made = choice
        self.choice = choice
        self.choice_shown = False
        self.waiting_for_choice = False
        self.showing_branch = True
        self.branch_text_index = 0

        if choice == "forgive":
            self.branch_texts = self.forgive_texts
            self.current_portrait_visible = "stid_max"
        else:
            self.branch_texts = self.exclude_texts
            self.current_portrait_visible = "max"

        if self.branch_texts:
            text_data = self.branch_texts[0]
            self.current_text = text_data[0]
            self.current_speaker = text_data[1]
            self.current_color = text_data[2]
            self.show_text = True
            self.can_click = True

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw_choice(self, mouse_pos):
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.fill(BLACK)
        overlay.set_alpha(200)
        self.screen.blit(overlay, (0, 0))

        title_font = pygame.font.Font(None, 52)
        title = title_font.render("Что сделать с Максом?", True, CHALK_WHITE)
        title_rect = title.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 120))
        self.screen.blit(title, title_rect)

        button_width = 300
        button_height = 60
        button_spacing = 30
        start_y = self.screen_height // 2 - 40

        forgive_rect = pygame.Rect(
            self.screen_width // 2 - button_width // 2,
            start_y,
            button_width,
            button_height
        )

        exclude_rect = pygame.Rect(
            self.screen_width // 2 - button_width // 2,
            start_y + button_height + button_spacing,
            button_width,
            button_height
        )

        forgive_hover = forgive_rect.collidepoint(mouse_pos)
        exclude_hover = exclude_rect.collidepoint(mouse_pos)

        forgive_color = (80, 120, 80) if forgive_hover else (40, 60, 40)
        pygame.draw.rect(self.screen, forgive_color, forgive_rect, border_radius=10)
        pygame.draw.rect(self.screen, CHALK_WHITE, forgive_rect, 2, border_radius=10)

        forgive_font = pygame.font.Font(None, 36)
        forgive_text = forgive_font.render("Простить и оставить", True, CHALK_WHITE)
        forgive_text_rect = forgive_text.get_rect(center=forgive_rect.center)
        self.screen.blit(forgive_text, forgive_text_rect)

        exclude_color = (120, 60, 60) if exclude_hover else (60, 40, 40)
        pygame.draw.rect(self.screen, exclude_color, exclude_rect, border_radius=10)
        pygame.draw.rect(self.screen, CHALK_WHITE, exclude_rect, 2, border_radius=10)

        exclude_text = forgive_font.render("Исключить из группы", True, CHALK_WHITE)
        exclude_text_rect = exclude_text.get_rect(center=exclude_rect.center)
        self.screen.blit(exclude_text, exclude_text_rect)

        self.forgive_rect = forgive_rect
        self.exclude_rect = exclude_rect

    def handle_choice_click(self, pos):
        if hasattr(self, 'forgive_rect') and self.forgive_rect.collidepoint(pos):
            self.make_choice("forgive")
            return "forgive"
        elif hasattr(self, 'exclude_rect') and self.exclude_rect.collidepoint(pos):
            self.make_choice("exclude")
            return "exclude"
        return None

    def draw(self):
        if self.gym_bg_scaled:
            self.screen.blit(self.gym_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "stid_max" and self.stid_max_portrait_scaled:
            portrait_x = (self.screen_width - self.stid_max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.stid_max_portrait_scaled.get_height()
            self.screen.blit(self.stid_max_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.choice_shown and self.waiting_for_choice and not self.fade_out_active:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_choice(mouse_pos)

        if self.show_text and self.current_text and not self.fade_out_active and not self.choice_shown:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready

    def get_choice(self):
        return self.choice


# ============================================================================
# ДЕНЬ 9 - СЦЕНА 4: ТАЙНАЯ КОМНАТА — СООБЩЕНИЕ ГРУППЕ
# ============================================================================

class Day9SecretMessageScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.lucia_visible = False
        self.choice = None

        self.texts_forgive = [
            ("Вечер", None, WHITE),
            ("Тайная комната", None, WHITE),
            ("Все в сборе", None, WHITE),
            ("Даже Макс", None, WHITE),
            ("Зачем ты его привёл?", "Люция", YELLOW),
            ("Ты же сказал, что знаешь, кто предатель", "Люция", YELLOW),
            ("Я знаю", "Кайл", KAIL_COLOR),
            ("И я решил", "Кайл", KAIL_COLOR),
            ("Макс остаётся", "Кайл", KAIL_COLOR),
            ("Он будет работать на нас", "Кайл", KAIL_COLOR),
            ("Передавать Охотнику ложную информацию", "Кайл", KAIL_COLOR),
            ("Тишина", None, WHITE),
            ("Люция смотрит на меня", None, WHITE),
            ("Потом на Макса", None, WHITE),
            ("Ты уверен?", "Люция", YELLOW),
            ("Да", "Кайл", KAIL_COLOR),
            ("Больше никто не говорит", None, WHITE),
            ("Сайлас что-то записывает в блокнот", None, WHITE),
            ("Ийна не поднимает головы", None, WHITE),
            ("Макс смотрит в пол", None, WHITE)
        ]

        self.texts_exclude = [
            ("Вечер", None, WHITE),
            ("Тайная комната", None, WHITE),
            ("Все в сборе", None, WHITE),
            ("Макса нет", None, WHITE),
            ("Где Макс?", "Люция", YELLOW),
            ("Я нашёл предателя", "Кайл", KAIL_COLOR),
            ("Это Макс", "Кайл", KAIL_COLOR),
            ("Охотник шантажирует его матерью", "Кайл", KAIL_COLOR),
            ("Он уходит из группы", "Кайл", KAIL_COLOR),
            ("Люция бледнеет", None, WHITE),
            ("Сайлас сжимает блокнот", None, WHITE),
            ("Ийна поднимает голову", None, WHITE),
            ("Ты уверен?", "Люция", YELLOW),
            ("Я видел доказательства", "Кайл", KAIL_COLOR),
            ("Если я увижу его рядом с кем-то из нас — я убью его сама", "Люция", YELLOW),
            ("Это не угроза", "Люция", YELLOW),
            ("Это обещание", "Люция", YELLOW),
            ("Никто не говорит", None, WHITE),
            ("Решение принято", None, WHITE)
        ]

        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def start(self, bg_path, lucia_path, choice):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.lucia_visible = False
        self.choice = choice
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            texts = self.texts_forgive if self.choice == "forgive" else self.texts_exclude

            if self.text_index < len(texts):
                current_speaker = texts[self.text_index][1]
                next_speaker = None
                if self.text_index + 1 < len(texts):
                    next_speaker = texts[self.text_index + 1][1]

                if current_speaker == "Люция":
                    self.lucia_visible = True
                elif current_speaker != "Люция" and self.lucia_visible:
                    if next_speaker != "Люция":
                        self.lucia_visible = False

                self.current_text = texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    texts = self.texts_forgive if self.choice == "forgive" else self.texts_exclude
                    self.show_text = True
                    self.current_text = texts[0][0]
                    self.current_speaker = texts[0][1]
                    self.current_color = texts[0][2]
                    self.can_click = True
                    self.lucia_visible = False
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.lucia_visible and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 9 - СЦЕНА 5: КОМНАТА ГГ — РАЗМЫШЛЕНИЯ
# ============================================================================

class Day9InsomniaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Ночь, я размышляю о случившемся", None, WHITE),
            ("Макс", None, WHITE),
            ("Он не враг", None, WHITE),
            ("Он жертва", None, WHITE),
            ("Но его слабость могла убить нас", None, WHITE),
            ("Я сделал выбор", None, WHITE),
            ("Теперь остаётся надеяться, что он был правильным", None, WHITE),
            ("Охотник всё ещё там", None, WHITE),
            ("Сайлас, Люция, Ийна", None, WHITE),
            ("Кто-то из них следующий?", None, WHITE),
            ("Или я?", None, WHITE),
            ("Завтра новый день", None, WHITE),
            ("Мы продолжим расследование", None, WHITE),
            ("И найдём его", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 9 - ПЕРЕХОД К ДНЮ 10
# ============================================================================

class Day10Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 10", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 10 - СЦЕНА 1: УТРО — ПОСЛЕ ВЧЕРАШНЕГО
# ============================================================================

class Day10MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера я решил судьбу Макса", None, WHITE),
            ("Я не знаю, правильно ли поступил", None, WHITE),
            ("Сегодня мы идём дальше", None, WHITE),
            ("Ийна нашла зацепку", None, WHITE),
            ("Говорит, что в медкрыле есть что-то ещё", None, WHITE),
            ("Скрытая лаборатория", None, WHITE),
            ("Возможно, там ответы", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - СЦЕНА 2: КОРИДОР — ВСТРЕЧА / НОВОСТИ
# ============================================================================

class Day10CorridorBranchScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None
        self.choice = None

        self.forgive_texts = [
            ("Я вышел из комнаты", None, WHITE),
            ("В коридоре — Макс", None, WHITE),
            ("Ждёт меня", None, WHITE),
            ("Я хочу сказать…", "Макс", MAX_COLOR),
            ("спасибо", "Макс", MAX_COLOR),
            ("Ты мог меня сдать", "Макс", MAX_COLOR),
            ("Но не стал", "Макс", MAX_COLOR),
            ("Не благодари", "Кайл", KAIL_COLOR),
            ("Ты теперь работаешь на меня", "Кайл", KAIL_COLOR),
            ("Охотник получит только то, что мы решим", "Кайл", KAIL_COLOR),
            ("Макс кивает", None, WHITE),
            ("В его глазах — решимость", None, WHITE),
            ("Я не подведу", "Макс", MAX_COLOR),
            ("Он уходит", None, WHITE),
            ("Я смотрю ему вслед", None, WHITE),
            ("Надеюсь", "Кайл", KAIL_COLOR)
        ]

        self.exclude_texts = [
            ("Я выхожу из комнаты", None, WHITE),
            ("В коридоре — Люция", None, WHITE),
            ("Лицо напряжённое", None, WHITE),
            ("Макс исчез", "Люция", YELLOW),
            ("Его нет в комнате", "Люция", YELLOW),
            ("Вещи на месте, но сам он… пропал", "Люция", YELLOW),
            ("Я промолчал", None, WHITE),
            ("Что я могу сказать?", None, WHITE),
            ("Охотник узнал, что он больше не нужен", "Люция", YELLOW),
            ("Или… он сам ушёл", "Люция", YELLOW),
            ("Не знаю", "Люция", YELLOW),
            ("Мы найдём его", "Кайл", KAIL_COLOR),
            ("Или то, что от него осталось", "Кайл", KAIL_COLOR),
            ("Люция смотрит на меня", None, WHITE),
            ("В её глазах — боль", None, WHITE)
        ]

        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_max_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.max_portrait_scaled = None
        else:
            self.max_portrait_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def start(self, bg_path, max_path, lucia_path, choice):
        self.load_background(bg_path)
        self.load_max_portrait(max_path)
        self.load_lucia_portrait(lucia_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.choice = choice
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            texts = self.forgive_texts if self.choice == "forgive" else self.exclude_texts

            if self.text_index < len(texts):
                current_speaker = texts[self.text_index][1]

                if self.choice == "forgive":
                    if current_speaker == "Макс":
                        self.current_portrait_visible = "max"
                    else:
                        self.current_portrait_visible = None
                else:
                    if current_speaker == "Люция":
                        self.current_portrait_visible = "lucia"
                    else:
                        self.current_portrait_visible = None

                self.current_text = texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    texts = self.forgive_texts if self.choice == "forgive" else self.exclude_texts
                    self.show_text = True
                    self.current_text = texts[0][0]
                    self.current_speaker = texts[0][1]
                    self.current_color = texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "max" and self.max_portrait_scaled:
            portrait_x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - СЦЕНА 3: ТАЙНАЯ КОМНАТА — ПЛАНИРОВАНИЕ
# ============================================================================

class Day10SecretPlanningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Все в сборе", None, WHITE),
            ("Ийна выводит на экран схему медкрыла", None, WHITE),
            ("Я нашла аномалию", "Ийна", GREEN),
            ("За третьим архивом — пустота", "Ийна", GREEN),
            ("Несуществующая стена", "Ийна", GREEN),
            ("Скорее всего, скрытая лаборатория", "Ийна", GREEN),
            ("Вероятность того, что там оборудование для стирания — 94%", "Сайлас", LIGHT_CYAN),
            ("Сегодня идём туда", "Люция", YELLOW),
            ("Ночью", "Люция", YELLOW),
            ("Надо узнать правду", "Люция", YELLOW),
            ("Все кивают", None, WHITE),
            ("Я смотрю на Сайласа", None, WHITE),
            ("Он слишком спокоен", None, WHITE),
            ("Слишком уверен", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def start(self, bg_path, iina_path, sailas_path, lucia_path):
        self.load_background(bg_path)
        self.load_iina_portrait(iina_path)
        self.load_sailas_portrait(sailas_path)
        self.load_lucia_portrait(lucia_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Ийна":
                    self.current_portrait_visible = "iina"
                elif current_speaker == "Сайлас":
                    self.current_portrait_visible = "sailas"
                elif current_speaker == "Люция":
                    self.current_portrait_visible = "lucia"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            portrait_x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - СЦЕНА 4: МЕДИЦИНСКОЕ КРЫЛО — ПУТЬ К ЛАБОРАТОРИИ
# ============================================================================

class Day10MedicalPathScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.medical_bg = None
        self.medical_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.glow_alpha = 0
        self.glow_active = False

        self.texts = [
            ("Ночь", None, WHITE),
            ("Медицинское крыло", None, WHITE),
            ("Идём по тому же коридору, что и в прошлый раз", None, WHITE),
            ("Только теперь — дальше", None, WHITE),
            ("Глубже", None, WHITE),
            ("За третьим архивом — тупик", None, WHITE),
            ("Стена", None, WHITE),
            ("Но я использую дар", None, WHITE),
            ("Вижу структуру", None, WHITE),
            ("Здесь стена тоньше", "Кайл", KAIL_COLOR),
            ("За ней — пустота", "Кайл", KAIL_COLOR),
            ("Люция нажимает на скрытый механизм", None, WHITE),
            ("Стена бесшумно отъезжает в сторону", None, WHITE),
            ("Тёмный коридор", None, WHITE),
            ("Уходит вниз", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.medical_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.medical_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.medical_bg_scaled = None
        else:
            self.medical_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.glow_alpha = 0
        self.glow_active = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index == 8:
                self.glow_active = True

            if self.text_index == 10:
                self.glow_active = False

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True
        if self.glow_active:
            self.glow_alpha += 5
            if self.glow_alpha > 100:
                self.glow_alpha = 100

    def draw(self):
        if self.medical_bg_scaled:
            self.screen.blit(self.medical_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.glow_active and self.glow_alpha > 0:
            glow_surface = pygame.Surface((self.screen_width, self.screen_height))
            glow_surface.fill(LIGHT_BLUE)
            glow_surface.set_alpha(self.glow_alpha)
            self.screen.blit(glow_surface, (0, 0))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - СЦЕНА 5: ЛАБОРАТОРИЯ ХАРТ — ОСМОТР
# ============================================================================

class Day10HartLabScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.lab_bg = None
        self.lab_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None

        self.texts = [
            ("Мы спустились вниз", None, WHITE),
            ("Лаборатория", None, WHITE),
            ("Столы с инструментами", None, WHITE),
            ("Мониторы", None, WHITE),
            ("Провода", None, WHITE),
            ("В центре — кресло с ремнями", None, WHITE),
            ("То самое кресло", None, WHITE),
            ("С видео", None, WHITE),
            ("Они проводили здесь процедуры", "Люция", YELLOW),
            ("Стирали память", "Люция", YELLOW),
            ("Убивали", "Люция", YELLOW),
            ("Ийна подходит к компьютеру", None, WHITE),
            ("Вставляет флешку", None, WHITE),
            ("Здесь всё", "Ийна", GREEN),
            ("Список субъектов", "Ийна", GREEN),
            ("Отчёты", "Ийна", GREEN),
            ("Имена", "Ийна", GREEN),
            ("Все, кого они… нейтрализовали", "Ийна", GREEN),
            ("Я смотрю на экран", None, WHITE),
            ("Список имён", None, WHITE),
            ("Знакомых", None, WHITE),
            ("Субъект No1, Субъект No4, Субъект No7, Субъект No11", None, WHITE),
            ("И внизу — пустая строка", None, WHITE),
            ("12", None, WHITE),
            ("Копируй всё", "Кайл", KAIL_COLOR),
            ("Мы выложим это в сеть", "Кайл", KAIL_COLOR),
            ("Пусть все узнают", "Кайл", KAIL_COLOR),
            ("Сайлас стоит в стороне", None, WHITE),
            ("Смотрит на кресло", None, WHITE),
            ("Его лицо — спокойное", None, WHITE),
            ("Слишком спокойное", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.lab_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.lab_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.lab_bg_scaled = None
        else:
            self.lab_bg_scaled = None

    def load_lucia_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.lucia_portrait_scaled = None
        else:
            self.lucia_portrait_scaled = None

    def load_iina_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.iina_portrait_scaled = None
        else:
            self.iina_portrait_scaled = None

    def load_sailas_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                portrait_width = int(self.screen_width * 0.6)
                portrait_height = int(original.get_height() * (portrait_width / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (portrait_width, portrait_height))
            except:
                self.sailas_portrait_scaled = None
        else:
            self.sailas_portrait_scaled = None

    def start(self, bg_path, lucia_path, iina_path, sailas_path):
        self.load_background(bg_path)
        self.load_lucia_portrait(lucia_path)
        self.load_iina_portrait(iina_path)
        self.load_sailas_portrait(sailas_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Люция":
                    self.current_portrait_visible = "lucia"
                elif current_speaker == "Ийна":
                    self.current_portrait_visible = "iina"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.lab_bg_scaled:
            self.screen.blit(self.lab_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            portrait_x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (portrait_x, portrait_y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            portrait_x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            portrait_y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (portrait_x, portrait_y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - СЦЕНА 6: КОМНАТА ГГ — РАЗМЫШЛЕНИЯ
# ============================================================================

class Day10InsomniaScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Ночь", None, WHITE),
            ("Я вернулся в комнату", None, WHITE),
            ("Передо мной — список", None, WHITE),
            ("Тот, что мы нашли в лаборатории", None, WHITE),
            ("Все кто были до нас", None, WHITE),
            ("Их убил Охотник", None, WHITE),
            ("Кто он?", None, WHITE),
            ("Сайлас слишком спокоен", None, WHITE),
            ("Его способность — видеть вероятности", None, WHITE),
            ("Он мог просчитать всё", None, WHITE),
            ("Каждое убийство", None, WHITE),
            ("Вспоминаю", None, WHITE),
            ("Он всегда был рядом", None, WHITE),
            ("Всегда знал, где мы будем", None, WHITE),
            ("Всегда говорил: «Вероятность успеха — 78%»", None, LIGHT_CYAN),
            ("Как будто… управлял нами", None, WHITE),
            ("Завтра я проверю его", None, WHITE),
            ("И если это правда…", None, WHITE),
            ("Он ответит", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 10 - ПЕРЕХОД К ДНЮ 11
# ============================================================================

class Day11Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 11", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ДЕНЬ 11 - СЦЕНА 1: УТРО — ПОДОЗРЕНИЯ
# ============================================================================

class Day11MorningScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вчера мы нашли лабораторию Харт", None, WHITE),
            ("Кресло с ремнями", None, WHITE),
            ("Оборудование для стирания", None, WHITE),
            ("Список имён", None, WHITE),
            ("Сайлас был спокоен", None, WHITE),
            ("Слишком спокоен", None, WHITE),
            ("Будто знал, что мы там найдём", None, WHITE),
            ("Будто уже всё видел", None, WHITE),
            ("Его дар — видеть вероятности", None, WHITE),
            ("Он мог просчитать каждое убийство", None, WHITE),
            ("Каждую жертву", None, WHITE),
            ("Каждое наше движение", None, WHITE),
            ("Сегодня я проверю его", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 11 - СЦЕНА 2: КОРИДОР — СЛЕЖКА
# ============================================================================

class Day11CorridorFollowScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Весь день я следую за Сайласом", None, WHITE),
            ("Не приближаясь", None, WHITE),
            ("Не привлекая внимания", None, WHITE),
            ("Он ходит на лекции", None, WHITE),
            ("Сидит в библиотеке", None, WHITE),
            ("Встречается с преподавателями", None, WHITE),
            ("Всё как обычно", None, WHITE),
            ("Но я замечаю", None, WHITE),
            ("Он постоянно что-то записывает в блокнот", None, WHITE),
            ("Цифры, Имена, Даты", None, WHITE),
            ("Имена тех, кто уже мёртв", None, WHITE),
            ("Субъект No1, Субъект No4, Субъект No7, Субъект No11", None, WHITE),
            ("Он помнит их", None, WHITE),
            ("Но не как жертв", None, WHITE),
            ("Как… расчёты", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 11 - СЦЕНА 3: БИБЛИОТЕКА — АНАЛИЗ
# ============================================================================

class Day11LibraryAnalysisScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.library_bg = None
        self.library_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Вечер", None, WHITE),
            ("Библиотека", None, WHITE),
            ("Я сижу за столом", None, WHITE),
            ("Передо мной — блокнот", None, WHITE),
            ("Мои заметки", None, WHITE),
            ("Сайлас всегда знал, где будет жертва", None, WHITE),
            ("Всегда говорил: «Вероятность успеха — 78%»", None, LIGHT_CYAN),
            ("Всегда был рядом", None, WHITE),
            ("Он не просто вычисляет", None, WHITE),
            ("Он управляет", None, WHITE),
            ("Он знает исход", None, WHITE),
            ("Потому что он его создаёт", None, WHITE),
            ("Вспоминаю его лицо, когда мы смотрели видео", None, WHITE),
            ("Ни страха", None, WHITE),
            ("Ни боли", None, WHITE),
            ("Только холодный расчёт", None, WHITE),
            ("Он не жертва", None, WHITE),
            ("Он убийца", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.library_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.library_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.library_bg_scaled = None
        else:
            self.library_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.library_bg_scaled:
            self.screen.blit(self.library_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 11 - СЦЕНА 4: КОМНАТА САЙЛАСА — НАХОДКА
# ============================================================================

class Day11SailasRoomScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.sailas_room_bg = None
        self.sailas_room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Ночь", None, WHITE),
            ("Все спят", None, WHITE),
            ("Я нахожусь в комнате Сайласа", None, WHITE),
            ("Дверь была не заперта", None, WHITE),
            ("В комнате темно", None, WHITE),
            ("Только свет от уличных фонарей проникает через окно", None, WHITE),
            ("На столе — блокнот", None, WHITE),
            ("Тот самый", None, WHITE),
            ("Я открыл его", None, WHITE),
            ("Страницы исписаны цифрами", None, WHITE),
            ("Вероятности", None, WHITE),
            ("Даты", None, WHITE),
            ("Имена", None, WHITE),
            ("И расчёты", None, WHITE),
            ("Как убить", None, WHITE),
            ("Когда", None, WHITE),
            ("Где", None, WHITE),
            ("Субъект No1 — телекинез; Подсыпать стимулятор; Вероятность успеха — 96%", None, LIGHT_CYAN),
            ("Субъект No4 — эмпатия; Страх от окружающих; Вероятность успеха — 98%", None, LIGHT_CYAN),
            ("Субъект No7 — аналитик; Ложный след с ловушкой; Вероятность успеха — 97%", None, LIGHT_CYAN),
            ("Субъект No11 — гиперчувствительность; Ультразвук; Вероятность успеха — 99%", None, LIGHT_CYAN),
            ("Внизу — моё имя", None, WHITE),
            ("Субъект No12 — структурный анализ", None, WHITE),
            ("Вероятность катастрофы — 52%", None, WHITE),
            ("Решение: наблюдать", None, WHITE),
            ("Закрываю блокнот", None, WHITE),
            ("Кладу на место", None, WHITE),
            ("Выхожу из комнаты", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.sailas_room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.sailas_room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.sailas_room_bg_scaled = None
        else:
            self.sailas_room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.sailas_room_bg_scaled:
            self.screen.blit(self.sailas_room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 11 - СЦЕНА 5: КОМНАТА ГГ — ПРИГОТОВЛЕНИЯ
# ============================================================================

class Day11PreparationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.room_bg = None
        self.room_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False

        self.texts = [
            ("Ночь", None, WHITE),
            ("Сижу за столом", None, WHITE),
            ("Передо мной — блокнот", None, WHITE),
            ("Список имён", None, WHITE),
            ("И одно имя, которое я не могу забыть", None, WHITE),
            ("Сайлас — Охотник", None, WHITE),
            ("Он убивал их", None, WHITE),
            ("Всех", None, WHITE),
            ("И чуть не убил нас", None, WHITE),
            ("Но он не убил меня", None, WHITE),
            ("Почему?", None, WHITE),
            ("Вероятность катастрофы — 52%", None, LIGHT_CYAN),
            ("Решение: наблюдать", None, LIGHT_CYAN),
            ("Я для него — эксперимент", None, WHITE),
            ("Ждёт, когда я ошибусь", None, WHITE),
            ("Когда стану угрозой", None, WHITE),
            ("Завтра я расскажу всё группе", None, WHITE),
            ("Мы должны остановить его", None, WHITE),
            ("До того, как он остановит нас", None, WHITE)
        ]
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.room_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.room_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.room_bg_scaled = None
        else:
            self.room_bg_scaled = None

    def start(self, bg_path):
        self.load_background(bg_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.room_bg_scaled:
            self.screen.blit(self.room_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)
        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ДЕНЬ 11 - ПЕРЕХОД К ДНЮ 12
# ============================================================================

class Day12Transition:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.fade_duration = 60
        self.text_timer = 0
        self.text_visible_duration = 180
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def start(self, bg_path=None):
        self.fade_alpha = 0
        self.state = "fade_out"
        self.fade_timer = 0
        self.text_timer = 0
        self.text_alpha = 0
        self.complete = False
        self.transition_complete = False

    def update(self):
        if self.complete:
            return
        if self.state == "fade_out":
            self.fade_timer += 1
            self.fade_alpha = int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 255
                self.state = "show_text"
                self.fade_timer = 0
        elif self.state == "show_text":
            self.text_timer += 1
            if self.text_timer <= 30:
                self.text_alpha = int(255 * (self.text_timer / 30))
            elif self.text_timer <= self.text_visible_duration - 30:
                self.text_alpha = 255
            else:
                self.text_alpha = 255 - int(255 * ((self.text_timer - (self.text_visible_duration - 30)) / 30))
                if self.text_alpha < 0:
                    self.text_alpha = 0
            if self.text_timer >= self.text_visible_duration:
                self.state = "fade_in"
                self.fade_timer = 0
                self.text_alpha = 0
        elif self.state == "fade_in":
            self.fade_timer += 1
            self.fade_alpha = 255 - int(255 * (self.fade_timer / self.fade_duration))
            if self.fade_timer >= self.fade_duration:
                self.fade_alpha = 0
                self.transition_complete = True
                self.complete = True

    def draw(self):
        self.screen.fill(BLACK)
        if self.text_alpha > 0:
            day_font = pygame.font.Font(None, 120)
            day_text = day_font.render("День 12", True, WHITE)
            day_text.set_alpha(self.text_alpha)
            text_rect = day_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(day_text, text_rect)
        if self.state == "show_text":
            if self.fade_alpha > 0:
                current_fade = max(0, self.fade_alpha - self.text_alpha)
                if current_fade > 0:
                    fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                    fade_surface.fill(BLACK)
                    fade_surface.set_alpha(current_fade)
                    self.screen.blit(fade_surface, (0, 0))
        else:
            if self.fade_alpha > 0:
                fade_surface = pygame.Surface((self.screen_width, self.screen_height))
                fade_surface.fill(BLACK)
                fade_surface.set_alpha(self.fade_alpha)
                self.screen.blit(fade_surface, (0, 0))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_complete
# ============================================================================
# ФИНАЛ - СЦЕНА 0: РАЗОБЛАЧЕНИЕ САЙЛАСА
# ============================================================================

class Act12RevelationScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.secret_bg = None
        self.secret_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.lucia_str_portrait = None
        self.lucia_str_portrait_scaled = None
        self.lucia_gnev_portrait = None
        self.lucia_gnev_portrait_scaled = None
        self.lucia_resh_portrait = None
        self.lucia_resh_portrait_scaled = None
        self.sailas_ras_portrait = None
        self.sailas_ras_portrait_scaled = None
        self.sailas_ist_portrait = None
        self.sailas_ist_portrait_scaled = None
        self.sailas_oder_portrait = None
        self.sailas_oder_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.max_gnev_portrait = None
        self.max_gnev_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.iina_str_portrait = None
        self.iina_str_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None
        self.max_alive = True

        self.texts = [
            ("Мы собрались в тайной комнате", None, WHITE),
            ("Все на месте", None, WHITE),
            ("Я стою у доски", None, WHITE),
            ("Смотрю на них", None, WHITE),
            ("Зачем ты всех собрал", "Люция", YELLOW),
            ("Что случилось", "Люция", YELLOW),
            ("Я перевожу взгляд на Сайласа", None, WHITE),
            ("Он сидит с блокнотом", None, WHITE),
            ("Как всегда", None, WHITE),
            ("Я знаю, кто Охотник", "Кайл", KAIL_COLOR),
            ("Тишина", None, WHITE),
            ("Все замирают", None, WHITE),
            ("И кто же", "Сайлас", LIGHT_CYAN),
            ("Он не смотрит на меня", None, WHITE),
            ("Перелистывает страницу блокнота", None, WHITE),
            ("Ты, Сайлас", "Кайл", KAIL_COLOR),
            ("Люция бледнеет", None, WHITE),
            ("Макс сжимает кулаки", None, WHITE),
            ("Ийна замирает с руками на клавиатуре", None, WHITE),
            ("Что? Нет… не может быть", "Люция", YELLOW),
            ("Почему ты так решил", "Сайлас", LIGHT_CYAN),
            ("Я был в твоей комнате", "Кайл", KAIL_COLOR),
            ("Видел блокнот", "Кайл", KAIL_COLOR),
            ("Твои расчёты", "Кайл", KAIL_COLOR),
            ("Вероятности", "Кайл", KAIL_COLOR),
            ("Методы убийства каждого из них", "Кайл", KAIL_COLOR),
            ("Сайлас медленно закрывает блокнот", None, WHITE),
            ("Снимает очки", None, WHITE),
            ("Протирает их", None, WHITE),
            ("И что ты там увидел", "Сайлас", LIGHT_CYAN),
            ("Субъект No1 — телекинез. Стимулятор. Вероятность успеха — 96%", "Кайл", KAIL_COLOR),
            ("Субъект No4 — эмпатия. Две недели страха. Вероятность — 98%", "Кайл", KAIL_COLOR),
            ("Субъект No7 — аналитик. Ложный след, шахта лифта. Вероятность — 97%", "Кайл", KAIL_COLOR),
            ("Субъект No11 — гиперчувствительность. Ультразвук. Вероятность — 99%", "Кайл", KAIL_COLOR),
            ("Тишина", None, WHITE),
            ("Сайлас… это правда", "Люция", YELLOW),
            ("Сайлас надевает очки", None, WHITE),
            ("Смотрит на неё", None, WHITE),
            ("Потом на меня", None, WHITE),
            ("Правда", "Сайлас", LIGHT_CYAN),
            ("Я не собираюсь отрицать", "Сайлас", LIGHT_CYAN),
            ("Ты убивал их! Наших!", "Макс", MAX_COLOR),
            ("ТЫ...УГРОЖАЛ МОЕЙ МАТЕРИ", "Макс", MAX_COLOR),
            ("Я спасал мир", "Сайлас", LIGHT_CYAN),
            ("Как можно спасать мир, убивая детей", "Ийна", GREEN),
            ("Вы не понимаете", "Сайлас", LIGHT_CYAN),
            ("Вы видите только смерти", "Сайлас", LIGHT_CYAN),
            ("А я вижу числа", "Сайлас", LIGHT_CYAN),
            ("Вероятности", "Сайлас", LIGHT_CYAN),
            ("Если бы я не остановил их, погибли бы тысячи", "Сайлас", LIGHT_CYAN),
            ("Он открывает блокнот", None, WHITE),
            ("Показывает страницы", None, WHITE),
            ("Субъект No1 через год разрушил бы полгорода", "Сайлас", LIGHT_CYAN),
            ("Субъект No4 стал бы манипулировать тысячами", "Сайлас", LIGHT_CYAN),
            ("Субъект No7 раскрыл бы секреты правительства. Началась бы война", "Сайлас", LIGHT_CYAN),
            ("Субъект No11… вы даже не представляете, на что она была способна", "Сайлас", LIGHT_CYAN),
            ("Ты не бог", "Кайл", KAIL_COLOR),
            ("Ты не имел права решать", "Кайл", KAIL_COLOR),
            ("Кто-то должен", "Сайлас", LIGHT_CYAN),
            ("Если не я — то кто? Харт", "Сайлас", LIGHT_CYAN),
            ("Она хуже", "Сайлас", LIGHT_CYAN),
            ("Она убивает без расчётов", "Сайлас", LIGHT_CYAN),
            ("Без логики", "Сайлас", LIGHT_CYAN),
            ("Я хотя бы знаю зачем", "Сайлас", LIGHT_CYAN),
            ("Ты чудовище", "Люция", YELLOW),
            ("Я математик", "Сайлас", LIGHT_CYAN),
            ("И числа не врут", "Сайлас", LIGHT_CYAN),
            ("Ты забыл о главном", "Кайл", KAIL_COLOR),
            ("О чём", "Сайлас", LIGHT_CYAN),
            ("О выборе", "Кайл", KAIL_COLOR),
            ("О том, что люди могут меняться", "Кайл", KAIL_COLOR),
            ("Ты не учёл это в своих расчётах", "Кайл", KAIL_COLOR),
            ("Сайлас смотрит на меня", None, WHITE),
            ("В его глазах — трещина", None, WHITE),
            ("Может быть", "Сайлас", LIGHT_CYAN),
            ("Но сейчас не время для философии", "Сайлас", LIGHT_CYAN),
            ("Что вы будете делать? Убьёте меня? Сдадите?", "Сайлас", LIGHT_CYAN),
            ("Ты пойдёшь с нами", "Люция", YELLOW),
            ("В башню", "Люция", YELLOW),
            ("А после — ответишь за всё", "Люция", YELLOW),
            ("Сайлас кивает", None, WHITE),
            ("Закрывает блокнот", None, WHITE),
            ("Хорошо", "Сайлас", LIGHT_CYAN),
            ("Я принимаю любой исход", "Сайлас", LIGHT_CYAN),
            ("Мы выходим из комнаты", None, WHITE),
            ("Сайлас идёт впереди", None, WHITE),
            ("Я смотрю ему в спину", None, WHITE)
        ]

    def load_background(self, path):
        if not path:
            self.secret_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.secret_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.secret_bg_scaled = None
        else:
            self.secret_bg_scaled = None

    def load_portraits(self, lucia_path, lucia_str_path, lucia_gnev_path, lucia_resh_path,
                       sailas_ras_path, sailas_ist_path, sailas_oder_path,
                       max_path, max_gnev_path, iina_path, iina_str_path):
        if os.path.exists(lucia_path):
            try:
                original = pygame.image.load(lucia_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(lucia_str_path):
            try:
                original = pygame.image.load(lucia_str_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_str_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(lucia_gnev_path):
            try:
                original = pygame.image.load(lucia_gnev_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_gnev_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(lucia_resh_path):
            try:
                original = pygame.image.load(lucia_resh_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_resh_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(sailas_ras_path):
            try:
                original = pygame.image.load(sailas_ras_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_ras_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(sailas_ist_path):
            try:
                original = pygame.image.load(sailas_ist_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_ist_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(sailas_oder_path):
            try:
                original = pygame.image.load(sailas_oder_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_oder_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(max_path):
            try:
                original = pygame.image.load(max_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(max_gnev_path):
            try:
                original = pygame.image.load(max_gnev_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.max_gnev_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(iina_path):
            try:
                original = pygame.image.load(iina_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(iina_str_path):
            try:
                original = pygame.image.load(iina_str_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.iina_str_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, portraits_data, max_alive):
        self.load_background(bg_path)
        self.load_portraits(**portraits_data)
        self.max_alive = max_alive
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False

            if not self.max_alive:
                next_idx = self.text_index + 1
                if next_idx < len(self.texts):
                    next_speaker = self.texts[next_idx][1]
                    if next_speaker == "Макс":
                        self.text_index += 1

            self.text_index += 1

            if not self.max_alive and self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]
                if current_speaker == "Макс":
                    self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Люция":
                    if "бледнеет" in self.texts[self.text_index][0] or "Что? Нет" in self.texts[self.text_index][0]:
                        self.current_portrait_visible = "lucia_str"
                    elif "чудовище" in self.texts[self.text_index][0] or "правда" in self.texts[self.text_index][0]:
                        self.current_portrait_visible = "lucia_gnev"
                    elif "Ты пойдёшь" in self.texts[self.text_index][0]:
                        self.current_portrait_visible = "lucia_resh"
                    else:
                        self.current_portrait_visible = "lucia"
                elif current_speaker == "Сайлас":
                    if "Правда" in self.texts[self.text_index][0] or "Я не собираюсь" in self.texts[self.text_index][0]:
                        self.current_portrait_visible = "sailas_ist"
                    elif "Вы не понимаете" in self.texts[self.text_index][0] or "Я спасал мир" in self.texts[self.text_index][0]:
                        self.current_portrait_visible = "sailas_oder"
                    else:
                        self.current_portrait_visible = "sailas_ras"
                elif current_speaker == "Макс" and self.max_alive:
                    self.current_portrait_visible = "max_gnev"
                elif current_speaker == "Ийна":
                    self.current_portrait_visible = "iina_str"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    start_idx = 0
                    if not self.max_alive and len(self.texts) > 0 and self.texts[0][1] == "Макс":
                        start_idx = 1
                    self.current_text = self.texts[start_idx][0]
                    self.current_speaker = self.texts[start_idx][1]
                    self.current_color = self.texts[start_idx][2]
                    self.text_index = start_idx
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.secret_bg_scaled:
            self.screen.blit(self.secret_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "lucia_str" and self.lucia_str_portrait_scaled:
            x = (self.screen_width - self.lucia_str_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_str_portrait_scaled.get_height()
            self.screen.blit(self.lucia_str_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "lucia_gnev" and self.lucia_gnev_portrait_scaled:
            x = (self.screen_width - self.lucia_gnev_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_gnev_portrait_scaled.get_height()
            self.screen.blit(self.lucia_gnev_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "lucia_resh" and self.lucia_resh_portrait_scaled:
            x = (self.screen_width - self.lucia_resh_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_resh_portrait_scaled.get_height()
            self.screen.blit(self.lucia_resh_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "sailas_ras" and self.sailas_ras_portrait_scaled:
            x = (self.screen_width - self.sailas_ras_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_ras_portrait_scaled.get_height()
            self.screen.blit(self.sailas_ras_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "sailas_ist" and self.sailas_ist_portrait_scaled:
            x = (self.screen_width - self.sailas_ist_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_ist_portrait_scaled.get_height()
            self.screen.blit(self.sailas_ist_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "sailas_oder" and self.sailas_oder_portrait_scaled:
            x = (self.screen_width - self.sailas_oder_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_oder_portrait_scaled.get_height()
            self.screen.blit(self.sailas_oder_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "max_gnev" and self.max_gnev_portrait_scaled and self.max_alive:
            x = (self.screen_width - self.max_gnev_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.max_gnev_portrait_scaled.get_height()
            self.screen.blit(self.max_gnev_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "iina_str" and self.iina_str_portrait_scaled:
            x = (self.screen_width - self.iina_str_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.iina_str_portrait_scaled.get_height()
            self.screen.blit(self.iina_str_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ФИНАЛ - СЦЕНА 1: ТИШИНА ПЕРЕД БУРЕЙ
# ============================================================================

class Act12SilenceBeforeStormScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.max_portrait = None
        self.max_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None
        self.max_alive = True

        self.texts = [
            ("23:00", None, WHITE),
            ("Башня директора", None, WHITE),
            ("Старое здание", None, WHITE),
            ("Каменные стены", None, WHITE),
            ("Мы идём в темноте", None, WHITE),
            ("Сайлас — впереди", None, WHITE),
            ("Под конвоем", None, WHITE),
            ("Но он не сопротивляется", None, WHITE),
            ("Ийна, сколько у нас времени", "Люция", YELLOW),
            ("Десять минут", "Ийна", GREEN),
            ("Потом система восстановится", "Ийна", GREEN),
            ("Я чувствую их", "Макс", MAX_COLOR),
            ("Они знают, что мы здесь", "Макс", MAX_COLOR),
            ("Мы поднимаемся по лестнице", None, WHITE),
            ("Каждый шаг — как удар сердца", None, WHITE),
            ("Сегодня всё кончится", "Кайл", KAIL_COLOR),
            ("Так или иначе", "Кайл", KAIL_COLOR)
        ]

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_portraits(self, lucia_path, iina_path, max_path):
        if os.path.exists(lucia_path):
            try:
                original = pygame.image.load(lucia_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(iina_path):
            try:
                original = pygame.image.load(iina_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(max_path):
            try:
                original = pygame.image.load(max_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.max_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, portraits_data, max_alive):
        self.load_background(bg_path)
        self.load_portraits(**portraits_data)
        self.max_alive = max_alive
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False

            if not self.max_alive:
                next_idx = self.text_index + 1
                if next_idx < len(self.texts):
                    next_speaker = self.texts[next_idx][1]
                    if next_speaker == "Макс":
                        self.text_index += 1

            self.text_index += 1

            if not self.max_alive and self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]
                if current_speaker == "Макс":
                    self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Люция":
                    self.current_portrait_visible = "lucia"
                elif current_speaker == "Ийна":
                    self.current_portrait_visible = "iina"
                elif current_speaker == "Макс" and self.max_alive:
                    self.current_portrait_visible = "max"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    start_idx = 0
                    if not self.max_alive and len(self.texts) > 11 and self.texts[11][1] == "Макс":
                        start_idx = 13
                    self.show_text = True
                    self.current_text = self.texts[start_idx][0]
                    self.current_speaker = self.texts[start_idx][1]
                    self.current_color = self.texts[start_idx][2]
                    self.text_index = start_idx
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "max" and self.max_portrait_scaled and self.max_alive:
            x = (self.screen_width - self.max_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.max_portrait_scaled.get_height()
            self.screen.blit(self.max_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready
# ============================================================================
# ФИНАЛ - СЦЕНА 2: ХОЛОДНАЯ УЛЫБКА ХАРТ
# ============================================================================

class Act12HartOfficeScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.dir_bg = None
        self.dir_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.hart_portrait = None
        self.hart_portrait_scaled = None
        self.sailas_portrait = None
        self.sailas_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None
        self.hart_visible = False

        self.texts = [
            ("Дверь открывается", None, WHITE),
            ("Внутри — темно", None, WHITE),
            ("Только свет от мониторов", None, WHITE),
            ("И она", None, WHITE),
            ("Стоит у окна", None, WHITE),
            ("Спиной к нам", None, WHITE),
            ("Я ждала вас", "Харт", SILVER_GRAY),
            ("Ровно в 23:00", "Харт", SILVER_GRAY),
            ("Как по расписанию", "Харт", SILVER_GRAY),
            ("Она поворачивается", None, WHITE),
            ("Улыбается", None, WHITE),
            ("Улыбка не доходит до глаз", None, WHITE),
            ("Сайлас, ты с ними? Я ожидала большего", "Харт", SILVER_GRAY),
            ("Вероятность моего предательства — 89%", "Сайлас", LIGHT_CYAN),
            ("Ты должна была предвидеть", "Сайлас", LIGHT_CYAN),
            ("Ты убивала их", "Люция", YELLOW),
            ("Своими руками", "Люция", YELLOW),
            ("Я лечила", "Харт", SILVER_GRAY),
            ("Пробуждение — это рак", "Харт", SILVER_GRAY),
            ("Я вырезала опухоль", "Харт", SILVER_GRAY),
            ("Ты стирала им личность", "Кайл", KAIL_COLOR),
            ("Превращала в овощей", "Кайл", KAIL_COLOR),
            ("Это не лечение", "Кайл", KAIL_COLOR),
            ("Это убийство", "Кайл", KAIL_COLOR),
            ("Вы дети", "Харт", SILVER_GRAY),
            ("Вы не понимаете", "Харт", SILVER_GRAY),
            ("Ваши способности — бомба замедленного действия", "Харт", SILVER_GRAY),
            ("Я спасала миллионы", "Харт", SILVER_GRAY),
            ("Всё кончено, Харт", "Кайл", KAIL_COLOR),
            ("Данные у нас", "Кайл", KAIL_COLOR),
            ("Лаборатория найдена", "Кайл", KAIL_COLOR),
            ("Завтра об этом узнает весь мир", "Кайл", KAIL_COLOR),
            ("Харт смотрит на меня", None, WHITE),
            ("Долго", None, WHITE),
            ("Потом смеётся", None, WHITE),
            ("Тихо", None, WHITE),
            ("Страшно", None, WHITE),
            ("Вы думаете, я одна", "Харт", SILVER_GRAY),
            ("Что это только моя идея", "Харт", SILVER_GRAY),
            ("Что ты имеешь в виду", "Кайл", KAIL_COLOR),
            ("Узнаете", "Харт", SILVER_GRAY),
            ("Когда будет поздно", "Харт", SILVER_GRAY),
            ("Она нажимает кнопку на стене", None, WHITE),
            ("Свет гаснет", None, WHITE)
        ]

    def load_background(self, path):
        if not path:
            self.dir_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.dir_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.dir_bg_scaled = None
        else:
            self.dir_bg_scaled = None

    def load_portraits(self, hart_path, sailas_path, lucia_path):
        if os.path.exists(hart_path):
            try:
                original = pygame.image.load(hart_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.hart_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(sailas_path):
            try:
                original = pygame.image.load(sailas_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(lucia_path):
            try:
                original = pygame.image.load(lucia_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, portraits_data):
        self.load_background(bg_path)
        self.load_portraits(**portraits_data)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.hart_visible = False
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if self.text_index >= 6 and not self.hart_visible:
                    self.hart_visible = True
                    self.current_portrait_visible = "hart"

                if current_speaker == "Сайлас":
                    self.current_portrait_visible = "sailas"
                elif current_speaker == "Люция":
                    self.current_portrait_visible = "lucia"
                elif current_speaker == "Харт":
                    self.current_portrait_visible = "hart"
                elif current_speaker == "Кайл":
                    if not self.hart_visible:
                        self.current_portrait_visible = None
                else:
                    if not self.hart_visible:
                        self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.dir_bg_scaled:
            self.screen.blit(self.dir_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "hart" and self.hart_portrait_scaled:
            x = (self.screen_width - self.hart_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.hart_portrait_scaled.get_height()
            self.screen.blit(self.hart_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "sailas" and self.sailas_portrait_scaled:
            x = (self.screen_width - self.sailas_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_portrait_scaled.get_height()
            self.screen.blit(self.sailas_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ФИНАЛ - СЦЕНА 3: ПОГОНЯ
# ============================================================================

class Act12ChaseScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.corridor_bg = None
        self.corridor_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.hart_portrait = None
        self.hart_portrait_scaled = None
        self.lucia_portrait = None
        self.lucia_portrait_scaled = None
        self.iina_portrait = None
        self.iina_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = None
        self.flash_alpha = 0
        self.flash_active = False
        self.flash_timer = 0
        self.max_alive = True

        self.texts = [
            ("Свет гаснет", None, WHITE),
            ("Темнота", None, WHITE),
            ("Крики", None, WHITE),
            ("Она уходит! Чёрный выход!", "Макс", MAX_COLOR),
            ("Держите её!", "Люция", YELLOW),
            ("Бежим", None, WHITE),
            ("Лабиринт коридоров", None, WHITE),
            ("Шаги", None, WHITE),
            ("Дыхание", None, WHITE),
            ("Хлопки дверей", None, WHITE),
            ("Я отключила лифт! Она не уйдёт!", "Ийна", GREEN),
            ("Вдруг вспышка - дверь", None, WHITE),
            ("Харт стоит на лестнице", None, WHITE),
            ("Смотрит на нас", None, WHITE),
            ("Вы победили", "Харт", SILVER_GRAY),
            ("Сегодня", "Харт", SILVER_GRAY),
            ("Но завтра придёт кто-то другой", "Харт", SILVER_GRAY),
            ("Проект не умирает", "Харт", SILVER_GRAY),
            ("Она делает шаг назад", None, WHITE),
            ("И исчезает в темноте", None, WHITE),
            ("Где она!", "Люция", YELLOW),
            ("Сигнал пропал", "Ийна", GREEN),
            ("Её нет в здании", "Ийна", GREEN),
            ("Тишина", None, WHITE),
            ("Харт ушла", None, WHITE),
            ("Но её слова остались", None, WHITE),
            ("«Проект не умирает»", None, SILVER_GRAY)
        ]

    def load_background(self, path):
        if not path:
            self.corridor_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.corridor_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.corridor_bg_scaled = None
        else:
            self.corridor_bg_scaled = None

    def load_portraits(self, hart_path, lucia_path, iina_path):
        if os.path.exists(hart_path):
            try:
                original = pygame.image.load(hart_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.hart_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(lucia_path):
            try:
                original = pygame.image.load(lucia_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass
        if os.path.exists(iina_path):
            try:
                original = pygame.image.load(iina_path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.iina_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, portraits_data, max_alive):
        self.load_background(bg_path)
        self.load_portraits(**portraits_data)
        self.max_alive = max_alive
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = None
        self.flash_alpha = 0
        self.flash_active = False
        self.flash_timer = 0
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False

            if not self.max_alive:
                next_idx = self.text_index + 1
                if next_idx < len(self.texts):
                    next_speaker = self.texts[next_idx][1]
                    if next_speaker == "Макс":
                        self.text_index += 1

            self.text_index += 1

            if not self.max_alive and self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]
                if current_speaker == "Макс":
                    self.text_index += 1

            if self.text_index == 11:
                self.flash_active = True
                self.flash_alpha = 255

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Харт":
                    self.current_portrait_visible = "hart"
                elif current_speaker == "Люция":
                    self.current_portrait_visible = "lucia"
                elif current_speaker == "Ийна":
                    self.current_portrait_visible = "iina"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    start_idx = 0
                    if not self.max_alive and len(self.texts) > 3 and self.texts[3][1] == "Макс":
                        start_idx = 4
                    self.show_text = True
                    self.current_text = self.texts[start_idx][0]
                    self.current_speaker = self.texts[start_idx][1]
                    self.current_color = self.texts[start_idx][2]
                    self.text_index = start_idx
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

        if self.flash_active:
            self.flash_timer += 1
            if self.flash_timer > 5:
                self.flash_alpha -= 30
                if self.flash_alpha <= 0:
                    self.flash_alpha = 0
                    self.flash_active = False
                    self.flash_timer = 0

    def draw(self):
        if self.corridor_bg_scaled:
            self.screen.blit(self.corridor_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "hart" and self.hart_portrait_scaled:
            x = (self.screen_width - self.hart_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.hart_portrait_scaled.get_height()
            self.screen.blit(self.hart_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "lucia" and self.lucia_portrait_scaled:
            x = (self.screen_width - self.lucia_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_portrait_scaled.get_height()
            self.screen.blit(self.lucia_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "iina" and self.iina_portrait_scaled:
            x = (self.screen_width - self.iina_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.iina_portrait_scaled.get_height()
            self.screen.blit(self.iina_portrait_scaled, (x, y))

        if self.flash_active and self.flash_alpha > 0:
            flash_surface = pygame.Surface((self.screen_width, self.screen_height))
            flash_surface.fill(WHITE)
            flash_surface.set_alpha(self.flash_alpha)
            self.screen.blit(flash_surface, (0, 0))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ФИНАЛ - СЦЕНА 4: ПРИЗНАНИЕ ЛЮЦИИ И ВЫБОР
# ============================================================================

class Act12LuciaConfessionScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.roof_bg = None
        self.roof_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.lucia_pain_portrait = None
        self.lucia_pain_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.choice_shown = False
        self.choice_made = None
        self.current_portrait_visible = "lucia_pain"
        self.branch_texts = []
        self.branch_text_index = 0
        self.showing_branch = False
        self.waiting_for_choice = False

        self.texts = [
            ("После погони я нахожу Люцию на крыше", None, WHITE),
            ("Она стоит одна", None, WHITE),
            ("Смотрит на звёзды", None, WHITE),
            ("Ветер развевает её волосы", None, WHITE),
            ("Ты здесь", "Кайл", KAIL_COLOR),
            ("Я искал тебя", "Кайл", KAIL_COLOR),
            ("Она не оборачивается", None, WHITE),
            ("Голос тихий. Дрожит", None, WHITE),
            ("Я должна тебе кое-что сказать", "Люция", YELLOW),
            ("И ты должен знать", "Люция", YELLOW),
            ("Прежде чем мы пойдём дальше", "Люция", YELLOW),
            ("Она поворачивается", None, WHITE),
            ("В её глазах — слёзы", None, WHITE),
            ("Впервые я вижу её такой", None, WHITE),
            ("Без маски", None, WHITE),
            ("Без брони", None, WHITE),
            ("Я работала на Харт", "Люция", YELLOW),
            ("В начале", "Люция", YELLOW),
            ("Когда только создавала группу", "Люция", YELLOW),
            ("Я думала, что спасаю нас", "Люция", YELLOW),
            ("Что если я буду давать ей имена — она оставит остальных в покое", "Люция", YELLOW),
            ("Я не знала, что их убивают", "Люция", YELLOW),
            ("Думала… их просто исключат", "Люция", YELLOW),
            ("Когда узнала… было поздно", "Люция", YELLOW),
            ("Она смотрит мне в глаза", None, WHITE),
            ("Впервые — не прячет взгляд", None, WHITE),
            ("Я не прошу прощения", "Люция", YELLOW),
            ("Я просто хочу, чтобы ты знал — всё, что между нами было… это не ложь", "Люция", YELLOW),
            ("Это единственное, что было правдой", "Люция", YELLOW),
            ("Ветер", None, WHITE),
            ("Тишина", None, WHITE),
            ("Звёзды над нами", None, WHITE)
        ]

        self.save_texts = [
            ("Я смотрю на неё", None, WHITE),
            ("Долго", None, WHITE),
            ("В голове — её слова", None, WHITE),
            ("«Единственное, что было правдой»", None, YELLOW),
            ("Я не могу тебя бросить", "Кайл", KAIL_COLOR),
            ("Ты ошибалась", "Кайл", KAIL_COLOR),
            ("Но ты пыталась исправить", "Кайл", KAIL_COLOR),
            ("Мы справимся вместе", "Кайл", KAIL_COLOR),
            ("Люция смотрит на меня", None, WHITE),
            ("Слёзы текут по щекам", None, WHITE),
            ("Ты… правда? После всего?", "Люция", YELLOW),
            ("Правда", "Кайл", KAIL_COLOR),
            ("Она делает шаг ко мне", None, WHITE),
            ("Я обнимаю её", None, WHITE),
            ("Ветер", None, WHITE),
            ("Звёзды", None, WHITE),
            ("Тишина", None, WHITE),
            ("Спасибо", "Люция", YELLOW),
            ("Я не заслуживаю…", "Люция", YELLOW),
            ("Не говори так", "Кайл", KAIL_COLOR),
            ("Просто будь рядом", "Кайл", KAIL_COLOR)
        ]

        self.duty_texts = [
            ("Я смотрю на неё", None, WHITE),
            ("Боль", None, WHITE),
            ("Гнев", None, WHITE),
            ("Любовь", None, WHITE),
            ("Всё смешалось", None, WHITE),
            ("Ты должна ответить за то, что сделала", "Кайл", KAIL_COLOR),
            ("Я не могу это игнорировать", "Кайл", KAIL_COLOR),
            ("Даже ради тебя", "Кайл", KAIL_COLOR),
            ("Люция смотрит на меня", None, WHITE),
            ("Боль в глазах", None, WHITE),
            ("Но она кивает", None, WHITE),
            ("Я понимаю", "Люция", YELLOW),
            ("Прощай", "Люция", YELLOW),
            ("Стой! Что ты собираешься делать?", "Кайл", KAIL_COLOR),
            ("Ответа я не получил", None, WHITE),
            ("Она ушла", None, WHITE),
            ("Её фигура исчезла в темноте", None, WHITE),
            ("Я остаюсь один", None, WHITE),
            ("На холодной крыше", None, WHITE),
            ("Под звёздами", None, WHITE)
        ]

        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.roof_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.roof_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.roof_bg_scaled = None
        else:
            self.roof_bg_scaled = None

    def load_lucia_pain_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.lucia_pain_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, lucia_pain_path):
        self.load_background(bg_path)
        self.load_lucia_pain_portrait(lucia_pain_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.choice_shown = False
        self.choice_made = None
        self.current_portrait_visible = "lucia_pain"
        self.showing_branch = False
        self.waiting_for_choice = False
        self.branch_texts = []
        self.branch_text_index = 0
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.showing_branch and self.can_click:
            self.can_click = False
            self.branch_text_index += 1
            if self.branch_text_index < len(self.branch_texts):
                text_data = self.branch_texts[self.branch_text_index]
                self.current_text = text_data[0]
                self.current_speaker = text_data[1]
                self.current_color = text_data[2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return None

        if self.show_text and self.can_click and not self.choice_shown and not self.showing_branch:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = self.texts[self.text_index][1]
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.choice_shown = True
                self.show_text = False
                self.waiting_for_choice = True
                return None
        return None

    def make_choice(self, choice):
        self.choice_made = choice
        self.choice_shown = False
        self.waiting_for_choice = False
        self.showing_branch = True
        self.branch_text_index = 0

        if choice == "save":
            self.branch_texts = self.save_texts
        else:
            self.branch_texts = self.duty_texts

        if self.branch_texts:
            text_data = self.branch_texts[0]
            self.current_text = text_data[0]
            self.current_speaker = text_data[1]
            self.current_color = text_data[2]
            self.show_text = True
            self.can_click = True

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw_choice(self, mouse_pos):
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.fill(BLACK)
        overlay.set_alpha(200)
        self.screen.blit(overlay, (0, 0))

        title_font = pygame.font.Font(None, 52)
        title = title_font.render("Что ты выберешь?", True, CHALK_WHITE)
        title_rect = title.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 120))
        self.screen.blit(title, title_rect)

        button_width = 300
        button_height = 60
        button_spacing = 30
        start_y = self.screen_height // 2 - 40

        save_rect = pygame.Rect(
            self.screen_width // 2 - button_width // 2,
            start_y,
            button_width,
            button_height
        )

        duty_rect = pygame.Rect(
            self.screen_width // 2 - button_width // 2,
            start_y + button_height + button_spacing,
            button_width,
            button_height
        )

        save_hover = save_rect.collidepoint(mouse_pos)
        duty_hover = duty_rect.collidepoint(mouse_pos)

        save_color = (80, 120, 80) if save_hover else (40, 60, 40)
        pygame.draw.rect(self.screen, save_color, save_rect, border_radius=10)
        pygame.draw.rect(self.screen, CHALK_WHITE, save_rect, 2, border_radius=10)

        button_font = pygame.font.Font(None, 36)
        save_text = button_font.render("Спасти Люцию", True, CHALK_WHITE)
        save_text_rect = save_text.get_rect(center=save_rect.center)
        self.screen.blit(save_text, save_text_rect)

        duty_color = (120, 60, 60) if duty_hover else (60, 40, 40)
        pygame.draw.rect(self.screen, duty_color, duty_rect, border_radius=10)
        pygame.draw.rect(self.screen, CHALK_WHITE, duty_rect, 2, border_radius=10)

        duty_text = button_font.render("Выбрать долг", True, CHALK_WHITE)
        duty_text_rect = duty_text.get_rect(center=duty_rect.center)
        self.screen.blit(duty_text, duty_text_rect)

        self.save_rect = save_rect
        self.duty_rect = duty_rect

    def handle_choice_click(self, pos):
        if hasattr(self, 'save_rect') and self.save_rect.collidepoint(pos):
            self.make_choice("save")
            return "save"
        elif hasattr(self, 'duty_rect') and self.duty_rect.collidepoint(pos):
            self.make_choice("duty")
            return "duty"
        return None

    def draw(self):
        if self.roof_bg_scaled:
            self.screen.blit(self.roof_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "lucia_pain" and self.lucia_pain_portrait_scaled:
            x = (self.screen_width - self.lucia_pain_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.lucia_pain_portrait_scaled.get_height()
            self.screen.blit(self.lucia_pain_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.choice_shown and self.waiting_for_choice and not self.fade_out_active:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_choice(mouse_pos)

        if self.show_text and self.current_text and not self.fade_out_active and not self.choice_shown:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready

    def get_choice(self):
        return self.choice_made
# ============================================================================
# ФИНАЛ - СЦЕНА 5: БЕЗУМИЕ САЙЛАСА
# ============================================================================

class Act12SailasMadnessScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.bash_bg = None
        self.bash_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_oder_portrait = None
        self.sailas_oder_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.current_portrait_visible = "sailas_oder"

        self.texts = [
            ("Я спустился вниз", None, WHITE),
            ("Там, где нас ждал Сайлас", None, WHITE),
            ("Он сидит на полу", None, WHITE),
            ("Обложенный листами с расчётами", None, WHITE),
            ("Глаза горят", None, WHITE),
            ("Сайлас", "Кайл", KAIL_COLOR),
            ("Он поднимает голову", None, WHITE),
            ("Улыбается", None, WHITE),
            ("Странно", None, WHITE),
            ("Безумно", None, WHITE),
            ("Ты знаешь, почему я не убил тебя", "Сайлас", LIGHT_CYAN),
            ("Потому что я не прошёл твой порог", "Кайл", KAIL_COLOR),
            ("Нет", "Сайлас", LIGHT_CYAN),
            ("Потому что я надеялся", "Сайлас", LIGHT_CYAN),
            ("Твоя вероятность — 52%", "Сайлас", LIGHT_CYAN),
            ("Ниже, чем у других. Я думал… может, ты докажешь, что я ошибался", "Сайлас", LIGHT_CYAN),
            ("Он встаёт", None, WHITE),
            ("Берёт блокнот", None, WHITE),
            ("Но сейчас… сейчас я вижу, что ошибся", "Сайлас", LIGHT_CYAN),
            ("Ты такой же", "Сайлас", LIGHT_CYAN),
            ("Ты тоже угроза", "Сайлас", LIGHT_CYAN),
            ("Твои действия — непредсказуемы", "Сайлас", LIGHT_CYAN),
            ("Ты — хаос", "Сайлас", LIGHT_CYAN),
            ("Ты не бог", "Кайл", KAIL_COLOR),
            ("Ты не имел права решать, кому жить, а кому умирать", "Кайл", KAIL_COLOR),
            ("Он открывает блокнот", None, WHITE),
            ("Листы летят на пол", None, WHITE),
            ("Субъект No1 — 96%", "Сайлас", LIGHT_CYAN),
            ("Субъект No4 — 98%", "Сайлас", LIGHT_CYAN),
            ("Субъект No7 — 97%", "Сайлас", LIGHT_CYAN),
            ("Субъект No11 — 99%", "Сайлас", LIGHT_CYAN),
            ("Они должны были умереть", "Сайлас", LIGHT_CYAN),
            ("Иначе погибли бы тысячи", "Сайлас", LIGHT_CYAN),
            ("А кто дал тебе право считать эти проценты", "Кайл", KAIL_COLOR),
            ("Кто сказал, что ты не ошибся", "Кайл", KAIL_COLOR),
            ("Сайлас замирает", None, WHITE),
            ("Смотрит на меня", None, WHITE),
            ("В его глазах — трещина", None, WHITE),
            ("Я не ошибся", "Сайлас", LIGHT_CYAN),
            ("Я не могу ошибаться", "Сайлас", LIGHT_CYAN),
            ("Это математика", "Сайлас", LIGHT_CYAN),
            ("Она не лжёт", "Сайлас", LIGHT_CYAN),
            ("Математика не знает всего", "Кайл", KAIL_COLOR),
            ("Она не знает любви", "Кайл", KAIL_COLOR),
            ("Дружбы", "Кайл", KAIL_COLOR),
            ("Жертвы", "Кайл", KAIL_COLOR),
            ("Выбора", "Кайл", KAIL_COLOR),
            ("Ты забыл, что люди — не числа", "Кайл", KAIL_COLOR),
            ("Сайлас смотрит на свои расчёты", None, WHITE),
            ("Рука дрожит", None, WHITE)
        ]

    def load_background(self, path):
        if not path:
            self.bash_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.bash_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.bash_bg_scaled = None
        else:
            self.bash_bg_scaled = None

    def load_sailas_oder_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_oder_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, sailas_oder_path):
        self.load_background(bg_path)
        self.load_sailas_oder_portrait(sailas_oder_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_portrait_visible = "sailas_oder"
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Сайлас":
                    self.current_portrait_visible = "sailas_oder"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return False
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw(self):
        if self.bash_bg_scaled:
            self.screen.blit(self.bash_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "sailas_oder" and self.sailas_oder_portrait_scaled:
            x = (self.screen_width - self.sailas_oder_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_oder_portrait_scaled.get_height()
            self.screen.blit(self.sailas_oder_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text and not self.fade_out_active:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready


# ============================================================================
# ФИНАЛ - СЦЕНА 6: ВЫБОР СУДЬБЫ САЙЛАСА
# ============================================================================

class Act12SailasChoiceScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.bash_bg = None
        self.bash_bg_scaled = None
        self.bg_offset_x = 0
        self.bg_offset_y = 0
        self.sailas_ist_portrait = None
        self.sailas_ist_portrait_scaled = None
        self.sailas_ras_portrait = None
        self.sailas_ras_portrait_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.choice_shown = False
        self.choice_made = None
        self.current_portrait_visible = "sailas_ist"
        self.branch_texts = []
        self.branch_text_index = 0
        self.showing_branch = False
        self.waiting_for_choice = False
        self.button_rects = {}

        self.texts = [
            ("Сайлас смотрит на меня", None, WHITE),
            ("Его рука с блокнотом дрожит", None, WHITE),
            ("Впервые я вижу его неуверенным", None, WHITE),
            ("Что ты выберешь? Убить меня? Сдать?", "Сайлас", LIGHT_CYAN),
            ("Тишина", None, WHITE),
            ("Ветер в окнах", None, WHITE),
            ("Скрип половиц", None, WHITE),
            ("Я выбираю…", "Кайл", KAIL_COLOR)
        ]

        self.kill_texts = [
            ("Я смотрю на него", None, WHITE),
            ("На его руки", None, WHITE),
            ("На блокнот", None, WHITE),
            ("На цифры", None, WHITE),
            ("На лица тех, кого он убил", None, WHITE),
            ("Ты убивал", "Кайл", KAIL_COLOR),
            ("Теперь ты заплатишь", "Кайл", KAIL_COLOR),
            ("Сайлас не сопротивляется", None, WHITE),
            ("Закрывает глаза", None, WHITE),
            ("Может… так и надо", "Сайлас", LIGHT_CYAN),
            ("В моих расчётах не было этого варианта", "Сайлас", LIGHT_CYAN),
            ("Смерть от твоей руки", "Сайлас", LIGHT_CYAN),
            ("Вероятность — 23%", "Сайлас", LIGHT_CYAN),
            ("Ниже, чем я думал", "Сайлас", LIGHT_CYAN),
            ("Я делаю шаг", None, WHITE),
            ("Всё кончается быстро", None, WHITE),
            ("Сайлас падает на пол", None, WHITE),
            ("Блокнот выпадает из рук", None, WHITE),
            ("Листы разлетаются", None, WHITE),
            ("Я стою над ним", None, WHITE),
            ("Смотрю на его лицо", None, WHITE),
            ("Он улыбается", None, WHITE),
            ("Спокойный", None, WHITE),
            ("Наконец-то", None, WHITE)
        ]

        self.arrest_texts = [
            ("Я смотрю на него", None, WHITE),
            ("На его руки", None, WHITE),
            ("На блокнот", None, WHITE),
            ("На его безумные глаза", None, WHITE),
            ("Ты ответишь за свои преступления", "Кайл", KAIL_COLOR),
            ("По закону", "Кайл", KAIL_COLOR),
            ("Не по моей воле", "Кайл", KAIL_COLOR),
            ("Сайлас кивает", None, WHITE),
            ("Спокойно", None, WHITE),
            ("Слишком спокойно", None, WHITE),
            ("Я принимаю любой исход", "Сайлас", LIGHT_CYAN),
            ("Числа не врут, но судьи… посмотрим", "Сайлас", LIGHT_CYAN),
            ("Вероятность того, что меня оправдают — 4%", "Сайлас", LIGHT_CYAN),
            ("Вероятность пожизненного — 89%", "Сайлас", LIGHT_CYAN),
            ("Остальное — смерть", "Сайлас", LIGHT_CYAN),
            ("Его уводят", None, WHITE),
            ("Он не сопротивляется", None, WHITE),
            ("На прощание оборачивается", None, WHITE),
            ("Ты был прав", "Сайлас", LIGHT_CYAN),
            ("Я не учёл выбор", "Сайлас", LIGHT_CYAN),
            ("Прощай, Субъект No12", "Сайлас", LIGHT_CYAN)
        ]

        self.release_texts = [
            ("Я смотрю на него", None, WHITE),
            ("Вспоминаю все смерти", None, WHITE),
            ("Все жертвы", None, WHITE),
            ("И его глаза", None, WHITE),
            ("Безумные", None, WHITE),
            ("Одинокие", None, WHITE),
            ("Уходи", "Кайл", KAIL_COLOR),
            ("Но если я узнаю, что ты снова убил — я найду тебя", "Кайл", KAIL_COLOR),
            ("Где бы ты ни был", "Кайл", KAIL_COLOR),
            ("Сайлас смотрит на меня", None, WHITE),
            ("Удивлённо", None, WHITE),
            ("Непонимающе", None, WHITE),
            ("Ты отпускаешь меня? Почему?", "Сайлас", LIGHT_CYAN),
            ("Потому что я не хочу быть как ты", "Кайл", KAIL_COLOR),
            ("Потому что убийство не решит ничего", "Кайл", KAIL_COLOR),
            ("Потому что я выбираю не твой путь", "Кайл", KAIL_COLOR),
            ("Сайлас молчит", None, WHITE),
            ("Потом улыбается", None, WHITE),
            ("Грустно", None, WHITE),
            ("Устало", None, WHITE),
            ("Ты странный", "Сайлас", LIGHT_CYAN),
            ("Нелогичный", "Сайлас", LIGHT_CYAN),
            ("Неправильный", "Сайлас", LIGHT_CYAN),
            ("Может… в этом и есть ответ", "Сайлас", LIGHT_CYAN),
            ("Он уходит", None, WHITE),
            ("Исчезает в темноте", None, WHITE),
            ("Блокнот остаётся на полу", None, WHITE),
            ("Я смотрю ему вслед", None, WHITE)
        ]

        self.convince_texts = [
            ("Я смотрю на него", None, WHITE),
            ("В его глазах — трещина", None, WHITE),
            ("Первый раз за всё время", None, WHITE),
            ("Ты не должен продолжать", "Кайл", KAIL_COLOR),
            ("Твои расчёты не учитывают главного — выбора", "Кайл", KAIL_COLOR),
            ("Люди могут меняться", "Кайл", KAIL_COLOR),
            ("Я докажу тебе это", "Кайл", KAIL_COLOR),
            ("Не сегодня", "Кайл", KAIL_COLOR),
            ("Не завтра", "Кайл", KAIL_COLOR),
            ("Но я докажу", "Кайл", KAIL_COLOR),
            ("Сайлас смотрит на меня", None, WHITE),
            ("Его лицо ломается", None, WHITE),
            ("Слёзы текут по щекам", None, WHITE),
            ("Я… я убивал", "Сайлас", LIGHT_CYAN),
            ("Столько лет", "Сайлас", LIGHT_CYAN),
            ("И всё зря", "Сайлас", LIGHT_CYAN),
            ("Каждый раз я думал, что спасаю", "Сайлас", LIGHT_CYAN),
            ("А сейчас… сейчас я не знаю", "Сайлас", LIGHT_CYAN),
            ("Он роняет блокнот", None, WHITE),
            ("Опускается на колени", None, WHITE),
            ("Руки дрожат", None, WHITE),
            ("Если ты ошибаешься", "Сайлас", LIGHT_CYAN),
            ("Если мир рухнет", "Сайлас", LIGHT_CYAN),
            ("Если я был прав", "Сайлас", LIGHT_CYAN),
            ("Что тогда?", "Сайлас", LIGHT_CYAN),
            ("Тогда мы будем вместе его спасать", "Кайл", KAIL_COLOR),
            ("Не убивая", "Кайл", KAIL_COLOR),
            ("Не стирая", "Кайл", KAIL_COLOR),
            ("А по-другому", "Кайл", KAIL_COLOR),
            ("Я не знаю как", "Кайл", KAIL_COLOR),
            ("Но мы найдём способ", "Кайл", KAIL_COLOR),
            ("Сайлас поднимает голову", None, WHITE),
            ("Смотрит на меня", None, WHITE),
            ("В его глазах — надежда", None, WHITE),
            ("В первый раз", None, WHITE),
            ("Ты правда веришь в это?", "Сайлас", LIGHT_CYAN),
            ("Верю", "Кайл", KAIL_COLOR),
            ("Сайлас встаёт", None, WHITE),
            ("Подбирает блокнот", None, WHITE),
            ("Закрывает его", None, WHITE),
            ("Я помогу вам", "Сайлас", LIGHT_CYAN),
            ("Всё расскажу", "Сайлас", LIGHT_CYAN),
            ("Пойду под суд", "Сайлас", LIGHT_CYAN),
            ("Всё, что нужно", "Сайлас", LIGHT_CYAN),
            ("Но… ты будешь рядом?", "Сайлас", LIGHT_CYAN),
            ("Буду", "Кайл", KAIL_COLOR)
        ]

        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def load_background(self, path):
        if not path:
            self.bash_bg_scaled = None
            return
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                orig_width = original.get_width()
                orig_height = original.get_height()
                scale_x = self.screen_width / orig_width
                scale_y = self.screen_height / orig_height
                scale = max(scale_x, scale_y)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                self.bash_bg_scaled = pygame.transform.scale(original, (new_width, new_height))
                self.bg_offset_x = (new_width - self.screen_width) // 2
                self.bg_offset_y = (new_height - self.screen_height) // 2
            except:
                self.bash_bg_scaled = None
        else:
            self.bash_bg_scaled = None

    def load_sailas_ist_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_ist_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def load_sailas_ras_portrait(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                w = int(self.screen_width * 0.6)
                h = int(original.get_height() * (w / original.get_width()))
                self.sailas_ras_portrait_scaled = pygame.transform.scale(original, (w, h))
            except:
                pass

    def start(self, bg_path, sailas_ist_path, sailas_ras_path):
        self.load_background(bg_path)
        self.load_sailas_ist_portrait(sailas_ist_path)
        self.load_sailas_ras_portrait(sailas_ras_path)
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.transition_ready = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.choice_shown = False
        self.choice_made = None
        self.current_portrait_visible = "sailas_ist"
        self.showing_branch = False
        self.waiting_for_choice = False
        self.branch_texts = []
        self.branch_text_index = 0
        self.button_rects = {}
        self.current_text = ""
        self.current_speaker = ""
        self.current_color = WHITE

    def handle_click(self):
        if self.showing_branch and self.can_click:
            self.can_click = False
            self.branch_text_index += 1
            if self.branch_text_index < len(self.branch_texts):
                text_data = self.branch_texts[self.branch_text_index]
                self.current_text = text_data[0]
                self.current_speaker = text_data[1]
                self.current_color = text_data[2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return None

        if self.show_text and self.can_click and not self.choice_shown and not self.showing_branch:
            self.can_click = False
            self.text_index += 1

            if self.text_index < len(self.texts):
                current_speaker = self.texts[self.text_index][1]

                if current_speaker == "Сайлас":
                    self.current_portrait_visible = "sailas_ist"
                else:
                    self.current_portrait_visible = None

                self.current_text = self.texts[self.text_index][0]
                self.current_speaker = current_speaker
                self.current_color = self.texts[self.text_index][2]
                self.show_text = True
                self.can_click = True
                return None
            else:
                self.choice_shown = True
                self.show_text = False
                self.waiting_for_choice = True
                return None
        return None

    def make_choice(self, choice):
        self.choice_made = choice
        self.choice_shown = False
        self.waiting_for_choice = False
        self.showing_branch = True
        self.branch_text_index = 0

        if choice == "kill":
            self.branch_texts = self.kill_texts
            self.current_portrait_visible = "sailas_ist"
        elif choice == "arrest":
            self.branch_texts = self.arrest_texts
            self.current_portrait_visible = "sailas_ist"
        elif choice == "release":
            self.branch_texts = self.release_texts
            self.current_portrait_visible = "sailas_ist"
        else:
            self.branch_texts = self.convince_texts
            self.current_portrait_visible = "sailas_ras"

        if self.branch_texts:
            text_data = self.branch_texts[0]
            self.current_text = text_data[0]
            self.current_speaker = text_data[1]
            self.current_color = text_data[2]
            self.show_text = True
            self.can_click = True

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    self.current_text = self.texts[0][0]
                    self.current_speaker = self.texts[0][1]
                    self.current_color = self.texts[0][2]
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True
                    self.transition_ready = True

    def draw_choice(self, mouse_pos):
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.fill(BLACK)
        overlay.set_alpha(200)
        self.screen.blit(overlay, (0, 0))

        title_font = pygame.font.Font(None, 48)
        title = title_font.render("Что сделать с Сайласом?", True, CHALK_WHITE)
        title_rect = title.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 150))
        self.screen.blit(title, title_rect)

        button_width = 350
        button_height = 55
        button_spacing = 15
        start_y = self.screen_height // 2 - 100

        buttons = [
            ("УБИТЬ", "kill", (120, 60, 60)),
            ("СДАТЬ ВЛАСТЯМ", "arrest", (80, 80, 120)),
            ("ОТПУСТИТЬ", "release", (80, 120, 80)),
            ("ПЕРЕУБЕДИТЬ", "convince", (120, 100, 60))
        ]

        self.button_rects = {}
        button_font = pygame.font.Font(None, 32)

        for i, (text, key, color) in enumerate(buttons):
            rect = pygame.Rect(
                self.screen_width // 2 - button_width // 2,
                start_y + i * (button_height + button_spacing),
                button_width,
                button_height
            )
            self.button_rects[key] = rect

            hover = rect.collidepoint(mouse_pos)
            btn_color = (color[0] + 30, color[1] + 30, color[2] + 30) if hover else color
            pygame.draw.rect(self.screen, btn_color, rect, border_radius=8)
            pygame.draw.rect(self.screen, CHALK_WHITE, rect, 2, border_radius=8)

            btn_text = button_font.render(text, True, CHALK_WHITE)
            btn_text_rect = btn_text.get_rect(center=rect.center)
            self.screen.blit(btn_text, btn_text_rect)

    def handle_choice_click(self, pos):
        if not self.button_rects:
            return None
        for key, rect in self.button_rects.items():
            if rect.collidepoint(pos):
                self.make_choice(key)
                return key
        return None

    def draw(self):
        if self.bash_bg_scaled:
            self.screen.blit(self.bash_bg_scaled, (-self.bg_offset_x, -self.bg_offset_y))
        else:
            self.screen.fill(BLACK)

        if self.current_portrait_visible == "sailas_ist" and self.sailas_ist_portrait_scaled:
            x = (self.screen_width - self.sailas_ist_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_ist_portrait_scaled.get_height()
            self.screen.blit(self.sailas_ist_portrait_scaled, (x, y))
        elif self.current_portrait_visible == "sailas_ras" and self.sailas_ras_portrait_scaled:
            x = (self.screen_width - self.sailas_ras_portrait_scaled.get_width()) // 2
            y = self.screen_height - self.sailas_ras_portrait_scaled.get_height()
            self.screen.blit(self.sailas_ras_portrait_scaled, (x, y))

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.choice_shown and self.waiting_for_choice and not self.fade_out_active:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_choice(mouse_pos)

        if self.show_text and self.current_text and not self.fade_out_active and not self.choice_shown:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete

    def can_transition(self):
        return self.transition_ready

    def get_choice(self):
        return self.choice_made


# ============================================================================
# ФИНАЛ - СЦЕНА 7: ЭПИЛОГ
# ============================================================================

class Act12EndingScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.ending_art = None
        self.ending_art_scaled = None
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.ending_type = None
        self.texts = []
        self.current_text = ""
        self.current_speaker = None
        self.current_color = WHITE
        self.final1_art_path = None
        self.final2_art_path = None
        self.final3_art_path = None
        self.roof_night_path = None
        self.roof_path = None  # ДОБАВЛЕНО

    def load_ending_art(self, path):
        if os.path.exists(path):
            try:
                original = pygame.image.load(path)
                self.ending_art_scaled = pygame.transform.scale(original, (self.screen_width, self.screen_height))
            except:
                self.ending_art_scaled = None
        else:
            self.ending_art_scaled = None

    def setup_ending(self, ending_type, lucia_choice, sailas_choice, max_alive):
        self.ending_type = ending_type

        if ending_type == "victory_freedom":
            self.load_ending_art(self.final1_art_path)
            self.texts = [
                ("Рассвет", None, WHITE),
                ("Академия встречает нас первыми лучами солнца", None, WHITE),
                ("Всё кончено", None, WHITE),
                ("Харт сбежала", None, WHITE),
                ("Но её лаборатория уничтожена", None, WHITE),
                ("Сайлас либо мёртв, либо за решёткой, либо раскаялся", None, WHITE),
                ("Данные — в сети", None, WHITE),
                ("Правда — наружу", None, WHITE),
                ("Мы стоим у ворот", None, WHITE),
                ("Люция — рядом", None, WHITE),
                ("Её рука в моей", None, WHITE),
                ("Макс — рядом", None, WHITE),
                ("Ийна — с нами", None, WHITE),
                ("Что теперь?", "Люция", YELLOW),
                ("Теперь мы живём", "Кайл", KAIL_COLOR),
                ("По-настоящему", "Кайл", KAIL_COLOR),
                ("Без масок", "Кайл", KAIL_COLOR),
                ("Без страха", "Кайл", KAIL_COLOR),
                ("Мы уходим", None, WHITE),
                ("Академия остаётся позади", None, WHITE),
                ("Солнце поднимается выше", None, WHITE),
                ("Новый день начинается", None, WHITE)
            ]
        elif ending_type == "victory_loss":
            self.load_ending_art(self.final2_art_path)
            self.texts = [
                ("Серое небо", None, WHITE),
                ("Холодный ветер", None, WHITE),
                ("Две могилы рядом", None, WHITE),
                ("Макс", None, WHITE),
                ("Люция", None, WHITE),
                ("Те, кто были рядом", None, WHITE),
                ("Те, кого мы потеряли", None, WHITE),
                ("Я стою один", None, WHITE),
                ("В одной руке — серебряный кулон Люции", None, WHITE),
                ("В другой — старый кожаный шнурок Макса", None, WHITE),
                ("Мы победили", None, WHITE),
                ("Сайлас наказан", None, WHITE),
                ("Но цена была слишком высока", None, WHITE),
                ("Я отдал слишком много", None, WHITE),
                ("Я кладу кулон и шнурок на могилы", None, WHITE),
                ("Поворачиваюсь", None, WHITE),
                ("Ухожу", None, WHITE),
                ("Не оглядываясь", None, WHITE)
            ]
        elif ending_type == "new_hunter":
            self.load_ending_art(self.final3_art_path)
            self.texts = [
                ("Ночь", None, WHITE),
                ("Кабинет директора", None, WHITE),
                ("Я сижу в его кресле", None, WHITE),
                ("Передо мной — список имён", None, WHITE),
                ("Субъект No13, No14, No15…", None, WHITE),
                ("Я стал тем, с кем боролся", None, WHITE),
                ("Новым Охотником", None, WHITE),
                ("Но теперь я решаю, кто жив, а кто мёртв", None, WHITE),
                ("На столе — блокнот Сайласа", None, WHITE),
                ("Я открываю его", None, WHITE),
                ("На первой странице — моё имя", None, WHITE),
                ("Субъект No12", None, WHITE),
                ("Вероятность катастрофы — 0%", None, WHITE),
                ("Перечёркнуто", None, WHITE),
                ("Рядом — новое число", None, WHITE),
                ("100%", None, WHITE),
                ("Я закрываю блокнот", None, WHITE),
                ("Улыбаюсь", None, WHITE),
                ("В темноте", None, WHITE)
            ]
        elif ending_type == "max_dead_lucia_alive":
            # ИСПРАВЛЕНО: используем roof_path вместо roof_night_path
            self.load_ending_art(self.roof_path)
            self.texts = [
                ("Рассвет", None, WHITE),
                ("Мы сидим на крыше", None, WHITE),
                ("Люция положила голову мне на плечо", None, WHITE),
                ("Её рука — в моей", None, WHITE),
                ("Макс… он искупил свою вину", "Люция", YELLOW),
                ("Да. И мы будем помнить", "Кайл", KAIL_COLOR),
                ("Она сжимает мою руку", None, WHITE),
                ("Что теперь?", "Люция", YELLOW),
                ("Теперь мы живём. За него тоже", "Кайл", KAIL_COLOR),
                ("Мы смотрим на восходящее солнце", None, WHITE),
                ("Впереди — новая жизнь", None, WHITE),
                ("С памятью о тех, кого мы потеряли", None, WHITE)
            ]
        else:  # lucia_dead_max_alive
            # ИСПРАВЛЕНО: используем roof_path вместо roof_night_path
            self.load_ending_art(self.roof_path)
            self.texts = [
                ("Рассвет", None, WHITE),
                ("Мы сидим на крыше", None, WHITE),
                ("Макс рядом", None, WHITE),
                ("Между нами — кулон Люции", None, WHITE),
                ("Её уже нет", None, WHITE),
                ("Мы победили", None, WHITE),
                ("Сайлас наказан", None, WHITE),
                ("Харт сбежала", None, WHITE),
                ("Но её лаборатория уничтожена", None, WHITE),
                ("Правда — в сети", None, WHITE),
                ("Весь мир узнает", None, WHITE),
                ("Она знала, на что шла", "Макс", MAX_COLOR),
                ("Она выбрала долг", "Макс", MAX_COLOR),
                ("Искупление", "Макс", MAX_COLOR),
                ("Я знаю", "Кайл", KAIL_COLOR),
                ("Но это не облегчает потерю, я её не остановил", "Кайл", KAIL_COLOR),
                ("Тишина", None, WHITE),
                ("Ветер", None, WHITE),
                ("Макс берёт кулон", None, WHITE),
                ("Смотрит на него", None, WHITE),
                ("Она хотела, чтобы мы жили", "Макс", MAX_COLOR),
                ("По-настоящему", "Макс", MAX_COLOR),
                ("Не просто выживали", "Макс", MAX_COLOR),
                ("Тогда давай жить", "Кайл", KAIL_COLOR),
                ("За неё тоже", "Кайл", KAIL_COLOR),
                ("Макс кивает", None, WHITE),
                ("Протягивает мне кулон", None, WHITE),
                ("Я беру его", None, WHITE),
                ("Надеваю на шею", None, WHITE),
                ("Пойдём", "Кайл", KAIL_COLOR),
                ("Нас ждут", "Кайл", KAIL_COLOR),
                ("Мы встаём", None, WHITE),
                ("Смотрим на восходящее солнце", None, WHITE),
                ("Впереди — новая жизнь", None, WHITE),
                ("С памятью о тех, кого мы потеряли", None, WHITE),
                ("С теми, кто остался", None, WHITE)
            ]

    # ИСПРАВЛЕНО: добавлен параметр roof_path
    def start(self, ending_type, lucia_choice, sailas_choice, max_alive,
              final1_path, final2_path, final3_path, roof_night_path, roof_path):
        self.final1_art_path = final1_path
        self.final2_art_path = final2_path
        self.final3_art_path = final3_path
        self.roof_night_path = roof_night_path
        self.roof_path = roof_path  # ДОБАВЛЕНО

        self.setup_ending(ending_type, lucia_choice, sailas_choice, max_alive)

        self.fade_alpha = 255
        self.fade_active = True
        self.fade_in = True
        self.fade_out_active = False
        self.text_index = 0
        self.show_text = False
        self.can_click = True
        self.complete = False
        self.current_text = ""
        self.current_speaker = None
        self.current_color = WHITE

    def handle_click(self):
        if self.show_text and self.can_click:
            self.can_click = False
            self.text_index += 1
            if self.text_index < len(self.texts):
                text_data = self.texts[self.text_index]
                self.current_text = text_data[0]
                self.current_speaker = text_data[1] if len(text_data) > 1 else None
                self.current_color = text_data[2] if len(text_data) > 2 else WHITE
                self.show_text = True
                self.can_click = True
                return False
            else:
                self.fade_out_active = True
                self.fade_active = True
                self.fade_in = False
                return True
        return False

    def update(self):
        if self.fade_active:
            if self.fade_in:
                self.fade_alpha -= 5
                if self.fade_alpha <= 0:
                    self.fade_alpha = 0
                    self.fade_active = False
                    self.show_text = True
                    text_data = self.texts[0]
                    self.current_text = text_data[0]
                    self.current_speaker = text_data[1] if len(text_data) > 1 else None
                    self.current_color = text_data[2] if len(text_data) > 2 else WHITE
                    self.can_click = True
            else:
                self.fade_alpha += 5
                if self.fade_alpha >= 255:
                    self.fade_alpha = 255
                    self.fade_active = False
                    self.complete = True

    def draw(self):
        if self.ending_art_scaled:
            self.screen.blit(self.ending_art_scaled, (0, 0))
        else:
            self.screen.fill(BLACK)

        if self.fade_active and self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen_width, self.screen_height))
            fade_surface.fill(BLACK)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))

        if self.show_text and self.current_text:
            box_w = int(self.screen_width * 0.8)
            box_h = 150
            box_x = (self.screen_width - box_w) // 2
            box_y = self.screen_height - box_h - 30
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            box.fill((0, 0, 0, 180))
            self.screen.blit(box, (box_x, box_y))
            pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)
            if self.current_speaker:
                name = self.font.render(self.current_speaker, True, self.current_color)
                self.screen.blit(name, (box_x + 20, box_y + 20))
                pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50), (box_x + box_w - 20, box_y + 50), 1)
                text_y = box_y + 70
            else:
                text_y = box_y + box_h // 2 - self.font.get_height() // 2
            text = self.font.render(self.current_text, True, self.current_color)
            text_x = box_x + 20
            self.screen.blit(text, (text_x, text_y))
            if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# ФИНАЛ - ФИНАЛЬНЫЙ ЧЕРНЫЙ ЭКРАН
# ============================================================================

class Act12FinalBlackScene:
    def __init__(self, screen, screen_width, screen_height, font):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.complete = False
        self.waiting_for_menu = True
        self.title_alpha = 255
        self.alpha_direction = 0

    def start(self):
        self.complete = False
        self.waiting_for_menu = True
        self.title_alpha = 255
        self.alpha_direction = 0

    def handle_click(self):
        if self.waiting_for_menu:
            return True
        return False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        if self.title_alpha > 0:
            title_font = pygame.font.Font(None, 72)
            title_surf = title_font.render("СУБЪЕКТ No 12", True, WHITE)
            title_surf.set_alpha(self.title_alpha)
            title_rect = title_surf.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(title_surf, title_rect)

    def is_complete(self):
        return self.complete

    def is_waiting_for_menu(self):
        return self.waiting_for_menu
# ============================================================================
# ПРОЛОГ
# ============================================================================

class Prologue:
    def __init__(self, screen, screen_width, screen_height, font, character_name):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font
        self.name = character_name
        self.art = None
        self.art_path = None

        self.black_texts = [
            ("Мне снится один и тот же сон", None, WHITE),
            ("Снова", None, WHITE)
        ]
        self.scene_texts = [
            ("Огромный зал", None, WHITE),
            ("Сотни парт", None, WHITE),
            ("Ни одного человека", None, WHITE),
            ("Только я", None, WHITE),
            ("И… он", None, WHITE),
            ("Он сидит за партой", None, WHITE),
            ("Смотрит на меня", None, WHITE),
            ("Улыбается", None, WHITE),
            ("Он похож на меня", None, WHITE),
            ("Но это не я", None, WHITE),
            ("Ты забыл, кто мы", "Кайл", LIGHT_BLUE),
            ("Но экзамен скоро начнётся", "Кайл", LIGHT_BLUE)
        ]

        self.state = "title"
        self.title_timer = 0
        self.title_alpha = 0
        self.title_duration = 420
        self.art_alpha = 0
        self.complete = False
        self.is_art_phase = False

        self.current_text = ""
        self.current_speaker = None
        self.current_color = CHALK_WHITE
        self.show_text = False
        self.can_click = True

        self.black_index = 0
        self.scene_index = 0

        self.zoom_level = 1.0
        self.zoom_target = 1.15
        self.zoom_target_close = 1.35
        self.zoom_speed = 0.008
        self.zoom_active = False
        self.zoom_started = False
        self.zoom_complete = False
        self.zoom_close_started = False

        self.zoom_center_x = WIDTH * 0.25
        self.zoom_center_y = HEIGHT * 0.5

    def load_art(self, path):
        self.art_path = path
        if os.path.exists(path):
            try:
                self.art = pygame.image.load(path)
                self.art = pygame.transform.scale(self.art, (self.screen_width, self.screen_height))
            except:
                pass

    def start(self, art_path):
        self.load_art(art_path)
        self.reset()

    def reset(self):
        self.state = "title"
        self.title_timer = 0
        self.title_alpha = 0
        self.art_alpha = 0
        self.complete = False
        self.is_art_phase = False
        self.current_text = ""
        self.current_speaker = None
        self.current_color = CHALK_WHITE
        self.show_text = False
        self.can_click = True
        self.black_index = 0
        self.scene_index = 0
        self.zoom_level = 1.0
        self.zoom_active = False
        self.zoom_started = False
        self.zoom_complete = False
        self.zoom_close_started = False

    def handle_click(self):
        if self.state == "title":
            self.title_timer = self.title_duration
            return False

        if self.show_text and self.can_click:
            self.can_click = False

            if not self.is_art_phase:
                self.black_index += 1
                if self.black_index < len(self.black_texts):
                    text_data = self.black_texts[self.black_index]
                    self.current_text = text_data[0]
                    self.current_speaker = text_data[1]
                    self.current_color = text_data[2]
                    self.show_text = True
                    self.can_click = True
                else:
                    self.is_art_phase = True
                    self.current_text = ""
                    self.current_speaker = None
                    self.show_text = False
                    self.scene_index = 0
                    if self.scene_index < len(self.scene_texts):
                        text_data = self.scene_texts[self.scene_index]
                        self.current_text = text_data[0]
                        self.current_speaker = text_data[1]
                        self.current_color = text_data[2]
                        self.show_text = True
                        self.can_click = True
            else:
                self.scene_index += 1
                if self.scene_index < len(self.scene_texts):
                    text_data = self.scene_texts[self.scene_index]
                    self.current_text = text_data[0]
                    self.current_speaker = text_data[1]
                    self.current_color = text_data[2]
                    self.show_text = True
                    self.can_click = True
                else:
                    self.complete = True
                    return True

        return False

    def update(self):
        if self.state == "title":
            self.title_timer += 1

            if self.title_timer < 60:
                self.title_alpha = min(255, self.title_timer * 4)
            elif self.title_timer > self.title_duration - 60:
                self.title_alpha = max(0, 255 - (self.title_timer - (self.title_duration - 60)) * 4)
            else:
                self.title_alpha = 255

            if self.title_timer >= self.title_duration:
                self.state = "scene"
                text_data = self.black_texts[0]
                self.current_text = text_data[0]
                self.current_speaker = text_data[1]
                self.current_color = text_data[2]
                self.show_text = True
                self.can_click = True

        elif self.state == "scene":
            if self.is_art_phase and self.art_alpha < 255:
                self.art_alpha += 10
                if self.art_alpha > 255:
                    self.art_alpha = 255

            if not self.zoom_started and self.is_art_phase and self.scene_index >= 5:
                self.zoom_started = True
                self.zoom_active = True

            if self.zoom_active and not self.zoom_complete:
                if self.zoom_level < self.zoom_target:
                    self.zoom_level += self.zoom_speed
                    if self.zoom_level >= self.zoom_target:
                        self.zoom_level = self.zoom_target
                        self.zoom_active = False
                        self.zoom_complete = True

            if not self.zoom_close_started and self.is_art_phase and self.scene_index >= 9:
                self.zoom_close_started = True
                self.zoom_active = True
                self.zoom_target = self.zoom_target_close

            if self.zoom_active and self.zoom_close_started and self.zoom_level < self.zoom_target_close:
                self.zoom_level += self.zoom_speed
                if self.zoom_level >= self.zoom_target_close:
                    self.zoom_level = self.zoom_target_close
                    self.zoom_active = False

    def draw(self):
        if self.state == "title":
            self.screen.fill(BLACK)
            title_font = pygame.font.Font(None, 72)
            title_surf = title_font.render("Субъект No 12", True, WHITE)
            title_surf.set_alpha(self.title_alpha)
            title_rect = title_surf.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(title_surf, title_rect)

        elif self.state == "scene":
            if self.is_art_phase and self.art:
                if self.zoom_level != 1.0:
                    new_width = int(self.screen_width * self.zoom_level)
                    new_height = int(self.screen_height * self.zoom_level)
                    zoomed_art = pygame.transform.scale(self.art, (new_width, new_height))

                    offset_x = int(self.zoom_center_x * self.zoom_level - self.zoom_center_x)
                    offset_y = int(self.zoom_center_y * self.zoom_level - self.zoom_center_y)

                    offset_x = min(offset_x, new_width - self.screen_width)
                    offset_y = min(offset_y, new_height - self.screen_height)
                    offset_x = max(offset_x, 0)
                    offset_y = max(offset_y, 0)

                    self.screen.blit(zoomed_art, (-offset_x, -offset_y))
                else:
                    art_copy = self.art.copy()
                    art_copy.set_alpha(self.art_alpha)
                    self.screen.blit(art_copy, (0, 0))
            else:
                self.screen.fill(BLACK)

            if self.show_text and self.current_text:
                box_w = int(self.screen_width * 0.8)
                box_h = 150
                box_x = (self.screen_width - box_w) // 2
                box_y = self.screen_height - box_h - 30

                box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
                box.fill((0, 0, 0, 180))
                self.screen.blit(box, (box_x, box_y))
                pygame.draw.rect(self.screen, CHALK_GRAY, (box_x, box_y, box_w, box_h), 2)

                if self.current_speaker:
                    name = self.font.render(self.current_speaker, True, self.current_color)
                    self.screen.blit(name, (box_x + 20, box_y + 20))
                    pygame.draw.line(self.screen, CHALK_GRAY, (box_x + 20, box_y + 50),
                                     (box_x + box_w - 20, box_y + 50), 1)
                    text_y = box_y + 70
                else:
                    text_y = box_y + box_h // 2 - self.font.get_height() // 2

                text = self.font.render(self.current_text, True, self.current_color)
                self.screen.blit(text, (box_x + 20, text_y))

                if self.can_click and pygame.time.get_ticks() % 1000 < 500:
                    arrow = pygame.font.Font(None, 24).render("▼", True, CHALK_GRAY)
                    self.screen.blit(arrow, (box_x + box_w - 40, box_y + box_h - 25))

    def is_complete(self):
        return self.complete


# ============================================================================
# МЕНЮ ПАУЗЫ
# ============================================================================

class PauseMenu:
    def __init__(self, font):
        self.font = font
        self.active = False
        self.buttons = []
        cx = WIDTH // 2
        y = HEIGHT // 2 - 100
        texts = ["ПРОДОЛЖИТЬ", "В МЕНЮ", "ВЫЙТИ"]
        for i, t in enumerate(texts):
            self.buttons.append({
                "text": t,
                "rect": pygame.Rect(cx - 100, y + i * 70, 200, 50),
                "hover": False
            })

    def update(self, pos):
        for b in self.buttons:
            b["hover"] = b["rect"].collidepoint(pos)

    def click(self, pos):
        for b in self.buttons:
            if b["rect"].collidepoint(pos):
                return b["text"]
        return None

    def draw(self, screen):
        if not self.active:
            return
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        screen.blit(overlay, (0, 0))

        for b in self.buttons:
            color = CHALK_WHITE if b["hover"] else CHALK_GRAY
            pygame.draw.rect(screen, color, b["rect"], 2)
            text = self.font.render(b["text"], True, CHALK_WHITE)
            text_rect = text.get_rect(center=b["rect"].center)
            screen.blit(text, text_rect)


# ============================================================================
# ОСНОВНАЯ ИГРА (ПОЛНАЯ ВЕРСИЯ С ДНЯМИ 1-12 И ФИНАЛОМ)
# ============================================================================

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Субъект No 12")
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 28)
        self.load_resources()

        self.state = State.BOOT
        self.boot = BootScreen()
        self.logo = LogoScreen("assets/pictures/logo.png") if os.path.exists("assets/pictures/logo.png") else None
        self.disclaimer = DisclaimerScreen(self.font)
        self.menu = MainMenu(self.font, self.bg_menu)

        # Сцены Дня 1
        self.prologue = None
        self.wake_up = None
        self.thoughts = None
        self.act1_transition = None
        self.morning_scene = None
        self.corridor_scene = None
        self.lesson_scene = None
        self.canteen_scene = None
        self.lucia_scene = None
        self.evening_scene = None
        self.night_scene = None
        self.empty_corridor_scene = None
        self.insomnia_scene = None
        self.day2_transition = None

        # Сцены Дня 2
        self.day2_morning = None
        self.day2_corridor = None
        self.lecture_scene = None
        self.post_lecture_scene = None
        self.closed_wing_scene = None
        self.library_scene = None
        self.day2_night = None
        self.day3_transition = None

        # Сцены Дня 3
        self.day3_morning = None
        self.math_exam_scene = None
        self.sailas_corridor_scene = None
        self.day3_library_scene = None
        self.awakening_scene = None
        self.day3_night = None
        self.day4_transition = None

        # Сцены Дня 4
        self.day4_morning = None
        self.day4_math_test = None
        self.day4_corridor_warning = None
        self.day4_old_library = None
        self.day4_secret_room = None
        self.day5_transition = None

        # Сцены Дня 5
        self.day5_morning = None
        self.day5_corridor_rules = None
        self.day5_secret_meeting = None
        self.day5_medical_infiltration = None
        self.day5_archive_find = None
        self.day5_video_procedure = None
        self.day5_meeting_krein = None
        self.day6_transition = None

        # Сцены Дня 6
        self.day6_morning = None
        self.day6_corridor = None
        self.day6_secret_room_traitor = None
        self.day6_roof_confrontation = None
        self.day6_corridor_return = None
        self.day6_insomnia = None
        self.day7_transition = None

        # Сцены Дня 7
        self.day7_morning = None
        self.day7_corridor_max = None
        self.day7_secret_planning = None
        self.day7_abandoned_trap = None
        self.day7_secret_return = None
        self.day7_insomnia = None
        self.day8_transition = None

        # Сцены Дня 8
        self.day8_morning = None
        self.day8_corridor_observe = None
        self.day8_library_analysis = None
        self.day8_dormitory_clues = None
        self.day8_preparation = None
        self.day9_transition = None

        # Сцены Дня 9
        self.day9_morning = None
        self.day9_gym_confrontation = None
        self.day9_confession_choice = None
        self.day9_secret_message = None
        self.day9_insomnia = None
        self.day10_transition = None

        # Сцены Дня 10
        self.day10_morning = None
        self.day10_corridor_branch = None
        self.day10_secret_planning = None
        self.day10_medical_path = None
        self.day10_hart_lab = None
        self.day10_insomnia = None
        self.day11_transition = None

        # Сцены Дня 11
        self.day11_morning = None
        self.day11_corridor_follow = None
        self.day11_library_analysis = None
        self.day11_sailas_room = None
        self.day11_preparation = None
        self.day12_transition = None

        # Сцены ФИНАЛА (День 12)
        self.act12_revelation = None
        self.act12_silence_before_storm = None
        self.act12_hart_office = None
        self.act12_chase = None
        self.act12_lucia_confession = None
        self.act12_sailas_madness = None
        self.act12_sailas_choice = None
        self.act12_ending = None
        self.act12_final_black = None

        # Для хранения выборов игрока
        self.player_choice = None
        self.lucia_choice = None
        self.sailas_choice = None

        self.pause = PauseMenu(self.font)

        self.menu_music_playing = False
        self.prologue_music_playing = False
        self.wake_music_playing = False
        self.music_paused = False
        self.music_pause_pos = 0

        # Пути к ресурсам
        self.art_path = None
        art_paths = ["assets/art/prologue.png", "prologue.png"]
        for path in art_paths:
            if os.path.exists(path):
                self.art_path = path
                break

        self.room_path = None
        room_paths = ["assets/backgrounds/roomGG.jpg", "roomGG.jpg", "assets/backgrounds/roomGG.png", "roomGG.png"]
        for path in room_paths:
            if os.path.exists(path):
                self.room_path = path
                break
        if self.room_path is None:
            self.room_path = ""

        self.corridor_path = None
        corridor_paths = ["assets/backgrounds/koridor(day).png", "koridor(day).png"]
        for path in corridor_paths:
            if os.path.exists(path):
                self.corridor_path = path
                break
        if self.corridor_path is None:
            self.corridor_path = ""

        self.morning_room_path = None
        morning_paths = ["assets/backgrounds/DayRoomGG.png", "DayRoomGG.png"]
        for path in morning_paths:
            if os.path.exists(path):
                self.morning_room_path = path
                break
        if self.morning_room_path is None:
            self.morning_room_path = ""

        self.class_path = None
        class_paths = ["assets/backgrounds/ClassHistory.png", "ClassHistory.png"]
        for path in class_paths:
            if os.path.exists(path):
                self.class_path = path
                break
        if self.class_path is None:
            self.class_path = ""

        self.krein_portrait_path = None
        krein_paths = ["assets/portraits/krein.jpg", "krein.jpg"]
        for path in krein_paths:
            if os.path.exists(path):
                self.krein_portrait_path = path
                break
        if self.krein_portrait_path is None:
            self.krein_portrait_path = ""

        self.max_portrait_path = None
        max_paths = ["assets/portraits/max.png", "max.png"]
        for path in max_paths:
            if os.path.exists(path):
                self.max_portrait_path = path
                break
        if self.max_portrait_path is None:
            self.max_portrait_path = ""

        self.lucia_portrait_path = None
        lucia_paths = ["assets/portraits/Lucia.png", "Lucia.png"]
        for path in lucia_paths:
            if os.path.exists(path):
                self.lucia_portrait_path = path
                break
        if self.lucia_portrait_path is None:
            self.lucia_portrait_path = ""

        self.canteen_path = None
        canteen_paths = ["assets/backgrounds/stolovka.png", "stolovka.png"]
        for path in canteen_paths:
            if os.path.exists(path):
                self.canteen_path = path
                break
        if self.canteen_path is None:
            self.canteen_path = ""

        self.dorm_path = None
        dorm_paths = ["assets/backgrounds/obchezhitia.png", "obchezhitia.png"]
        for path in dorm_paths:
            if os.path.exists(path):
                self.dorm_path = path
                break
        if self.dorm_path is None:
            self.dorm_path = ""

        self.dorm_night_path = None
        dorm_night_paths = ["assets/backgrounds/obchezhitiaN.png", "obchezhitiaN.png"]
        for path in dorm_night_paths:
            if os.path.exists(path):
                self.dorm_night_path = path
                break
        if self.dorm_night_path is None:
            self.dorm_night_path = ""

        self.lecture_path = None
        lecture_paths = ["assets/backgrounds/psih.png", "psih.png"]
        for path in lecture_paths:
            if os.path.exists(path):
                self.lecture_path = path
                break
        if self.lecture_path is None:
            self.lecture_path = ""

        self.hart_portrait_path = None
        hart_paths = ["assets/portraits/hart.png", "hart.png"]
        for path in hart_paths:
            if os.path.exists(path):
                self.hart_portrait_path = path
                break
        if self.hart_portrait_path is None:
            self.hart_portrait_path = ""

        self.closed_wing_path = None
        closed_paths = ["assets/backgrounds/closed.png", "closed.png"]
        for path in closed_paths:
            if os.path.exists(path):
                self.closed_wing_path = path
                break
        if self.closed_wing_path is None:
            self.closed_wing_path = ""

        self.security_portrait_path = None
        security_paths = ["assets/portraits/security.png", "security.png"]
        for path in security_paths:
            if os.path.exists(path):
                self.security_portrait_path = path
                break
        if self.security_portrait_path is None:
            self.security_portrait_path = ""

        self.library_path = None
        library_paths = ["assets/backgrounds/library.png", "library.png"]
        for path in library_paths:
            if os.path.exists(path):
                self.library_path = path
                break
        if self.library_path is None:
            self.library_path = ""

        self.iina_portrait_path = None
        iina_paths = ["assets/portraits/iina.png", "iina.png"]
        for path in iina_paths:
            if os.path.exists(path):
                self.iina_portrait_path = path
                break
        if self.iina_portrait_path is None:
            self.iina_portrait_path = ""

        self.math_path = None
        math_paths = ["assets/backgrounds/classMath.png", "classMath.png"]
        for path in math_paths:
            if os.path.exists(path):
                self.math_path = path
                break
        if self.math_path is None:
            self.math_path = ""

        self.sailas_portrait_path = None
        sailas_paths = ["assets/portraits/sailas.png", "sailas.png"]
        for path in sailas_paths:
            if os.path.exists(path):
                self.sailas_portrait_path = path
                break
        if self.sailas_portrait_path is None:
            self.sailas_portrait_path = ""

        self.corner_path = None
        corner_paths = ["assets/backgrounds/ygolok.png", "ygolok.png"]
        for path in corner_paths:
            if os.path.exists(path):
                self.corner_path = path
                break
        if self.corner_path is None:
            self.corner_path = ""

        self.old_library_path = None
        old_library_paths = ["assets/backgrounds/oldLib.png", "oldLib.png"]
        for path in old_library_paths:
            if os.path.exists(path):
                self.old_library_path = path
                break
        if self.old_library_path is None:
            self.old_library_path = ""

        self.secret_room_path = None
        secret_room_paths = ["assets/backgrounds/bg_secret_room.webp", "bg_secret_room.png", "secret_room.png"]
        for path in secret_room_paths:
            if os.path.exists(path):
                self.secret_room_path = path
                break
        if self.secret_room_path is None:
            self.secret_room_path = ""

        self.iina_sos_portrait_path = None
        iina_sos_paths = ["assets/portraits/iinaSOS.png", "iinaSOS.png"]
        for path in iina_sos_paths:
            if os.path.exists(path):
                self.iina_sos_portrait_path = path
                break
        if self.iina_sos_portrait_path is None:
            self.iina_sos_portrait_path = ""

        self.medical_corridor_path = None
        medical_corridor_paths = ["assets/backgrounds/MedKoridor.png", "MedKoridor.png"]
        for path in medical_corridor_paths:
            if os.path.exists(path):
                self.medical_corridor_path = path
                break
        if self.medical_corridor_path is None:
            self.medical_corridor_path = ""

        self.medical_archive_path = None
        medical_archive_paths = ["assets/backgrounds/MedArxiv.png", "MedArxiv.png"]
        for path in medical_archive_paths:
            if os.path.exists(path):
                self.medical_archive_path = path
                break
        if self.medical_archive_path is None:
            self.medical_archive_path = ""

        self.corridor_night_path = None
        corridor_night_paths = ["assets/backgrounds/koridor(night).png", "koridor(night).png"]
        for path in corridor_night_paths:
            if os.path.exists(path):
                self.corridor_night_path = path
                break
        if self.corridor_night_path is None:
            self.corridor_night_path = ""

        self.sailas_ras_portrait_path = None
        sailas_ras_paths = ["assets/portraits/sailasRas.png", "sailasRas.png"]
        for path in sailas_ras_paths:
            if os.path.exists(path):
                self.sailas_ras_portrait_path = path
                break
        if self.sailas_ras_portrait_path is None:
            self.sailas_ras_portrait_path = ""

        self.lucia_pain_portrait_path = None
        lucia_pain_paths = ["assets/portraits/LuciaPain.png", "LuciaPain.png"]
        for path in lucia_pain_paths:
            if os.path.exists(path):
                self.lucia_pain_portrait_path = path
                break
        if self.lucia_pain_portrait_path is None:
            self.lucia_pain_portrait_path = ""

        self.iina_str_portrait_path = None
        iina_str_paths = ["assets/portraits/iinaStr.png", "iinaStr.png"]
        for path in iina_str_paths:
            if os.path.exists(path):
                self.iina_str_portrait_path = path
                break
        if self.iina_str_portrait_path is None:
            self.iina_str_portrait_path = ""

        self.roof_night_path = None
        roof_night_paths = ["assets/backgrounds/roofN.png", "roofN.png"]
        for path in roof_night_paths:
            if os.path.exists(path):
                self.roof_night_path = path
                break
        if self.roof_night_path is None:
            self.roof_night_path = ""

        # ========== ДОБАВЛЕНО: путь для обычной крыши Roof.png (для концовок) ==========
        self.roof_path = None
        roof_paths = ["assets/backgrounds/Roof.png", "Roof.png"]
        for path in roof_paths:
            if os.path.exists(path):
                self.roof_path = path
                break
        if self.roof_path is None:
            self.roof_path = ""

        self.lucia_gnev_portrait_path = None
        lucia_gnev_paths = ["assets/portraits/LuciaGnev.png", "LuciaGnev.png"]
        for path in lucia_gnev_paths:
            if os.path.exists(path):
                self.lucia_gnev_portrait_path = path
                break
        if self.lucia_gnev_portrait_path is None:
            self.lucia_gnev_portrait_path = ""

        self.abandoned_path = None
        abandoned_paths = ["assets/backgrounds/zabKrilo.png", "zabKrilo.png"]
        for path in abandoned_paths:
            if os.path.exists(path):
                self.abandoned_path = path
                break
        if self.abandoned_path is None:
            self.abandoned_path = ""

        self.room_max_path = None
        room_max_paths = ["assets/backgrounds/roomMax.png", "roomMax.png"]
        for path in room_max_paths:
            if os.path.exists(path):
                self.room_max_path = path
                break
        if self.room_max_path is None:
            self.room_max_path = ""

        self.zkvnut_path = None
        zkvnut_paths = ["assets/backgrounds/ZKVnut.png", "ZKVnut.png"]
        for path in zkvnut_paths:
            if os.path.exists(path):
                self.zkvnut_path = path
                break
        if self.zkvnut_path is None:
            self.zkvnut_path = ""

        self.gym_path = None
        gym_paths = ["assets/backgrounds/gym.png", "gym.png"]
        for path in gym_paths:
            if os.path.exists(path):
                self.gym_path = path
                break
        if self.gym_path is None:
            self.gym_path = ""

        self.stid_max_portrait_path = None
        stid_max_paths = ["assets/portraits/stidMax.png", "stidMax.png"]
        for path in stid_max_paths:
            if os.path.exists(path):
                self.stid_max_portrait_path = path
                break
        if self.stid_max_portrait_path is None:
            self.stid_max_portrait_path = ""

        self.hart_lab_path = None
        hart_lab_paths = ["assets/backgrounds/hartLab.png", "hartLab.png"]
        for path in hart_lab_paths:
            if os.path.exists(path):
                self.hart_lab_path = path
                break
        if self.hart_lab_path is None:
            self.hart_lab_path = ""

        self.lucia_str_portrait_path = None
        lucia_str_paths = ["assets/portraits/LuciaStr.png", "LuciaStr.png"]
        for path in lucia_str_paths:
            if os.path.exists(path):
                self.lucia_str_portrait_path = path
                break
        if self.lucia_str_portrait_path is None:
            self.lucia_str_portrait_path = ""

        self.sailas_room_path = None
        sailas_room_paths = ["assets/backgrounds/roomSailas.png", "roomSailas.png"]
        for path in sailas_room_paths:
            if os.path.exists(path):
                self.sailas_room_path = path
                break
        if self.sailas_room_path is None:
            self.sailas_room_path = ""

        self.koridor_bash_path = None
        koridor_bash_paths = ["assets/backgrounds/koridorBash.png", "koridorBash.png"]
        for path in koridor_bash_paths:
            if os.path.exists(path):
                self.koridor_bash_path = path
                break
        if self.koridor_bash_path is None:
            self.koridor_bash_path = ""

        self.dir_path = None
        dir_paths = ["assets/backgrounds/dir.png", "dir.png"]
        for path in dir_paths:
            if os.path.exists(path):
                self.dir_path = path
                break
        if self.dir_path is None:
            self.dir_path = ""

        self.bash_path = None
        bash_paths = ["assets/backgrounds/bash.png", "bash.png"]
        for path in bash_paths:
            if os.path.exists(path):
                self.bash_path = path
                break
        if self.bash_path is None:
            self.bash_path = ""

        self.lucia_resh_portrait_path = None
        lucia_resh_paths = ["assets/portraits/LuciaResh.png", "LuciaResh.png"]
        for path in lucia_resh_paths:
            if os.path.exists(path):
                self.lucia_resh_portrait_path = path
                break
        if self.lucia_resh_portrait_path is None:
            self.lucia_resh_portrait_path = ""

        self.sailas_ist_portrait_path = None
        sailas_ist_paths = ["assets/portraits/sailasIst.png", "sailasIst.png"]
        for path in sailas_ist_paths:
            if os.path.exists(path):
                self.sailas_ist_portrait_path = path
                break
        if self.sailas_ist_portrait_path is None:
            self.sailas_ist_portrait_path = ""

        self.sailas_oder_portrait_path = None
        sailas_oder_paths = ["assets/portraits/sailasOder.png", "sailasOder.png"]
        for path in sailas_oder_paths:
            if os.path.exists(path):
                self.sailas_oder_portrait_path = path
                break
        if self.sailas_oder_portrait_path is None:
            self.sailas_oder_portrait_path = ""

        self.max_gnev_portrait_path = None
        max_gnev_paths = ["assets/portraits/maxGnev.png", "maxGnev.png"]
        for path in max_gnev_paths:
            if os.path.exists(path):
                self.max_gnev_portrait_path = path
                break
        if self.max_gnev_portrait_path is None:
            self.max_gnev_portrait_path = ""

        self.hart_zhest_portrait_path = None
        hart_zhest_paths = ["assets/portraits/hartZhest.png", "hartZhest.png"]
        for path in hart_zhest_paths:
            if os.path.exists(path):
                self.hart_zhest_portrait_path = path
                break
        if self.hart_zhest_portrait_path is None:
            self.hart_zhest_portrait_path = ""

        self.final1_art_path = None
        final1_paths = ["assets/art/final1.png", "final1.png"]
        for path in final1_paths:
            if os.path.exists(path):
                self.final1_art_path = path
                break

        self.final2_art_path = None
        final2_paths = ["assets/art/final2.png", "final2.png"]
        for path in final2_paths:
            if os.path.exists(path):
                self.final2_art_path = path
                break

        self.final3_art_path = None
        final3_paths = ["assets/art/final3.png", "final3.png"]
        for path in final3_paths:
            if os.path.exists(path):
                self.final3_art_path = path
                break

        # Звуки
        self.gasp_sound = None
        gasp_paths = ["assets/sounds/Vzdox.mp3", "Vzdox.mp3"]
        for path in gasp_paths:
            if os.path.exists(path):
                try:
                    self.gasp_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.door_sound = None
        door_paths = ["assets/sounds/door.mp3", "door.mp3"]
        for path in door_paths:
            if os.path.exists(path):
                try:
                    self.door_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.ambient_sound = None
        ambient_paths = ["assets/sounds/studentKushaet.mp3", "studentKushaet.mp3"]
        for path in ambient_paths:
            if os.path.exists(path):
                try:
                    self.ambient_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.crash_sound = None
        crash_paths = ["assets/sounds/padenie.mp3", "padenie.mp3"]
        for path in crash_paths:
            if os.path.exists(path):
                try:
                    self.crash_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.key_sound = None
        key_paths = ["assets/sounds/key.mp3", "key.mp3"]
        for path in key_paths:
            if os.path.exists(path):
                try:
                    self.key_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.scratch_sound = None
        scratch_paths = ["assets/sounds/carapanie.mp3", "carapanie.mp3"]
        for path in scratch_paths:
            if os.path.exists(path):
                try:
                    self.scratch_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.tick_tock_sound = None
        tick_paths = ["assets/sounds/tiktak.mp3", "tiktak.mp3"]
        for path in tick_paths:
            if os.path.exists(path):
                try:
                    self.tick_tock_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.footsteps_sound = None
        footsteps_paths = ["assets/sounds/sfx_footsteps.mp3", "sfx_footsteps.mp3"]
        for path in footsteps_paths:
            if os.path.exists(path):
                try:
                    self.footsteps_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        # Музыка
        self.wake_music_path = None
        wake_paths = ["assets/music/probuzhdenie.mp3", "probuzhdenie.mp3"]
        for path in wake_paths:
            if os.path.exists(path):
                self.wake_music_path = path
                break

        self.day_music_path = None
        day_paths = ["assets/music/defday.mp3", "defday.mp3"]
        for path in day_paths:
            if os.path.exists(path):
                self.day_music_path = path
                break

        self.tense_music_path = None
        tense_paths = ["assets/music/napryazhenie.mp3", "napryazhenie.mp3"]
        for path in tense_paths:
            if os.path.exists(path):
                self.tense_music_path = path
                break

        self.anxiety_music_path = None
        anxiety_paths = ["assets/music/trevoga.mp3", "trevoga.mp3"]
        for path in anxiety_paths:
            if os.path.exists(path):
                self.anxiety_music_path = path
                break

        self.aftermath_music_path = None
        aftermath_paths = ["assets/music/Aftermath.mp3", "Aftermath.mp3"]
        for path in aftermath_paths:
            if os.path.exists(path):
                self.aftermath_music_path = path
                break

        self.dar_music_path = None
        dar_paths = ["assets/music/dar.mp3", "dar.mp3"]
        for path in dar_paths:
            if os.path.exists(path):
                self.dar_music_path = path
                break

        self.kulm_music_path = None
        kulm_paths = ["assets/music/kulm.mp3", "kulm.mp3"]
        for path in kulm_paths:
            if os.path.exists(path):
                self.kulm_music_path = path
                break

        self.dark_walk_music_path = None
        dark_walk_paths = ["assets/music/darkWalk.mp3", "darkWalk.mp3"]
        for path in dark_walk_paths:
            if os.path.exists(path):
                self.dark_walk_music_path = path
                break

        self.tuctuc_music_path = None
        tuctuc_paths = ["assets/music/tuctuc.mp3", "tuctuc.mp3"]
        for path in tuctuc_paths:
            if os.path.exists(path):
                self.tuctuc_music_path = path
                break

        self.prizn_music_path = None
        prizn_paths = ["assets/music/prizn.mp3", "prizn.mp3"]
        for path in prizn_paths:
            if os.path.exists(path):
                self.prizn_music_path = path
                break

        self.pogon_music_path = None
        pogon_paths = ["assets/music/pogon.mp3", "pogon.mp3"]
        for path in pogon_paths:
            if os.path.exists(path):
                self.pogon_music_path = path
                break

        self.priz_music_path = None
        priz_paths = ["assets/music/priz.mp3", "priz.mp3"]
        for path in priz_paths:
            if os.path.exists(path):
                self.priz_music_path = path
                break

        self.bezumie_music_path = None
        bezumie_paths = ["assets/music/bezumie.mp3", "bezumie.mp3"]
        for path in bezumie_paths:
            if os.path.exists(path):
                self.bezumie_music_path = path
                break

        self.sailas_music_path = None
        sailas_music_paths = ["assets/music/sailsas.mp3", "sailsas.mp3"]
        for path in sailas_music_paths:
            if os.path.exists(path):
                self.sailas_music_path = path
                break

        self.final1_music_path = None
        final1_music_paths = ["assets/music/final1.mp3", "final1.mp3"]
        for path in final1_music_paths:
            if os.path.exists(path):
                self.final1_music_path = path
                break

        self.final2_music_path = None
        final2_music_paths = ["assets/music/final2.mp3", "final2.mp3"]
        for path in final2_music_paths:
            if os.path.exists(path):
                self.final2_music_path = path
                break

        self.final3_music_path = None
        final3_music_paths = ["assets/music/final3.mp3", "final3.mp3"]
        for path in final3_music_paths:
            if os.path.exists(path):
                self.final3_music_path = path
                break

        self.final_music_path = None
        final_music_paths = ["assets/music/final.mp3", "final.mp3"]
        for path in final_music_paths:
            if os.path.exists(path):
                self.final_music_path = path
                break

        self.end_music_path = None
        end_paths = ["assets/music/end.mp3", "end.mp3"]
        for path in end_paths:
            if os.path.exists(path):
                self.end_music_path = path
                break

    def load_resources(self):
        self.bg_menu = None
        bg_paths = ["assets/pictures/doska.png", "doska.png"]
        for path in bg_paths:
            if os.path.exists(path):
                try:
                    self.bg_menu = pygame.image.load(path)
                    self.bg_menu = pygame.transform.scale(self.bg_menu, (WIDTH, HEIGHT))
                    break
                except:
                    pass

        self.chalk_sound = None
        sound_paths = ["assets/sounds/mel.mp3", "mel.mp3"]
        for path in sound_paths:
            if os.path.exists(path):
                try:
                    self.chalk_sound = pygame.mixer.Sound(path)
                    break
                except:
                    pass

        self.menu_music_path = None
        music_paths = ["assets/music/crypto.mp3", "crypto.mp3"]
        for path in music_paths:
            if os.path.exists(path):
                self.menu_music_path = path
                break

        self.prologue_music_path = None
        prologue_paths = ["assets/music/prologue.mp3", "prologue.mp3"]
        for path in prologue_paths:
            if os.path.exists(path):
                self.prologue_music_path = path
                break
    def start_menu_music(self):
        if self.menu_music_path and not self.menu_music_playing:
            try:
                pygame.mixer.music.load(self.menu_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.menu_music_playing = True
                self.prologue_music_playing = False
                self.wake_music_playing = False
            except:
                pass

    def start_prologue_music(self):
        if self.prologue_music_path and not self.prologue_music_playing:
            try:
                pygame.mixer.music.load(self.prologue_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.prologue_music_playing = True
                self.menu_music_playing = False
                self.wake_music_playing = False
            except:
                pass

    def start_wake_music(self):
        if self.wake_music_path and not self.wake_music_playing:
            try:
                pygame.mixer.music.load(self.wake_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_day_music(self):
        if self.day_music_path:
            try:
                pygame.mixer.music.load(self.day_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_tense_music(self):
        if self.tense_music_path:
            try:
                pygame.mixer.music.load(self.tense_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_anxiety_music(self):
        if self.anxiety_music_path:
            try:
                pygame.mixer.music.load(self.anxiety_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_aftermath_music(self):
        if self.aftermath_music_path:
            try:
                pygame.mixer.music.load(self.aftermath_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_dar_music(self):
        if self.dar_music_path:
            try:
                pygame.mixer.music.load(self.dar_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_kulm_music(self):
        if self.kulm_music_path:
            try:
                pygame.mixer.music.load(self.kulm_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_dark_walk_music(self):
        if self.dark_walk_music_path:
            try:
                pygame.mixer.music.load(self.dark_walk_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_tuctuc_music(self):
        if self.tuctuc_music_path:
            try:
                pygame.mixer.music.load(self.tuctuc_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_prizn_music(self):
        if self.prizn_music_path:
            try:
                pygame.mixer.music.load(self.prizn_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
                self.menu_music_playing = False
                self.prologue_music_playing = False
            except:
                pass

    def start_pogon_music(self):
        if self.pogon_music_path:
            try:
                pygame.mixer.music.load(self.pogon_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_priz_music(self):
        if self.priz_music_path:
            try:
                pygame.mixer.music.load(self.priz_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_bezumie_music(self):
        if self.bezumie_music_path:
            try:
                pygame.mixer.music.load(self.bezumie_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_sailas_music(self):
        if self.sailas_music_path:
            try:
                pygame.mixer.music.load(self.sailas_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_final1_music(self):
        if self.final1_music_path:
            try:
                pygame.mixer.music.load(self.final1_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_final2_music(self):
        if self.final2_music_path:
            try:
                pygame.mixer.music.load(self.final2_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_final3_music(self):
        if self.final3_music_path:
            try:
                pygame.mixer.music.load(self.final3_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_final_music(self):
        if self.final_music_path:
            try:
                pygame.mixer.music.load(self.final_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def start_end_music(self):
        if self.end_music_path:
            try:
                pygame.mixer.music.load(self.end_music_path)
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.wake_music_playing = True
            except:
                pass

    def pause_music(self):
        if not self.music_paused:
            self.music_pause_pos = pygame.mixer.music.get_pos()
            pygame.mixer.music.pause()
            self.music_paused = True

    def unpause_music(self):
        if self.music_paused:
            pygame.mixer.music.unpause()
            self.music_paused = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.menu_music_playing = False
        self.prologue_music_playing = False
        self.wake_music_playing = False
        self.music_paused = False

    def play_footsteps(self):
        if self.footsteps_sound:
            self.footsteps_sound.play()
    def create_new_prologue(self):
        self.prologue = Prologue(self.screen, WIDTH, HEIGHT, self.font, "Кайл")
        self.prologue.start(self.art_path)
        self.start_prologue_music()

    def create_wake_up(self, skip_fade=False):
        self.wake_up = WakeUpScene(self.screen, WIDTH, HEIGHT, self.font)
        self.wake_up.start(self.room_path, skip_fade)

    def create_thoughts(self, skip_animation=False):
        self.thoughts = ThoughtsScene(self.screen, WIDTH, HEIGHT, self.font)
        self.thoughts.start(self.room_path, skip_animation)

    def create_act1_transition(self):
        self.act1_transition = Act1Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.act1_transition.start()

    def create_morning_scene(self):
        self.morning_scene = MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.morning_scene.start(self.morning_room_path)

    def create_corridor_scene(self):
        self.corridor_scene = CorridorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.corridor_scene.start(self.corridor_path)

    def create_lesson_scene(self):
        self.lesson_scene = LessonScene(self.screen, WIDTH, HEIGHT, self.font)
        self.lesson_scene.start(self.class_path, self.krein_portrait_path)

    def create_canteen_scene(self):
        self.canteen_scene = CanteenScene(self.screen, WIDTH, HEIGHT, self.font)
        self.canteen_scene.start(self.canteen_path, self.max_portrait_path)

    def create_lucia_scene(self):
        self.lucia_scene = LuciaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.lucia_scene.start(self.corridor_path, self.lucia_portrait_path)

    def create_evening_scene(self):
        self.evening_scene = EveningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.evening_scene.start(self.dorm_path)

    def create_night_scene(self):
        self.night_scene = NightScene(self.screen, WIDTH, HEIGHT, self.font)
        self.night_scene.start(self.room_path)

    def create_empty_corridor_scene(self):
        self.empty_corridor_scene = EmptyCorridorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.empty_corridor_scene.start(self.dorm_night_path)

    def create_insomnia_scene(self):
        self.insomnia_scene = InsomniaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.insomnia_scene.start(self.room_path)

    def create_day2_transition(self):
        self.day2_transition = Day2Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day2_transition.start()

    def create_day2_morning(self):
        self.day2_morning = Day2MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day2_morning.start(self.morning_room_path)

    def create_day2_corridor(self):
        self.day2_corridor = Day2CorridorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day2_corridor.start(self.corridor_path)

    def create_lecture_scene(self):
        self.lecture_scene = LectureScene(self.screen, WIDTH, HEIGHT, self.font)
        self.lecture_scene.start(self.lecture_path, self.hart_portrait_path)

    def create_post_lecture_scene(self):
        self.post_lecture_scene = PostLectureScene(self.screen, WIDTH, HEIGHT, self.font)
        self.post_lecture_scene.start(self.corridor_path)

    def create_closed_wing_scene(self):
        self.closed_wing_scene = ClosedWingScene(self.screen, WIDTH, HEIGHT, self.font)
        self.closed_wing_scene.start(self.closed_wing_path, self.security_portrait_path)

    def create_library_scene(self):
        self.library_scene = LibraryScene(self.screen, WIDTH, HEIGHT, self.font)
        self.library_scene.start(self.library_path, self.iina_portrait_path)

    def create_day2_night(self):
        self.day2_night = Day2NightScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day2_night.start(self.room_path)

    def create_day3_transition(self):
        self.day3_transition = Day3Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day3_transition.start()

    def create_day3_morning(self):
        self.day3_morning = Day3MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day3_morning.start(self.morning_room_path)

    def create_math_exam_scene(self):
        self.math_exam_scene = MathExamScene(self.screen, WIDTH, HEIGHT, self.font)
        self.math_exam_scene.start(self.math_path)

    def create_sailas_corridor_scene(self):
        self.sailas_corridor_scene = SailasCorridorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.sailas_corridor_scene.start(self.corridor_path, self.sailas_portrait_path)

    def create_day3_library_scene(self):
        self.day3_library_scene = Day3LibraryScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day3_library_scene.start(self.library_path, self.iina_portrait_path)

    def create_awakening_scene(self):
        self.awakening_scene = AwakeningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.awakening_scene.start(self.corner_path)

    def create_day3_night(self):
        self.day3_night = Day3NightScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day3_night.start(self.room_path)

    def create_day4_transition(self):
        self.day4_transition = Day4Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_transition.start()

    def create_day4_morning(self):
        self.day4_morning = Day4MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_morning.start(self.morning_room_path)

    def create_day4_math_test(self):
        self.day4_math_test = Day4MathTestScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_math_test.start(self.math_path)

    def create_day4_corridor_warning(self):
        self.day4_corridor_warning = Day4CorridorWarningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_corridor_warning.start(self.corridor_path, self.sailas_portrait_path, self.max_portrait_path)

    def create_day4_old_library(self):
        self.day4_old_library = Day4OldLibraryScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_old_library.start(self.old_library_path)

    def create_day4_secret_room(self):
        self.day4_secret_room = Day4SecretRoomScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day4_secret_room.start(self.secret_room_path, self.lucia_portrait_path, self.max_portrait_path,
                                     self.sailas_portrait_path, self.iina_sos_portrait_path)

    def create_day5_transition(self):
        self.day5_transition = Day5Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_transition.start()

    def create_day5_morning(self):
        self.day5_morning = Day5MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_morning.start(self.morning_room_path)

    def create_day5_corridor_rules(self):
        self.day5_corridor_rules = Day5CorridorRulesScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_corridor_rules.start(self.corridor_path)

    def create_day5_secret_meeting(self):
        self.day5_secret_meeting = Day5SecretMeetingScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_secret_meeting.start(self.secret_room_path, self.lucia_portrait_path, self.max_portrait_path,
                                        self.sailas_portrait_path, self.iina_portrait_path)

    def create_day5_medical_infiltration(self):
        self.day5_medical_infiltration = Day5MedicalInfiltrationScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_medical_infiltration.start(self.medical_corridor_path, self.max_portrait_path, self.iina_portrait_path)

    def create_day5_archive_find(self):
        self.day5_archive_find = Day5ArchiveFindScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_archive_find.start(self.medical_archive_path, self.lucia_portrait_path, self.max_portrait_path)

    def create_day5_video_procedure(self):
        self.day5_video_procedure = Day5VideoProcedureScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_video_procedure.start(self.medical_archive_path, self.sailas_portrait_path)

    def create_day5_meeting_krein(self):
        self.day5_meeting_krein = Day5MeetingKreinScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day5_meeting_krein.start(self.corridor_night_path, self.krein_portrait_path, self.lucia_portrait_path)

    def create_day6_transition(self):
        self.day6_transition = Day6Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_transition.start()

    def create_day6_morning(self):
        self.day6_morning = Day6MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_morning.start(self.morning_room_path)

    def create_day6_corridor(self):
        self.day6_corridor = Day6CorridorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_corridor.start(self.corridor_path)

    def create_day6_secret_room_traitor(self):
        self.day6_secret_room_traitor = Day6SecretRoomTraitorScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_secret_room_traitor.start(self.secret_room_path, self.sailas_ras_portrait_path,
                                             self.lucia_portrait_path, self.lucia_pain_portrait_path,
                                             self.iina_str_portrait_path)

    def create_day6_roof_confrontation(self):
        self.day6_roof_confrontation = Day6RoofConfrontationScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_roof_confrontation.start(self.roof_path, self.lucia_pain_portrait_path)  # ← ИСПРАВЛЕНО

    def create_day6_corridor_return(self):
        self.day6_corridor_return = Day6CorridorReturnScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_corridor_return.start(self.corridor_path)

    def create_day6_insomnia(self):
        self.day6_insomnia = Day6InsomniaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day6_insomnia.start(self.room_path)

    def create_day7_transition(self):
        self.day7_transition = Day7Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_transition.start()

    def create_day7_morning(self):
        self.day7_morning = Day7MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_morning.start(self.morning_room_path)

    def create_day7_corridor_max(self):
        self.day7_corridor_max = Day7CorridorMaxScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_corridor_max.start(self.corridor_path, self.max_portrait_path)

    def create_day7_secret_planning(self):
        self.day7_secret_planning = Day7SecretPlanningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_secret_planning.start(self.secret_room_path, self.lucia_portrait_path, self.sailas_portrait_path,
                                         self.max_portrait_path, self.iina_portrait_path)

    def create_day7_abandoned_trap(self):
        self.day7_abandoned_trap = Day7AbandonedTrapScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_abandoned_trap.start(self.abandoned_path, self.max_portrait_path, self.lucia_portrait_path,
                                        self.sailas_portrait_path)

    def create_day7_secret_return(self):
        self.day7_secret_return = Day7SecretReturnScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_secret_return.start(self.secret_room_path, self.lucia_portrait_path, self.lucia_gnev_portrait_path,
                                       self.max_portrait_path, self.sailas_portrait_path, self.sailas_ras_portrait_path,
                                       self.iina_portrait_path)

    def create_day7_insomnia(self):
        self.day7_insomnia = Day7InsomniaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day7_insomnia.start(self.room_path)

    def create_day8_transition(self):
        self.day8_transition = Day8Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_transition.start()

    def create_day8_morning(self):
        self.day8_morning = Day8MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_morning.start(self.morning_room_path)

    def create_day8_corridor_observe(self):
        self.day8_corridor_observe = Day8CorridorObserveScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_corridor_observe.start(self.corridor_path)

    def create_day8_library_analysis(self):
        self.day8_library_analysis = Day8LibraryAnalysisScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_library_analysis.start(self.library_path)

    def create_day8_dormitory_clues(self):
        self.day8_dormitory_clues = Day8DormitoryCluesScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_dormitory_clues.start(self.dorm_night_path, self.room_max_path)

    def create_day8_preparation(self):
        self.day8_preparation = Day8PreparationScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day8_preparation.start(self.room_path)

    def create_day9_transition(self):
        self.day9_transition = Day9Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_transition.start()

    def create_day9_morning(self):
        self.day9_morning = Day9MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_morning.start(self.morning_room_path)

    def create_day9_gym_confrontation(self):
        self.day9_gym_confrontation = Day9GymConfrontationScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_gym_confrontation.start(self.gym_path, self.max_portrait_path)

    def create_day9_confession_choice(self):
        self.day9_confession_choice = Day9ConfessionChoiceScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_confession_choice.start(self.gym_path, self.max_portrait_path, self.stid_max_portrait_path)

    def create_day9_secret_message(self, choice):
        self.day9_secret_message = Day9SecretMessageScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_secret_message.start(self.secret_room_path, self.lucia_portrait_path, choice)

    def create_day9_insomnia(self):
        self.day9_insomnia = Day9InsomniaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day9_insomnia.start(self.room_path)

    def create_day10_transition(self):
        self.day10_transition = Day10Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_transition.start()

    def create_day10_morning(self):
        self.day10_morning = Day10MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_morning.start(self.morning_room_path)

    def create_day10_corridor_branch(self, choice):
        self.day10_corridor_branch = Day10CorridorBranchScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_corridor_branch.start(self.corridor_path, self.max_portrait_path,
                                         self.lucia_portrait_path, choice)

    def create_day10_secret_planning(self):
        self.day10_secret_planning = Day10SecretPlanningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_secret_planning.start(self.secret_room_path, self.iina_sos_portrait_path,
                                         self.sailas_ras_portrait_path, self.lucia_portrait_path)

    def create_day10_medical_path(self):
        self.day10_medical_path = Day10MedicalPathScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_medical_path.start(self.medical_corridor_path)

    def create_day10_hart_lab(self):
        self.day10_hart_lab = Day10HartLabScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_hart_lab.start(self.hart_lab_path, self.lucia_str_portrait_path,
                                  self.iina_str_portrait_path, self.sailas_portrait_path)

    def create_day10_insomnia(self):
        self.day10_insomnia = Day10InsomniaScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day10_insomnia.start(self.room_path)

    def create_day11_transition(self):
        self.day11_transition = Day11Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_transition.start()

    def create_day11_morning(self):
        self.day11_morning = Day11MorningScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_morning.start(self.morning_room_path)

    def create_day11_corridor_follow(self):
        self.day11_corridor_follow = Day11CorridorFollowScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_corridor_follow.start(self.corridor_path)

    def create_day11_library_analysis(self):
        self.day11_library_analysis = Day11LibraryAnalysisScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_library_analysis.start(self.library_path)

    def create_day11_sailas_room(self):
        self.day11_sailas_room = Day11SailasRoomScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_sailas_room.start(self.sailas_room_path)

    def create_day11_preparation(self):
        self.day11_preparation = Day11PreparationScene(self.screen, WIDTH, HEIGHT, self.font)
        self.day11_preparation.start(self.room_path)

    def create_day12_transition(self):
        self.day12_transition = Day12Transition(self.screen, WIDTH, HEIGHT, self.font)
        self.day12_transition.start()
    def create_act12_revelation(self):
        self.act12_revelation = Act12RevelationScene(self.screen, WIDTH, HEIGHT, self.font)
        portraits_data = {
            "lucia_path": self.lucia_portrait_path,
            "lucia_str_path": self.lucia_str_portrait_path,
            "lucia_gnev_path": self.lucia_gnev_portrait_path,
            "lucia_resh_path": self.lucia_resh_portrait_path,
            "sailas_ras_path": self.sailas_ras_portrait_path,
            "sailas_ist_path": self.sailas_ist_portrait_path,
            "sailas_oder_path": self.sailas_oder_portrait_path,
            "max_path": self.max_portrait_path,
            "max_gnev_path": self.max_gnev_portrait_path,
            "iina_path": self.iina_portrait_path,
            "iina_str_path": self.iina_str_portrait_path
        }
        max_alive = (self.player_choice == "forgive")
        self.act12_revelation.start(self.secret_room_path, portraits_data, max_alive)

    def create_act12_silence_before_storm(self):
        self.act12_silence_before_storm = Act12SilenceBeforeStormScene(self.screen, WIDTH, HEIGHT, self.font)
        portraits_data = {
            "lucia_path": self.lucia_portrait_path,
            "iina_path": self.iina_sos_portrait_path,
            "max_path": self.max_portrait_path
        }
        max_alive = (self.player_choice == "forgive")
        self.act12_silence_before_storm.start(self.koridor_bash_path, portraits_data, max_alive)

    def create_act12_hart_office(self):
        self.act12_hart_office = Act12HartOfficeScene(self.screen, WIDTH, HEIGHT, self.font)
        portraits_data = {
            "hart_path": self.hart_zhest_portrait_path,
            "sailas_path": self.sailas_ist_portrait_path,
            "lucia_path": self.lucia_gnev_portrait_path
        }
        self.act12_hart_office.start(self.dir_path, portraits_data)

    def create_act12_chase(self):
        self.act12_chase = Act12ChaseScene(self.screen, WIDTH, HEIGHT, self.font)
        portraits_data = {
            "hart_path": self.hart_zhest_portrait_path,
            "lucia_path": self.lucia_gnev_portrait_path,
            "iina_path": self.iina_sos_portrait_path
        }
        max_alive = (self.player_choice == "forgive")
        self.act12_chase.start(self.koridor_bash_path, portraits_data, max_alive)

    def create_act12_lucia_confession(self):
        self.act12_lucia_confession = Act12LuciaConfessionScene(self.screen, WIDTH, HEIGHT, self.font)
        self.act12_lucia_confession.start(self.roof_night_path, self.lucia_pain_portrait_path)

    def create_act12_sailas_madness(self):
        self.act12_sailas_madness = Act12SailasMadnessScene(self.screen, WIDTH, HEIGHT, self.font)
        self.act12_sailas_madness.start(self.bash_path, self.sailas_oder_portrait_path)

    def create_act12_sailas_choice(self):
        self.act12_sailas_choice = Act12SailasChoiceScene(self.screen, WIDTH, HEIGHT, self.font)
        self.act12_sailas_choice.start(self.bash_path, self.sailas_ist_portrait_path, self.sailas_ras_portrait_path)

    # ========== ИСПРАВЛЕНО: добавлен параметр roof_path ==========
    def create_act12_ending(self):
        self.act12_ending = Act12EndingScene(self.screen, WIDTH, HEIGHT, self.font)

        max_alive = (self.player_choice == "forgive")
        lucia_alive = (self.lucia_choice == "save")
        sailas_killed = (self.sailas_choice == "kill")

        if max_alive and lucia_alive:
            ending_type = "victory_freedom"
            self.start_final1_music()
        elif not max_alive and not lucia_alive and sailas_killed:
            ending_type = "new_hunter"
            self.start_final3_music()
        elif not max_alive and not lucia_alive and not sailas_killed:
            ending_type = "victory_loss"
            self.start_final2_music()
        elif not max_alive and lucia_alive:
            ending_type = "max_dead_lucia_alive"
            self.start_final2_music()
        else:
            ending_type = "lucia_dead_max_alive"
            self.start_final2_music()

        # ИСПРАВЛЕНО: передаём roof_night_path и roof_path
        self.act12_ending.start(ending_type, self.lucia_choice, self.sailas_choice, max_alive,
                                self.final1_art_path, self.final2_art_path, self.final3_art_path,
                                self.roof_night_path, self.roof_path)

    def create_act12_final_black(self):
        self.act12_final_black = Act12FinalBlackScene(self.screen, WIDTH, HEIGHT, self.font)
        self.act12_final_black.start()
        self.start_end_music()

    def start_new_game(self):
        self.create_new_prologue()
        self.state = State.PROLOGUE
    # ========== ОСНОВНОЙ ИГРОВОЙ ЦИКЛ ==========

    def run(self):
        running = True
        white_flash_alpha = 0
        white_flash_active = False
        white_flash_timer = 0
        ambient_channel = None
        tick_tock_channel = None
        footsteps_channel = None

        while running:
            dt = self.clock.tick(FPS)
            mouse_pos = pygame.mouse.get_pos()
            click_pos = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.state in [State.PROLOGUE, State.PROLOGUE_WAKE, State.THOUGHTS,
                                            State.ACT1_TRANSITION, State.ACT1_MORNING, State.ACT1_CORRIDOR,
                                            State.ACT1_LESSON, State.ACT1_CANTEEN, State.ACT1_LUCIA,
                                            State.ACT1_EVENING, State.ACT1_NIGHT, State.ACT1_EMPTY_CORRIDOR,
                                            State.ACT1_INSOMNIA, State.ACT1_DAY2_TRANSITION,
                                            State.ACT2_MORNING, State.ACT2_CORRIDOR, State.ACT2_LECTURE,
                                            State.ACT2_POST_LECTURE, State.ACT2_CLOSED_WING, State.ACT2_LIBRARY,
                                            State.ACT2_NIGHT, State.ACT2_DAY3_TRANSITION,
                                            State.ACT3_MORNING, State.ACT3_MATH_EXAM, State.ACT3_CORRIDOR_SAILAS,
                                            State.ACT3_LIBRARY_EVENING, State.ACT3_AWAKENING, State.ACT3_NIGHT,
                                            State.ACT3_DAY4_TRANSITION,
                                            State.ACT4_MORNING, State.ACT4_MATH_TEST, State.ACT4_CORRIDOR_WARNING,
                                            State.ACT4_OLD_LIBRARY, State.ACT4_SECRET_ROOM, State.ACT4_DAY5_TRANSITION,
                                            State.ACT5_MORNING, State.ACT5_CORRIDOR_RULES, State.ACT5_SECRET_MEETING,
                                            State.ACT5_MEDICAL_INFILTRATION, State.ACT5_ARCHIVE_FIND,
                                            State.ACT5_VIDEO_PROCEDURE, State.ACT5_MEETING_KREIN,
                                            State.ACT5_DAY6_TRANSITION,
                                            State.ACT6_MORNING, State.ACT6_CORRIDOR, State.ACT6_SECRET_ROOM_TRAITOR,
                                            State.ACT6_ROOF_CONFRONTATION, State.ACT6_CORRIDOR_RETURN,
                                            State.ACT6_INSOMNIA, State.ACT6_DAY7_TRANSITION,
                                            State.ACT7_MORNING, State.ACT7_CORRIDOR_MAX, State.ACT7_SECRET_PLANNING,
                                            State.ACT7_ABANDONED_TRAP, State.ACT7_SECRET_RETURN,
                                            State.ACT7_INSOMNIA, State.ACT7_DAY8_TRANSITION,
                                            State.ACT8_MORNING, State.ACT8_CORRIDOR_OBSERVE,
                                            State.ACT8_LIBRARY_ANALYSIS, State.ACT8_DORMITORY_CLUES,
                                            State.ACT8_PREPARATION, State.ACT8_DAY9_TRANSITION,
                                            State.ACT9_MORNING, State.ACT9_GYM_CONFRONTATION,
                                            State.ACT9_CONFESSION_CHOICE, State.ACT9_SECRET_MESSAGE,
                                            State.ACT9_INSOMNIA, State.ACT9_DAY10_TRANSITION,
                                            State.ACT10_MORNING, State.ACT10_CORRIDOR_BRANCH,
                                            State.ACT10_SECRET_PLANNING, State.ACT10_MEDICAL_PATH,
                                            State.ACT10_HART_LAB, State.ACT10_INSOMNIA, State.ACT10_DAY11_TRANSITION,
                                            State.ACT11_MORNING, State.ACT11_CORRIDOR_FOLLOW,
                                            State.ACT11_LIBRARY_ANALYSIS, State.ACT11_SAILAS_ROOM,
                                            State.ACT11_PREPARATION, State.ACT11_DAY12_TRANSITION,
                                            State.ACT12_REVELATION, State.ACT12_SILENCE_BEFORE_STORM,
                                            State.ACT12_HART_OFFICE, State.ACT12_CHASE,
                                            State.ACT12_LUCIA_CONFESSION, State.ACT12_SAILAS_MADNESS,
                                            State.ACT12_SAILAS_CHOICE, State.ACT12_ENDING, State.ACT12_FINAL_BLACK]:
                            self.pause_music()
                            self.pause.active = True
                            self.state = State.PAUSE
                        elif self.state == State.PAUSE:
                            self.pause.active = False
                            self.unpause_music()
                            if self.act12_final_black:
                                self.state = State.ACT12_FINAL_BLACK
                            elif self.act12_ending:
                                self.state = State.ACT12_ENDING
                            elif self.act12_sailas_choice:
                                self.state = State.ACT12_SAILAS_CHOICE
                            elif self.act12_sailas_madness:
                                self.state = State.ACT12_SAILAS_MADNESS
                            elif self.act12_lucia_confession:
                                self.state = State.ACT12_LUCIA_CONFESSION
                            elif self.act12_chase:
                                self.state = State.ACT12_CHASE
                            elif self.act12_hart_office:
                                self.state = State.ACT12_HART_OFFICE
                            elif self.act12_silence_before_storm:
                                self.state = State.ACT12_SILENCE_BEFORE_STORM
                            elif self.act12_revelation:
                                self.state = State.ACT12_REVELATION
                            elif self.day12_transition:
                                self.state = State.ACT11_DAY12_TRANSITION
                            elif self.day11_preparation:
                                self.state = State.ACT11_PREPARATION
                            elif self.day11_sailas_room:
                                self.state = State.ACT11_SAILAS_ROOM
                            elif self.day11_library_analysis:
                                self.state = State.ACT11_LIBRARY_ANALYSIS
                            elif self.day11_corridor_follow:
                                self.state = State.ACT11_CORRIDOR_FOLLOW
                            elif self.day11_morning:
                                self.state = State.ACT11_MORNING
                            elif self.day11_transition:
                                self.state = State.ACT10_DAY11_TRANSITION
                            elif self.day10_insomnia:
                                self.state = State.ACT10_INSOMNIA
                            elif self.day10_hart_lab:
                                self.state = State.ACT10_HART_LAB
                            elif self.day10_medical_path:
                                self.state = State.ACT10_MEDICAL_PATH
                            elif self.day10_secret_planning:
                                self.state = State.ACT10_SECRET_PLANNING
                            elif self.day10_corridor_branch:
                                self.state = State.ACT10_CORRIDOR_BRANCH
                            elif self.day10_morning:
                                self.state = State.ACT10_MORNING
                            elif self.day10_transition:
                                self.state = State.ACT9_DAY10_TRANSITION
                            elif self.day9_insomnia:
                                self.state = State.ACT9_INSOMNIA
                            elif self.day9_secret_message:
                                self.state = State.ACT9_SECRET_MESSAGE
                            elif self.day9_confession_choice:
                                self.state = State.ACT9_CONFESSION_CHOICE
                            elif self.day9_gym_confrontation:
                                self.state = State.ACT9_GYM_CONFRONTATION
                            elif self.day9_morning:
                                self.state = State.ACT9_MORNING
                            elif self.day9_transition:
                                self.state = State.ACT8_DAY9_TRANSITION
                            elif self.day8_preparation:
                                self.state = State.ACT8_PREPARATION
                            elif self.day8_dormitory_clues:
                                self.state = State.ACT8_DORMITORY_CLUES
                            elif self.day8_library_analysis:
                                self.state = State.ACT8_LIBRARY_ANALYSIS
                            elif self.day8_corridor_observe:
                                self.state = State.ACT8_CORRIDOR_OBSERVE
                            elif self.day8_morning:
                                self.state = State.ACT8_MORNING
                            elif self.day8_transition:
                                self.state = State.ACT7_DAY8_TRANSITION
                            elif self.day7_insomnia:
                                self.state = State.ACT7_INSOMNIA
                            elif self.day7_secret_return:
                                self.state = State.ACT7_SECRET_RETURN
                            elif self.day7_abandoned_trap:
                                self.state = State.ACT7_ABANDONED_TRAP
                            elif self.day7_secret_planning:
                                self.state = State.ACT7_SECRET_PLANNING
                            elif self.day7_corridor_max:
                                self.state = State.ACT7_CORRIDOR_MAX
                            elif self.day7_morning:
                                self.state = State.ACT7_MORNING
                            elif self.day7_transition:
                                self.state = State.ACT6_DAY7_TRANSITION
                            elif self.day6_insomnia:
                                self.state = State.ACT6_INSOMNIA
                            elif self.day6_corridor_return:
                                self.state = State.ACT6_CORRIDOR_RETURN
                            elif self.day6_roof_confrontation:
                                self.state = State.ACT6_ROOF_CONFRONTATION
                            elif self.day6_secret_room_traitor:
                                self.state = State.ACT6_SECRET_ROOM_TRAITOR
                            elif self.day6_corridor:
                                self.state = State.ACT6_CORRIDOR
                            elif self.day6_morning:
                                self.state = State.ACT6_MORNING
                            elif self.day6_transition:
                                self.state = State.ACT5_DAY6_TRANSITION
                            elif self.day5_meeting_krein:
                                self.state = State.ACT5_MEETING_KREIN
                            elif self.day5_video_procedure:
                                self.state = State.ACT5_VIDEO_PROCEDURE
                            elif self.day5_archive_find:
                                self.state = State.ACT5_ARCHIVE_FIND
                            elif self.day5_medical_infiltration:
                                self.state = State.ACT5_MEDICAL_INFILTRATION
                            elif self.day5_secret_meeting:
                                self.state = State.ACT5_SECRET_MEETING
                            elif self.day5_corridor_rules:
                                self.state = State.ACT5_CORRIDOR_RULES
                            elif self.day5_morning:
                                self.state = State.ACT5_MORNING
                            elif self.day5_transition:
                                self.state = State.ACT4_DAY5_TRANSITION
                            elif self.day4_secret_room:
                                self.state = State.ACT4_SECRET_ROOM
                            elif self.day4_old_library:
                                self.state = State.ACT4_OLD_LIBRARY
                            elif self.day4_corridor_warning:
                                self.state = State.ACT4_CORRIDOR_WARNING
                            elif self.day4_math_test:
                                self.state = State.ACT4_MATH_TEST
                            elif self.day4_morning:
                                self.state = State.ACT4_MORNING
                            elif self.day4_transition:
                                self.state = State.ACT3_DAY4_TRANSITION
                            elif self.day3_night:
                                self.state = State.ACT3_NIGHT
                            elif self.awakening_scene:
                                self.state = State.ACT3_AWAKENING
                            elif self.day3_library_scene:
                                self.state = State.ACT3_LIBRARY_EVENING
                            elif self.sailas_corridor_scene:
                                self.state = State.ACT3_CORRIDOR_SAILAS
                            elif self.math_exam_scene:
                                self.state = State.ACT3_MATH_EXAM
                            elif self.day3_morning:
                                self.state = State.ACT3_MORNING
                            elif self.day3_transition:
                                self.state = State.ACT2_DAY3_TRANSITION
                            elif self.day2_night:
                                self.state = State.ACT2_NIGHT
                            elif self.library_scene:
                                self.state = State.ACT2_LIBRARY
                            elif self.closed_wing_scene:
                                self.state = State.ACT2_CLOSED_WING
                            elif self.post_lecture_scene:
                                self.state = State.ACT2_POST_LECTURE
                            elif self.lecture_scene:
                                self.state = State.ACT2_LECTURE
                            elif self.day2_corridor:
                                self.state = State.ACT2_CORRIDOR
                            elif self.day2_morning:
                                self.state = State.ACT2_MORNING
                            elif self.day2_transition:
                                self.state = State.ACT1_DAY2_TRANSITION
                            elif self.insomnia_scene:
                                self.state = State.ACT1_INSOMNIA
                            elif self.empty_corridor_scene:
                                self.state = State.ACT1_EMPTY_CORRIDOR
                            elif self.night_scene:
                                self.state = State.ACT1_NIGHT
                            elif self.evening_scene:
                                self.state = State.ACT1_EVENING
                            elif self.lucia_scene:
                                self.state = State.ACT1_LUCIA
                            elif self.canteen_scene:
                                self.state = State.ACT1_CANTEEN
                            elif self.lesson_scene:
                                self.state = State.ACT1_LESSON
                            elif self.corridor_scene:
                                self.state = State.ACT1_CORRIDOR
                            elif self.morning_scene:
                                self.state = State.ACT1_MORNING
                            elif self.act1_transition:
                                self.state = State.ACT1_TRANSITION
                            elif self.thoughts:
                                self.state = State.THOUGHTS
                            elif self.wake_up:
                                self.state = State.PROLOGUE_WAKE
                            else:
                                self.state = State.PROLOGUE
                        elif self.state == State.DISCLAIMER:
                            self.state = State.MENU
                            self.start_menu_music()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_pos = event.pos

                        if self.state == State.DISCLAIMER:
                            self.state = State.MENU
                            self.start_menu_music()
                            continue

                        # ПРОЛОГ И НАЧАЛО ИГРЫ
                        if self.state == State.PROLOGUE and self.prologue:
                            if self.prologue.handle_click():
                                self.create_wake_up()
                                white_flash_active = True
                                white_flash_alpha = 255
                                white_flash_timer = 0
                                self.stop_music()
                                if self.gasp_sound:
                                    self.gasp_sound.play()
                                self.state = State.PROLOGUE_WAKE
                                self.prologue = None

                        elif self.state == State.PROLOGUE_WAKE and self.wake_up:
                            if self.wake_up.handle_click():
                                self.create_thoughts()
                                self.start_wake_music()
                                self.state = State.THOUGHTS
                                self.wake_up = None

                        elif self.state == State.THOUGHTS and self.thoughts:
                            if self.thoughts.handle_click():
                                self.create_act1_transition()
                                self.stop_music()
                                self.state = State.ACT1_TRANSITION
                                self.thoughts = None

                        # ДЕНЬ 1
                        elif self.state == State.ACT1_TRANSITION and self.act1_transition:
                            self.act1_transition.update()
                            if self.act1_transition.can_transition_to_morning():
                                self.create_morning_scene()
                                self.start_day_music()
                                self.state = State.ACT1_MORNING
                                self.act1_transition = None

                        elif self.state == State.ACT1_MORNING and self.morning_scene:
                            if self.morning_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_CORRIDOR and self.corridor_scene:
                            if self.corridor_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_LESSON and self.lesson_scene:
                            if self.lesson_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_CANTEEN and self.canteen_scene:
                            if self.canteen_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_LUCIA and self.lucia_scene:
                            if self.lucia_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_EVENING and self.evening_scene:
                            if self.evening_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_NIGHT and self.night_scene:
                            if self.night_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_EMPTY_CORRIDOR and self.empty_corridor_scene:
                            if self.empty_corridor_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_INSOMNIA and self.insomnia_scene:
                            if self.insomnia_scene.handle_click():
                                pass

                        elif self.state == State.ACT1_DAY2_TRANSITION and self.day2_transition:
                            self.day2_transition.update()
                            if self.day2_transition.can_transition():
                                self.create_day2_morning()
                                self.start_day_music()
                                self.state = State.ACT2_MORNING
                                self.day2_transition = None

                        # ДЕНЬ 2
                        elif self.state == State.ACT2_MORNING and self.day2_morning:
                            if self.day2_morning.handle_click():
                                pass

                        elif self.state == State.ACT2_CORRIDOR and self.day2_corridor:
                            if self.day2_corridor.handle_click():
                                pass

                        elif self.state == State.ACT2_LECTURE and self.lecture_scene:
                            if self.lecture_scene.handle_click():
                                pass

                        elif self.state == State.ACT2_POST_LECTURE and self.post_lecture_scene:
                            if self.post_lecture_scene.handle_click():
                                pass

                        elif self.state == State.ACT2_CLOSED_WING and self.closed_wing_scene:
                            if self.closed_wing_scene.handle_click():
                                pass

                        elif self.state == State.ACT2_LIBRARY and self.library_scene:
                            if self.library_scene.handle_click():
                                pass

                        elif self.state == State.ACT2_NIGHT and self.day2_night:
                            if self.day2_night.handle_click():
                                pass

                        elif self.state == State.ACT2_DAY3_TRANSITION and self.day3_transition:
                            self.day3_transition.update()
                            if self.day3_transition.can_transition():
                                self.create_day3_morning()
                                self.start_day_music()
                                self.state = State.ACT3_MORNING
                                self.day3_transition = None

                        # ДЕНЬ 3
                        elif self.state == State.ACT3_MORNING and self.day3_morning:
                            if self.day3_morning.handle_click():
                                pass

                        elif self.state == State.ACT3_MATH_EXAM and self.math_exam_scene:
                            if self.math_exam_scene.handle_click():
                                pass

                        elif self.state == State.ACT3_CORRIDOR_SAILAS and self.sailas_corridor_scene:
                            if self.sailas_corridor_scene.handle_click():
                                pass

                        elif self.state == State.ACT3_LIBRARY_EVENING and self.day3_library_scene:
                            if self.day3_library_scene.handle_click():
                                pass

                        elif self.state == State.ACT3_AWAKENING and self.awakening_scene:
                            if self.awakening_scene.handle_click():
                                pass

                        elif self.state == State.ACT3_NIGHT and self.day3_night:
                            if self.day3_night.handle_click():
                                pass

                        elif self.state == State.ACT3_DAY4_TRANSITION and self.day4_transition:
                            self.day4_transition.update()
                            if self.day4_transition.can_transition():
                                self.create_day4_morning()
                                self.start_day_music()
                                self.state = State.ACT4_MORNING
                                self.day4_transition = None

                        # ДЕНЬ 4
                        elif self.state == State.ACT4_MORNING and self.day4_morning:
                            if self.day4_morning.handle_click():
                                pass

                        elif self.state == State.ACT4_MATH_TEST and self.day4_math_test:
                            if self.day4_math_test.handle_click():
                                pass

                        elif self.state == State.ACT4_CORRIDOR_WARNING and self.day4_corridor_warning:
                            if self.day4_corridor_warning.handle_click():
                                pass

                        elif self.state == State.ACT4_OLD_LIBRARY and self.day4_old_library:
                            if self.day4_old_library.handle_click():
                                pass

                        elif self.state == State.ACT4_SECRET_ROOM and self.day4_secret_room:
                            if self.day4_secret_room.handle_click():
                                pass

                        elif self.state == State.ACT4_DAY5_TRANSITION and self.day5_transition:
                            self.day5_transition.update()
                            if self.day5_transition.can_transition():
                                self.create_day5_morning()
                                self.start_day_music()
                                self.state = State.ACT5_MORNING
                                self.day5_transition = None

                        # ДЕНЬ 5
                        elif self.state == State.ACT5_MORNING and self.day5_morning:
                            if self.day5_morning.handle_click():
                                pass

                        elif self.state == State.ACT5_CORRIDOR_RULES and self.day5_corridor_rules:
                            if self.day5_corridor_rules.handle_click():
                                pass

                        elif self.state == State.ACT5_SECRET_MEETING and self.day5_secret_meeting:
                            if self.day5_secret_meeting.handle_click():
                                pass

                        elif self.state == State.ACT5_MEDICAL_INFILTRATION and self.day5_medical_infiltration:
                            if self.day5_medical_infiltration.handle_click():
                                pass

                        elif self.state == State.ACT5_ARCHIVE_FIND and self.day5_archive_find:
                            if self.day5_archive_find.handle_click():
                                pass

                        elif self.state == State.ACT5_VIDEO_PROCEDURE and self.day5_video_procedure:
                            if self.day5_video_procedure.handle_click():
                                pass

                        elif self.state == State.ACT5_MEETING_KREIN and self.day5_meeting_krein:
                            if self.day5_meeting_krein.handle_click():
                                pass

                        elif self.state == State.ACT5_DAY6_TRANSITION and self.day6_transition:
                            self.day6_transition.update()
                            if self.day6_transition.can_transition():
                                self.create_day6_morning()
                                self.start_day_music()
                                self.state = State.ACT6_MORNING
                                self.day6_transition = None

                        # ДЕНЬ 6
                        elif self.state == State.ACT6_MORNING and self.day6_morning:
                            if self.day6_morning.handle_click():
                                pass

                        elif self.state == State.ACT6_CORRIDOR and self.day6_corridor:
                            if self.day6_corridor.handle_click():
                                pass

                        elif self.state == State.ACT6_SECRET_ROOM_TRAITOR and self.day6_secret_room_traitor:
                            if self.day6_secret_room_traitor.handle_click():
                                pass

                        elif self.state == State.ACT6_ROOF_CONFRONTATION and self.day6_roof_confrontation:
                            if self.day6_roof_confrontation.handle_click():
                                pass

                        elif self.state == State.ACT6_CORRIDOR_RETURN and self.day6_corridor_return:
                            if self.day6_corridor_return.handle_click():
                                pass

                        elif self.state == State.ACT6_INSOMNIA and self.day6_insomnia:
                            if self.day6_insomnia.handle_click():
                                pass

                        elif self.state == State.ACT6_DAY7_TRANSITION and self.day7_transition:
                            self.day7_transition.update()
                            if self.day7_transition.can_transition():
                                self.create_day7_morning()
                                self.start_day_music()
                                self.state = State.ACT7_MORNING
                                self.day7_transition = None

                        # ДЕНЬ 7
                        elif self.state == State.ACT7_MORNING and self.day7_morning:
                            if self.day7_morning.handle_click():
                                pass

                        elif self.state == State.ACT7_CORRIDOR_MAX and self.day7_corridor_max:
                            if self.day7_corridor_max.handle_click():
                                pass

                        elif self.state == State.ACT7_SECRET_PLANNING and self.day7_secret_planning:
                            if self.day7_secret_planning.handle_click():
                                pass

                        elif self.state == State.ACT7_ABANDONED_TRAP and self.day7_abandoned_trap:
                            if self.day7_abandoned_trap.handle_click():
                                pass

                        elif self.state == State.ACT7_SECRET_RETURN and self.day7_secret_return:
                            if self.day7_secret_return.handle_click():
                                pass

                        elif self.state == State.ACT7_INSOMNIA and self.day7_insomnia:
                            if self.day7_insomnia.handle_click():
                                pass

                        elif self.state == State.ACT7_DAY8_TRANSITION and self.day8_transition:
                            self.day8_transition.update()
                            if self.day8_transition.can_transition():
                                self.create_day8_morning()
                                self.start_tense_music()
                                self.state = State.ACT8_MORNING
                                self.day8_transition = None

                        # ДЕНЬ 8
                        elif self.state == State.ACT8_MORNING and self.day8_morning:
                            if self.day8_morning.handle_click():
                                pass

                        elif self.state == State.ACT8_CORRIDOR_OBSERVE and self.day8_corridor_observe:
                            if self.day8_corridor_observe.handle_click():
                                pass

                        elif self.state == State.ACT8_LIBRARY_ANALYSIS and self.day8_library_analysis:
                            if self.day8_library_analysis.handle_click():
                                pass

                        elif self.state == State.ACT8_DORMITORY_CLUES and self.day8_dormitory_clues:
                            if self.day8_dormitory_clues.handle_click():
                                pass

                        elif self.state == State.ACT8_PREPARATION and self.day8_preparation:
                            if self.day8_preparation.handle_click():
                                pass

                        elif self.state == State.ACT8_DAY9_TRANSITION and self.day9_transition:
                            self.day9_transition.update()
                            if self.day9_transition.can_transition():
                                self.create_day9_morning()
                                self.start_tense_music()
                                self.state = State.ACT9_MORNING
                                self.day9_transition = None

                        # ДЕНЬ 9
                        elif self.state == State.ACT9_MORNING and self.day9_morning:
                            if self.day9_morning.handle_click():
                                pass

                        elif self.state == State.ACT9_GYM_CONFRONTATION and self.day9_gym_confrontation:
                            if self.day9_gym_confrontation.handle_click():
                                pass

                        elif self.state == State.ACT9_CONFESSION_CHOICE and self.day9_confession_choice:
                            if self.day9_confession_choice.handle_click() is not None:
                                pass

                        elif self.state == State.ACT9_SECRET_MESSAGE and self.day9_secret_message:
                            if self.day9_secret_message.handle_click():
                                pass

                        elif self.state == State.ACT9_INSOMNIA and self.day9_insomnia:
                            if self.day9_insomnia.handle_click():
                                pass

                        elif self.state == State.ACT9_DAY10_TRANSITION and self.day10_transition:
                            self.day10_transition.update()
                            if self.day10_transition.can_transition():
                                self.create_day10_morning()
                                self.start_day_music()
                                self.state = State.ACT10_MORNING
                                self.day10_transition = None

                        # ДЕНЬ 10
                        elif self.state == State.ACT10_MORNING and self.day10_morning:
                            if self.day10_morning.handle_click():
                                pass

                        elif self.state == State.ACT10_CORRIDOR_BRANCH and self.day10_corridor_branch:
                            if self.day10_corridor_branch.handle_click():
                                pass

                        elif self.state == State.ACT10_SECRET_PLANNING and self.day10_secret_planning:
                            if self.day10_secret_planning.handle_click():
                                pass

                        elif self.state == State.ACT10_MEDICAL_PATH and self.day10_medical_path:
                            if self.day10_medical_path.handle_click():
                                pass

                        elif self.state == State.ACT10_HART_LAB and self.day10_hart_lab:
                            if self.day10_hart_lab.handle_click():
                                pass

                        elif self.state == State.ACT10_INSOMNIA and self.day10_insomnia:
                            if self.day10_insomnia.handle_click():
                                pass

                        elif self.state == State.ACT10_DAY11_TRANSITION and self.day11_transition:
                            self.day11_transition.update()
                            if self.day11_transition.can_transition():
                                self.create_day11_morning()
                                self.start_tense_music()
                                self.state = State.ACT11_MORNING
                                self.day11_transition = None

                        # ДЕНЬ 11
                        elif self.state == State.ACT11_MORNING and self.day11_morning:
                            if self.day11_morning.handle_click():
                                pass

                        elif self.state == State.ACT11_CORRIDOR_FOLLOW and self.day11_corridor_follow:
                            if self.day11_corridor_follow.handle_click():
                                pass

                        elif self.state == State.ACT11_LIBRARY_ANALYSIS and self.day11_library_analysis:
                            if self.day11_library_analysis.handle_click():
                                pass

                        elif self.state == State.ACT11_SAILAS_ROOM and self.day11_sailas_room:
                            if self.day11_sailas_room.handle_click():
                                pass

                        elif self.state == State.ACT11_PREPARATION and self.day11_preparation:
                            if self.day11_preparation.handle_click():
                                pass

                        elif self.state == State.ACT11_DAY12_TRANSITION and self.day12_transition:
                            self.day12_transition.update()
                            if self.day12_transition.can_transition():
                                self.create_act12_revelation()
                                self.start_tense_music()
                                self.state = State.ACT12_REVELATION
                                self.day12_transition = None

                        # ФИНАЛ
                        elif self.state == State.ACT12_REVELATION and self.act12_revelation:
                            if self.act12_revelation.handle_click():
                                pass

                        elif self.state == State.ACT12_SILENCE_BEFORE_STORM and self.act12_silence_before_storm:
                            if self.act12_silence_before_storm.handle_click():
                                pass

                        elif self.state == State.ACT12_HART_OFFICE and self.act12_hart_office:
                            if self.act12_hart_office.handle_click():
                                pass

                        elif self.state == State.ACT12_CHASE and self.act12_chase:
                            if self.act12_chase.handle_click():
                                pass

                        elif self.state == State.ACT12_LUCIA_CONFESSION and self.act12_lucia_confession:
                            if self.act12_lucia_confession.handle_click() is not None:
                                pass

                        elif self.state == State.ACT12_SAILAS_MADNESS and self.act12_sailas_madness:
                            if self.act12_sailas_madness.handle_click():
                                pass

                        elif self.state == State.ACT12_SAILAS_CHOICE and self.act12_sailas_choice:
                            if self.act12_sailas_choice.handle_click() is not None:
                                pass

                        elif self.state == State.ACT12_ENDING and self.act12_ending:
                            if self.act12_ending.handle_click():
                                self.create_act12_final_black()
                                self.start_final_music()
                                self.state = State.ACT12_FINAL_BLACK
                                self.act12_ending = None

                        elif self.state == State.ACT12_FINAL_BLACK and self.act12_final_black:
                            if self.act12_final_black.handle_click():
                                self.stop_music()
                                self.start_menu_music()
                                self.act12_final_black = None
                                self.state = State.MENU

                        # ПАУЗА И МЕНЮ
                        elif self.state == State.PAUSE:
                            res = self.pause.click(click_pos)
                            if res == "ПРОДОЛЖИТЬ":
                                self.pause.active = False
                                self.unpause_music()
                                # Восстановление состояния после паузы
                                if self.act12_final_black:
                                    self.state = State.ACT12_FINAL_BLACK
                                elif self.act12_ending:
                                    self.state = State.ACT12_ENDING
                                elif self.act12_sailas_choice:
                                    self.state = State.ACT12_SAILAS_CHOICE
                                elif self.act12_sailas_madness:
                                    self.state = State.ACT12_SAILAS_MADNESS
                                elif self.act12_lucia_confession:
                                    self.state = State.ACT12_LUCIA_CONFESSION
                                elif self.act12_chase:
                                    self.state = State.ACT12_CHASE
                                elif self.act12_hart_office:
                                    self.state = State.ACT12_HART_OFFICE
                                elif self.act12_silence_before_storm:
                                    self.state = State.ACT12_SILENCE_BEFORE_STORM
                                elif self.act12_revelation:
                                    self.state = State.ACT12_REVELATION
                                elif self.day12_transition:
                                    self.state = State.ACT11_DAY12_TRANSITION
                                elif self.day11_preparation:
                                    self.state = State.ACT11_PREPARATION
                                elif self.day11_sailas_room:
                                    self.state = State.ACT11_SAILAS_ROOM
                                elif self.day11_library_analysis:
                                    self.state = State.ACT11_LIBRARY_ANALYSIS
                                elif self.day11_corridor_follow:
                                    self.state = State.ACT11_CORRIDOR_FOLLOW
                                elif self.day11_morning:
                                    self.state = State.ACT11_MORNING
                                elif self.day11_transition:
                                    self.state = State.ACT10_DAY11_TRANSITION
                                elif self.day10_insomnia:
                                    self.state = State.ACT10_INSOMNIA
                                elif self.day10_hart_lab:
                                    self.state = State.ACT10_HART_LAB
                                elif self.day10_medical_path:
                                    self.state = State.ACT10_MEDICAL_PATH
                                elif self.day10_secret_planning:
                                    self.state = State.ACT10_SECRET_PLANNING
                                elif self.day10_corridor_branch:
                                    self.state = State.ACT10_CORRIDOR_BRANCH
                                elif self.day10_morning:
                                    self.state = State.ACT10_MORNING
                                elif self.day10_transition:
                                    self.state = State.ACT9_DAY10_TRANSITION
                                elif self.day9_insomnia:
                                    self.state = State.ACT9_INSOMNIA
                                elif self.day9_secret_message:
                                    self.state = State.ACT9_SECRET_MESSAGE
                                elif self.day9_confession_choice:
                                    self.state = State.ACT9_CONFESSION_CHOICE
                                elif self.day9_gym_confrontation:
                                    self.state = State.ACT9_GYM_CONFRONTATION
                                elif self.day9_morning:
                                    self.state = State.ACT9_MORNING
                                elif self.day9_transition:
                                    self.state = State.ACT8_DAY9_TRANSITION
                                elif self.day8_preparation:
                                    self.state = State.ACT8_PREPARATION
                                elif self.day8_dormitory_clues:
                                    self.state = State.ACT8_DORMITORY_CLUES
                                elif self.day8_library_analysis:
                                    self.state = State.ACT8_LIBRARY_ANALYSIS
                                elif self.day8_corridor_observe:
                                    self.state = State.ACT8_CORRIDOR_OBSERVE
                                elif self.day8_morning:
                                    self.state = State.ACT8_MORNING
                                elif self.day8_transition:
                                    self.state = State.ACT7_DAY8_TRANSITION
                                elif self.day7_insomnia:
                                    self.state = State.ACT7_INSOMNIA
                                elif self.day7_secret_return:
                                    self.state = State.ACT7_SECRET_RETURN
                                elif self.day7_abandoned_trap:
                                    self.state = State.ACT7_ABANDONED_TRAP
                                elif self.day7_secret_planning:
                                    self.state = State.ACT7_SECRET_PLANNING
                                elif self.day7_corridor_max:
                                    self.state = State.ACT7_CORRIDOR_MAX
                                elif self.day7_morning:
                                    self.state = State.ACT7_MORNING
                                elif self.day7_transition:
                                    self.state = State.ACT6_DAY7_TRANSITION
                                elif self.day6_insomnia:
                                    self.state = State.ACT6_INSOMNIA
                                elif self.day6_corridor_return:
                                    self.state = State.ACT6_CORRIDOR_RETURN
                                elif self.day6_roof_confrontation:
                                    self.state = State.ACT6_ROOF_CONFRONTATION
                                elif self.day6_secret_room_traitor:
                                    self.state = State.ACT6_SECRET_ROOM_TRAITOR
                                elif self.day6_corridor:
                                    self.state = State.ACT6_CORRIDOR
                                elif self.day6_morning:
                                    self.state = State.ACT6_MORNING
                                elif self.day6_transition:
                                    self.state = State.ACT5_DAY6_TRANSITION
                                elif self.day5_meeting_krein:
                                    self.state = State.ACT5_MEETING_KREIN
                                elif self.day5_video_procedure:
                                    self.state = State.ACT5_VIDEO_PROCEDURE
                                elif self.day5_archive_find:
                                    self.state = State.ACT5_ARCHIVE_FIND
                                elif self.day5_medical_infiltration:
                                    self.state = State.ACT5_MEDICAL_INFILTRATION
                                elif self.day5_secret_meeting:
                                    self.state = State.ACT5_SECRET_MEETING
                                elif self.day5_corridor_rules:
                                    self.state = State.ACT5_CORRIDOR_RULES
                                elif self.day5_morning:
                                    self.state = State.ACT5_MORNING
                                elif self.day5_transition:
                                    self.state = State.ACT4_DAY5_TRANSITION
                                elif self.day4_secret_room:
                                    self.state = State.ACT4_SECRET_ROOM
                                elif self.day4_old_library:
                                    self.state = State.ACT4_OLD_LIBRARY
                                elif self.day4_corridor_warning:
                                    self.state = State.ACT4_CORRIDOR_WARNING
                                elif self.day4_math_test:
                                    self.state = State.ACT4_MATH_TEST
                                elif self.day4_morning:
                                    self.state = State.ACT4_MORNING
                                elif self.day4_transition:
                                    self.state = State.ACT3_DAY4_TRANSITION
                                elif self.day3_night:
                                    self.state = State.ACT3_NIGHT
                                elif self.awakening_scene:
                                    self.state = State.ACT3_AWAKENING
                                elif self.day3_library_scene:
                                    self.state = State.ACT3_LIBRARY_EVENING
                                elif self.sailas_corridor_scene:
                                    self.state = State.ACT3_CORRIDOR_SAILAS
                                elif self.math_exam_scene:
                                    self.state = State.ACT3_MATH_EXAM
                                elif self.day3_morning:
                                    self.state = State.ACT3_MORNING
                                elif self.day3_transition:
                                    self.state = State.ACT2_DAY3_TRANSITION
                                elif self.day2_night:
                                    self.state = State.ACT2_NIGHT
                                elif self.library_scene:
                                    self.state = State.ACT2_LIBRARY
                                elif self.closed_wing_scene:
                                    self.state = State.ACT2_CLOSED_WING
                                elif self.post_lecture_scene:
                                    self.state = State.ACT2_POST_LECTURE
                                elif self.lecture_scene:
                                    self.state = State.ACT2_LECTURE
                                elif self.day2_corridor:
                                    self.state = State.ACT2_CORRIDOR
                                elif self.day2_morning:
                                    self.state = State.ACT2_MORNING
                                elif self.day2_transition:
                                    self.state = State.ACT1_DAY2_TRANSITION
                                elif self.insomnia_scene:
                                    self.state = State.ACT1_INSOMNIA
                                elif self.empty_corridor_scene:
                                    self.state = State.ACT1_EMPTY_CORRIDOR
                                elif self.night_scene:
                                    self.state = State.ACT1_NIGHT
                                elif self.evening_scene:
                                    self.state = State.ACT1_EVENING
                                elif self.lucia_scene:
                                    self.state = State.ACT1_LUCIA
                                elif self.canteen_scene:
                                    self.state = State.ACT1_CANTEEN
                                elif self.lesson_scene:
                                    self.state = State.ACT1_LESSON
                                elif self.corridor_scene:
                                    self.state = State.ACT1_CORRIDOR
                                elif self.morning_scene:
                                    self.state = State.ACT1_MORNING
                                elif self.act1_transition:
                                    self.state = State.ACT1_TRANSITION
                                elif self.thoughts:
                                    self.state = State.THOUGHTS
                                elif self.wake_up:
                                    self.state = State.PROLOGUE_WAKE
                                else:
                                    self.state = State.PROLOGUE
                            elif res == "В МЕНЮ":
                                self.stop_music()
                                self.start_menu_music()
                                # Очистка всех сцен
                                self.prologue = None
                                self.wake_up = None
                                self.thoughts = None
                                self.act1_transition = None
                                self.morning_scene = None
                                self.corridor_scene = None
                                self.lesson_scene = None
                                self.canteen_scene = None
                                self.lucia_scene = None
                                self.evening_scene = None
                                self.night_scene = None
                                self.empty_corridor_scene = None
                                self.insomnia_scene = None
                                self.day2_transition = None
                                self.day2_morning = None
                                self.day2_corridor = None
                                self.lecture_scene = None
                                self.post_lecture_scene = None
                                self.closed_wing_scene = None
                                self.library_scene = None
                                self.day2_night = None
                                self.day3_transition = None
                                self.day3_morning = None
                                self.math_exam_scene = None
                                self.sailas_corridor_scene = None
                                self.day3_library_scene = None
                                self.awakening_scene = None
                                self.day3_night = None
                                self.day4_transition = None
                                self.day4_morning = None
                                self.day4_math_test = None
                                self.day4_corridor_warning = None
                                self.day4_old_library = None
                                self.day4_secret_room = None
                                self.day5_transition = None
                                self.day5_morning = None
                                self.day5_corridor_rules = None
                                self.day5_secret_meeting = None
                                self.day5_medical_infiltration = None
                                self.day5_archive_find = None
                                self.day5_video_procedure = None
                                self.day5_meeting_krein = None
                                self.day6_transition = None
                                self.day6_morning = None
                                self.day6_corridor = None
                                self.day6_secret_room_traitor = None
                                self.day6_roof_confrontation = None
                                self.day6_corridor_return = None
                                self.day6_insomnia = None
                                self.day7_transition = None
                                self.day7_morning = None
                                self.day7_corridor_max = None
                                self.day7_secret_planning = None
                                self.day7_abandoned_trap = None
                                self.day7_secret_return = None
                                self.day7_insomnia = None
                                self.day8_transition = None
                                self.day8_morning = None
                                self.day8_corridor_observe = None
                                self.day8_library_analysis = None
                                self.day8_dormitory_clues = None
                                self.day8_preparation = None
                                self.day9_transition = None
                                self.day9_morning = None
                                self.day9_gym_confrontation = None
                                self.day9_confession_choice = None
                                self.day9_secret_message = None
                                self.day9_insomnia = None
                                self.day10_transition = None
                                self.day10_morning = None
                                self.day10_corridor_branch = None
                                self.day10_secret_planning = None
                                self.day10_medical_path = None
                                self.day10_hart_lab = None
                                self.day10_insomnia = None
                                self.day11_transition = None
                                self.day11_morning = None
                                self.day11_corridor_follow = None
                                self.day11_library_analysis = None
                                self.day11_sailas_room = None
                                self.day11_preparation = None
                                self.day12_transition = None
                                self.act12_revelation = None
                                self.act12_silence_before_storm = None
                                self.act12_hart_office = None
                                self.act12_chase = None
                                self.act12_lucia_confession = None
                                self.act12_sailas_madness = None
                                self.act12_sailas_choice = None
                                self.act12_ending = None
                                self.act12_final_black = None
                                self.state = State.MENU
                            elif res == "ВЫЙТИ":
                                running = False

                        # ГЛАВНОЕ МЕНЮ
                        elif self.state == State.MENU:
                            res = self.menu.click(click_pos)
                            if self.chalk_sound:
                                self.chalk_sound.play()
                            if res == "НОВАЯ ИГРА":
                                self.start_new_game()
                            elif res == "ВЫХОД":
                                running = False
            # ОБРАБОТКА ВЫБОРОВ
            if self.state == State.ACT9_CONFESSION_CHOICE and self.day9_confession_choice and self.day9_confession_choice.choice_shown:
                if click_pos:
                    choice = self.day9_confession_choice.handle_choice_click(click_pos)
                    if choice:
                        self.player_choice = choice

            if self.state == State.ACT12_LUCIA_CONFESSION and self.act12_lucia_confession and self.act12_lucia_confession.waiting_for_choice:
                if click_pos:
                    choice = self.act12_lucia_confession.handle_choice_click(click_pos)
                    if choice:
                        self.lucia_choice = choice

            if self.state == State.ACT12_SAILAS_CHOICE and self.act12_sailas_choice and self.act12_sailas_choice.waiting_for_choice:
                if click_pos:
                    choice = self.act12_sailas_choice.handle_choice_click(click_pos)
                    if choice:
                        self.sailas_choice = choice

            # ОБНОВЛЕНИЕ ВСПЫШКИ
            if white_flash_active:
                white_flash_timer += 1
                if white_flash_timer > 10:
                    white_flash_alpha -= 25
                    if white_flash_alpha <= 0:
                        white_flash_alpha = 0
                        white_flash_active = False
                        self.start_wake_music()

            # ОБНОВЛЕНИЕ СОСТОЯНИЙ
            if self.state == State.BOOT:
                if self.boot.update():
                    self.state = State.LOGO

            elif self.state == State.LOGO:
                if self.logo:
                    self.logo.update()
                    if self.logo.complete:
                        self.state = State.DISCLAIMER
                else:
                    self.state = State.DISCLAIMER

            elif self.state == State.PROLOGUE:
                if self.prologue:
                    self.prologue.update()

            elif self.state == State.PROLOGUE_WAKE:
                if self.wake_up:
                    self.wake_up.update()

            elif self.state == State.THOUGHTS:
                if self.thoughts:
                    self.thoughts.update()

            elif self.state == State.ACT1_TRANSITION:
                if self.act1_transition:
                    self.act1_transition.update()
                    if self.act1_transition.can_transition_to_morning():
                        self.create_morning_scene()
                        self.start_day_music()
                        self.state = State.ACT1_MORNING
                        self.act1_transition = None

            elif self.state == State.ACT1_MORNING:
                if self.morning_scene:
                    self.morning_scene.update()
                    if self.morning_scene.is_complete():
                        self.create_corridor_scene()
                        self.state = State.ACT1_CORRIDOR
                        self.morning_scene = None

            elif self.state == State.ACT1_CORRIDOR:
                if self.corridor_scene:
                    self.corridor_scene.update()
                    if self.corridor_scene.can_transition():
                        self.create_lesson_scene()
                        if self.door_sound:
                            self.door_sound.play()
                        self.start_tense_music()
                        self.state = State.ACT1_LESSON
                        self.corridor_scene = None

            elif self.state == State.ACT1_LESSON:
                if self.lesson_scene:
                    self.lesson_scene.update()
                    if self.lesson_scene.can_transition():
                        self.create_canteen_scene()
                        if self.ambient_sound:
                            ambient_channel = self.ambient_sound.play(-1)
                            self.ambient_sound.set_volume(0.5)
                        self.start_day_music()
                        self.state = State.ACT1_CANTEEN
                        self.lesson_scene = None

            elif self.state == State.ACT1_CANTEEN:
                if self.canteen_scene:
                    self.canteen_scene.update()
                    if self.canteen_scene.crash_triggered and not self.canteen_scene.crash_sound_played:
                        self.canteen_scene.crash_sound_played = True
                        if self.ambient_sound:
                            self.ambient_sound.stop()
                        if self.crash_sound:
                            self.crash_sound.play()
                    if self.canteen_scene.can_transition():
                        self.create_lucia_scene()
                        self.state = State.ACT1_LUCIA
                        self.canteen_scene = None

            elif self.state == State.ACT1_LUCIA:
                if self.lucia_scene:
                    self.lucia_scene.update()
                    if self.lucia_scene.can_transition():
                        self.create_evening_scene()
                        self.state = State.ACT1_EVENING
                        self.lucia_scene = None

            elif self.state == State.ACT1_EVENING:
                if self.evening_scene:
                    self.evening_scene.update()
                    if self.evening_scene.should_play_key_sound():
                        if self.key_sound:
                            self.key_sound.play()
                    if self.evening_scene.can_transition():
                        self.create_night_scene()
                        self.start_anxiety_music()
                        self.state = State.ACT1_NIGHT
                        self.evening_scene = None

            elif self.state == State.ACT1_NIGHT:
                if self.night_scene:
                    self.night_scene.update()
                    if self.night_scene.should_play_scratch():
                        if self.scratch_sound:
                            self.scratch_sound.play()
                    if self.night_scene.can_transition():
                        self.create_empty_corridor_scene()
                        self.start_anxiety_music()
                        self.state = State.ACT1_EMPTY_CORRIDOR
                        self.night_scene = None

            elif self.state == State.ACT1_EMPTY_CORRIDOR:
                if self.empty_corridor_scene:
                    self.empty_corridor_scene.update()
                    if self.empty_corridor_scene.can_transition():
                        self.create_insomnia_scene()
                        self.start_aftermath_music()
                        self.state = State.ACT1_INSOMNIA
                        self.empty_corridor_scene = None

            elif self.state == State.ACT1_INSOMNIA:
                if self.insomnia_scene:
                    self.insomnia_scene.update()
                    if self.insomnia_scene.can_transition():
                        self.create_day2_transition()
                        self.stop_music()
                        self.state = State.ACT1_DAY2_TRANSITION
                        self.insomnia_scene = None

            elif self.state == State.ACT1_DAY2_TRANSITION:
                if self.day2_transition:
                    self.day2_transition.update()
                    if self.day2_transition.can_transition():
                        self.create_day2_morning()
                        self.start_day_music()
                        self.state = State.ACT2_MORNING
                        self.day2_transition = None

            elif self.state == State.ACT2_MORNING:
                if self.day2_morning:
                    self.day2_morning.update()
                    if self.day2_morning.is_complete():
                        self.create_day2_corridor()
                        self.state = State.ACT2_CORRIDOR
                        self.day2_morning = None

            elif self.state == State.ACT2_CORRIDOR:
                if self.day2_corridor:
                    self.day2_corridor.update()
                    if self.day2_corridor.can_transition():
                        self.create_lecture_scene()
                        if self.door_sound:
                            self.door_sound.play()
                        self.start_tense_music()
                        self.state = State.ACT2_LECTURE
                        self.day2_corridor = None

            elif self.state == State.ACT2_LECTURE:
                if self.lecture_scene:
                    self.lecture_scene.update()
                    if self.lecture_scene.can_transition():
                        self.create_post_lecture_scene()
                        self.state = State.ACT2_POST_LECTURE
                        self.lecture_scene = None

            elif self.state == State.ACT2_POST_LECTURE:
                if self.post_lecture_scene:
                    self.post_lecture_scene.update()
                    if self.post_lecture_scene.can_transition():
                        self.create_closed_wing_scene()
                        self.start_anxiety_music()
                        self.state = State.ACT2_CLOSED_WING
                        self.post_lecture_scene = None

            elif self.state == State.ACT2_CLOSED_WING:
                if self.closed_wing_scene:
                    self.closed_wing_scene.update()
                    if self.closed_wing_scene.can_transition():
                        self.create_library_scene()
                        self.start_day_music()
                        self.state = State.ACT2_LIBRARY
                        self.closed_wing_scene = None

            elif self.state == State.ACT2_LIBRARY:
                if self.library_scene:
                    self.library_scene.update()
                    if self.library_scene.can_transition():
                        self.create_day2_night()
                        self.start_aftermath_music()
                        self.state = State.ACT2_NIGHT
                        self.library_scene = None

            elif self.state == State.ACT2_NIGHT:
                if self.day2_night:
                    self.day2_night.update()
                    if self.day2_night.can_transition():
                        self.create_day3_transition()
                        self.stop_music()
                        self.state = State.ACT2_DAY3_TRANSITION
                        self.day2_night = None

            elif self.state == State.ACT2_DAY3_TRANSITION:
                if self.day3_transition:
                    self.day3_transition.update()
                    if self.day3_transition.can_transition():
                        self.create_day3_morning()
                        self.start_day_music()
                        self.state = State.ACT3_MORNING
                        self.day3_transition = None

            elif self.state == State.ACT3_MORNING:
                if self.day3_morning:
                    self.day3_morning.update()
                    if self.day3_morning.is_complete():
                        self.create_math_exam_scene()
                        if self.tick_tock_sound:
                            tick_tock_channel = self.tick_tock_sound.play(-1)
                            self.tick_tock_sound.set_volume(0.3)
                        self.start_tense_music()
                        self.state = State.ACT3_MATH_EXAM
                        self.day3_morning = None

            elif self.state == State.ACT3_MATH_EXAM:
                if self.math_exam_scene:
                    self.math_exam_scene.update()
                    if self.math_exam_scene.can_transition():
                        if self.tick_tock_sound:
                            self.tick_tock_sound.stop()
                        self.create_sailas_corridor_scene()
                        self.start_anxiety_music()
                        self.state = State.ACT3_CORRIDOR_SAILAS
                        self.math_exam_scene = None

            elif self.state == State.ACT3_CORRIDOR_SAILAS:
                if self.sailas_corridor_scene:
                    self.sailas_corridor_scene.update()
                    if self.sailas_corridor_scene.can_transition():
                        self.create_day3_library_scene()
                        self.start_aftermath_music()
                        self.state = State.ACT3_LIBRARY_EVENING
                        self.sailas_corridor_scene = None

            elif self.state == State.ACT3_LIBRARY_EVENING:
                if self.day3_library_scene:
                    self.day3_library_scene.update()
                    if self.day3_library_scene.can_transition():
                        self.create_awakening_scene()
                        self.start_dar_music()
                        self.state = State.ACT3_AWAKENING
                        self.day3_library_scene = None

            elif self.state == State.ACT3_AWAKENING:
                if self.awakening_scene:
                    self.awakening_scene.update()
                    if self.awakening_scene.can_transition():
                        self.create_day3_night()
                        self.start_aftermath_music()
                        self.state = State.ACT3_NIGHT
                        self.awakening_scene = None

            elif self.state == State.ACT3_NIGHT:
                if self.day3_night:
                    self.day3_night.update()
                    if self.day3_night.can_transition():
                        self.create_day4_transition()
                        self.stop_music()
                        self.state = State.ACT3_DAY4_TRANSITION
                        self.day3_night = None

            elif self.state == State.ACT3_DAY4_TRANSITION:
                if self.day4_transition:
                    self.day4_transition.update()
                    if self.day4_transition.can_transition():
                        self.create_day4_morning()
                        self.start_day_music()
                        self.state = State.ACT4_MORNING
                        self.day4_transition = None

            elif self.state == State.ACT4_MORNING:
                if self.day4_morning:
                    self.day4_morning.update()
                    if self.day4_morning.can_transition():
                        self.create_day4_math_test()
                        if self.tick_tock_sound:
                            tick_tock_channel = self.tick_tock_sound.play(-1)
                            self.tick_tock_sound.set_volume(0.3)
                        self.start_tense_music()
                        self.state = State.ACT4_MATH_TEST
                        self.day4_morning = None

            elif self.state == State.ACT4_MATH_TEST:
                if self.day4_math_test:
                    self.day4_math_test.update()
                    if self.day4_math_test.can_transition():
                        if self.tick_tock_sound:
                            self.tick_tock_sound.stop()
                        self.create_day4_corridor_warning()
                        self.start_anxiety_music()
                        self.state = State.ACT4_CORRIDOR_WARNING
                        self.day4_math_test = None

            elif self.state == State.ACT4_CORRIDOR_WARNING:
                if self.day4_corridor_warning:
                    self.day4_corridor_warning.update()
                    if self.day4_corridor_warning.can_transition():
                        self.create_day4_old_library()
                        self.start_kulm_music()
                        self.state = State.ACT4_OLD_LIBRARY
                        self.day4_corridor_warning = None

            elif self.state == State.ACT4_OLD_LIBRARY:
                if self.day4_old_library:
                    self.day4_old_library.update()
                    if self.day4_old_library.can_transition():
                        self.create_day4_secret_room()
                        self.state = State.ACT4_SECRET_ROOM
                        self.day4_old_library = None

            elif self.state == State.ACT4_SECRET_ROOM:
                if self.day4_secret_room:
                    self.day4_secret_room.update()
                    if self.day4_secret_room.can_transition():
                        self.create_day5_transition()
                        self.stop_music()
                        self.state = State.ACT4_DAY5_TRANSITION
                        self.day4_secret_room = None

            elif self.state == State.ACT4_DAY5_TRANSITION:
                if self.day5_transition:
                    self.day5_transition.update()
                    if self.day5_transition.can_transition():
                        self.create_day5_morning()
                        self.start_day_music()
                        self.state = State.ACT5_MORNING
                        self.day5_transition = None

            elif self.state == State.ACT5_MORNING:
                if self.day5_morning:
                    self.day5_morning.update()
                    if self.day5_morning.can_transition():
                        self.create_day5_corridor_rules()
                        self.play_footsteps()
                        self.state = State.ACT5_CORRIDOR_RULES
                        self.day5_morning = None

            elif self.state == State.ACT5_CORRIDOR_RULES:
                if self.day5_corridor_rules:
                    self.day5_corridor_rules.update()
                    if self.day5_corridor_rules.can_transition():
                        self.create_day5_secret_meeting()
                        self.start_kulm_music()
                        self.state = State.ACT5_SECRET_MEETING
                        self.day5_corridor_rules = None

            elif self.state == State.ACT5_SECRET_MEETING:
                if self.day5_secret_meeting:
                    self.day5_secret_meeting.update()
                    if self.day5_secret_meeting.can_transition():
                        self.create_day5_medical_infiltration()
                        self.start_dark_walk_music()
                        self.play_footsteps()
                        self.state = State.ACT5_MEDICAL_INFILTRATION
                        self.day5_secret_meeting = None

            elif self.state == State.ACT5_MEDICAL_INFILTRATION:
                if self.day5_medical_infiltration:
                    self.day5_medical_infiltration.update()
                    if self.day5_medical_infiltration.can_transition():
                        self.create_day5_archive_find()
                        self.state = State.ACT5_ARCHIVE_FIND
                        self.day5_medical_infiltration = None

            elif self.state == State.ACT5_ARCHIVE_FIND:
                if self.day5_archive_find:
                    self.day5_archive_find.update()
                    if self.day5_archive_find.can_transition():
                        self.create_day5_video_procedure()
                        self.start_tuctuc_music()
                        self.state = State.ACT5_VIDEO_PROCEDURE
                        self.day5_archive_find = None

            elif self.state == State.ACT5_VIDEO_PROCEDURE:
                if self.day5_video_procedure:
                    self.day5_video_procedure.update()
                    if self.day5_video_procedure.can_transition():
                        self.create_day5_meeting_krein()
                        self.start_tense_music()
                        self.state = State.ACT5_MEETING_KREIN
                        self.day5_video_procedure = None

            elif self.state == State.ACT5_MEETING_KREIN:
                if self.day5_meeting_krein:
                    self.day5_meeting_krein.update()
                    if self.day5_meeting_krein.can_transition():
                        self.create_day6_transition()
                        self.stop_music()
                        self.state = State.ACT5_DAY6_TRANSITION
                        self.day5_meeting_krein = None

            elif self.state == State.ACT5_DAY6_TRANSITION:
                if self.day6_transition:
                    self.day6_transition.update()
                    if self.day6_transition.can_transition():
                        self.create_day6_morning()
                        self.start_day_music()
                        self.state = State.ACT6_MORNING
                        self.day6_transition = None

            elif self.state == State.ACT6_MORNING:
                if self.day6_morning:
                    self.day6_morning.update()
                    if self.day6_morning.can_transition():
                        self.create_day6_corridor()
                        self.play_footsteps()
                        self.state = State.ACT6_CORRIDOR
                        self.day6_morning = None

            elif self.state == State.ACT6_CORRIDOR:
                if self.day6_corridor:
                    self.day6_corridor.update()
                    if self.day6_corridor.can_transition():
                        self.create_day6_secret_room_traitor()
                        self.start_tense_music()
                        self.state = State.ACT6_SECRET_ROOM_TRAITOR
                        self.day6_corridor = None

            elif self.state == State.ACT6_SECRET_ROOM_TRAITOR:
                if self.day6_secret_room_traitor:
                    self.day6_secret_room_traitor.update()
                    if self.day6_secret_room_traitor.can_transition():
                        self.create_day6_roof_confrontation()
                        self.start_aftermath_music()
                        self.state = State.ACT6_ROOF_CONFRONTATION
                        self.day6_secret_room_traitor = None

            elif self.state == State.ACT6_ROOF_CONFRONTATION:
                if self.day6_roof_confrontation:
                    self.day6_roof_confrontation.update()
                    if self.day6_roof_confrontation.can_transition():
                        self.create_day6_corridor_return()
                        self.start_anxiety_music()
                        self.state = State.ACT6_CORRIDOR_RETURN
                        self.day6_roof_confrontation = None

            elif self.state == State.ACT6_CORRIDOR_RETURN:
                if self.day6_corridor_return:
                    self.day6_corridor_return.update()
                    if self.day6_corridor_return.can_transition():
                        self.create_day6_insomnia()
                        self.start_aftermath_music()
                        self.state = State.ACT6_INSOMNIA
                        self.day6_corridor_return = None

            elif self.state == State.ACT6_INSOMNIA:
                if self.day6_insomnia:
                    self.day6_insomnia.update()
                    if self.day6_insomnia.can_transition():
                        self.create_day7_transition()
                        self.stop_music()
                        self.state = State.ACT6_DAY7_TRANSITION
                        self.day6_insomnia = None

            elif self.state == State.ACT6_DAY7_TRANSITION:
                if self.day7_transition:
                    self.day7_transition.update()
                    if self.day7_transition.can_transition():
                        self.create_day7_morning()
                        self.start_day_music()
                        self.state = State.ACT7_MORNING
                        self.day7_transition = None

            elif self.state == State.ACT7_MORNING:
                if self.day7_morning:
                    self.day7_morning.update()
                    if self.day7_morning.can_transition():
                        self.create_day7_corridor_max()
                        self.play_footsteps()
                        self.state = State.ACT7_CORRIDOR_MAX
                        self.day7_morning = None

            elif self.state == State.ACT7_CORRIDOR_MAX:
                if self.day7_corridor_max:
                    self.day7_corridor_max.update()
                    if self.day7_corridor_max.can_transition():
                        self.create_day7_secret_planning()
                        self.start_kulm_music()
                        self.state = State.ACT7_SECRET_PLANNING
                        self.day7_corridor_max = None

            elif self.state == State.ACT7_SECRET_PLANNING:
                if self.day7_secret_planning:
                    self.day7_secret_planning.update()
                    if self.day7_secret_planning.can_transition():
                        self.create_day7_abandoned_trap()
                        self.start_anxiety_music()
                        self.play_footsteps()
                        self.state = State.ACT7_ABANDONED_TRAP
                        self.day7_secret_planning = None

            elif self.state == State.ACT7_ABANDONED_TRAP:
                if self.day7_abandoned_trap:
                    self.day7_abandoned_trap.update()
                    if self.day7_abandoned_trap.can_transition():
                        self.create_day7_secret_return()
                        self.start_tense_music()
                        self.state = State.ACT7_SECRET_RETURN
                        self.day7_abandoned_trap = None

            elif self.state == State.ACT7_SECRET_RETURN:
                if self.day7_secret_return:
                    self.day7_secret_return.update()
                    if self.day7_secret_return.can_transition():
                        self.create_day7_insomnia()
                        self.start_aftermath_music()
                        self.state = State.ACT7_INSOMNIA
                        self.day7_secret_return = None

            elif self.state == State.ACT7_INSOMNIA:
                if self.day7_insomnia:
                    self.day7_insomnia.update()
                    if self.day7_insomnia.can_transition():
                        self.create_day8_transition()
                        self.stop_music()
                        self.state = State.ACT7_DAY8_TRANSITION
                        self.day7_insomnia = None

            elif self.state == State.ACT7_DAY8_TRANSITION:
                if self.day8_transition:
                    self.day8_transition.update()
                    if self.day8_transition.can_transition():
                        self.create_day8_morning()
                        self.start_tense_music()
                        self.state = State.ACT8_MORNING
                        self.day8_transition = None

            elif self.state == State.ACT8_MORNING:
                if self.day8_morning:
                    self.day8_morning.update()
                    if self.day8_morning.can_transition():
                        self.create_day8_corridor_observe()
                        self.state = State.ACT8_CORRIDOR_OBSERVE
                        self.day8_morning = None

            elif self.state == State.ACT8_CORRIDOR_OBSERVE:
                if self.day8_corridor_observe:
                    self.day8_corridor_observe.update()
                    if self.day8_corridor_observe.can_transition():
                        self.create_day8_library_analysis()
                        self.start_day_music()
                        self.state = State.ACT8_LIBRARY_ANALYSIS
                        self.day8_corridor_observe = None

            elif self.state == State.ACT8_LIBRARY_ANALYSIS:
                if self.day8_library_analysis:
                    self.day8_library_analysis.update()
                    if self.day8_library_analysis.can_transition():
                        self.create_day8_dormitory_clues()
                        self.start_anxiety_music()
                        self.state = State.ACT8_DORMITORY_CLUES
                        self.day8_library_analysis = None

            elif self.state == State.ACT8_DORMITORY_CLUES:
                if self.day8_dormitory_clues:
                    self.day8_dormitory_clues.update()
                    if self.day8_dormitory_clues.can_transition():
                        self.create_day8_preparation()
                        self.start_aftermath_music()
                        self.state = State.ACT8_PREPARATION
                        self.day8_dormitory_clues = None

            elif self.state == State.ACT8_PREPARATION:
                if self.day8_preparation:
                    self.day8_preparation.update()
                    if self.day8_preparation.can_transition():
                        self.create_day9_transition()
                        self.stop_music()
                        self.state = State.ACT8_DAY9_TRANSITION
                        self.day8_preparation = None

            elif self.state == State.ACT8_DAY9_TRANSITION:
                if self.day9_transition:
                    self.day9_transition.update()
                    if self.day9_transition.can_transition():
                        self.create_day9_morning()
                        self.start_tense_music()
                        self.state = State.ACT9_MORNING
                        self.day9_transition = None

            # ДЕНЬ 9 - ОБНОВЛЕНИЯ
            elif self.state == State.ACT9_MORNING:
                if self.day9_morning:
                    self.day9_morning.update()
                    if self.day9_morning.can_transition():
                        self.create_day9_gym_confrontation()
                        self.start_anxiety_music()
                        self.state = State.ACT9_GYM_CONFRONTATION
                        self.day9_morning = None

            elif self.state == State.ACT9_GYM_CONFRONTATION:
                if self.day9_gym_confrontation:
                    self.day9_gym_confrontation.update()
                    if self.day9_gym_confrontation.can_transition():
                        self.create_day9_confession_choice()
                        self.start_prizn_music()
                        self.state = State.ACT9_CONFESSION_CHOICE
                        self.day9_gym_confrontation = None

            elif self.state == State.ACT9_CONFESSION_CHOICE:
                if self.day9_confession_choice:
                    self.day9_confession_choice.update()
                    if self.day9_confession_choice.can_transition():
                        if self.player_choice:
                            self.create_day9_secret_message(self.player_choice)
                            self.state = State.ACT9_SECRET_MESSAGE
                            self.day9_confession_choice = None

            elif self.state == State.ACT9_SECRET_MESSAGE:
                if self.day9_secret_message:
                    self.day9_secret_message.update()
                    if self.day9_secret_message.can_transition():
                        self.create_day9_insomnia()
                        self.start_aftermath_music()
                        self.state = State.ACT9_INSOMNIA
                        self.day9_secret_message = None

            elif self.state == State.ACT9_INSOMNIA:
                if self.day9_insomnia:
                    self.day9_insomnia.update()
                    if self.day9_insomnia.can_transition():
                        self.create_day10_transition()
                        self.stop_music()
                        self.state = State.ACT9_DAY10_TRANSITION
                        self.day9_insomnia = None

            elif self.state == State.ACT9_DAY10_TRANSITION:
                if self.day10_transition:
                    self.day10_transition.update()
                    if self.day10_transition.can_transition():
                        self.create_day10_morning()
                        self.start_day_music()
                        self.state = State.ACT10_MORNING
                        self.day10_transition = None

            # ДЕНЬ 10 - ОБНОВЛЕНИЯ
            elif self.state == State.ACT10_MORNING:
                if self.day10_morning:
                    self.day10_morning.update()
                    if self.day10_morning.can_transition():
                        self.create_day10_corridor_branch(self.player_choice)
                        self.start_day_music()
                        self.state = State.ACT10_CORRIDOR_BRANCH
                        self.day10_morning = None

            elif self.state == State.ACT10_CORRIDOR_BRANCH:
                if self.day10_corridor_branch:
                    self.day10_corridor_branch.update()
                    if self.day10_corridor_branch.can_transition():
                        self.create_day10_secret_planning()
                        self.start_kulm_music()
                        self.state = State.ACT10_SECRET_PLANNING
                        self.day10_corridor_branch = None

            elif self.state == State.ACT10_SECRET_PLANNING:
                if self.day10_secret_planning:
                    self.day10_secret_planning.update()
                    if self.day10_secret_planning.can_transition():
                        self.create_day10_medical_path()
                        self.start_anxiety_music()
                        self.state = State.ACT10_MEDICAL_PATH
                        self.day10_secret_planning = None

            elif self.state == State.ACT10_MEDICAL_PATH:
                if self.day10_medical_path:
                    self.day10_medical_path.update()
                    if self.day10_medical_path.can_transition():
                        self.create_day10_hart_lab()
                        self.start_tuctuc_music()
                        self.state = State.ACT10_HART_LAB
                        self.day10_medical_path = None

            elif self.state == State.ACT10_HART_LAB:
                if self.day10_hart_lab:
                    self.day10_hart_lab.update()
                    if self.day10_hart_lab.can_transition():
                        self.create_day10_insomnia()
                        self.start_tense_music()
                        self.state = State.ACT10_INSOMNIA
                        self.day10_hart_lab = None

            elif self.state == State.ACT10_INSOMNIA:
                if self.day10_insomnia:
                    self.day10_insomnia.update()
                    if self.day10_insomnia.can_transition():
                        self.create_day11_transition()
                        self.stop_music()
                        self.state = State.ACT10_DAY11_TRANSITION
                        self.day10_insomnia = None

            elif self.state == State.ACT10_DAY11_TRANSITION:
                if self.day11_transition:
                    self.day11_transition.update()
                    if self.day11_transition.can_transition():
                        self.create_day11_morning()
                        self.start_tense_music()
                        self.state = State.ACT11_MORNING
                        self.day11_transition = None

            # ДЕНЬ 11 - ОБНОВЛЕНИЯ
            elif self.state == State.ACT11_MORNING:
                if self.day11_morning:
                    self.day11_morning.update()
                    if self.day11_morning.can_transition():
                        self.create_day11_corridor_follow()
                        self.start_tense_music()
                        self.state = State.ACT11_CORRIDOR_FOLLOW
                        self.day11_morning = None

            elif self.state == State.ACT11_CORRIDOR_FOLLOW:
                if self.day11_corridor_follow:
                    self.day11_corridor_follow.update()
                    if self.day11_corridor_follow.can_transition():
                        self.create_day11_library_analysis()
                        self.start_day_music()
                        self.state = State.ACT11_LIBRARY_ANALYSIS
                        self.day11_corridor_follow = None

            elif self.state == State.ACT11_LIBRARY_ANALYSIS:
                if self.day11_library_analysis:
                    self.day11_library_analysis.update()
                    if self.day11_library_analysis.can_transition():
                        self.create_day11_sailas_room()
                        self.start_anxiety_music()
                        self.state = State.ACT11_SAILAS_ROOM
                        self.day11_library_analysis = None

            elif self.state == State.ACT11_SAILAS_ROOM:
                if self.day11_sailas_room:
                    self.day11_sailas_room.update()
                    if self.day11_sailas_room.can_transition():
                        self.create_day11_preparation()
                        self.start_aftermath_music()
                        self.state = State.ACT11_PREPARATION
                        self.day11_sailas_room = None

            elif self.state == State.ACT11_PREPARATION:
                if self.day11_preparation:
                    self.day11_preparation.update()
                    if self.day11_preparation.can_transition():
                        self.create_day12_transition()
                        self.stop_music()
                        self.state = State.ACT11_DAY12_TRANSITION
                        self.day11_preparation = None

            elif self.state == State.ACT11_DAY12_TRANSITION:
                if self.day12_transition:
                    self.day12_transition.update()
                    if self.day12_transition.can_transition():
                        self.create_act12_revelation()
                        self.start_tense_music()
                        self.state = State.ACT12_REVELATION
                        self.day12_transition = None

            # ФИНАЛ - ОБНОВЛЕНИЯ
            elif self.state == State.ACT12_REVELATION:
                if self.act12_revelation:
                    self.act12_revelation.update()
                    if self.act12_revelation.can_transition():
                        self.create_act12_silence_before_storm()
                        self.start_anxiety_music()
                        self.state = State.ACT12_SILENCE_BEFORE_STORM
                        self.act12_revelation = None

            elif self.state == State.ACT12_SILENCE_BEFORE_STORM:
                if self.act12_silence_before_storm:
                    self.act12_silence_before_storm.update()
                    if self.act12_silence_before_storm.can_transition():
                        self.create_act12_hart_office()
                        self.start_tuctuc_music()
                        self.state = State.ACT12_HART_OFFICE
                        self.act12_silence_before_storm = None

            elif self.state == State.ACT12_HART_OFFICE:
                if self.act12_hart_office:
                    self.act12_hart_office.update()
                    if self.act12_hart_office.can_transition():
                        self.create_act12_chase()
                        self.start_pogon_music()
                        self.state = State.ACT12_CHASE
                        self.act12_hart_office = None

            elif self.state == State.ACT12_CHASE:
                if self.act12_chase:
                    self.act12_chase.update()
                    if self.act12_chase.can_transition():
                        self.create_act12_lucia_confession()
                        self.start_priz_music()
                        self.state = State.ACT12_LUCIA_CONFESSION
                        self.act12_chase = None

            elif self.state == State.ACT12_LUCIA_CONFESSION:
                if self.act12_lucia_confession:
                    self.act12_lucia_confession.update()
                    if self.act12_lucia_confession.can_transition():
                        if self.lucia_choice:
                            self.create_act12_sailas_madness()
                            self.start_bezumie_music()
                            self.state = State.ACT12_SAILAS_MADNESS
                            self.act12_lucia_confession = None

            elif self.state == State.ACT12_SAILAS_MADNESS:
                if self.act12_sailas_madness:
                    self.act12_sailas_madness.update()
                    if self.act12_sailas_madness.can_transition():
                        self.create_act12_sailas_choice()
                        self.start_sailas_music()
                        self.state = State.ACT12_SAILAS_CHOICE
                        self.act12_sailas_madness = None

            elif self.state == State.ACT12_SAILAS_CHOICE:
                if self.act12_sailas_choice:
                    self.act12_sailas_choice.update()
                    if self.act12_sailas_choice.can_transition():
                        if self.sailas_choice:
                            self.create_act12_ending()
                            self.state = State.ACT12_ENDING
                            self.act12_sailas_choice = None

            elif self.state == State.ACT12_ENDING:
                if self.act12_ending:
                    self.act12_ending.update()
                    if self.act12_ending.is_complete():
                        self.create_act12_final_black()
                        self.start_final_music()
                        self.state = State.ACT12_FINAL_BLACK
                        self.act12_ending = None

            elif self.state == State.ACT12_FINAL_BLACK:
                if self.act12_final_black:
                    self.act12_final_black.update()

            elif self.state == State.MENU:
                self.menu.update(mouse_pos)

            elif self.state == State.PAUSE:
                self.pause.update(mouse_pos)

            # ОТРИСОВКА
            if self.state == State.BOOT:
                self.boot.draw(self.screen)
            elif self.state == State.LOGO:
                if self.logo:
                    self.logo.draw(self.screen)
            elif self.state == State.DISCLAIMER:
                self.disclaimer.draw(self.screen)
            elif self.state == State.PROLOGUE:
                if self.prologue:
                    self.prologue.draw()
            elif self.state == State.PROLOGUE_WAKE:
                if self.wake_up:
                    self.wake_up.draw()
                if white_flash_active and white_flash_alpha > 0:
                    flash_surface = pygame.Surface((WIDTH, HEIGHT))
                    flash_surface.fill(WHITE)
                    flash_surface.set_alpha(white_flash_alpha)
                    self.screen.blit(flash_surface, (0, 0))
            elif self.state == State.THOUGHTS:
                if self.thoughts:
                    self.thoughts.draw()
            elif self.state == State.ACT1_TRANSITION:
                if self.act1_transition:
                    self.act1_transition.draw()
            elif self.state == State.ACT1_MORNING:
                if self.morning_scene:
                    self.morning_scene.draw()
            elif self.state == State.ACT1_CORRIDOR:
                if self.corridor_scene:
                    self.corridor_scene.draw()
            elif self.state == State.ACT1_LESSON:
                if self.lesson_scene:
                    self.lesson_scene.draw()
            elif self.state == State.ACT1_CANTEEN:
                if self.canteen_scene:
                    self.canteen_scene.draw()
            elif self.state == State.ACT1_LUCIA:
                if self.lucia_scene:
                    self.lucia_scene.draw()
            elif self.state == State.ACT1_EVENING:
                if self.evening_scene:
                    self.evening_scene.draw()
            elif self.state == State.ACT1_NIGHT:
                if self.night_scene:
                    self.night_scene.draw()
            elif self.state == State.ACT1_EMPTY_CORRIDOR:
                if self.empty_corridor_scene:
                    self.empty_corridor_scene.draw()
            elif self.state == State.ACT1_INSOMNIA:
                if self.insomnia_scene:
                    self.insomnia_scene.draw()
            elif self.state == State.ACT1_DAY2_TRANSITION:
                if self.day2_transition:
                    self.day2_transition.draw()
            elif self.state == State.ACT2_MORNING:
                if self.day2_morning:
                    self.day2_morning.draw()
            elif self.state == State.ACT2_CORRIDOR:
                if self.day2_corridor:
                    self.day2_corridor.draw()
            elif self.state == State.ACT2_LECTURE:
                if self.lecture_scene:
                    self.lecture_scene.draw()
            elif self.state == State.ACT2_POST_LECTURE:
                if self.post_lecture_scene:
                    self.post_lecture_scene.draw()
            elif self.state == State.ACT2_CLOSED_WING:
                if self.closed_wing_scene:
                    self.closed_wing_scene.draw()
            elif self.state == State.ACT2_LIBRARY:
                if self.library_scene:
                    self.library_scene.draw()
            elif self.state == State.ACT2_NIGHT:
                if self.day2_night:
                    self.day2_night.draw()
            elif self.state == State.ACT2_DAY3_TRANSITION:
                if self.day3_transition:
                    self.day3_transition.draw()
            elif self.state == State.ACT3_MORNING:
                if self.day3_morning:
                    self.day3_morning.draw()
            elif self.state == State.ACT3_MATH_EXAM:
                if self.math_exam_scene:
                    self.math_exam_scene.draw()
            elif self.state == State.ACT3_CORRIDOR_SAILAS:
                if self.sailas_corridor_scene:
                    self.sailas_corridor_scene.draw()
            elif self.state == State.ACT3_LIBRARY_EVENING:
                if self.day3_library_scene:
                    self.day3_library_scene.draw()
            elif self.state == State.ACT3_AWAKENING:
                if self.awakening_scene:
                    self.awakening_scene.draw()
            elif self.state == State.ACT3_NIGHT:
                if self.day3_night:
                    self.day3_night.draw()
            elif self.state == State.ACT3_DAY4_TRANSITION:
                if self.day4_transition:
                    self.day4_transition.draw()
            elif self.state == State.ACT4_MORNING:
                if self.day4_morning:
                    self.day4_morning.draw()
            elif self.state == State.ACT4_MATH_TEST:
                if self.day4_math_test:
                    self.day4_math_test.draw()
            elif self.state == State.ACT4_CORRIDOR_WARNING:
                if self.day4_corridor_warning:
                    self.day4_corridor_warning.draw()
            elif self.state == State.ACT4_OLD_LIBRARY:
                if self.day4_old_library:
                    self.day4_old_library.draw()
            elif self.state == State.ACT4_SECRET_ROOM:
                if self.day4_secret_room:
                    self.day4_secret_room.draw()
            elif self.state == State.ACT4_DAY5_TRANSITION:
                if self.day5_transition:
                    self.day5_transition.draw()
            elif self.state == State.ACT5_MORNING:
                if self.day5_morning:
                    self.day5_morning.draw()
            elif self.state == State.ACT5_CORRIDOR_RULES:
                if self.day5_corridor_rules:
                    self.day5_corridor_rules.draw()
            elif self.state == State.ACT5_SECRET_MEETING:
                if self.day5_secret_meeting:
                    self.day5_secret_meeting.draw()
            elif self.state == State.ACT5_MEDICAL_INFILTRATION:
                if self.day5_medical_infiltration:
                    self.day5_medical_infiltration.draw()
            elif self.state == State.ACT5_ARCHIVE_FIND:
                if self.day5_archive_find:
                    self.day5_archive_find.draw()
            elif self.state == State.ACT5_VIDEO_PROCEDURE:
                if self.day5_video_procedure:
                    self.day5_video_procedure.draw()
            elif self.state == State.ACT5_MEETING_KREIN:
                if self.day5_meeting_krein:
                    self.day5_meeting_krein.draw()
            elif self.state == State.ACT5_DAY6_TRANSITION:
                if self.day6_transition:
                    self.day6_transition.draw()
            elif self.state == State.ACT6_MORNING:
                if self.day6_morning:
                    self.day6_morning.draw()
            elif self.state == State.ACT6_CORRIDOR:
                if self.day6_corridor:
                    self.day6_corridor.draw()
            elif self.state == State.ACT6_SECRET_ROOM_TRAITOR:
                if self.day6_secret_room_traitor:
                    self.day6_secret_room_traitor.draw()
            elif self.state == State.ACT6_ROOF_CONFRONTATION:
                if self.day6_roof_confrontation:
                    self.day6_roof_confrontation.draw()
            elif self.state == State.ACT6_CORRIDOR_RETURN:
                if self.day6_corridor_return:
                    self.day6_corridor_return.draw()
            elif self.state == State.ACT6_INSOMNIA:
                if self.day6_insomnia:
                    self.day6_insomnia.draw()
            elif self.state == State.ACT6_DAY7_TRANSITION:
                if self.day7_transition:
                    self.day7_transition.draw()
            elif self.state == State.ACT7_MORNING:
                if self.day7_morning:
                    self.day7_morning.draw()
            elif self.state == State.ACT7_CORRIDOR_MAX:
                if self.day7_corridor_max:
                    self.day7_corridor_max.draw()
            elif self.state == State.ACT7_SECRET_PLANNING:
                if self.day7_secret_planning:
                    self.day7_secret_planning.draw()
            elif self.state == State.ACT7_ABANDONED_TRAP:
                if self.day7_abandoned_trap:
                    self.day7_abandoned_trap.draw()
            elif self.state == State.ACT7_SECRET_RETURN:
                if self.day7_secret_return:
                    self.day7_secret_return.draw()
            elif self.state == State.ACT7_INSOMNIA:
                if self.day7_insomnia:
                    self.day7_insomnia.draw()
            elif self.state == State.ACT7_DAY8_TRANSITION:
                if self.day8_transition:
                    self.day8_transition.draw()
            elif self.state == State.ACT8_MORNING:
                if self.day8_morning:
                    self.day8_morning.draw()
            elif self.state == State.ACT8_CORRIDOR_OBSERVE:
                if self.day8_corridor_observe:
                    self.day8_corridor_observe.draw()
            elif self.state == State.ACT8_LIBRARY_ANALYSIS:
                if self.day8_library_analysis:
                    self.day8_library_analysis.draw()
            elif self.state == State.ACT8_DORMITORY_CLUES:
                if self.day8_dormitory_clues:
                    self.day8_dormitory_clues.draw()
            elif self.state == State.ACT8_PREPARATION:
                if self.day8_preparation:
                    self.day8_preparation.draw()
            elif self.state == State.ACT8_DAY9_TRANSITION:
                if self.day9_transition:
                    self.day9_transition.draw()
            elif self.state == State.ACT9_MORNING:
                if self.day9_morning:
                    self.day9_morning.draw()
            elif self.state == State.ACT9_GYM_CONFRONTATION:
                if self.day9_gym_confrontation:
                    self.day9_gym_confrontation.draw()
            elif self.state == State.ACT9_CONFESSION_CHOICE:
                if self.day9_confession_choice:
                    self.day9_confession_choice.draw()
            elif self.state == State.ACT9_SECRET_MESSAGE:
                if self.day9_secret_message:
                    self.day9_secret_message.draw()
            elif self.state == State.ACT9_INSOMNIA:
                if self.day9_insomnia:
                    self.day9_insomnia.draw()
            elif self.state == State.ACT9_DAY10_TRANSITION:
                if self.day10_transition:
                    self.day10_transition.draw()
            elif self.state == State.ACT10_MORNING:
                if self.day10_morning:
                    self.day10_morning.draw()
            elif self.state == State.ACT10_CORRIDOR_BRANCH:
                if self.day10_corridor_branch:
                    self.day10_corridor_branch.draw()
            elif self.state == State.ACT10_SECRET_PLANNING:
                if self.day10_secret_planning:
                    self.day10_secret_planning.draw()
            elif self.state == State.ACT10_MEDICAL_PATH:
                if self.day10_medical_path:
                    self.day10_medical_path.draw()
            elif self.state == State.ACT10_HART_LAB:
                if self.day10_hart_lab:
                    self.day10_hart_lab.draw()
            elif self.state == State.ACT10_INSOMNIA:
                if self.day10_insomnia:
                    self.day10_insomnia.draw()
            elif self.state == State.ACT10_DAY11_TRANSITION:
                if self.day11_transition:
                    self.day11_transition.draw()
            elif self.state == State.ACT11_MORNING:
                if self.day11_morning:
                    self.day11_morning.draw()
            elif self.state == State.ACT11_CORRIDOR_FOLLOW:
                if self.day11_corridor_follow:
                    self.day11_corridor_follow.draw()
            elif self.state == State.ACT11_LIBRARY_ANALYSIS:
                if self.day11_library_analysis:
                    self.day11_library_analysis.draw()
            elif self.state == State.ACT11_SAILAS_ROOM:
                if self.day11_sailas_room:
                    self.day11_sailas_room.draw()
            elif self.state == State.ACT11_PREPARATION:
                if self.day11_preparation:
                    self.day11_preparation.draw()
            elif self.state == State.ACT11_DAY12_TRANSITION:
                if self.day12_transition:
                    self.day12_transition.draw()
            elif self.state == State.ACT12_REVELATION:
                if self.act12_revelation:
                    self.act12_revelation.draw()
            elif self.state == State.ACT12_SILENCE_BEFORE_STORM:
                if self.act12_silence_before_storm:
                    self.act12_silence_before_storm.draw()
            elif self.state == State.ACT12_HART_OFFICE:
                if self.act12_hart_office:
                    self.act12_hart_office.draw()
            elif self.state == State.ACT12_CHASE:
                if self.act12_chase:
                    self.act12_chase.draw()
            elif self.state == State.ACT12_LUCIA_CONFESSION:
                if self.act12_lucia_confession:
                    self.act12_lucia_confession.draw()
            elif self.state == State.ACT12_SAILAS_MADNESS:
                if self.act12_sailas_madness:
                    self.act12_sailas_madness.draw()
            elif self.state == State.ACT12_SAILAS_CHOICE:
                if self.act12_sailas_choice:
                    self.act12_sailas_choice.draw()
            elif self.state == State.ACT12_ENDING:
                if self.act12_ending:
                    self.act12_ending.draw()
            elif self.state == State.ACT12_FINAL_BLACK:
                if self.act12_final_black:
                    self.act12_final_black.draw()
            elif self.state == State.MENU:
                self.menu.draw(self.screen)
            elif self.state == State.PAUSE:
                # Отрисовка текущей сцены под меню паузы
                if self.act12_final_black:
                    self.act12_final_black.draw()
                elif self.act12_ending:
                    self.act12_ending.draw()
                elif self.act12_sailas_choice:
                    self.act12_sailas_choice.draw()
                elif self.act12_sailas_madness:
                    self.act12_sailas_madness.draw()
                elif self.act12_lucia_confession:
                    self.act12_lucia_confession.draw()
                elif self.act12_chase:
                    self.act12_chase.draw()
                elif self.act12_hart_office:
                    self.act12_hart_office.draw()
                elif self.act12_silence_before_storm:
                    self.act12_silence_before_storm.draw()
                elif self.act12_revelation:
                    self.act12_revelation.draw()
                elif self.day12_transition:
                    self.day12_transition.draw()
                elif self.day11_preparation:
                    self.day11_preparation.draw()
                elif self.day11_sailas_room:
                    self.day11_sailas_room.draw()
                elif self.day11_library_analysis:
                    self.day11_library_analysis.draw()
                elif self.day11_corridor_follow:
                    self.day11_corridor_follow.draw()
                elif self.day11_morning:
                    self.day11_morning.draw()
                elif self.day11_transition:
                    self.day11_transition.draw()
                elif self.day10_insomnia:
                    self.day10_insomnia.draw()
                elif self.day10_hart_lab:
                    self.day10_hart_lab.draw()
                elif self.day10_medical_path:
                    self.day10_medical_path.draw()
                elif self.day10_secret_planning:
                    self.day10_secret_planning.draw()
                elif self.day10_corridor_branch:
                    self.day10_corridor_branch.draw()
                elif self.day10_morning:
                    self.day10_morning.draw()
                elif self.day10_transition:
                    self.day10_transition.draw()
                elif self.day9_insomnia:
                    self.day9_insomnia.draw()
                elif self.day9_secret_message:
                    self.day9_secret_message.draw()
                elif self.day9_confession_choice:
                    self.day9_confession_choice.draw()
                elif self.day9_gym_confrontation:
                    self.day9_gym_confrontation.draw()
                elif self.day9_morning:
                    self.day9_morning.draw()
                elif self.day9_transition:
                    self.day9_transition.draw()
                elif self.day8_preparation:
                    self.day8_preparation.draw()
                elif self.day8_dormitory_clues:
                    self.day8_dormitory_clues.draw()
                elif self.day8_library_analysis:
                    self.day8_library_analysis.draw()
                elif self.day8_corridor_observe:
                    self.day8_corridor_observe.draw()
                elif self.day8_morning:
                    self.day8_morning.draw()
                elif self.day8_transition:
                    self.day8_transition.draw()
                elif self.day7_insomnia:
                    self.day7_insomnia.draw()
                elif self.day7_secret_return:
                    self.day7_secret_return.draw()
                elif self.day7_abandoned_trap:
                    self.day7_abandoned_trap.draw()
                elif self.day7_secret_planning:
                    self.day7_secret_planning.draw()
                elif self.day7_corridor_max:
                    self.day7_corridor_max.draw()
                elif self.day7_morning:
                    self.day7_morning.draw()
                elif self.day7_transition:
                    self.day7_transition.draw()
                elif self.day6_insomnia:
                    self.day6_insomnia.draw()
                elif self.day6_corridor_return:
                    self.day6_corridor_return.draw()
                elif self.day6_roof_confrontation:
                    self.day6_roof_confrontation.draw()
                elif self.day6_secret_room_traitor:
                    self.day6_secret_room_traitor.draw()
                elif self.day6_corridor:
                    self.day6_corridor.draw()
                elif self.day6_morning:
                    self.day6_morning.draw()
                elif self.day6_transition:
                    self.day6_transition.draw()
                elif self.day5_meeting_krein:
                    self.day5_meeting_krein.draw()
                elif self.day5_video_procedure:
                    self.day5_video_procedure.draw()
                elif self.day5_archive_find:
                    self.day5_archive_find.draw()
                elif self.day5_medical_infiltration:
                    self.day5_medical_infiltration.draw()
                elif self.day5_secret_meeting:
                    self.day5_secret_meeting.draw()
                elif self.day5_corridor_rules:
                    self.day5_corridor_rules.draw()
                elif self.day5_morning:
                    self.day5_morning.draw()
                elif self.day5_transition:
                    self.day5_transition.draw()
                elif self.day4_secret_room:
                    self.day4_secret_room.draw()
                elif self.day4_old_library:
                    self.day4_old_library.draw()
                elif self.day4_corridor_warning:
                    self.day4_corridor_warning.draw()
                elif self.day4_math_test:
                    self.day4_math_test.draw()
                elif self.day4_morning:
                    self.day4_morning.draw()
                elif self.day4_transition:
                    self.day4_transition.draw()
                elif self.day3_night:
                    self.day3_night.draw()
                elif self.awakening_scene:
                    self.awakening_scene.draw()
                elif self.day3_library_scene:
                    self.day3_library_scene.draw()
                elif self.sailas_corridor_scene:
                    self.sailas_corridor_scene.draw()
                elif self.math_exam_scene:
                    self.math_exam_scene.draw()
                elif self.day3_morning:
                    self.day3_morning.draw()
                elif self.day3_transition:
                    self.day3_transition.draw()
                elif self.day2_night:
                    self.day2_night.draw()
                elif self.library_scene:
                    self.library_scene.draw()
                elif self.closed_wing_scene:
                    self.closed_wing_scene.draw()
                elif self.post_lecture_scene:
                    self.post_lecture_scene.draw()
                elif self.lecture_scene:
                    self.lecture_scene.draw()
                elif self.day2_corridor:
                    self.day2_corridor.draw()
                elif self.day2_morning:
                    self.day2_morning.draw()
                elif self.day2_transition:
                    self.day2_transition.draw()
                elif self.insomnia_scene:
                    self.insomnia_scene.draw()
                elif self.empty_corridor_scene:
                    self.empty_corridor_scene.draw()
                elif self.night_scene:
                    self.night_scene.draw()
                elif self.evening_scene:
                    self.evening_scene.draw()
                elif self.lucia_scene:
                    self.lucia_scene.draw()
                elif self.canteen_scene:
                    self.canteen_scene.draw()
                elif self.lesson_scene:
                    self.lesson_scene.draw()
                elif self.corridor_scene:
                    self.corridor_scene.draw()
                elif self.morning_scene:
                    self.morning_scene.draw()
                elif self.act1_transition:
                    self.act1_transition.draw()
                elif self.thoughts:
                    self.thoughts.draw()
                elif self.wake_up:
                    self.wake_up.draw()
                elif self.prologue:
                    self.prologue.draw()

                self.pause.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
