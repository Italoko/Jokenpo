import hands_detector as detector

def is_pedra(hand_detected, side, max_x):
    if hand_detected:
        if side == "Left":  
            dist_index_finger_tip_to_border = detector.get_landmark(hand_detected,8)[0] - 0
            dist_index_finger_pip_to_border = detector.get_landmark(hand_detected,6)[0] - 0

            dist_middle_finger_tip_to_border = detector.get_landmark(hand_detected,12)[0] - 0
            dist_middle_finger_pip_to_border = detector.get_landmark(hand_detected,10)[0] - 0  
        else:
            dist_index_finger_tip_to_border = max_x - detector.get_landmark(hand_detected,8)[0] 
            dist_index_finger_pip_to_border = max_x - detector.get_landmark(hand_detected,6)[0]

            dist_middle_finger_tip_to_border = max_x - detector.get_landmark(hand_detected,12)[0] 
            dist_middle_finger_pip_to_border = max_x - detector.get_landmark(hand_detected,10)[0]

        if dist_index_finger_tip_to_border < dist_index_finger_pip_to_border and dist_middle_finger_tip_to_border < dist_middle_finger_pip_to_border:
            return True
        else:
            return False
    return None

def is_papel(hand_detected, side, max_x):
    if hand_detected:
        if side == "Left":
            dist_index_finger_tip_to_border = detector.get_landmark(hand_detected,8)[0] - 0
            dist_index_finger_pip_to_border = detector.get_landmark(hand_detected,6)[0] - 0

            dist_middle_finger_tip_to_border = detector.get_landmark(hand_detected,12)[0] - 0
            dist_middle_finger_pip_to_border = detector.get_landmark(hand_detected,10)[0] - 0  
        else:
            dist_index_finger_tip_to_border = max_x - detector.get_landmark(hand_detected,8)[0]
            dist_index_finger_pip_to_border = max_x - detector.get_landmark(hand_detected,6)[0]

            dist_middle_finger_tip_to_border = max_x - detector.get_landmark(hand_detected,12)[0] 
            dist_middle_finger_pip_to_border = max_x - detector.get_landmark(hand_detected,10)[0]

        if dist_index_finger_tip_to_border > dist_index_finger_pip_to_border and dist_middle_finger_tip_to_border > dist_middle_finger_pip_to_border:
            return True
        else:
            return False
    return None

def is_tesoura(hand_detected, side, max_x):
    if hand_detected:
        if side == "Left":
            dist_pinky_tip_to_border = detector.get_landmark(hand_detected,20)[0] - 0
            dist_pinky_pip_to_border = detector.get_landmark(hand_detected,18)[0] - 0
            
            dist_ring_finger_tip_to_border = detector.get_landmark(hand_detected,16)[0] - 0
            dist_ring_finger_pip_to_border = detector.get_landmark(hand_detected,14)[0] - 0 
        else:
            dist_pinky_tip_to_border = max_x - detector.get_landmark(hand_detected,20)[0]
            dist_pinky_pip_to_border = max_x - detector.get_landmark(hand_detected,18)[0]

            dist_ring_finger_tip_to_border = max_x - detector.get_landmark(hand_detected,16)[0]
            dist_ring_finger_pip_to_border = max_x - detector.get_landmark(hand_detected,14)[0] 

        if detector.linked_finger(hand_detected,4,14):
            if dist_pinky_tip_to_border < dist_pinky_pip_to_border and dist_ring_finger_tip_to_border < dist_ring_finger_pip_to_border:
                return True
            return False
        else:
            return False
    return None

def get_movimento(hand_detected,side,max_x):
    if is_pedra(hand_detected,side,max_x):
        return (0,"Pedra")
    elif is_tesoura(hand_detected,side,max_x):
        return (2,"Tesoura")
    elif is_papel(hand_detected,side,max_x):
        return (1,"Papel")
    else:
        return (-1,"Desconhecido")