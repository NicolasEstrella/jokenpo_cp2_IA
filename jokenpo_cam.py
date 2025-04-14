import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)

def dedos_levantados(landmarks) -> list:
    dedos = []

    if landmarks[4].x < landmarks[3].x:
        dedos.append(1)
    else:
        dedos.append(0)

    for tip_id in [8, 12, 16, 20]:
        if landmarks[tip_id].y < landmarks[tip_id - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return dedos

def reconhecer_gesto(dedos) -> str:
    indicadores = dedos[1:]

    if indicadores == [0, 0, 0, 0]:
        return "Pedra"
    elif indicadores == [1, 1, 1, 1]:
        return "Papel"
    elif indicadores == [1, 1, 0, 0]:
        return "Tesoura"
    else:
        return "GESTO NAO RECONHECIDO"

def decidir_vencedor(gesto1, gesto2) -> str:
    if gesto1 == gesto2:
        return "EMPATE!"
    elif (gesto1 == "Pedra" and gesto2 == "Tesoura") or \
         (gesto1 == "Tesoura" and gesto2 == "Papel") or \
         (gesto1 == "Papel" and gesto2 == "Pedra"):
        return "MAO 1 VENCE!"
    else:
        return "MAO 2 VENCE!"

def main() -> None:

    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        gestos_detectados = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                dedos = dedos_levantados(hand_landmarks.landmark)
                gesto = reconhecer_gesto(dedos)

                h, w, _ = frame.shape
                cx = int(hand_landmarks.landmark[0].x * w)
                cy = int(hand_landmarks.landmark[0].y * h)

                # Salva gesto e posição da mão
                gestos_detectados.append((gesto, (cx, cy)))

        if len(gestos_detectados) == 1:
            gesto, (cx, cy) = gestos_detectados[0]
            cv2.putText(frame, f"MAO 1", (cx - 60, cy + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.putText(frame, gesto, (cx - 60, cy + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        elif len(gestos_detectados) == 2:
            gestos_ordenados = sorted(gestos_detectados, key=lambda x: x[1][0])

            for i, (gesto, (cx, cy)) in enumerate(gestos_ordenados):
                cv2.putText(frame, f"MAO {i+1}", (cx - 60, cy + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                cv2.putText(frame, gesto, (cx - 60, cy + 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            vencedor = decidir_vencedor(gestos_ordenados[0][0], gestos_ordenados[1][0])
            cv2.putText(frame, vencedor, (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        cv2.imshow("Jokenpo", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
