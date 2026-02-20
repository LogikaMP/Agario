from random import randint, choice
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkCanvas, CTkImage
from PIL import Image


class Cicrle:
    def __init__(self, canvas):
        self.x0 = randint(0, 500)
        self.y0 = randint(0, 500)
        self.radius = randint(20, 60)
        self.x1 = self.x0 + self.radius * 2
        self.y1 = self.y0 + self.radius * 2
        self.dx = choice([-5, -4, -3, 3, 4, 5])
        self.dy = choice([-5, -4, -3, 3, 4, 5])
        self.color = "#{:06x}".format(randint(0x1E3A8A, 0x38BDF8))
        self.id = canvas.create_oval(
            self.x0, self.y0, self.x1, self.y1,
            fill=self.color,
            outline=""
        )
        self.canvas = canvas

    def move(self):
        if self.x0 <= 0 or self.x1 >= 700:
            self.dx *= -1
        if self.y0 <= 0 or self.y1 >= 700:
            self.dy *= -1

        self.x0 += self.dx
        self.y0 += self.dy
        self.x1 += self.dx
        self.y1 += self.dy
        self.canvas.move(self.id, self.dx, self.dy)


class Launcher(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Agario")
        self.configure(fg_color="#0F172A")  # темно-синій фон

        self.fon = CTkCanvas(
            self,
            width=500,
            height=750,
            bg="#0B1120",   # глибокий синій
            highlightthickness=0
        )
        self.fon.pack(fill="both")

        self.circles = [Cicrle(self.fon) for i in range(30)]
        self.update_circles()

    def update_circles(self):
        for circles in self.circles:
            circles.move()
        self.after(16, self.update_circles)

    def window_start(self):

        img1 = CTkLabel(
            self.fon,
            text="",
            image=CTkImage(Image.open("flash.png"), size=(35, 35))
        )
        img2 = CTkLabel(
            self.fon,
            text="",
            image=CTkImage(Image.open("flash.png"), size=(35, 35))
        )

        img1.place(x=140, y=80)
        img2.place(x=325, y=80)

        lbl = CTkLabel(
            self.fon,
            text="AGARIO",
            font=("Montserrat", 28, "bold"),
            text_color="#38BDF8"
        )
        lbl.place(x=190, y=80)

        self.nick_entry = CTkEntry(
            self.fon,
            width=260,
            height=45,
            corner_radius=15,
            placeholder_text="Введіть нікнейм",
            fg_color="#1E293B",
            border_color="#38BDF8",
            border_width=2,
            text_color="#E2E8F0"
        )
        self.nick_entry.place(x=120, y=170)

        self.ip_entry = CTkEntry(
            self.fon,
            width=260,
            height=45,
            corner_radius=15,
            placeholder_text="Введіть IP адресу",
            fg_color="#1E293B",
            border_color="#38BDF8",
            border_width=2,
            text_color="#E2E8F0"
        )
        self.ip_entry.place(x=120, y=230)

        self.port_entry = CTkEntry(
            self.fon,
            width=260,
            height=45,
            corner_radius=15,
            placeholder_text="Введіть порт",
            fg_color="#1E293B",
            border_color="#38BDF8",
            border_width=2,
            text_color="#E2E8F0"
        )
        self.port_entry.place(x=120, y=290)

        start_btn = CTkButton(
            self.fon,
            text="Почати гру",
            width=260,
            height=45,
            corner_radius=15,
            fg_color="#0EA5E9",
            hover_color="#38BDF8",
            text_color="#FFFFFF",
            font=("Montserrat", 16, "bold"),
            command=self.start_game
        )
        start_btn.place(x=120, y=360)

        self.mainloop()

    def window_end(self):

        lbl = CTkLabel(
            self.fon,
            text="AGARIO",
            font=("Montserrat", 26, "bold"),
            text_color="#38BDF8"
        )
        lbl.place(x=190, y=80)

        lbl2 = CTkLabel(
            self.fon,
            text="Game Over",
            font=("Montserrat", 22, "bold"),
            text_color="#E2E8F0"
        )
        lbl2.place(x=180, y=140)

        lbl3 = CTkLabel(
            self.fon,
            text="Restart game?",
            font=("Montserrat", 18),
            text_color="#94A3B8"
        )
        lbl3.place(x=170, y=190)

        yes_btn = CTkButton(
            self.fon,
            text="Yes",
            width=120,
            height=40,
            corner_radius=12,
            fg_color="#0EA5E9",
            hover_color="#38BDF8",
            font=("Montserrat", 14, "bold"),
            command=self.restart_game
        )
        yes_btn.place(x=135, y=260)

        no_btn = CTkButton(
            self.fon,
            text="No",
            width=120,
            height=40,
            corner_radius=12,
            fg_color="#334155",
            hover_color="#475569",
            font=("Montserrat", 14),
            command=self.game_over
        )
        no_btn.place(x=245, y=260)

        self.mainloop()

    def restart_game(self):
        self.destroy()
        self.restart = True

    def game_over(self):
        self.destroy()
        self.end = True

    def start_game(self):
        self.nick = self.nick_entry.get()
        self.ip = self.ip_entry.get()
        self.port = self.port_entry.get()

        if self.nick and self.ip and self.port:
            self.destroy()
        else:
            error_lbl = CTkLabel(
                self.fon,
                text="Заповніть всі поля",
                font=("Montserrat", 14),
                text_color="#FF6B6B"
            )
            error_lbl.place(x=170, y=330)