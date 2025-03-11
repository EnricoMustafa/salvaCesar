import pyautogui as pa
import time

def aut(vezes): 
    for i in range(vezes):
        pa.click(x=535, y=740);
        pa.click();
        pa.moveTo(x=646, y=628);
        pa.scroll(-450);
        pa.click(x=428, y=669);
        pa.click(x=940, y=792);
        time.sleep(6)
        pa.scroll(-200);
        pa.click(x=1596, y=855);
        pa.click(x=800, y=432);
        pa.click(x=1531, y=875);
        pa.click(x=469, y=306);
        time.sleep(3)
        pa.write('239');
        pa.click(x=526, y=300);
        time.sleep(2)
        pa.click(x=953, y=887);
        time.sleep(2)
        pa.moveTo(x=1644, y=664);
        pa.scroll(-600);
        pa.click(x=882, y=983);
        time.sleep(2)
        pa.click(x=1172, y=605);
        time.sleep(6)

        print(f'Execução número {i+1}');
