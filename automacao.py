import pyautogui as pa
import time

def aut(vezes): 
    for i in range(vezes):
        pa.click(x=563, y=736);
        pa.click();
        pa.moveTo(x=646, y=628);
        pa.scroll(-490);
        time.sleep(2);
        pa.scroll(-100);
        pa.click(x=417, y=623);
        pa.click(x=942, y=789);
        time.sleep(6)
        pa.scroll(-200);
        pa.click(x=1583, y=799);
        pa.click(x=803, y=391);
        pa.click(x=1480, y=823);
        pa.click(x=1449, y=819);
        pa.click(x=1516, y=819);
        time.sleep(2);
        pa.click(x=452, y=303);
        time.sleep(3)
        pa.write('239');
        pa.click(x=527, y=303);
        time.sleep(2)
        pa.click(x=937, y=887);
        time.sleep(2)
        pa.moveTo(x=1644, y=664);
        pa.scroll(-600);
        pa.click(x=872, y=979);
        time.sleep(2)
        pa.click(x=1128, y=602);
        time.sleep(6)

        print(f'Execução número {i+1}');