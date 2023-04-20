# Демкин Алексей 368096
import cv2
import time

cap = cv2.VideoCapture(0)  # захват картинки с видеокамеры
down_points = (640, 480)  # изменяем размер изображения до 640х480 пикселей
R, L, i = 0, 0, 0  # заводим переменные для счётчиков
img = cv2.imread('fly64.png')
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)  # подгоняем размер кадра
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # преобразуем кадр в серый цветовой формат
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # используем сглаживание, для минимизации шумов
    ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        new_img = cv2.resize(img, (w, h))  # масштабируем изображение под найденный контур
        frame[y:y + h, x:x + w] = new_img  # добавляем изображение на видео
        cv2.putText(frame, f"Count left: {L}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0),
                    1)  # вывод левого счётчика
        cv2.putText(frame, f"Count right: {R}", (down_points[0] - 180, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0),
                    1)  # вывод правого счётчика
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 200, 0),
                      2)  # выделяем найденный контур голубым прямоугольником
        if i % 10 == 0:  # определяем в какой половине находится контур
            a = x + (w // 2)
            if a > down_points[0] // 2:
                R += 1
            elif a < down_points[0] // 2:
                L += 1
    cv2.imshow('frame', frame)  # вывод изображения со всеми наложениями
    if cv2.waitKey(1) & 0xFF == ord('q'):  # закрывает программу, клавишей "q"
        break

    time.sleep(0.1)
    i += 1

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
