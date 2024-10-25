import pyautogui
import time
from pynput import mouse
import streamlit as st

# ตัวแปรสำหรับเก็บค่าพิกัดตำแหน่ง
target_x = st.number_input("Enter X coordinate:", value=3789)  # ค่าเริ่มต้น X
target_y = st.number_input("Enter Y coordinate:", value=911)   # ค่าเริ่มต้น Y

# ตัวแปรสำหรับเก็บจำนวนครั้งที่ต้องการคลิก
click_count = st.number_input("Enter number of clicks:", min_value=1, value=100)  # อย่างน้อย 1 ครั้ง

# Slider สำหรับเลือกระยะเวลาหน่วง (0.05 ถึง 1 วินาที)
click_delay = st.slider("Select click interval (seconds):", 0.05, 1.0, 0.5)  # ค่าเริ่มต้น 0.5 วินาที

# Flag สำหรับตรวจจับการขยับเมาส์
mouse_moved = False

# ฟังก์ชันสำหรับดักฟังเหตุการณ์การเคลื่อนไหวของเมาส์
def on_move(x, y):
    global mouse_moved
    mouse_moved = True  # ตั้งค่าเป็น True เมื่อมีการขยับ

# เริ่มต้น Listener สำหรับตรวจจับการขยับเมาส์
listener = mouse.Listener(on_move=on_move)
listener.start()

if st.button("Start Clicking"):  # เมื่อกดปุ่มนี้
    st.write(f"เริ่มการคลิก {click_count} ครั้ง...")  # แสดงจำนวนครั้งที่คลิก
    pyautogui.FAILSAFE = True  # เปิดฟังก์ชันหยุดฉุกเฉิน

    # วนลูปเพื่อคลิกตามจำนวนครั้งที่ระบุ หรือหยุดหากเมาส์ขยับ
    for i in range(click_count):
        if mouse_moved:  # ตรวจสอบ Flag
            st.write("หยุดคลิก: ตรวจพบการขยับเมาส์!")
            break
        pyautogui.click(target_x, target_y)  # คลิกที่ตำแหน่งที่กำหนด
        time.sleep(click_delay)  # รอระยะเวลาที่ผู้ใช้กำหนด

    st.write("การคลิกเสร็จสิ้น!")

listener.stop()  # หยุด Listener