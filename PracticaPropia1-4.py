import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("MENÚ")
        self.master.configure(bg="Light cyan")

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Inicio de Sesion", command=self.open_file11)  # 1ra practica inicio de sesion
        self.file_menu.add_command(label="Registros",
                                   command=self.open_file)  # 2a, 3ra y 4ta practica registro base de datos
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, text="¿Quiéres que te salude?", bg="Light cyan")
        self.label.pack(pady=20)
        self.label.config(fg="black", bg="Light cyan", font=("Consolas", 22))
        self.button1 = tk.Button(self, text="SI", bg="Light cyan", command=self.open_file1)
        self.button1.config(fg="black", bg="Light cyan", font=("Comic Sans", 12))
        self.button1.pack()
        self.button2 = tk.Button(self, text="NO", bg="Light cyan", command=self.open_file2)
        self.button2.pack(pady=30)
        self.button2.config(fg="black", bg="Light cyan", font=("Comic Sans", 12))
        self.button2.pack()

        self.pack()

    def open_file11(self):  # 1ra practica

        def iniciar_sesion():
            usuario = nombre_usuario.get()
            contrasena = contrasena_usuario.get()
            sesion = usuario
            if sesion == usuario and contrasena == "admin":
                resultado.config(text="Inicio de sesión exitoso")
            elif contrasena != "admin":
                resultado.config(text="Nombre de usuario o contraseña incorrectos")

        def open_ventana2():
            ventana2 = tk.Tk()
            ventana2.title("Restablecimineto de contraseña")
            ventana2.geometry("400x300")
            ventana2.resizable(width=False, height=False)
            ventana2.config(bg="Light cyan")
            # titulo
            titul = tk.Label(ventana2, text=" Ingrese una contraseña nueva ").pack()
            # crear campos de entrada cambio de contraseña
            olvida_contraseña = tk.Entry(ventana2, show="*")
            olvida_contraseña.pack(pady=30)
            confirmacion_contraseña = tk.Entry(ventana2, show="*")
            confirmacion_contraseña.pack(pady=50)

            def contraseña_nueva():
                cambio = olvida_contraseña.get()
                nueva = cambio
                if nueva == "admin":
                    resultado.config(text="Ingrese una contraseña diferente")
                elif nueva == cambio:
                    resultado.config(text="Restablecimiento exitoso")

            # boton aceptar
            contraseña_nueva = tk.Button(ventana2, text="Restablecer", command=contraseña_nueva)
            contraseña_nueva.pack(padx=10, pady=10)

            resultado = tk.Label(ventana2, text="")
            resultado.pack(pady=10)

        import tkinter as tk

        # creacion de la ventana inicio sesion
        ventana = tk.Tk()
        ventana.title("Inicio de sesión")
        ventana.geometry("300x300")
        ventana.resizable(width=False,
                          height=False)  # puedes usar ese comando o "0,0" para que el tamaño no sea alterado
        ventana.config(bg="Light cyan")
        # TITULO
        titulo = tk.Label(ventana, text=" BIENVENIDO USUARIO ").pack()
        # Crear campos de entrada para el nombre de usuario y la contraseña
        nombre_usuario = tk.Entry(ventana)
        nombre_usuario.pack(pady=10)
        contrasena_usuario = tk.Entry(ventana, show="*")
        contrasena_usuario.pack()
        # Crear botones para iniciar sesión y salir
        iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
        iniciar_sesion.pack(padx=10, pady=10)
        salir = tk.Button(ventana, text="Salir", command=ventana.quit)
        salir.pack()
        olvida_contraseña = tk.Button(ventana, text="Olvide mi contraseña",
                                      command=open_ventana2)  # no quiero que cierre simo que salga un mensaje de restablecimiento
        olvida_contraseña.pack(padx=10, pady=10)
        # Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
        resultado = tk.Label(ventana, text="")
        resultado.pack(pady=10)
        ventana.mainloop()

    def open_file(self):  # 2a y 3ra practica registro base de datos

        import tkinter as tk
        from tkinter import messagebox
        import sqlite3

        def conectar_db():
            conexion = sqlite3.connect("escuela.db")
            conexion.execute("""
                        create table if not exists alumnos(
                        id integer primary key AUTOINCREMENT,
                        nombre varchar,
                        edad integer)
            """)
            conexion.close()

        def guardar_alumno():
            conexion = sqlite3.connect("escuela.db")
            if name.get() == "" or age.get() == "":
                messagebox.showerror("Error en los datos", "Debe completar los datos del alumno")
                return
            int_age = int(age.get())
            print(int_age)
            print(name.get())
            conexion.execute("insert into alumnos(nombre, edad) values (?,?)", (name.get(), int_age))
            conexion.commit()
            conexion.close()
            ventana_nuevo.destroy()
            actualiza_listado()

        def get_alumnos():
            conexion = sqlite3.connect("escuela.db")
            cursor = conexion.cursor()
            registros_raw = cursor.execute("select * from alumnos")
            registros_fetch = registros_raw.fetchall()
            print(registros_fetch)
            global registros
            registros = registros_fetch
            cursor.close()

        def actualiza_listado():
            registros_lb.delete(0, tk.END)
            get_alumnos()
            for registro in registros:
                registros_lb.insert(tk.END, registro)

        def nuevo_alumno(event=None):
            ventana_nuevo_alumno = tk.Toplevel(ventana)
            ventana_nuevo_alumno.title("Agregar Alumno")
            # Crear la etiqueta y el campo de entrada para el nombre
            name_label = tk.Label(ventana_nuevo_alumno, text="Nombre:")
            name_label.grid(row=0, column=0, padx=(10, 0))

            name_entry = tk.Entry(ventana_nuevo_alumno)
            name_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

            # Crear la etiqueta y el campo de entrada para la edad
            age_label = tk.Label(ventana_nuevo_alumno, text="Edad:", )
            age_label.grid(row=1, column=0, padx=(10, 0))

            age_entry = tk.Entry(ventana_nuevo_alumno)
            age_entry.grid(row=1, column=1, padx=(0, 10))

            global name
            name = name_entry
            global age
            age = age_entry
            global ventana_nuevo
            ventana_nuevo = ventana_nuevo_alumno

            # Crear el botón para enviar los datos
            submit_button = tk.Button(ventana_nuevo_alumno, text="Guardar", command=guardar_alumno)
            submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        conectar_db()
        get_alumnos()
        ventana = tk.Tk()
        ventana.title("Control de Alumnos")
        ventana.config(width=300, height=300)
        barra_menus = tk.Menu()
        # Crear el primer menú.
        menu_alumnos = tk.Menu(barra_menus, tearoff=False)
        # Agregarlo a la barra.
        barra_menus.add_cascade(menu=menu_alumnos, label="Alumnos")
        menu_alumnos.add_command(label="presione ctrl+n", accelerator="Ctrl+N", command=nuevo_alumno)
        ventana.config(menu=barra_menus, bg="Light cyan")
        mi_label5 = tk.Label(ventana,
                            text="""PRESIONA CTRL+N         
            PARA AGREGAR ALUMNOS""", bg="Light cyan")
        mi_label5.pack()                    #tuve que agregar un label ya que la barra no salia el boton pero el comando si
        registros_lb = tk.Listbox(ventana)     #solo le indico al usuario que presionar
        for registro in registros:
            registros_lb.insert(tk.END, registro)

        registros_lb.pack(pady=20, padx=20)
        ventana.bind_all("<Control-n>", nuevo_alumno)
        ventana.mainloop()

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Copiar")

    def paste(self):
        print("Pegar")

    def open_file1(self):
        ventana = tk.Tk()
        ventana.title("Boton presionado")
        ventana.geometry("300x300")
        ventana.resizable(width=False,
                          height=False)  # puedes usar ese comando o "0,0" para que el tamaño no sea alterado
        ventana.config(bg="Light cyan")

        self.label = tk.Label(ventana, text="HOLA :D")
        self.label.pack(pady=20)
        self.label.config(fg="black", bg="Light cyan", font=("Segoe Script", 22))

        open_file1 = tk.Button(ventana, text="BAIBAI :3", command=ventana.quit)
        open_file1.pack(padx=10, pady=10)

    def open_file2(self):
        ventana = tk.Tk()
        ventana.title("Boton presionado")
        ventana.geometry("300x300")
        ventana.resizable(width=False,
                          height=False)  # puedes usar ese comando o "0,0" para que el tamaño no sea alterado
        ventana.config(bg="Light cyan")

        self.label = tk.Label(ventana, text="Eres un grosero >:v")
        self.label.pack(pady=20)
        self.label.config(fg="black", bg="Light cyan", font=("Lucida Console", 19))

        open_file2 = tk.Button(ventana, text="ADIOS", command=ventana.quit)
        open_file2.pack(padx=10, pady=10)


root = tk.Tk()
root.geometry("420x380")
root.resizable(width=False, height=False)
root.config(bg="Light cyan")
app = MenuScreen(root)
app.mainloop()