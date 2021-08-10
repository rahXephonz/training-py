import tkinter as contoh

main_window = contoh.Tk()

def event_tekan():
    label2 = contoh.Label(main_window,text="I was Pushed")
    label2.pack()
def event_tekans():
    label3 = contoh.Label(main_window,text="I was pushed v2")
    label3.pack()


label = contoh.Label(main_window, text="Hello, this is python!")
tombol1 = contoh.Button(main_window, text="Push Me!",command = event_tekan)
tombol2 = contoh.Button(main_window, text="Another Push!",command = event_tekans)

tombol1.pack()
tombol2.pack()
label.pack()
main_window.mainloop()



