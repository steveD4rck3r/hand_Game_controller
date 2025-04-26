import cv2
import mediapipe as mp
import pygame
import os
from settings import *

class HandController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5)
        
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        
        # Charger les images de la main
        self.hand_img = self._load_image("hand.png", HAND_SCALE)
        self.pointing_img = self._load_image("pic.png", HAND_SCALE)
        
        self.hand_position = None
        self.is_pointing = False
    
    def _load_image(self, filename, scale):
        path = os.path.join(ASSETS_DIR, filename)
        try:
            img = pygame.image.load(path).convert_alpha()
            width = int(img.get_width() * scale)
            height = int(img.get_height() * scale)
            return pygame.transform.scale(img, (width, height))
        except:
            # Fallback si l'image ne charge pas
            surf = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 0, 0) if filename == "pic.png" else (0, 0, 255), (25, 25), 25)
            return surf
    
    def update(self):
        success, img = self.cap.read()
        if not success:
            return
        
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        
        self.hand_position = None
        self.is_pointing = False
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                landmark = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
                self.hand_position = (landmark.x, landmark.y)
                self._detect_pointing_gesture(hand_landmarks)
        
        cv2.imshow("Camera", img)
        cv2.waitKey(1)
    
    def _detect_pointing_gesture(self, landmarks):
        tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]
        
        mcp = [
            self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
            self.mp_hands.HandLandmark.RING_FINGER_MCP,
            self.mp_hands.HandLandmark.PINKY_MCP
        ]
        
        index_tip = landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_mcp = landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP]
        
        is_index_extended = index_tip.y < index_mcp.y
        
        other_fingers_folded = True
        for tip, joint in zip(tips[1:], mcp[1:]):
            tip_pos = landmarks.landmark[tip]
            joint_pos = landmarks.landmark[joint]
            if tip_pos.y < joint_pos.y:
                other_fingers_folded = False
                break
        
        self.is_pointing = is_index_extended and other_fingers_folded
    
    def get_screen_position(self):
        if self.hand_position:
            x, y = self.hand_position
            screen_x = int(x * SCREEN_WIDTH)
            screen_y = int(y * SCREEN_HEIGHT)
            return (screen_x, screen_y)
        return None
    
    def get_hand_image(self):
        return self.pointing_img if self.is_pointing else self.hand_img
    
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()