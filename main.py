import flet as ft

class CalculatorApp(ft.UserControl):
    def build(self):
        self.reset()
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=30)

        return ft.Container(
            width=400,
            height=350,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=30,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[self.result],
                        spacing=10,
                        alignment="end",
                    ),
                    ft.Row(
                        controls=[
                            self.create_button("AC", ft.colors.PINK_100, "AC"),
                            self.create_button("+/-", ft.colors.PINK_100, "+/-"),
                            self.create_button("%", ft.colors.PINK_100, "%"),
                            self.create_button("/", ft.colors.PINK_100, "/"),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            self.create_button("7", ft.colors.PINK_600, "7"),
                            self.create_button("8", ft.colors.PINK_600, "8"),
                            self.create_button("9", ft.colors.PINK_600, "9"),
                            self.create_button("*", ft.colors.YELLOW_200, "*"),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            self.create_button("4", ft.colors.PINK_600, "4"),
                            self.create_button("5", ft.colors.PINK_600, "5"),
                            self.create_button("6", ft.colors.PINK_600, "6"),
                            self.create_button("-", ft.colors.YELLOW_200, "-"),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            self.create_button("1", ft.colors.PINK_600, "1"),
                            self.create_button("2", ft.colors.PINK_600, "2"),
                            self.create_button("3", ft.colors.PINK_600, "3"),
                            self.create_button("+", ft.colors.YELLOW_200, "+"),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            self.create_button("0", ft.colors.PINK_600, "0"),
                            self.create_button(".", ft.colors.BLUE_100, "."),
                            self.create_button("=", ft.colors.BLUE_100, "="),
                        ],
                        spacing=10,
                    ),
                ],
            ),
        )


    def create_button(self, text, bgcolor, data):
        return ft.ElevatedButton(
            text=text,
            bgcolor=bgcolor,
            color=ft.colors.WHITE,
            expand=1,
            on_click=self.button_clicked,
            data=data,
        )

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def calculate(self, operand1, operand2, operator):
        try:
            if operator == "+":
                return str(operand1 + operand2)
            elif operator == "-":
                return str(operand1 - operand2)
            elif operator == "*":
                return str(operand1 * operand2)
            elif operator == "/":
                if operand2 == 0:
                    return "Error"
                return str(operand1 / operand2)
        except Exception:
            return "Error"

def main(page: ft.Page):
    page.title = "Calculator App"
    calculator_app = CalculatorApp()
    page.add(calculator_app)

ft.app(target=main)
