import pyautogui
import time
import subprocess
pdf_name= input("Enter your own pdf file name (without extension): ")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file_path = r"file:///D:/startup/automation_pdf/test.html"
subprocess.Popen([chrome_path, html_file_path])
time.sleep(5)
pyautogui.hotkey('ctrl', 'p')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
save_location = f"D:\\startup\\automation_pdf\\pdf_storage\\{pdf_name}.pdf"
pyautogui.write(save_location)
pyautogui.press('enter')
time.sleep(2)
print(f"PDF saved successfully as {save_location}!")